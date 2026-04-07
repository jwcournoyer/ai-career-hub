# Career Hub — Claude Code Project Instructions

## Who This Is For

[YOUR NAME] — [Your title, experience level, certifications, location. This helps Claude tailor its tone and depth.]

## Repository Structure

This is a single private repo managing interconnected career workstreams. Each has its own SKILL.md with detailed instructions:

- `engineering-journal/` — Career journal (entries organized by employer, two templates)
- `resumes/` — Master resume + role-specific variants + certification PDFs
- `interview-prep/` — Per-role interview prep, mock interviews, candidate profile
- `job-search/` — Opportunity tracker, company files, context brief

## Cross-Cutting Rules

1. **Voice:** [Describe your preferred communication style — direct, formal, casual, etc.]
2. **Format:** Markdown everywhere. Binary files (docx, pdf, pptx) only where the deliverable requires it.
3. **Commit messages:** Use conventional commits — `feat(journal):`, `fix(resume):`, `docs(study):`, `chore:`.
4. **No destructive changes without confirmation.** Always confirm before deleting or overwriting existing content.
5. **Cross-reference freely.** Journal entries feed resume bullets. Interview prep references journal narratives. Job search files link to prep files. The sections are interconnected.

## Workflow Rules
- Before creating or modifying files in any section, read that section's SKILL.md first.
- When a task spans multiple sections (e.g., new opportunity → tracker + interview prep), read each relevant SKILL.md.

## Key Context

- **Communication pattern:** [Describe your natural interview style and what you want Claude to help you improve. Example: "I lead with technical detail before the conclusion — help me flip that."]
- **Differentiating closer:** [Your one-liner that captures what makes you different. Example: "My strength is that I do both — architecture and hands-on build."]
- **Known gaps (be honest about):** [List technologies or skills you don't have deep experience in. Honesty here helps Claude prep you realistically for interviews.]

## Canonical File Locations (No Duplicates)

- `interview-prep/CANDIDATE_PROFILE.md` — Single source for candidate profile and STAR story bank. Referenced by job-search and interview-prep skills.
- `interview-prep/INTERVIEW_PREP_TEMPLATE.md` — Single source for prep template. Copy per interview, don't modify the template.
- `interview-prep/MOCK_INTERVIEW_TEMPLATE.md` — Single source for mock interview template.
- `job-search/00_context_brief.md` — Single source for positioning, comp targets, and known gaps.
- `engineering-journal/` — Source of truth for all career accomplishments. Resumes and interview prep pull from here.

## Data Flow

```
engineering-journal → resumes (bullet points)
engineering-journal → interview-prep (STAR stories, technical narratives)
job-search → interview-prep (when opportunity reaches interview stage)
interview-prep/done → job-search (outcome updates)
```
