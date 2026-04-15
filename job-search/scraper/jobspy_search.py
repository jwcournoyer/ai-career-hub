"""
Job Search Scraper — python-jobspy wrapper with SQLite dedup and CSV output.

Usage:
    python jobspy_search.py              # Run with default config.yaml
    python jobspy_search.py --config custom.yaml
    python jobspy_search.py --days 3     # Override hours_old to 3 days
    python jobspy_search.py --reset      # Clear history DB and start fresh
"""

import argparse
import hashlib
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
import yaml
from jobspy import scrape_jobs


SCRIPT_DIR = Path(__file__).parent
DEFAULT_CONFIG = SCRIPT_DIR / "config.yaml"
HISTORY_DB = SCRIPT_DIR / "history.sqlite"


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def init_db(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS seen_jobs (
            job_hash TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            site TEXT,
            first_seen TEXT,
            job_url TEXT
        )
    """)
    conn.commit()
    return conn


def reset_db(db_path: Path):
    if db_path.exists():
        db_path.unlink()
        print(f"Deleted history database: {db_path}")
    else:
        print("No history database to reset.")


def job_hash(row: pd.Series) -> str:
    """Create a unique hash for a job posting based on title + company + location."""
    raw = f"{row.get('title', '')}|{row.get('company', '')}|{row.get('location', '')}".lower().strip()
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def is_excluded_company(company: str, excluded: list[str]) -> bool:
    if pd.isna(company):
        return False
    company_lower = company.lower()
    return any(exc.lower() in company_lower for exc in excluded)


def has_exclude_keyword(text: str, keywords: list[str]) -> bool:
    if pd.isna(text):
        return False
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)


def run_search(config: dict, days_override: int | None = None) -> pd.DataFrame:
    search_terms = config["search_terms"]
    sites = config["sites"]
    filters = config["filters"]
    hours_old = (days_override * 24) if days_override else filters.get("hours_old", 168)

    all_results = []

    for term in search_terms:
        print(f"  Searching: \"{term}\" across {', '.join(sites)}...")
        try:
            jobs = scrape_jobs(
                site_name=sites,
                search_term=term,
                location=filters.get("location", "United States"),
                is_remote=filters.get("is_remote", True),
                results_wanted=filters.get("results_wanted", 50),
                hours_old=hours_old,
                country_indeed=filters.get("country_indeed", "USA"),
            )
            if jobs is not None and len(jobs) > 0:
                print(f"    Found {len(jobs)} results")
                all_results.append(jobs)
            else:
                print(f"    No results")
        except Exception as e:
            print(f"    Error searching \"{term}\": {e}")

    if not all_results:
        print("\nNo results found across any search terms.")
        return pd.DataFrame()

    combined = pd.concat(all_results, ignore_index=True)
    print(f"\nTotal raw results: {len(combined)}")
    return combined


def filter_results(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    if df.empty:
        return df

    excluded_companies = config.get("excluded_companies", [])
    exclude_keywords = config.get("exclude_keywords", [])
    min_salary = config.get("min_annual_salary", 0)

    original_count = len(df)

    # Filter excluded companies
    if excluded_companies:
        mask = df["company"].apply(lambda c: not is_excluded_company(c, excluded_companies))
        df = df[mask]
        print(f"  After excluding companies: {len(df)} (removed {original_count - len(df)})")

    # Filter exclude keywords in title or description
    if exclude_keywords:
        before = len(df)
        title_mask = df["title"].apply(lambda t: not has_exclude_keyword(t, exclude_keywords))
        desc_mask = df["description"].apply(lambda d: not has_exclude_keyword(d, exclude_keywords)) if "description" in df.columns else True
        df = df[title_mask & desc_mask]
        print(f"  After keyword exclusions: {len(df)} (removed {before - len(df)})")

    # Filter minimum salary if set and column exists
    if min_salary > 0 and "min_amount" in df.columns:
        before = len(df)
        df = df[(df["min_amount"].isna()) | (df["min_amount"] >= min_salary)]
        print(f"  After salary filter (>=${min_salary:,}): {len(df)} (removed {before - len(df)})")

    return df


def dedup_results(df: pd.DataFrame, conn: sqlite3.Connection) -> pd.DataFrame:
    """Remove jobs we've already seen in previous runs."""
    if df.empty:
        return df

    df["_hash"] = df.apply(job_hash, axis=1)

    # Check which hashes are already in the DB
    existing = set()
    for h in df["_hash"].unique():
        row = conn.execute("SELECT 1 FROM seen_jobs WHERE job_hash = ?", (h,)).fetchone()
        if row:
            existing.add(h)

    new_jobs = df[~df["_hash"].isin(existing)].copy()
    print(f"  After dedup (vs. history): {len(new_jobs)} new (skipped {len(existing)} previously seen)")

    # Also dedup within current batch (same job from multiple sites/terms)
    before = len(new_jobs)
    new_jobs = new_jobs.drop_duplicates(subset=["_hash"], keep="first")
    if before > len(new_jobs):
        print(f"  After cross-source dedup: {len(new_jobs)} (removed {before - len(new_jobs)} duplicates)")

    return new_jobs


def save_to_history(df: pd.DataFrame, conn: sqlite3.Connection):
    """Record new jobs in the history DB so they don't appear next run."""
    if df.empty:
        return

    now = datetime.now().isoformat()
    for _, row in df.iterrows():
        conn.execute(
            "INSERT OR IGNORE INTO seen_jobs (job_hash, title, company, site, first_seen, job_url) VALUES (?, ?, ?, ?, ?, ?)",
            (
                row.get("_hash", ""),
                row.get("title", ""),
                row.get("company", ""),
                row.get("site", ""),
                now,
                row.get("job_url", ""),
            ),
        )
    conn.commit()
    print(f"  Saved {len(df)} new jobs to history DB")


def save_csv(df: pd.DataFrame, config: dict) -> Path:
    output_dir = SCRIPT_DIR / config.get("output", {}).get("directory", "output")
    output_dir.mkdir(parents=True, exist_ok=True)

    prefix = config.get("output", {}).get("filename_prefix", "jobspy_results")
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    filename = f"{prefix}_{date_str}.csv"
    filepath = output_dir / filename

    # Select and order columns for easy scanning
    columns_priority = [
        "title",
        "company",
        "location",
        "min_amount",
        "max_amount",
        "currency",
        "job_type",
        "date_posted",
        "site",
        "job_url",
        "description",
    ]
    available = [c for c in columns_priority if c in df.columns]
    extra = [c for c in df.columns if c not in columns_priority and c != "_hash"]
    output_cols = available + extra

    df[output_cols].to_csv(filepath, index=False)
    return filepath


def main():
    parser = argparse.ArgumentParser(description="Job search scraper with dedup")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Path to config YAML")
    parser.add_argument("--days", type=int, default=None, help="Override: only search postings from last N days")
    parser.add_argument("--reset", action="store_true", help="Reset the history database")
    args = parser.parse_args()

    if args.reset:
        reset_db(HISTORY_DB)
        if not args.days:
            return

    config = load_config(args.config)
    conn = init_db(HISTORY_DB)

    print("=" * 60)
    print(f"Job Search Scraper — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    print("\n[1/4] Scraping job sites...")
    raw = run_search(config, args.days)

    if raw.empty:
        print("\nNo results. Try broadening search terms or increasing --days.")
        conn.close()
        return

    print("\n[2/4] Filtering results...")
    filtered = filter_results(raw, config)

    print("\n[3/4] Deduplicating against history...")
    new_jobs = dedup_results(filtered, conn)

    if new_jobs.empty:
        print("\nNo new jobs since last run. Try again in a few days or use --reset.")
        conn.close()
        return

    print("\n[4/4] Saving results...")
    save_to_history(new_jobs, conn)
    filepath = save_csv(new_jobs, config)

    print(f"\n{'=' * 60}")
    print(f"Done! {len(new_jobs)} new jobs saved to: {filepath}")
    print(f"{'=' * 60}")

    # Print a quick summary to terminal
    print(f"\nTop results:")
    print("-" * 60)
    for _, row in new_jobs.head(15).iterrows():
        salary = ""
        if pd.notna(row.get("min_amount")):
            salary = f" | ${row['min_amount']:,.0f}"
            if pd.notna(row.get("max_amount")):
                salary += f"-${row['max_amount']:,.0f}"
        print(f"  {row.get('title', 'N/A')}")
        print(f"    {row.get('company', 'N/A')} | {row.get('location', 'N/A')}{salary}")
        print(f"    {row.get('job_url', 'N/A')}")
        print()

    conn.close()


if __name__ == "__main__":
    main()
