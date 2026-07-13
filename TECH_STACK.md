# Technology Decision Document

This document tracks candidate technologies for the AI Video Factory.
No final choices have been made yet — every candidate is under evaluation and all statuses are **Research**.
Selection follows the project principles: open-source first, self-hostable, modular, and quality over speed.

---

# Programming Languages

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| Python | Rich AI/ML ecosystem, fast to prototype, huge community | Slower runtime, GIL limits parallelism | Research |
| TypeScript / Node.js | Strong for backend + frontend, async-friendly, typed | Weaker native ML support, callback complexity | Research |
| Go | Fast, great concurrency, easy deployment | Smaller AI ecosystem, more verbose | Research |
| Rust | High performance, memory safety, reliable | Steep learning curve, slower development | Research |

# AI Frameworks

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| LangChain | Mature agent/RAG tooling, wide integrations | Heavy abstraction, frequent API changes | Research |
| LlamaIndex | Strong retrieval/knowledge-base focus | Narrower agent orchestration | Research |
| Haystack | Production-oriented, modular pipelines | Smaller community than LangChain | Research |
| Custom / lightweight | Full control, minimal dependencies | More to build and maintain | Research |

# Video Generation

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| Stable Diffusion / SDXL (+ video ext.) | Open-source, self-hostable, active community | Needs strong GPU, quality tuning required | Research |
| AnimateDiff | Adds motion to image models, open | Limited clip length, resource heavy | Research |
| ComfyUI pipelines | Flexible node-based workflows, self-hosted | Complex setup, workflow maintenance | Research |
| Hosted APIs (Runway, Pika) | High quality, no infra needed | Proprietary, ongoing cost, not self-hosted | Research |

# Voice Generation

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| Coqui TTS | Open-source, multi-language, self-hostable | Setup effort, quality varies by voice | Research |
| Piper | Lightweight, fast, runs on modest hardware | Fewer voice options, simpler prosody | Research |
| XTTS | Voice cloning, natural output | Heavier, licensing/usage caveats | Research |
| Hosted APIs (ElevenLabs) | Very natural voices, easy | Proprietary, per-use cost, not self-hosted | Research |

# LLM Providers

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| Llama (self-hosted) | Open weights, private, no per-call cost | Needs GPU, ops overhead | Research |
| Mistral (self-hosted) | Efficient, strong for size, open | Hardware needs, tuning | Research |
| Ollama (local runtime) | Simple local hosting of open models | Limited by local hardware | Research |
| Hosted APIs (Claude, GPT) | Top quality, no infra | Proprietary, recurring cost, external dependency | Research |

# Databases

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| PostgreSQL | Reliable, feature-rich, open-source | Requires tuning at scale | Research |
| SQLite | Zero-config, file-based, simple | Limited concurrency, not for heavy load | Research |
| MongoDB | Flexible schema, easy for documents | Weaker relational queries, memory use | Research |
| Vector DB (Qdrant / Weaviate) | Built for embeddings/RAG, self-hostable | Extra component to operate | Research |

# Backend

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| FastAPI (Python) | Fast, typed, async, great for AI services | Python runtime limits | Research |
| Django (Python) | Batteries-included, mature | Heavier, less async-native | Research |
| Express / NestJS (Node) | Flexible, unified with JS frontend | More manual structure (Express) | Research |
| Go (net/http, Fiber) | Fast, low resource, easy deploy | Smaller AI ecosystem | Research |

# Frontend

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| React | Huge ecosystem, flexible, well-supported | Boilerplate, decision overhead | Research |
| Vue | Approachable, clean, good docs | Smaller ecosystem than React | Research |
| Svelte / SvelteKit | Minimal, fast, less boilerplate | Smaller community | Research |
| Next.js | SSR, full-stack React, strong tooling | Heavier, opinionated | Research |

# Deployment

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| Docker + Compose | Reproducible, self-hosted, simple | Manual scaling | Research |
| Kubernetes | Scalable, resilient orchestration | Complex, heavy for a single server | Research |
| Systemd services | Lightweight, native to the server | Manual, less isolated | Research |
| CI/CD (GitHub Actions / Gitea) | Automated builds and releases | Setup and maintenance effort | Research |

# Monitoring

| Candidate | Pros | Cons | Status |
|---|---|---|---|
| Prometheus + Grafana | Powerful metrics + dashboards, open-source | Setup and storage overhead | Research |
| Loki | Log aggregation, pairs with Grafana | Another component to run | Research |
| Uptime Kuma | Simple self-hosted uptime monitoring | Basic metrics only | Research |
| Sentry (self-hosted) | Detailed error tracking | Resource-heavy self-hosted setup | Research |
