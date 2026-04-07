---
name: engineering-journal
description: "Manage the candidate's engineering journal — add new entries, update existing ones, generate resume bullets, certification narratives, weekly/monthly summaries, and LinkedIn content from journal entries. Use this skill whenever the user mentions journal entries, career documentation, adding a new project or decision entry, generating summaries from past work, pulling resume bullets, or preparing certification experience narratives. Also trigger when they reference specific past engagements and want to document or extract from them."
---

# Engineering Journal

## Purpose

Permanent engineering journal documenting your career in software engineering and architecture. Powers resume bullets, LinkedIn content, certification experience portfolios, interview prep narratives, and performance reviews.

## Structure

```
engineering-journal/
├── README.md                    ← Master index with career timeline
├── templates/
│   ├── project-narrative-template.md
│   ├── decision-discovery-template.md
│   └── TEMPLATE-REDESIGN-RATIONALE.md
├── [company-name]/              ← One folder per employer (reverse chronological)
│   └── decisions/               ← Decision/Discovery entries for that employer
├── independent/                 ← Independent/consulting work
├── personal/                    ← Non-career entries
└── summaries/                   ← Generated summaries
```

## Two Templates

1. **Project Narrative** — Full engagements, major initiatives, multi-week efforts. Tells the complete story: situation → decisions → implementation → impact → lessons. Use for new client engagements, major features, or career milestones.

2. **Decision / Discovery** — Focused architecture decisions, debugging sessions, design spikes, technical discoveries. Short, punchy. Powers certification scenarios and interview answers. Use for "I chose X because Y" moments.

Read the actual templates in `templates/` before creating new entries — they have specific sections that must be filled.

## Operations

### Adding a New Entry
1. Determine template type (narrative vs decision)
2. Copy the appropriate template
3. Name it: `YYYY-MM_short-topic-slug.md` (or `YYYY-MM_to_YYYY-MM_` for ranges)
4. Place in the correct company/year folder
5. Fill ALL sections — do not abbreviate technical depth
6. Update `README.md` career timeline if this is a new engagement

### Generating Outputs
Feed relevant entries and ask for:
- Resume bullet points (use action verbs, quantify impact)
- certification experience narratives (map to certification domains)
- LinkedIn accomplishment posts
- Weekly/monthly summaries
- Interview story prep (situation → action → result)

### Cross-References
- Each entry contains **Narrative Hooks** — one-liners that trigger the full story for interviews
- Each entry maps to **certification domains** with specific evidence
- Resume bullets are pre-written in each entry — pull from these when updating resumes

## Key Rules
- Never shorten technical depth — the journal IS the depth
- Entries are append-only by default (add, don't overwrite history)
- Date prefixes in filenames, not numbered prefixes
- Company folder structure matches the career timeline
