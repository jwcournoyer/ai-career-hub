---
name: resumes
description: "Manage the candidate's resume variants — create role-specific tailored versions, update the master resume, track certification PDFs, and generate targeted resume content from engineering journal entries. Use this skill whenever the user asks to tailor a resume for a specific role, update their resume, create a new variant, compare resume versions, or pull accomplishment bullets from their journal. Also trigger when they mention cover letters, one-pagers, C2C resume formatting, or certification documentation."
---

# Resumes

## Purpose

Maintain the master resume and generate role-specific variants tailored to specific job descriptions. Resume content is sourced from the engineering journal — the journal is the source of truth, resumes are the output.

## Structure

```
resumes/
├── SKILL.md
├── [year]/                      ← Current year variants
│   ├── Your_Name_Resume_[year].docx          ← Master (W2/FTE)
│   ├── Your_Name_Resume_[year]_C2C.docx      ← C2C variant (if applicable)
│   ├── Your_Name_Resume_OnePager_[year].docx ← One-page summary
│   └── Your_Name_Resume_[year]_[Variant].docx
├── [previous-year]/             ← Previous versions (reference only)
│   └── [older formats]
├── certifications/              ← Cert PDFs
│   └── [certification files]
└── variants/                    ← .gitkeep placeholder
```

## Current Resume Variants

| File | Use Case |
|------|----------|
| `*_[year].docx` | Standard W2/FTE applications |
| `*_[year]_C2C.docx` | Contract/C2C through your LLC (if applicable) |
| `*_OnePager_[year].docx` | Quick summary for recruiter screens |
| `*_[Variant].docx` | Role-specific emphasis variants |

## Operations

### Tailoring for a Specific Role
1. Read the target job description
2. Read the master resume
3. Read relevant engineering journal entries for matching experience
4. Adjust emphasis: reorder bullets, swap in relevant accomplishments, tune the summary
5. Save as a new variant: `Your_Name_Resume_[year]_[Company]_[Role].docx`
6. Keep the same formatting/layout as the master

### Key Positioning
- **Summary lead:** [Your title, years of experience, key certifications]
- **Differentiator:** [Your one-liner — what makes you different]
- **Strongest stories:** [List your strongest project stories here]
- **Current:** [Your current title and company]

### Resume Rules
- Action verbs, quantified impact (numbers, percentages, scale)
- No "helped with" or "was involved in" — own the scope
- Technical depth belongs in the journal; resumes get the impact statement
- Keep 2-page max for standard, 1-page for one-pager
- Include current role and engagement

### Cross-References
- `../engineering-journal/` — Source of truth for all accomplishment bullets
- `../job-search/00_context_brief.md` — Known gaps and positioning
- `../interview-prep/CANDIDATE_PROFILE.md` — Communication style notes
