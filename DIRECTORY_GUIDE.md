# Directory Guide

This guide documents every top-level folder in the project: its purpose, what belongs in it, what must never be placed there, and its planned future contents. Keep this document updated whenever the directory structure changes.

---

## `docs/`

- **Purpose:** Human-facing project documentation.
- **What belongs there:** Architecture overviews, design decisions, API references, setup and deployment guides, diagrams, and changelogs.
- **What must never be placed there:** Executable code, secrets, credentials, or generated build artifacts.
- **Future planned contents:** Versioned API docs, onboarding handbook, and architecture decision records (ADRs).

---

## `agents/`

- **Purpose:** Autonomous agent definitions that orchestrate the video generation pipeline.
- **What belongs there:** Agent logic, role definitions, prompt templates, and agent-specific tools.
- **What must never be placed there:** API keys or tokens, shared infrastructure code, or frontend assets.
- **Future planned contents:** Specialized agents (research, scripting, voiceover, editing) and a shared agent base class.

---

## `backend/`

- **Purpose:** Server-side application code and business logic.
- **What belongs there:** API endpoints, services, database access layers, job queues, and integration clients.
- **What must never be placed there:** Frontend UI code, large binary media, hardcoded secrets, or trained model weights.
- **Future planned contents:** REST/GraphQL API layer, task orchestration service, and webhook handlers.

---

## `frontend/`

- **Purpose:** Client-facing user interface.
- **What belongs there:** UI components, pages, styles, client-side state, and static frontend assets.
- **What must never be placed there:** Server secrets, backend business logic, or private model artifacts.
- **Future planned contents:** Dashboard, video preview and review UI, and job monitoring views.

---

## `models/`

- **Purpose:** Machine learning model definitions and interfaces.
- **What belongs there:** Model wrappers, inference adapters, and configuration for local or hosted models.
- **What must never be placed there:** Large binary weight files (use external storage or a registry), training datasets, or application logic.
- **Future planned contents:** Model registry references, provider adapters, and evaluation harnesses.

---

## `workflows/`

- **Purpose:** End-to-end pipeline and workflow definitions.
- **What belongs there:** Pipeline stage definitions, step orchestration, and workflow configuration.
- **What must never be placed there:** One-off scripts, secrets, or generated output.
- **Future planned contents:** Reusable pipeline templates, conditional branching flows, and retry/recovery policies.

---

## `scripts/`

- **Purpose:** Operational and developer utility scripts.
- **What belongs there:** Setup, deployment, migration, maintenance, and one-off automation scripts.
- **What must never be placed there:** Core application logic, secrets, or persistent data.
- **Future planned contents:** CI helpers, database migration runners, and local environment bootstrap scripts.

---

## `configs/`

- **Purpose:** Configuration files that drive behavior across environments.
- **What belongs there:** Non-secret settings, environment templates (e.g. `.env.example`), feature flags, and brand/profile config.
- **What must never be placed there:** Real secrets, credentials, or API keys — these belong in a secret manager or ignored environment files.
- **Future planned contents:** Per-environment config sets (dev/staging/prod) and schema validation for configs.

---

## `data/`

- **Purpose:** Structured working data used and produced by the pipeline.
- **What belongs there:** Input datasets, intermediate results, and small reference data.
- **What must never be placed there:** Secrets, source code, or large media better suited to `assets/` or external storage.
- **Future planned contents:** Cached research data, job state records, and processed metadata stores.

---

## `assets/`

- **Purpose:** Static and generated media assets.
- **What belongs there:** Images, audio, video, fonts, and brand media.
- **What must never be placed there:** Source code, secrets, or configuration.
- **Future planned contents:** Generated video outputs, thumbnails, and reusable brand asset libraries (managed via appropriate large-file storage).

---

## `tests/`

- **Purpose:** Automated tests that verify the system.
- **What belongs there:** Unit, integration, and end-to-end tests, along with fixtures and test helpers.
- **What must never be placed there:** Production code, real credentials, or production data.
- **Future planned contents:** Coverage for each backend service, agent behavior tests, and pipeline smoke tests.
