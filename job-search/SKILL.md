---
name: job-search
description: "Manage the candidate's active job search — update the opportunity tracker, add new leads, research companies, draft outreach messages, track recruiter communications, and analyze role fit. Use this skill whenever the candidate mentions a new job opportunity, asks to update the tracker, wants to research a company, needs to draft a recruiter response, asks about his pipeline status, or wants to compare opportunities. Also trigger when he mentions recruiter names, company names from his search, rate negotiations, or prioritization of opportunities."
---

# Job Search

## Purpose

Track and manage all job opportunities from first contact through offer/close. Each opportunity gets a numbered file. The master tracker provides the pipeline view.

## Structure

```
job-search/
├── SKILL.md
├── 00_context_brief.md       ← Who the candidate is, positioning, comp targets, gaps
├── 00_master_tracker.md           ← Pipeline view: active, pending, closed
├── 01_example_job1.md             ← Per-opportunity files
├── 02_example_job2.md
├── ...
└── 30_example_job30.md
```

## File Conventions

- `00_` prefix = meta files (context brief, master tracker)
- `NN_company_name.md` = per-opportunity file, numbered sequentially
- Each opportunity file tracks: role, type (FTE/contract/C2C), comp, recruiter, status timeline, notes
- Files are append-only for status updates — add new entries at the top of the status section

## Key Files

### 00_context_brief.md
Comprehensive positioning doc: identity, career arc summary, technical strengths, known gaps, communication style, comp targets, what he's looking for. Also contains **manager references** for recruiter requests. **Read this before doing anything in the job search space.**

### 00_master_tracker.md
Pipeline summary with sections: Active/In Progress, Pending, Closed. Each entry has type, rate/salary, location, status, priority rating, and file reference.

## Operations

### Adding a New Opportunity
1. Create `NN_[company_slug].md` (next number in sequence)
2. Fill in: company, role, type, comp, recruiter, source, JD
3. Add entry to `00_master_tracker.md` in the appropriate section
4. Assess fit against `00_context_brief.md` — flag gaps and strengths

### Updating Status
1. Add a dated status entry to the opportunity file
2. Update `00_master_tracker.md` status and priority
3. If moving to interview stage → create files in `../interview-prep/`

### Closing an Opportunity
1. Add final status note to the opportunity file
2. Move entry from Active to Closed in the master tracker
3. Move any interview prep files to `../interview-prep/done/`

### Providing References
When a recruiter requests references, pull manager references from `00_context_brief.md`. the candidate may have limited manager references — flag any gaps and suggest alternatives (senior colleagues, client stakeholders).

### Comparing Opportunities
Read active entries and assess against:
- Comp vs. target ([YOUR TARGET COMP RANGE])
- Architecture ownership vs. ticket execution
- Remote preference (South FL hybrid acceptable)
- Strategic value (AI intersection, federal clearance, resume trajectory)
- Domain overlap with existing experience

## Priority Framework
- **HIGH:** Strong comp + strong fit + clear path forward
- **MEDIUM-HIGH:** Good bridge income or strategic value, active movement
- **MEDIUM:** Decent fit but missing something (comp, location, domain)
- **LOW:** Fallback or long-shot, not actively pursuing

## Daily Task Review
When the candidate asks "what do I need to do today/tomorrow?", scan the **Action Items** section at the top of `00_master_tracker.md` for dated tasks. Also scan active opportunity files for pending follow-ups. Group response by:
1. **Scheduled** — Calls, interviews, meetings with a specific date/time
2. **Follow-ups due** — Items where enough time has passed to check in (3+ business days since last contact)
3. **Waiting on** — Items where ball is in someone else's court (no action needed, but worth noting)

## Job Search Scraper

Automated job search tool in `scraper/` that scrapes LinkedIn and Indeed for Salesforce architect roles, filters out excluded companies and irrelevant keywords, deduplicates against a SQLite history database, and outputs a CSV for manual review.

### Usage
```bash
# Standard run — last 7 days, skips previously seen jobs
python job-search/scraper/jobspy_search.py

# Only last 3 days
python job-search/scraper/jobspy_search.py --days 3

# Reset history and start fresh
python job-search/scraper/jobspy_search.py --reset
```

### Configuration (`scraper/config.yaml`)
- **search_terms** — List of search queries (e.g., "Salesforce Architect", "CRM Architect")
- **sites** — Job boards to scrape (linkedin, indeed; glassdoor/zip_recruiter currently blocked)
- **excluded_companies** — Companies to filter out (already applied, ghosted, spam posters, active processes)
- **exclude_keywords** — Keywords that indicate a bad fit (e.g., "Marketing Cloud", "CPQ", "nCino")
- **filters** — Location, remote, results count, posting age

### Workflow
1. Run the scraper (daily or every few days)
2. Open the CSV in `scraper/output/`
3. Scan title/company/salary/URL columns
4. Anything interesting → create a new opportunity file (`NN_company.md`) and add to master tracker
5. Next run automatically skips previously seen postings via SQLite history

### Maintenance
- Add new excluded companies to `config.yaml` as opportunities close
- Use `--reset` if the history DB gets too large or you want a fresh sweep
- Output CSVs are gitignored — they're ephemeral scan-and-discard files

## Cross-References
- `../interview-prep/` — Prep docs for opportunities reaching interview stage
- `../resumes/` — Which variant to submit (W2 vs C2C vs one-pager)
- `../engineering-journal/` — Source experience for role fit analysis
