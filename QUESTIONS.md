# Open Questions

Important technical decisions that are still unanswered.
These are tracked here until resolved; answers and rationale will be documented as decisions are made.

## AI & Models

1. Which open-source LLM should be the project's brain?
2. Should the LLM be fully self-hosted, or is a hosted fallback acceptable?
3. Which video generation model should be used?
4. Which voice synthesis engine should be used?
5. How many languages and voices must voice generation support?

## Agents & Orchestration

6. Which orchestration framework should manage the agents?
7. What agent roles are needed, and where are their boundaries?
8. How should agents communicate with each other?
9. How should agent outputs be reviewed and quality-checked?
10. When should a human be required to approve or override?

## Workflows & Pipeline

11. How should workflows be defined?
12. How should the pipeline handle step failures and retries?
13. Should production run sequentially, in parallel, or in batches?
14. How is job state stored and recovered?

## Data & Knowledge

15. Which database should store long-term memory?
16. Which store should hold embeddings for retrieval?
17. How should the knowledge base be structured and indexed?
18. How are sources and provenance tracked?
19. How is generated media stored, versioned, and reused?

## Learning & Improvement

20. How should the system learn from previous videos?
21. Which performance metrics define a "good" video?
22. How is feedback collected and fed back into agents and prompts?

## Infrastructure & Operations

23. How should the system be deployed on our own server?
24. What are the server's hardware and GPU requirements?
25. How should monitoring, logging, and alerting be implemented?
26. How should secrets and configuration be managed?
27. What is the backup and disaster-recovery strategy?
