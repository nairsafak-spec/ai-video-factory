# Research Methodology

The official process for selecting any technology used in this project. It ensures decisions are **evidence-based, comparable, and documented** rather than driven by hype, familiarity, or popularity. Every technology selection must follow these steps in order.

> **Core principle:** Technologies must **never** be selected based only on popularity. Stars, trends, and brand recognition are weak signals, not decisions. A candidate is chosen only when objective evidence and testing — scored against `EVALUATION_CRITERIA.md` — support it. Popularity may inform *Community Support* and *Development Activity*, but it can never substitute for measured evaluation.

---

## Process Overview

| Step | Name | Output |
|---|---|---|
| 1 | Identify candidates | Candidate shortlist |
| 2 | Collect objective information | Fact sheet per candidate |
| 3 | Compare strengths and weaknesses | Comparison table |
| 4 | Evaluate using criteria | Weighted scores |
| 5 | Test the top candidates | Working test results |
| 6 | Measure performance | Benchmark data |
| 7 | Document results | Research report |
| 8 | Make an ADR decision | Accepted/Rejected ADR |
| 9 | Re-evaluate periodically | Review outcome |

---

## 1. Identify Candidates

- Define the requirement and constraints the technology must satisfy.
- Gather a broad set of candidates from `OPEN_SOURCE_SHORTLIST.md`, prior research, and new discovery.
- Exclude only on **objective disqualifiers** (e.g. incompatible license, cannot self-host), not on preference.

## 2. Collect Objective Information

- For each candidate, record verifiable facts: license, maintenance status, requirements, features, and interfaces.
- Cite sources (official docs, repository, benchmarks). Avoid opinion and marketing claims.
- Note gaps where information is unavailable rather than guessing.

## 3. Compare Strengths and Weaknesses

- Build a side-by-side comparison of candidates across the same dimensions.
- State each strength and weakness concretely, tied to project needs.
- Narrow to a small set of top candidates for deeper evaluation.

## 4. Evaluate Using EVALUATION_CRITERIA.md

- Score every top candidate against the 13 weighted criteria defined in `EVALUATION_CRITERIA.md`.
- Apply the shared 0–10 scale and record a justification for each score.
- Compute the normalized weighted score and note any **blocking criteria**.

## 5. Test the Top Candidates

- Do not decide on paper alone — run the leading candidates in a realistic, controlled trial.
- Use representative inputs and the actual integration path where feasible.
- Capture setup effort, friction, and any failures encountered.

## 6. Measure Performance

- Collect quantitative data: speed, throughput, resource use, and output quality under comparable conditions.
- Use the same test harness and inputs across candidates for fair comparison.
- Record raw numbers, not just impressions, so results are reproducible.

## 7. Document Results

- Produce a research report summarizing information, scores, test setup, and measurements.
- Make the report auditable: anyone should be able to trace how the conclusion was reached.
- Store the report alongside the candidate and link it from the eventual ADR.

## 8. Make an ADR Decision

- Record the outcome as an Architecture Decision Record per `DECISION_LOG.md`.
- The ADR must reference the evaluation scores and test evidence that justify the choice.
- Assign a status (Accepted/Rejected) and a review date.

## 9. Re-evaluate Periodically

- Revisit each accepted technology by its ADR review date, or sooner on a material change (major release, license change, maintenance decline).
- Re-run relevant steps and update scores; supersede the ADR with a new one if direction changes.
- Keep the decision history intact — never silently replace a past decision.

---

## Guardrails

- **Evidence over popularity** — a large community never overrides poor measured results.
- **Objectivity over preference** — personal familiarity is not a selection reason.
- **Reproducibility** — every score and benchmark must be traceable to its source.
- **Documentation is mandatory** — an undocumented evaluation did not happen.
