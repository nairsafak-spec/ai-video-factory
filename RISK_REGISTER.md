# Risk Register

The initial risk register for the Autonomous AI Video Factory. It tracks known project risks, their potential impact and likelihood, planned mitigations, and current status. This is a living document — review and update it regularly as risks evolve or new ones emerge.

- **Impact / Probability scale:** Low · Medium · High
- **Status values:** Open · Monitoring · Mitigating · Closed
- **Last reviewed:** 2026-07-13

---

## Register

| Risk ID | Risk | Impact | Probability | Mitigation | Status |
|---|---|---|---|---|---|
| R-001 | Open-source project abandoned or unmaintained | High | Medium | Prefer active projects per evaluation criteria; keep alternatives shortlisted; pin known-good versions; be ready to fork | Open |
| R-002 | GPU memory (VRAM) limitations on available hardware | High | High | Use quantization/offloading; batch/schedule jobs; fall back to hosted inference for heavy models; right-size model choices | Monitoring |
| R-003 | Breaking API changes in a dependency or framework | Medium | High | Pin versions; isolate integrations behind adapters; test before upgrading; track release notes | Open |
| R-004 | Model or weights licensing changes (e.g. non-commercial) | High | Medium | Track licenses at adoption and review; prefer permissive licenses; document license per component; keep replacements ready | Open |
| R-005 | Security vulnerabilities in dependencies or models | High | Medium | Minimize dependencies; scan regularly; patch promptly; least-privilege access; isolate untrusted inputs | Monitoring |
| R-006 | Hardware failure (GPU, disk, or host) | High | Medium | Back up data and configs; use reproducible setup; keep spare/hosted capacity; monitor hardware health | Open |
| R-007 | Vendor or platform lock-in | Medium | Medium | Favor self-hostable, open tools; abstract provider-specific code; keep data portable and exportable | Open |
| R-008 | Poor or inconsistent output quality | High | Medium | Define quality gates; automated review/critic step; human spot-checks; prompt and model tuning; A/B comparisons | Mitigating |
| R-009 | Performance bottlenecks in the pipeline | Medium | High | Benchmark stages; profile and optimize hot paths; parallelize; cache; scale critical stages | Monitoring |
| R-010 | Dependency conflicts across components | Medium | High | Isolated environments/containers; lock files; minimal shared dependencies; CI validation | Open |
| R-011 | Secrets or credentials leaked (in code, logs, or history) | High | Medium | Store secrets in env/secret manager; never log secrets; gitignore secret files; rotate on exposure; scan commits | Mitigating |
| R-012 | Rapidly changing AI landscape makes chosen tools obsolete | Medium | High | Periodic re-evaluation via ADR review dates; modular architecture; avoid deep coupling to any single tool | Monitoring |
| R-013 | Cost overruns (compute, storage, or hosted APIs) | Medium | Medium | Budget and monitor usage; cap/quota jobs; prefer self-hosting where cheaper; alert on spend | Open |
| R-014 | Generated content violates copyright, IP, or platform policy | High | Medium | Use licensed/permissible assets and models; content review; policy checks before publishing; audit trail | Open |
| R-015 | Autonomous agent makes unsafe or unintended actions | High | Medium | Human-in-the-loop for irreversible/outward actions; guardrails and permissions; dry-run modes; audit logging | Mitigating |
| R-016 | Data loss or corruption (assets, intermediate data, memory) | High | Low | Regular backups; integrity checks; versioned storage; tested restore procedures | Open |
| R-017 | Insufficient documentation causes knowledge loss | Medium | Medium | Enforce documentation standards; ADRs for decisions; update docs with each change | Monitoring |
| R-018 | Third-party API rate limits or outages disrupt the pipeline | Medium | Medium | Retries with backoff; queueing; graceful degradation; local fallbacks; monitor availability | Open |
| R-019 | Scalability limits as volume grows | Medium | Medium | Design for horizontal scaling; decouple stages via queues; load-test early; monitor throughput | Open |
| R-020 | Regulatory or compliance changes (AI content, data privacy) | Medium | Low | Track relevant regulations; keep data handling compliant; maintain audit records; adapt policies as needed | Monitoring |

---

## Maintenance

- Review this register on a regular cadence and whenever the architecture or toolset changes.
- Add new risks as they are identified; update impact, probability, and status as conditions change.
- When a risk is resolved, set its status to **Closed** but keep the row for historical traceability.
- Link significant risk-driven decisions to their Architecture Decision Records.
