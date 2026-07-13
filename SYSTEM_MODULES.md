# System Modules

The first version of the AI Video Factory module map. It defines the agent modules that make up the production pipeline, each with a single clear responsibility and well-defined inputs and outputs so any module can be developed, replaced, or upgraded independently.

- **Status:** Design — planning phase. This is a conceptual map, not an implementation.
- **Flow (high level):** Research → Planning → Script → Prompts → Image / Video / Voice generation → Editing → Thumbnail → Publish → Analytics → Learning (feedback loop).

---

## 1. Research Agent

- **Purpose:** Discover topics, trends, and reference material worth producing videos about.
- **Inputs:** Topic seeds or goals, knowledge base, external research sources.
- **Outputs:** Ranked research findings and source material for planning.
- **Dependencies:** Knowledge base, LLM, external data/search access.
- **Future Improvements:** Trend scoring, source credibility weighting, deduplication against past topics.

## 2. Planning Agent

- **Purpose:** Turn research into a concrete content plan for a specific video.
- **Inputs:** Research findings, content strategy, brand/guidelines.
- **Outputs:** A structured video plan (angle, key points, target length, format).
- **Dependencies:** Research Agent output, knowledge base, LLM.
- **Future Improvements:** Audience-aware planning, format templates, priority scheduling.

## 3. Script Writer Agent

- **Purpose:** Write the narration script and on-screen text from the plan.
- **Inputs:** Video plan, tone/style guidelines.
- **Outputs:** A structured script (scenes, narration lines, captions).
- **Dependencies:** Planning Agent output, LLM.
- **Future Improvements:** Multi-language scripts, tone variants, length calibration to target duration.

## 4. Prompt Generator Agent

- **Purpose:** Convert the script into precise generation prompts for image, video, and voice.
- **Inputs:** Script, style guidelines, target model constraints.
- **Outputs:** Per-scene prompts for the generation agents (visual, motion, voice).
- **Dependencies:** Script Writer Agent output, reusable prompt library, LLM.
- **Future Improvements:** Model-specific prompt tuning, prompt versioning, automatic prompt refinement from results.

## 5. Image Generation Agent

- **Purpose:** Produce still images and visual assets from prompts.
- **Inputs:** Image prompts, style/reference constraints.
- **Outputs:** Generated images with metadata.
- **Dependencies:** Prompt Generator output, image model, GPU resources, Asset Manager.
- **Future Improvements:** Style consistency across scenes, reference-image conditioning, automated quality checks.

## 6. Video Generation Agent

- **Purpose:** Produce video clips or animated segments from prompts and/or images.
- **Inputs:** Video prompts, source images, duration/motion parameters.
- **Outputs:** Generated video clips with metadata.
- **Dependencies:** Prompt Generator and/or Image Generation output, video model, GPU resources, Asset Manager.
- **Future Improvements:** Longer coherent clips, motion control, resolution upscaling, VRAM-aware scheduling.

## 7. Voice Generation Agent

- **Purpose:** Produce narration audio from the script.
- **Inputs:** Script narration text, voice/style selection.
- **Outputs:** Narration audio tracks with timing metadata.
- **Dependencies:** Script Writer output, TTS model, Asset Manager.
- **Future Improvements:** Voice cloning, multi-language narration, prosody/emotion control.

## 8. Video Editor Agent

- **Purpose:** Assemble clips, images, narration, captions, and music into a finished video.
- **Inputs:** Generated clips, images, voice tracks, captions, timing data.
- **Outputs:** A rendered, ready-to-publish video file.
- **Dependencies:** Image/Video/Voice generation outputs, Asset Manager, media processing tools.
- **Future Improvements:** Automated transitions and pacing, background music, subtitle styling, template-based editing.

## 9. Thumbnail Agent

- **Purpose:** Create an attention-grabbing thumbnail for the video.
- **Inputs:** Video plan/title, key frames or generated imagery, brand style.
- **Outputs:** Thumbnail image variants with metadata.
- **Dependencies:** Image Generation Agent, Asset Manager, LLM (for title/hook text).
- **Future Improvements:** A/B thumbnail variants, click-through optimization, brand-consistent templates.

## 10. Publisher Agent

- **Purpose:** Publish the finished video and metadata to target platforms.
- **Inputs:** Rendered video, thumbnail, title, description, tags, schedule.
- **Outputs:** Published post and a record of the publish result (IDs, status).
- **Dependencies:** Video Editor and Thumbnail outputs, platform APIs, credentials/config.
- **Future Improvements:** Multi-platform publishing, optimal-time scheduling, safe dry-run/preview mode.

## 11. Analytics Agent

- **Purpose:** Collect and summarize performance data on published videos.
- **Inputs:** Publish records, platform metrics (views, watch time, engagement).
- **Outputs:** Structured performance reports per video and over time.
- **Dependencies:** Publisher output, platform analytics APIs, storage.
- **Future Improvements:** Cross-platform aggregation, benchmark comparisons, anomaly detection.

## 12. Learning Agent

- **Purpose:** Turn analytics into insights that improve future productions.
- **Inputs:** Analytics reports, historical performance, production metadata.
- **Outputs:** Learned rules and recommendations fed back into research, planning, and prompts.
- **Dependencies:** Analytics Agent output, knowledge base/memory.
- **Future Improvements:** Confidence-weighted recommendations, automated prompt/plan adjustments, measurable improvement tracking.

---

## Notes

- This map is the **first version** and will evolve; changes to module boundaries should be recorded as ADRs.
- Modules communicate through defined inputs/outputs and shared services (Orchestrator, Knowledge Base, Asset Manager) described in [`SYSTEM_ARCHITECTURE.md`](SYSTEM_ARCHITECTURE.md).
- The Analytics → Learning → Research/Planning path forms the system's continuous improvement loop.
