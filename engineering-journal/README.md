# Engineering Journal — Master Index

**Purpose:** Permanent engineering journal documenting your career in software engineering and architecture. Designed for generating resume bullet points, LinkedIn content, interview STAR stories, and certification-level architectural experience portfolios.

## Template System

This journal uses two templates:

1. **Project Narrative Template** (`templates/project-narrative-template.md`) — For full engagements, major initiatives, or significant multi-week efforts. Tells the complete story: situation, decisions, implementation, impact, lessons.

2. **Decision / Discovery Template** (`templates/decision-discovery-template.md`) — For focused architecture decisions, debugging sessions, design spikes, or technical discoveries. The entries that power certification scenarios and interview answers.

See `templates/TEMPLATE-REDESIGN-RATIONALE.md` for the reasoning behind the template redesign.

## Directory Structure

Organize entries by employer/company in reverse chronological order:

```
engineering-journal/
├── README.md                          # This file
├── SKILL.md                          # AI instructions for this workstream
├── templates/
│   ├── project-narrative-template.md
│   ├── decision-discovery-template.md
│   └── TEMPLATE-REDESIGN-RATIONALE.md
├── [current-company]/                 # Most recent employer
│   ├── YYYY-MM_project-name.md        # Project narrative entries
│   └── decisions/                     # Decision/discovery entries
│       └── YYYY-MM_decision-name.md
├── [previous-company]/                # Previous employers
└── entries/                           # .gitkeep placeholder
```

## Adding New Entries

1. Choose the appropriate template:
   - **Project Narrative** for full engagements or major initiatives
   - **Decision / Discovery** for focused technical decisions, debugging sessions, or design spikes
2. Copy the template and name it: `YYYY-MM_short-topic-slug.md`
3. Place in the appropriate company folder (or `decisions/` subfolder)
4. Fill in all sections — do NOT shorten technical depth

## Generating Outputs

Feed relevant entries to Claude Code and ask for:
- Resume bullet points (use action verbs, quantify impact)
- STAR stories for behavioral interviews
- LinkedIn accomplishment posts
- certification experience narratives (map to certification domains)

## Key Themes to Track Across Your Career

As you build entries, patterns will emerge. Common themes:
- Greenfield builds vs. optimization of existing systems
- Data migration expertise and patterns
- Integration architecture across systems
- Multi-org / multi-system complexity
- DevOps and custom tooling
- Industry breadth
- Solo delivery capability
- Architecture documentation as a deliverable
- AI-driven development practices
