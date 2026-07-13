# Infrastructure

Infrastructure-as-code and operational configuration for self-hosting the AI Video Factory. This is the foundation for deploying and running the system on our own infrastructure. Folders are currently placeholders; contents will be added as the platform is built.

## Folder Purpose

| Folder | Purpose |
|---|---|
| `docker/` | Dockerfiles and image build context for the project's services. |
| `compose/` | Docker Compose files that define and wire services together for local and server deployment. |
| `nginx/` | Nginx reverse-proxy and web server configuration (routing, TLS, upstreams). |
| `monitoring/` | Monitoring, metrics, logging, and alerting configuration for observing the system. |
| `scripts/` | Deployment and operational scripts (setup, backup, maintenance, provisioning). |

## Conventions

- Never commit secrets or credentials here — use environment variables or a secret manager.
- Keep configuration environment-agnostic where possible; parameterize per-environment values.
- Document any non-obvious operational step alongside the relevant configuration.
