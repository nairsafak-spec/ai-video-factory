# Open-Source Shortlist — Autonomous AI Video Factory

A research shortlist of leading open-source projects across the stack needed to build an autonomous AI Video Factory. This is **research only** — no final selections have been made. Every entry is marked `Research`. Verify licenses, hardware requirements, and current activity before any decision.

> **Legend** — *Self-hosted*: can run on your own infrastructure. *Community Activity*: relative momentum (stars, commits, releases) at time of research. Assessments are indicative, not exhaustive.

---

## LLMs (Open Models & Serving)

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| Llama (Meta) | https://github.com/meta-llama/llama-models | Strong general quality, broad ecosystem, many fine-tunes | Community license (not pure OSI), large VRAM for big variants | Yes | Very High | Research |
| Mistral / Mixtral | https://github.com/mistralai/mistral-inference | Efficient, Apache-2.0 weights, strong per-parameter quality | Smaller model family than some rivals | Yes | High | Research |
| Qwen | https://github.com/QwenLM/Qwen | Multilingual, many sizes, strong benchmarks | Governance/geo considerations for some orgs | Yes | Very High | Research |
| DeepSeek | https://github.com/deepseek-ai/DeepSeek-V3 | Strong reasoning/coding, cost-efficient MoE | Very large flagship needs heavy hardware | Yes | High | Research |
| Gemma (Google) | https://github.com/google-deepmind/gemma | Compact, permissive terms, good small-model quality | Trails frontier models on hardest tasks | Yes | High | Research |
| vLLM (serving) | https://github.com/vllm-project/vllm | High-throughput inference, wide model support | Ops complexity; GPU-focused | Yes | Very High | Research |
| Ollama (serving) | https://github.com/ollama/ollama | Trivial local setup, great DX | Less tuned for large-scale serving | Yes | Very High | Research |

---

## Agent Frameworks

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| LangGraph | https://github.com/langchain-ai/langgraph | Graph-based control, stateful multi-agent flows | Learning curve; LangChain coupling | Yes | Very High | Research |
| CrewAI | https://github.com/crewAIInc/crewAI | Simple role/task model, fast to prototype | Less control for complex branching | Yes | Very High | Research |
| AutoGen (Microsoft) | https://github.com/microsoft/autogen | Mature multi-agent conversations, tooling | API churn across versions | Yes | Very High | Research |
| LlamaIndex | https://github.com/run-llama/llama_index | Strong data/RAG + agent workflows | Broad surface can feel heavy | Yes | Very High | Research |
| Semantic Kernel | https://github.com/microsoft/semantic-kernel | Enterprise-friendly, multi-language | Heavier abstractions | Yes | High | Research |
| OpenHands | https://github.com/All-Hands-AI/OpenHands | Capable autonomous coding/task agents | Resource-hungry; evolving fast | Yes | Very High | Research |

---

## Video Generation

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| HunyuanVideo (Tencent) | https://github.com/Tencent/HunyuanVideo | High-quality text-to-video, open weights | Very high VRAM, slow generation | Yes | High | Research |
| CogVideoX (THUDM) | https://github.com/THUDM/CogVideo | Strong quality, active releases, image/text-to-video | Heavy compute; length limits | Yes | High | Research |
| Mochi 1 (Genmo) | https://github.com/genmoai/models | Strong motion fidelity, permissive license | Large model, demanding hardware | Yes | Medium | Research |
| Open-Sora | https://github.com/hpcaitech/Open-Sora | Fully open pipeline, training code included | Quality trails closed leaders | Yes | High | Research |
| LTX-Video (Lightricks) | https://github.com/Lightricks/LTX-Video | Fast, efficient, real-time-ish generation | Fidelity trade-off vs. larger models | Yes | High | Research |
| Stable Video Diffusion | https://github.com/Stability-AI/generative-models | Established, image-to-video, tooling support | Short clips; older architecture | Yes | High | Research |

---

## Image Generation

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| FLUX (Black Forest Labs) | https://github.com/black-forest-labs/flux | State-of-the-art quality, strong prompt adherence | Large models; license varies by variant | Yes | Very High | Research |
| Stable Diffusion / SDXL | https://github.com/Stability-AI/generative-models | Huge ecosystem, LoRAs, fine-tunes | Base quality trails newest models | Yes | Very High | Research |
| ComfyUI | https://github.com/comfyanonymous/ComfyUI | Node-based pipelines, extremely flexible | Complexity; graph management overhead | Yes | Very High | Research |
| Fooocus | https://github.com/lllyasviel/Fooocus | Simple UX, good defaults | Less flexible for advanced pipelines | Yes | High | Research |
| Kolors | https://github.com/Kwai-Kolors/Kolors | Strong bilingual text rendering, photorealism | Smaller ecosystem | Yes | Medium | Research |

---

## Voice Generation (TTS)

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| Coqui TTS / XTTS | https://github.com/coqui-ai/TTS | Multilingual, voice cloning, mature | Original org wound down; community-maintained | Yes | High | Research |
| F5-TTS | https://github.com/SWivid/F5-TTS | High-quality, fast zero-shot cloning | Newer; smaller tooling ecosystem | Yes | High | Research |
| Piper | https://github.com/rhasspy/piper | Lightweight, fast, runs on edge devices | Lower naturalness than large models | Yes | High | Research |
| OpenVoice (MyShell) | https://github.com/myshell-ai/OpenVoice | Flexible voice cloning, tone control | Quality varies across languages | Yes | High | Research |
| StyleTTS 2 | https://github.com/yl4579/StyleTTS2 | Very natural prosody | Setup/training complexity | Yes | Medium | Research |
| Kokoro | https://github.com/hexgrad/kokoro | Tiny, efficient, strong quality-for-size | Limited voices/languages | Yes | High | Research |

---

## Lip Sync

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| LatentSync (ByteDance) | https://github.com/bytedance/LatentSync | High-fidelity diffusion-based sync | Heavy compute | Yes | High | Research |
| MuseTalk | https://github.com/TMElyralab/MuseTalk | Real-time capable, good quality | Face-region constraints | Yes | High | Research |
| SadTalker | https://github.com/OpenTalker/SadTalker | Single-image talking head, expressive | Artifacts on large motion | Yes | High | Research |
| Wav2Lip | https://github.com/Rudrabha/Wav2Lip | Robust, widely used baseline | Low-res mouth region, dated quality | Yes | High | Research |
| Hallo | https://github.com/fudan-generative-vision/hallo | Natural, audio-driven portrait animation | Slow; high VRAM | Yes | Medium | Research |

---

## Workflow Automation

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| n8n | https://github.com/n8n-io/n8n | Visual flows, 400+ integrations, AI nodes | Fair-code license nuances | Yes | Very High | Research |
| Temporal | https://github.com/temporalio/temporal | Durable, reliable long-running workflows | Operationally heavy | Yes | Very High | Research |
| Prefect | https://github.com/PrefectHQ/prefect | Pythonic orchestration, good DX | Python-centric | Yes | High | Research |
| Apache Airflow | https://github.com/apache/airflow | Mature, battle-tested scheduling | Verbose; heavier for dynamic flows | Yes | Very High | Research |
| Windmill | https://github.com/windmill-labs/windmill | Scripts + flows + internal UIs, fast | Younger ecosystem | Yes | High | Research |
| Dagster | https://github.com/dagster-io/dagster | Asset-oriented, strong observability | Concepts have a learning curve | Yes | High | Research |

---

## Vector Databases

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| Qdrant | https://github.com/qdrant/qdrant | Fast, Rust, rich filtering, easy ops | Fewer enterprise features than giants | Yes | Very High | Research |
| Milvus | https://github.com/milvus-io/milvus | Scales to billions, mature | Heavier to operate at small scale | Yes | Very High | Research |
| Weaviate | https://github.com/weaviate/weaviate | Hybrid search, modules, GraphQL API | Resource use; opinionated model | Yes | Very High | Research |
| Chroma | https://github.com/chroma-core/chroma | Simple, great for prototyping | Less proven at large scale | Yes | Very High | Research |
| pgvector | https://github.com/pgvector/pgvector | Reuses Postgres, transactional, simple stack | Not specialized ANN performance ceiling | Yes | Very High | Research |
| LanceDB | https://github.com/lancedb/lancedb | Embedded, fast, multimodal-friendly | Younger; smaller ecosystem | Yes | High | Research |

---

## Memory Systems

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| Mem0 | https://github.com/mem0ai/mem0 | Simple agent memory layer, popular API | Young; evolving abstractions | Yes | Very High | Research |
| Letta (MemGPT) | https://github.com/letta-ai/letta | Persistent agent state, memory tiers | Heavier framework footprint | Yes | High | Research |
| Zep | https://github.com/getzep/zep | Long-term memory + retrieval for chat | Opinionated; extra service to run | Yes | High | Research |
| Cognee | https://github.com/topoteretes/cognee | Knowledge-graph-backed memory | Newer; smaller community | Yes | Medium | Research |
| txtai | https://github.com/neuml/txtai | All-in-one embeddings/search/memory | Broad scope vs. specialized tools | Yes | High | Research |

---

## Web UI Frameworks

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| Next.js (React) | https://github.com/vercel/next.js | Full-stack, huge ecosystem, production-grade | Complexity for simple apps | Yes | Very High | Research |
| SvelteKit | https://github.com/sveltejs/kit | Lean, fast, great DX | Smaller ecosystem than React | Yes | High | Research |
| Nuxt (Vue) | https://github.com/nuxt/nuxt | Batteries-included Vue framework | Vue-only; some abstraction overhead | Yes | High | Research |
| Gradio | https://github.com/gradio-app/gradio | Fastest path to ML demos/UIs | Limited for complex product UIs | Yes | Very High | Research |
| Streamlit | https://github.com/streamlit/streamlit | Rapid data/AI dashboards in Python | Reruns model; less UI control | Yes | Very High | Research |

---

## Speech-to-Text & Subtitles

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| Whisper (OpenAI) | https://github.com/openai/whisper | Accurate multilingual ASR, robust to noise | Vanilla is slow; no word-level timing | Yes | Very High | Research |
| faster-whisper | https://github.com/SYSTRAN/faster-whisper | CTranslate2 speed + low memory | Requires extra setup vs. reference | Yes | Very High | Research |
| WhisperX | https://github.com/m-bain/whisperX | Word-level timestamps, alignment, diarization | Dependency-heavy pipeline | Yes | High | Research |
| whisper.cpp | https://github.com/ggml-org/whisper.cpp | Runs on CPU/edge, portable, no GPU needed | Fewer high-level features | Yes | Very High | Research |

---

## Music & Sound Generation

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| AudioCraft / MusicGen (Meta) | https://github.com/facebookresearch/audiocraft | High-quality music + sound generation | Some weights are non-commercial (CC-BY-NC) | Yes | High | Research |
| Stable Audio Open | https://github.com/Stability-AI/stable-audio-tools | Open weights, music and sound effects | Short durations; setup complexity | Yes | Medium | Research |
| YuE | https://github.com/multimodal-art-projection/YuE | Full-song (lyrics-to-music) generation | Very compute-heavy; newer project | Yes | Medium | Research |

---

## Video Editing & Assembly

| Project | GitHub URL | Strengths | Weaknesses | Self-hosted | Community Activity | Status |
|---|---|---|---|---|---|---|
| FFmpeg | https://github.com/FFmpeg/FFmpeg | Universal media processing; the pipeline glue | Low-level; steep CLI learning curve | Yes | Very High | Research |
| MoviePy | https://github.com/Zulko/moviepy | Pythonic clip editing/composition | Performance limits on large jobs | Yes | High | Research |
| Remotion | https://github.com/remotion-dev/remotion | Programmatic video via React, templating | Company-use license restrictions | Yes | Very High | Research |
| Auto-Editor | https://github.com/WyattBlue/auto-editor | Automated silence/scene trimming | Narrow scope (pre/post step) | Yes | Medium | Research |

---

## Notes

- All entries are **research candidates only**; none is endorsed or selected.
- Confirm each project's **license** against project requirements before adoption.
- Re-check **community activity** and maintenance status at decision time — this landscape moves quickly.
- Consider **hardware/VRAM** budgets for generation models; several video/lip-sync options are compute-intensive.
