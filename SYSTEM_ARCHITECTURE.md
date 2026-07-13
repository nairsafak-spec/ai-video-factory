# System Architecture — AI Video Factory

This document describes the high-level architecture of the AI Video Factory.
The system is a modular pipeline: each module has a single clear responsibility and communicates through well-defined inputs and outputs, so any component can be replaced or upgraded independently.

---

## Architecture Overview

At a high level, the **Orchestrator** coordinates the flow. **AI Agents** plan and script content using the **Knowledge Base**. The **Workflow Engine** drives the production steps, calling the **Video** and **Voice Generation Engines** to produce media, which the **Asset Manager** stores and versions. The **Scheduler** triggers runs, **Monitoring** observes the whole system, and the **Web Dashboard** provides human oversight and control.

```
Scheduler ──▶ Orchestrator ──▶ Workflow Engine ──▶ Video / Voice Engines
                  │  ▲                 │                     │
              AI Agents ◀── Knowledge Base            Asset Manager
                  │                                          │
              Monitoring ◀───────────────────────────────────┘
                  │
              Web Dashboard (human oversight)
```

---

## Orchestrator

- **Purpose:** The central coordinator that manages the end-to-end lifecycle of a video production job.
- **Responsibilities:**
  - Receive and interpret production requests
  - Coordinate agents, workflows, and engines in the correct order
  - Maintain job state and handle failures/retries
  - Enforce priorities and resource limits
- **Inputs:** Production requests (from Scheduler or Dashboard), module status updates
- **Outputs:** Job commands to other modules, job state and results

## AI Agents

- **Purpose:** The reasoning layer that plans topics, writes scripts, and makes creative/editorial decisions.
- **Responsibilities:**
  - Generate ideas and select topics
  - Produce scripts, scene descriptions, and narration text
  - Review and refine outputs for quality
  - Consult the Knowledge Base for facts and brand rules
- **Inputs:** Job goals from Orchestrator, context from Knowledge Base
- **Outputs:** Scripts, scene/shot plans, narration text, decisions

## Knowledge Base

- **Purpose:** The system's durable memory of facts, sources, brand rules, and past outputs.
- **Responsibilities:**
  - Store and index reference material and prior work
  - Provide retrieval/search for agents
  - Track sources and provenance
  - Version and update knowledge over time
- **Inputs:** Reference material, agent queries, past production records
- **Outputs:** Retrieved context, facts, citations, brand guidelines

## Workflow Engine

- **Purpose:** Executes the defined production pipeline step by step.
- **Responsibilities:**
  - Run production workflows in the correct sequence
  - Manage dependencies between steps
  - Handle step-level retries and error recovery
  - Report progress back to the Orchestrator
- **Inputs:** Workflow definitions, job data from Orchestrator
- **Outputs:** Step results, progress events, completion status

## Video Generation Engine

- **Purpose:** Produces the visual content — scenes, shots, and imagery — from a script and shot plan.
- **Responsibilities:**
  - Generate or assemble visuals per scene
  - Apply format, resolution, and aspect-ratio standards
  - Perform quality checks on generated visuals
  - Return finished visual assets
- **Inputs:** Scene/shot plans, visual prompts, format requirements
- **Outputs:** Video/image assets, generation metadata

## Voice Generation Engine

- **Purpose:** Converts narration text into natural spoken audio.
- **Responsibilities:**
  - Synthesize narration from script text
  - Support multiple voices and languages
  - Normalize and clean the audio
  - Provide timing data for synchronization
- **Inputs:** Narration text, voice/language settings
- **Outputs:** Audio tracks, timing/alignment data

## Asset Manager

- **Purpose:** Stores, organizes, and versions all media and intermediate artifacts.
- **Responsibilities:**
  - Store visuals, audio, and final renders
  - Track versions and relationships between assets
  - Enable reuse and caching of assets
  - Serve assets to other modules on request
- **Inputs:** Generated media, metadata, storage/retrieval requests
- **Outputs:** Stored assets, asset references, version history

## Scheduler

- **Purpose:** Triggers production jobs on a schedule or by defined rules.
- **Responsibilities:**
  - Launch jobs at configured times or intervals
  - Manage batch and recurring production
  - Prevent duplicate or overlapping runs
  - Respect resource and rate constraints
- **Inputs:** Schedules, triggers, configuration
- **Outputs:** Job requests to the Orchestrator

## Monitoring

- **Purpose:** Observes the health, performance, and cost of the entire system.
- **Responsibilities:**
  - Collect logs and metrics from all modules
  - Detect errors, anomalies, and resource issues
  - Raise alerts when thresholds are crossed
  - Provide data for dashboards and analysis
- **Inputs:** Logs, metrics, and events from all modules
- **Outputs:** Metrics, alerts, health reports

## Web Dashboard

- **Purpose:** The human interface for oversight, control, and review.
- **Responsibilities:**
  - Display job status, output, and system health
  - Allow manual triggering, approval, and overrides
  - Present monitoring data and reports
  - Provide access to produced content and history
- **Inputs:** State and metrics from Orchestrator and Monitoring, user actions
- **Outputs:** Views and reports for users, control commands to the system
