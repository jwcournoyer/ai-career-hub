# Engineering Journal — Decision / Discovery Entry
## [TITLE: What You Decided or Discovered]

> **Use this template for:** A single architecture decision, a debugging session, a design spike, a technical discovery, or any focused moment of engineering judgment. These are the entries that power certification scenarios and "tell me about a time" interview answers. They should be tight, specific, and technically deep.
>
> **Not every entry needs the full project narrative.** If you already have a Project Narrative entry for this engagement, this entry supplements it — link back to the parent entry and skip the engagement-level context.

---

## Quick Context

| Field | Value |
|-------|-------|
| **Company** | [Name] |
| **Role** | [Your title] |
| **Date(s)** | [When this happened — can be a single day] |
| **Type** | [Architecture Decision / Debugging Session / Design Spike / Technical Discovery / Incident Response / Code Review Finding / Performance Investigation] |
| **Parent Entry** | [Link to Project Narrative entry if one exists, or "standalone"] |
| **Time Invested** | [How long this took — "2 hours", "3 days", "2 weeks". Useful for estimating similar work later.] |

---

## The Situation

**What triggered this?**
[A bug report, a new requirement, a design question, a production incident, a code review finding, a whiteboard session. One paragraph max.]

**What was the existing state?**
[What existed before you intervened. What was working, what wasn't, what assumption was wrong.]

---

## The Investigation (if applicable)

> **Include this section for debugging sessions, discovery work, and design spikes where the path to the answer wasn't obvious.** Skip for clean architecture decisions where you knew the options upfront.

### What was tried and failed
[Be specific. Each failed attempt is valuable documentation — it shows the diagnostic path and eliminates options for future reference. Use a numbered list.]

1. **[Attempted approach 1]** — [Why it didn't work / what it revealed]
2. **[Attempted approach 2]** — [Why it didn't work / what it revealed]
3. **[Attempted approach 3]** — [Why it didn't work / what it revealed]

### The breakthrough
[What led to the answer? A specific log line, a doc reference, an experiment, a conversation? This is the "aha" moment.]

### Root cause
[The actual underlying reason, stated clearly. Technical root cause first, then organizational/process root cause if relevant.]

---

## The Decision

**What was decided:**
[One clear statement. "We will use X instead of Y for Z."]

**Alternatives evaluated:**

| Option | Pros | Cons | Why Rejected/Selected |
|--------|------|------|----------------------|
| [Option A] | [+] | [-] | [Selected / Rejected because...] |
| [Option B] | [+] | [-] | [Selected / Rejected because...] |
| [Option C] | [+] | [-] | [Selected / Rejected because...] |

**Constraints that shaped this:**
[What made the choice non-obvious? Platform limits, timeline, team capability, cost, political reality, regulatory requirement?]

**Trade-offs accepted:**
[What's the downside of this choice? What did you give up?]

---

## Technical Detail

> **Go as deep as needed.** This section is the reference material future-you will come back to. Include code, schemas, flow diagrams, configuration, ERDs — whatever makes the solution concrete and reproducible.

### Implementation
[The actual technical solution. Code snippets, object schemas, flow architecture, config details.]

### Key Patterns / Principles Established
[Any governing rules or reusable patterns that came out of this work. These are the things you'd tell a future developer on Day 1.]

- **Rule:** [e.g., "Never hardcode configuration values in application code. Use metadata-driven configuration instead."]
- **Rule:** [e.g., "All third-party SDK calls should use the minimum viable configuration — let the SDK resolve defaults before adding explicit overrides."]
- **Pattern:** [e.g., "Two-stage record creation: bulk insert first, then patch parent-child relationships in a second pass."]

---

## Outcome

**Did it work?**
[Yes/no, and what happened when it hit production or passed testing.]

**Downstream impact:**
[What else changed as a result? Did this decision affect other components, other teams, future architecture?]

**Anything that surprised you after the fact?**
[Post-implementation learnings, edge cases discovered later, feedback from users or stakeholders.]

---

## The Lesson

> **Distill this to one or two transferable principles.** Not "I learned about the payment API" but "Over-specifying third-party SDK calls can bypass the SDK's built-in resolution engine — start with the minimum viable call and add complexity only when needed."

**Primary lesson:**
[The transferable principle you'd apply to a different technology, different client, different problem.]

**Secondary lesson (if applicable):**
[A process, communication, or organizational lesson alongside the technical one.]

---

## certification / Interview Hook

> **One-liner you can use to trigger this story in a certification scenario or interview.** Format: "The time I [situation] and discovered [insight] by [action]."

**Hook:** [e.g., "The time I spent two weeks debugging blank merge fields and discovered that over-specifying SDK calls bypasses the built-in resolution engine — the fix was to remove code, not add it."]

**Certification Domains:** [e.g., Integration Architecture, Solution Architecture]

---

## Resume Bullet Point

> **One bullet, tight.** If this discovery is significant enough to make the resume, write it here. If not, skip this section — not every discovery is resume-worthy and that's fine.

- [Bullet]

---

*Tags: [comma-separated]*
*Status: Complete*
*Last Updated: [Date]*
