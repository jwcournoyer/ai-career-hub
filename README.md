# Career Hub — AI-Driven Career Operations Framework

A personal career management system designed for use with **Claude Code** in VS Code. Manages job search, engineering journal, resumes, interview prep, and certification study — all interconnected, version-controlled, and AI-assisted.

## What This Is

This is a **framework** — the SKILL.md files, templates, and CLAUDE.md that teach an AI assistant how to manage your career operations. Fork it, fill in your own information, and use it with Claude Code (or adapt it for any AI assistant).

## Structure

```
career-hub/
├── CLAUDE.md                 # Project-level AI instructions (customize for you)
├── engineering-journal/      # Career journal with two templates
│   ├── SKILL.md              #   How the journal works
│   └── templates/            #   Project narrative + decision/discovery templates
├── resumes/                  # Master resume + role-specific variants
│   └── SKILL.md              #   Resume management rules
├── interview-prep/           # Per-interview prep, mock interviews, STAR stories
│   ├── SKILL.md              #   Three-file system (prep + mock + debrief)
│   ├── INTERVIEW_PREP_TEMPLATE.md
│   ├── MOCK_INTERVIEW_TEMPLATE.md
│   └── DEBRIEF_TEMPLATE.md
└── job-search/               # Opportunity tracker
    └── SKILL.md              #   Tracking, prioritization, daily review
```

## How It Works

Each folder has a `SKILL.md` that acts as a **domain API** — it teaches the AI how to operate in that area: file naming conventions, operations, cross-references, and rules. When you tell Claude Code to "prep me for an interview" or "add a new job opportunity," it reads the relevant SKILL.md and follows the conventions automatically.

### Key Patterns

- **SKILL.md as domain API** — each folder's instructions are version-controlled alongside the data
- **Cross-referencing over duplication** — canonical files exist in one location only
- **Append-only status tracking** — opportunity files preserve full history, never overwrite
- **Feedback loops** — interview debriefs inform future prep docs automatically
- **STAR story bank** — behavioral interview stories structured as Situation/Task/Action/Result, maintained in one place, reused across interviews
- **Three-file interview system** — prep doc (JD mapping + talking points) + mock interview (AI-simulated with interviewer personas) + debrief (post-interview coaching)
- **Conventional commits** — `feat(journal):`, `fix(resume):`, `docs(study):`, `chore:`

### Data Flow

```
engineering-journal → resumes (bullet points)
engineering-journal → interview-prep (STAR stories, technical narratives)
job-search → interview-prep (when opportunity reaches interview stage)
interview-prep/done → job-search (outcome updates)
```

## Getting Started

1. Fork or clone this repo
2. Edit `CLAUDE.md` with your identity, communication style, gaps, and differentiators
3. Create your `interview-prep/CANDIDATE_PROFILE.md` with your career arc and STAR stories
4. Create your `job-search/00_context_brief.md` with your positioning and comp targets
5. Start adding engineering journal entries using the templates
6. When an opportunity comes in, tell Claude Code — it handles the rest

## Example Commands in Claude Code

- "Add a journal entry for today's work"
- "Here's a new JD — add it to the tracker and assess fit"
- "Prep me for the interview — here's the JD and interviewer LinkedIn profiles"
- "Run a mock interview for tomorrow"
- "Update the tracker — they passed on me"
- "What do I need to do today?"

## Requirements

- [Claude Code](https://claude.ai/code) (CLI or VS Code extension)
- Git + GitHub (private repo recommended)
- A career worth documenting

## License

This framework is shared freely. Use it however you want. The templates and SKILL.md files are the value — fill them with your own story.
