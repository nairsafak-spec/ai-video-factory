# Evaluation Criteria

A standardized, weighted scoring system for evaluating every technology considered for this project. It exists to make technology decisions **objective, comparable, and repeatable**. No technology is evaluated in this document — it defines the method only.

---

## Scoring Method

Each candidate is assessed against 13 criteria. Every criterion receives an integer **score from 0 to 10** using the shared scale below, then is multiplied by its **weight**. The weighted results are summed and normalized to a final **0–10** score.

**Formula:**

```
Weighted Score = Σ (criterion_score × criterion_weight) / 100
```

Because the weights total **100**, dividing by 100 returns the final result to the same 0–10 scale as the individual scores.

### The 0–10 Scale

| Score | Meaning |
|---|---|
| 0–2 | Unacceptable — fails the criterion or is a blocker |
| 3–4 | Weak — significant gaps or risks |
| 5–6 | Adequate — usable with reservations |
| 7–8 | Strong — meets expectations well |
| 9–10 | Excellent — best-in-class, few or no concerns |

### Rules

- Score against **evidence** (benchmarks, docs, repository signals, tests), not impressions.
- Record a one-line justification for every score so results are auditable.
- Use whole numbers only; if unsure between two values, choose the lower.
- If a criterion cannot be assessed, mark it explicitly and do **not** silently assume a value.
- Re-score when a candidate materially changes (major release, license change, maintenance shift).

---

## Weighted Criteria

Weights reflect what matters most for an autonomous, self-hosted AI video pipeline: the quality of what it produces, and its ability to run reliably over the long term.

| # | Criterion | Weight | What It Measures |
|---|---|---:|---|
| 1 | Output Quality | 15 | Quality and consistency of the produced result (video, audio, text, etc.) |
| 2 | Performance | 10 | Speed, throughput, and latency under realistic load |
| 3 | Stability | 10 | Reliability, maturity, and freedom from breaking changes/crashes |
| 4 | Long-term Sustainability | 10 | Likelihood the project survives and stays maintained |
| 5 | Open Source License | 8 | Permissiveness and compatibility with project and commercial use |
| 6 | Self-hosting Capability | 8 | Ability to run fully on our own infrastructure without lock-in |
| 7 | Ease of Integration | 8 | Effort to connect into the existing pipeline and tooling |
| 8 | Community Support | 6 | Size and responsiveness of the user/contributor community |
| 9 | Development Activity | 6 | Commit cadence, releases, and issue/PR responsiveness |
| 10 | Extensibility | 5 | Ability to customize, extend, or plug in new behavior |
| 11 | Documentation Quality | 5 | Completeness, accuracy, and clarity of official docs |
| 12 | API Availability | 5 | Presence of stable, well-defined programmatic interfaces |
| 13 | Hardware Requirements | 4 | Reasonableness of compute/VRAM/memory needs (higher score = lighter needs) |
| | **Total** | **100** | |

> **Note on direction:** For *Hardware Requirements*, a **higher score means lighter/more affordable** requirements. All other criteria follow the intuitive direction (higher is better).

---

## Interpreting Results

The following bands are **guidance for discussion**, not automatic decisions. Final selection always involves human judgment and context.

| Final Score | Interpretation |
|---|---|
| 8.5–10 | Strong candidate — shortlist for adoption |
| 7.0–8.4 | Viable — acceptable, weigh against alternatives |
| 5.0–6.9 | Marginal — only if no better option exists |
| Below 5.0 | Not recommended |

### Blocking Criteria

Some low scores should halt evaluation regardless of the total, pending explicit review:

- **Open Source License** scored 0–2 (incompatible or prohibitive license).
- **Self-hosting Capability** scored 0–2 (cannot run on our infrastructure).
- **Stability** scored 0–2 (unreliable for production use).

A blocking score does not auto-reject a candidate, but it must be explicitly acknowledged and justified before proceeding.

---

## Evaluation Record Template

Each future evaluation should capture scores and justifications in this shape (one row per criterion):

| Criterion | Weight | Score (0–10) | Weighted (Score × Weight) | Justification |
|---|---:|---:|---:|---|
| Output Quality | 15 | — | — | — |
| … | … | — | — | — |
| **Weighted Score** | **100** | | **Σ / 100 = —** | |

Store completed evaluations alongside the candidate under review, and link them from the relevant decision record.
