# Decision Log

The official index of Architecture Decision Records (ADRs) for this project. Every significant architectural or technology decision is recorded here as a numbered, immutable entry.

---

## Purpose

- Provide a **single, authoritative history** of why the architecture is the way it is.
- Make decisions **transparent, traceable, and reviewable** by current and future contributors.
- Prevent re-litigating settled questions and preserve the context behind each choice.
- Serve as the destination for evaluations produced under the project's evaluation criteria.

An ADR is warranted whenever a decision is hard to reverse, affects multiple components, introduces or removes a core dependency, or sets a standard others must follow.

---

## Numbering Format

- Each decision has a unique, sequential identifier: **`ADR-001`, `ADR-002`, `ADR-003`, …**
- Numbers are zero-padded to three digits and **never reused**, even if a decision is later rejected or deprecated.
- Each ADR lives in its own file named `ADR-NNN-short-title.md` and is listed in the index below.
- Numbers are assigned in the order decisions are proposed.

---

## Status Values

Every ADR carries exactly one status at a time:

| Status | Meaning |
|---|---|
| **Proposed** | Under discussion; not yet agreed. |
| **Accepted** | Approved and in effect. |
| **Rejected** | Considered but not adopted; kept for the historical record. |
| **Deprecated** | Previously accepted but no longer in effect (typically superseded by a newer ADR). |

**Rules:**

- ADRs are **immutable once Accepted** — do not rewrite them. To change direction, create a new ADR that supersedes the old one and update the old ADR's status to `Deprecated` with a link to the successor.
- Status transitions should be reflected in both the ADR file and this index.

---

## Required Sections for Every Decision

Every ADR **must** contain the following sections, in this order:

1. **Title** — A short, descriptive name, prefixed with its identifier (e.g. `ADR-001: Choose Vector Database`).
2. **Context** — The problem, constraints, and forces driving the decision. Why is a decision needed now?
3. **Alternatives** — The options considered, each with a brief note on trade-offs.
4. **Decision** — The option chosen and the rationale for choosing it.
5. **Consequences** — The resulting outcomes: benefits, costs, risks, and follow-up work (positive and negative).
6. **Review Date** — The date by which the decision should be revisited to confirm it still holds.

Each ADR should also record its **status** and the **date** it was last updated in a short header.

---

## ADR Template

```markdown
# ADR-NNN: <Title>

- **Status:** Proposed | Accepted | Rejected | Deprecated
- **Date:** YYYY-MM-DD
- **Review Date:** YYYY-MM-DD

## Context
<The problem, constraints, and forces at play.>

## Alternatives
<Options considered and their trade-offs.>

## Decision
<The chosen option and why.>

## Consequences
<Benefits, costs, risks, and follow-up work.>
```

---

## Decision Index

Decisions will be listed here as they are created. No decisions have been recorded yet.

| ID | Title | Status | Date | Review Date |
|---|---|---|---|---|
| — | _No decisions recorded yet_ | — | — | — |
