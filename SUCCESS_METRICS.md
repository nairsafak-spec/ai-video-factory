# Success Metrics

How the success of the Autonomous AI Video Factory is measured. Each area defines concrete, measurable KPIs with targets, a measurement method, and a review cadence. Targets are initial baselines and should be revisited as the system matures.

- **Scope:** Applies to the end-to-end pipeline (input → generation → assembly → publish).
- **Last reviewed:** 2026-07-13

---

## 1. System Reliability

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Pipeline success rate | ≥ 98% of jobs complete without failure | Completed jobs ÷ total jobs from run logs | Weekly |
| Uptime of core services | ≥ 99.5% | Uptime monitoring over the period | Monthly |
| Mean time to recovery (MTTR) | < 30 min | Time from failure detection to restored service | Monthly |

## 2. Video Quality

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Automated quality-gate pass rate | ≥ 90% pass on first render | Critic/quality-check step results | Weekly |
| Human acceptance rate | ≥ 85% approved without rework | Reviewer sign-off vs. total reviewed | Weekly |
| Rejection/rework rate | ≤ 10% | Rejected or reworked videos ÷ total produced | Weekly |

## 3. Voice Quality

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Voice naturalness (MOS) | ≥ 4.0 / 5.0 | Mean Opinion Score from rater sampling | Monthly |
| Pronunciation/error rate | ≤ 2% of segments flagged | Sampled audio review + transcript comparison | Monthly |
| Audio–video sync accuracy | ≥ 95% within tolerance | Automated timing checks on sampled outputs | Weekly |

## 4. Automation Rate

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Fully autonomous completion | ≥ 90% of jobs need no manual step | Jobs with zero human intervention ÷ total | Weekly |
| Manual interventions per video | < 0.2 on average | Count of manual actions ÷ videos produced | Weekly |
| Manual time per video | Decreasing trend | Tracked human minutes per delivered video | Monthly |

## 5. Agent Accuracy

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Correct agent decisions | ≥ 95% | Audited agent actions vs. expected outcome | Weekly |
| Task completion without retry | ≥ 90% | First-attempt successes ÷ total agent tasks | Weekly |
| Unsafe/unintended action rate | 0 critical incidents | Audit-log review of guarded actions | Weekly |

## 6. Processing Speed

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| End-to-end time per video | Within defined SLA per length | Timestamps from job start to final output | Weekly |
| Stage latency (bottleneck) | No single stage > 40% of total time | Per-stage profiling data | Monthly |
| Throughput | Meets or exceeds volume demand | Videos produced per hour/day | Weekly |

## 7. Resource Usage

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Peak VRAM per job | ≤ available GPU capacity, no OOM | GPU memory monitoring during runs | Weekly |
| Cost per video | Within budget target | Total compute/storage/API cost ÷ videos | Monthly |
| CPU/RAM utilization | Efficient, no sustained saturation | System resource monitoring | Monthly |

## 8. Learning Effectiveness

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Quality improvement over time | Positive trend in acceptance rate | Trend of quality KPIs across periods | Monthly |
| Applied learnings | ≥ 1 validated improvement per cycle | Learning system outputs vs. adopted changes | Monthly |
| Repeat-error rate | Decreasing trend | Recurrence of previously flagged issues | Monthly |

## 9. User Productivity

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Human effort per video | Decreasing trend | Tracked operator time per delivered video | Monthly |
| Time from request to delivery | Within target lead time | Timestamp of request to published output | Weekly |
| Output volume per operator | Increasing trend | Videos delivered ÷ operator effort | Monthly |

## 10. Maintainability

| Metric | Target | Measurement Method | Review Frequency |
|---|---|---|---|
| Documentation coverage | 100% of modules documented | Modules with current docs ÷ total modules | Monthly |
| Time to onboard a change | Decreasing trend | Lead time from change start to merged/deployed | Monthly |
| Test coverage of critical paths | ≥ 80% | Coverage reports on core components | Monthly |

---

## Notes

- Targets are **initial baselines**; adjust them as the system and its usage evolve.
- Measure with consistent methods and inputs so trends are comparable over time.
- Where a KPI depends on human rating, sample fairly and record the method.
- Review KPIs at their stated cadence; escalate sustained misses through the risk register and, where architectural, an ADR.
