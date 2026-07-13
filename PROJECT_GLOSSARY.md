# Project Glossary

Shared definitions for key terms used across the Autonomous AI Video Factory. Consistent language keeps documentation, decisions, and discussions unambiguous. Terms are listed alphabetically.

---

### Agent
**Definition:** An autonomous software component that perceives context, makes decisions, and takes actions toward a goal, often using an LLM and tools.
**Why it matters:** Agents drive the factory's autonomy — planning, scripting, generating, and assembling videos with minimal human intervention.

### API (Application Programming Interface)
**Definition:** A defined contract that lets software components communicate programmatically.
**Why it matters:** Every model, service, and integration in the pipeline is connected through APIs; stable APIs make the system modular and swappable.

### Context Window
**Definition:** The maximum amount of text (measured in tokens) an LLM can consider at once, including input and output.
**Why it matters:** It bounds how much instruction, memory, and reference material an agent can use per step; exceeding it forces truncation or summarization.

### Embedding
**Definition:** A numerical vector representation of content (text, image, audio) that captures its meaning for similarity comparison.
**Why it matters:** Embeddings power semantic search and memory retrieval, enabling agents to find relevant prior content and knowledge.

### Fine-tuning
**Definition:** Further training of a pre-trained model on specific data to specialize its behavior or style.
**Why it matters:** May be used to tailor generation (voice, visual style, brand tone) beyond what prompting alone achieves.

### GPU (Graphics Processing Unit)
**Definition:** Specialized hardware for massively parallel computation, essential for AI model training and inference.
**Why it matters:** Video, image, and voice generation are GPU-bound; available VRAM is a primary constraint on which models can run locally.

### Inference
**Definition:** Running a trained model to produce an output from a given input.
**Why it matters:** Every generation step (text, image, video, voice) is an inference call; its speed and cost shape pipeline performance and budget.

### LLM (Large Language Model)
**Definition:** A neural network trained on large text corpora to understand and generate natural language.
**Why it matters:** LLMs are the reasoning core for agents — scripting, planning, and decision-making throughout the factory.

### Memory
**Definition:** Stored state that lets agents recall past interactions, decisions, and produced content across steps or sessions.
**Why it matters:** Memory gives the system continuity and learning, avoiding repetition and improving consistency over time.

### Model
**Definition:** A trained artifact that maps inputs to outputs for a task (e.g. text, image, video, or speech generation).
**Why it matters:** Models are the interchangeable engines of the factory; selecting and evaluating them is central to the project.

### Open Source
**Definition:** Software whose source is publicly available under a license permitting use, study, modification, and distribution.
**Why it matters:** The project favors open-source tools for control, transparency, cost, and independence from vendors.

### Orchestrator
**Definition:** The component that coordinates multiple agents, models, and services, directing the overall flow of work.
**Why it matters:** It turns individual capabilities into a coherent end-to-end pipeline and enforces order, retries, and error handling.

### Pipeline
**Definition:** An ordered sequence of processing stages that transforms an input into a finished output.
**Why it matters:** The video factory is fundamentally a pipeline (idea → script → media → assembly → publish); clear stages enable measurement and optimization.

### Prompt
**Definition:** The instruction or input given to a model to elicit a desired response.
**Why it matters:** Prompt quality directly affects output quality; prompt templates are a core, reusable asset of the system.

### Queue
**Definition:** A buffer that holds tasks awaiting processing, typically handled in order.
**Why it matters:** Queues decouple pipeline stages, smooth load, and enable reliable, scalable, asynchronous processing.

### RAG (Retrieval-Augmented Generation)
**Definition:** A technique that retrieves relevant external information and supplies it to a model to ground its output.
**Why it matters:** RAG lets agents use current, project-specific knowledge instead of relying only on the model's training data.

### Scheduler
**Definition:** A component that decides when and in what order tasks or jobs run, including recurring ones.
**Why it matters:** Automation depends on scheduling — triggering generation, publishing, and maintenance jobs at the right times.

### Self-hosted
**Definition:** Software run on infrastructure you control rather than a third-party managed service.
**Why it matters:** Self-hosting gives data control, cost predictability, and freedom from lock-in — a core project preference.

### Vector Database
**Definition:** A database optimized for storing and searching embeddings by similarity.
**Why it matters:** It underpins memory and RAG, letting the system retrieve semantically related content quickly at scale.

### Workflow
**Definition:** A defined set of steps and rules describing how a particular process is carried out.
**Why it matters:** Workflows encode repeatable processes (e.g. producing one video), making automation predictable and maintainable.
