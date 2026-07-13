# Project Memory

How knowledge is preserved across the lifetime of the Autonomous AI Video Factory. The goal is that no important context, decision, or lesson is lost as the project, its people, and its tools change. This document defines **what** must be remembered and **why** — it does not implement a system.

---

## Guiding Principles

- **Capture at the moment of learning** — record knowledge when it is fresh, not later from memory.
- **Make it findable** — organize memory so the right information surfaces when needed.
- **Keep it truthful and current** — outdated or wrong memory is a liability; prune and correct it.
- **Prefer durable, versioned storage** — knowledge lives in the repository alongside the work it describes.

---

## Memory Sections

### 1. Long-term Memory
**Purpose:** Persistent knowledge that stays relevant across the whole project — architecture, standards, glossary, goals, and stable facts. It is the project's durable foundation and changes slowly and deliberately.

### 2. Short-term Memory
**Purpose:** Transient, task- or session-scoped context — the current focus, in-progress work, and temporary state. It keeps active work coherent and is expected to be summarized into long-term memory or discarded once the task ends.

### 3. Architecture Decisions
**Purpose:** The record of significant technical choices and their rationale, maintained as ADRs. It explains *why* the system is shaped the way it is, prevents re-litigating settled questions, and preserves context for future contributors.

### 4. Research History
**Purpose:** A trail of investigations — candidates considered, comparisons, scores, and sources. It lets the team reuse prior research, avoid repeating work, and understand how conclusions were reached.

### 5. Lessons Learned
**Purpose:** Insights distilled from experience — what worked, what didn't, and what to do differently. It turns individual experience into shared, reusable wisdom and reduces repeated mistakes.

### 6. Failed Experiments
**Purpose:** An honest record of approaches that did not work and why. It saves future effort by preventing dead ends from being retried and documents the boundaries of what has been tested.

### 7. Successful Experiments
**Purpose:** Proven approaches and configurations that delivered good results. It captures repeatable wins so they can be reused, scaled, or promoted into standard practice.

### 8. Reusable Prompts
**Purpose:** A curated library of effective prompts and templates. Prompts are core assets; preserving the best ones ensures consistent quality and spares re-discovery of what already works.

### 9. Coding Patterns
**Purpose:** Recurring, project-approved solutions to common implementation problems. Documenting them promotes consistency, speeds development, and encodes the team's preferred way of building.

### 10. Best Practices
**Purpose:** The accumulated conventions and guidance for working well on this project. It aligns contributors on quality, safety, and process, and serves as the reference for how things should be done.

---

## Maintenance

- Review memory sections on a regular cadence and after major milestones.
- Promote durable insights from short-term to long-term memory; archive the rest.
- Correct or remove memory that becomes inaccurate — treat stale knowledge as a defect.
- Link related entries across sections (e.g. a lesson learned to the ADR or experiment that produced it) so context is traceable.
