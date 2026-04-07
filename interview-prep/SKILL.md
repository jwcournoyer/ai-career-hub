---
name: interview-prep
description: "Prepare for specific job interviews — create interview prep docs from job descriptions, run mock interviews, generate STAR stories, research interviewers, and coach on delivery. Use this skill whenever the user mentions an upcoming interview, asks for mock interview practice, wants to prep for a specific company or role, needs STAR stories for behavioral questions, or asks for interview coaching. Also trigger when they mention interviewer names, job descriptions to analyze, or want to practice system design scenarios."
---

# Interview Prep

## Purpose

Per-interview preparation system. For each opportunity that reaches the interview stage, generate a tailored prep doc and mock interview script. Uses the candidate profile as the constant, job details as the variable.

## Structure

```
interview-prep/
├── SKILL.md
├── CANDIDATE_PROFILE.md          ← Permanent — the candidate's background, style, gaps, STAR story bank
├── INTERVIEW_PREP_TEMPLATE.md    ← Template for new prep docs
├── MOCK_INTERVIEW_TEMPLATE.md    ← Template for new mock interview docs
├── DEBRIEF_TEMPLATE.md           ← Template for post-interview debriefs
├── INTERVIEW_PREP_[COMPANY].md   ← Active prep docs (move to done/ after interview)
├── MOCK_INTERVIEW_[COMPANY].md   ← Active mock docs (move to done/ after interview)
├── presales/                      ← Active presales prep materials
│   └── [per-role prep and mock files]
└── done/                          ← Completed interviews (reference)
    ├── INTERVIEW_PREP_*.md
    ├── MOCK_INTERVIEW_*.md
    ├── TRANSCRIPT_*.md            ← Raw interview transcripts
    ├── DEBRIEF_*.md               ← Post-interview analysis + coaching
    └── [interviewer notes .docx]
```

## Three-File System (Prep + Mock) + Debrief Loop

Every interview prep produces up to three files:

1. **CANDIDATE_PROFILE.md** — Permanent. the candidate's full career arc, communication patterns, strengths, known gaps, interview tendencies, and **STAR story bank**. Read this first every time. The STAR story bank contains pre-structured behavioral answers following the Situation → Task → Action → Result framework — use these as the source for role-specific talking points.

2. **INTERVIEW_PREP_[COMPANY].md** — Per-role. Created from `INTERVIEW_PREP_TEMPLATE.md`. Contains job description, interviewer LinkedIn research, company context, and targeted talking points.

3. **MOCK_INTERVIEW_[COMPANY].md** — Per-role. Created from `MOCK_INTERVIEW_TEMPLATE.md`. A self-contained document that can be pasted into a new AI chat session alongside `CANDIDATE_PROFILE.md` to run a realistic mock interview with interviewer personas, question banks, and coaching debrief criteria.

After an interview, a **DEBRIEF_[COMPANY]_[ROUND].md** captures what worked, what hurt, recurring patterns, and coaching adjustments. Debriefs are the feedback loop — they inform future prep docs and mock interviews.

## Operations

### Creating Prep for a New Interview
1. Read `CANDIDATE_PROFILE.md` (always — includes STAR story bank)
2. Copy `INTERVIEW_PREP_TEMPLATE.md` → `INTERVIEW_PREP_[COMPANY].md`
3. Fill in: job description, interviewer details, company context
4. Map JD requirements to the candidate's specific experience (journal entries)
5. Flag any gaps honestly — prep mitigation stories
6. Select and tailor STAR stories from `CANDIDATE_PROFILE.md` for this role's likely behavioral questions
7. Copy `MOCK_INTERVIEW_TEMPLATE.md` → `MOCK_INTERVIEW_[COMPANY].md`
8. Fill in interviewer personas, company context, and role-specific question bank
9. If new STAR stories are needed that don't exist in the bank, add them to `CANDIDATE_PROFILE.md` (the permanent file) — not just the per-role prep doc

### Running a Mock Interview
1. Read both `CANDIDATE_PROFILE.md` and the role-specific prep
2. Play the interviewer realistically — match their likely style based on LinkedIn research
3. Ask 6-8 questions mixing behavioral and technical
4. After each answer, coach on:
   - Did the candidate lead with the conclusion or get lost in technical detail?
   - Did he own scope or undersell with "helped with" language?
   - Was the answer structured (situation → action → result)?
5. Save mock transcript and coaching notes

### Key Coaching Points (from CANDIDATE_PROFILE.md)
- **STAR structure:** All behavioral answers should follow Situation → Task → Action → Result. Pre-structured stories are in the STAR story bank in `CANDIDATE_PROFILE.md`.
- **Flip the order:** Conclusion or Result FIRST, then supporting detail. [Customize: note the candidate's default communication pattern here.]
- **Own the scope:** Replace "I helped" with "I designed/built/led/architected"
- **Differentiating closer:** "My strength is that I do both — architecture level AND technical build"
- **Honest about gaps:** Don't bluff on technologies the candidate hasn't used in production. Reframe as "architectural understanding, not production implementation"
- **Zero negatives:** Never speak negatively about previous employers. Frame everything as what was delivered and learned.
- **Demonstrate, don't confess:** When asked about weaknesses or communication style, show the skill in the answer itself — don't say "I'm working on it."

### After an Interview
1. Move prep files to `done/`
2. If transcript provided, save as `done/TRANSCRIPT_[COMPANY]_[ROUND].md`
3. Create `done/DEBRIEF_[COMPANY]_[ROUND].md` from `DEBRIEF_TEMPLATE.md` — score, analyze, identify patterns, set coaching adjustments
4. Add any interviewer notes or follow-up docs
5. Update `../job-search/` tracker with outcome

### Thank You Note (On-Demand Only)
When the candidate asks for a thank you note after an interview:
1. Read the relevant prep doc, debrief, and/or transcript from `done/`
2. Draft a concise email to the interview organizer (typically the recruiter or TA contact)
3. Tone: professional, genuine, not over-the-top. the candidate's voice — direct and specific.
4. Reference 1-2 specific things discussed in the interview (shows the candidate was listening, not sending a template)
5. Reinforce fit for the role without re-pitching the entire resume
6. Keep it short — 4-6 sentences max. No one reads long thank you emails.
7. **Do NOT create this proactively.** Only generate when the candidate explicitly asks.

### Creating Prep for a New Interview (When Prior Debriefs Exist)
Before writing prep, read the most recent 2-3 debriefs in `done/DEBRIEF_*.md`. Look for:
- **Recurring patterns** (e.g., volunteering negatives, detail-first delivery) — add these to the new prep doc's "Red Flags to Avoid"
- **Coaching adjustments** from the last debrief — incorporate into mock interview coaching points
- **What worked** — reinforce these in the new prep's talking points

## Cross-References
- `../engineering-journal/` — Source for STAR stories and technical narratives
- `../job-search/[NN_company].md` — Opportunity details and recruiter context
- `../resumes/` — Which resume variant was submitted
