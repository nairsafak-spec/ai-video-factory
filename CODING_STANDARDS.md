# Coding Standards

Project-wide coding standards. These rules are technology-agnostic and apply to every language and component in the codebase. Consistency takes precedence over personal preference.

---

## Naming Conventions

- Use descriptive, intention-revealing names; avoid abbreviations and single letters except for well-known loop indices.
- Names describe **what** something is or does, not **how** it is implemented.
- Booleans read as predicates: `is_ready`, `has_access`, `should_retry`.
- Avoid encoding type or scope into names (no Hungarian notation).
- Be consistent: the same concept uses the same word everywhere.

## Folder Conventions

- Each folder has a single, clear responsibility documented in the directory guide.
- Group by domain or feature, not by incidental file type.
- Keep nesting shallow; deep hierarchies signal a structure that needs flattening.
- Never mix source code, configuration, secrets, and generated artifacts in the same folder.

## File Naming Rules

- One primary unit (module, class, or component) per file; the file name matches that unit.
- Use a single, consistent casing style per language and never mix styles within a directory.
- Names are lowercase where the platform is case-insensitive, to avoid collisions.
- No spaces or special characters; use hyphens or underscores as the project convention dictates.
- Test files clearly mirror the unit they cover (e.g. `<unit>.test` / `test_<unit>`).

## Function Naming

- Functions are named with a verb or verb phrase describing their action: `fetch_profile`, `render_frame`.
- One function does one thing; if the name needs "and", split it.
- Keep functions short and focused; extract nested logic into named helpers.
- Side-effecting functions make the effect explicit in the name.

## Class Naming

- Classes are nouns or noun phrases naming the concept they model.
- One responsibility per class; avoid "manager"/"util" catch-alls.
- Interfaces and abstract types express a capability or role.
- Keep public surfaces minimal; expose behavior, not internal state.

## Configuration Rules

- Prefer configuration over hardcoding for any value that varies by environment, brand, or deployment.
- Store non-secret settings in versioned config files; provide a documented template for required values.
- Never commit real secrets — load them from environment variables or a secret manager.
- Validate configuration at startup and fail fast with a clear message when required values are missing.
- Provide safe defaults and degrade gracefully when optional configuration is absent.

## Logging Rules

- Log meaningful events: start/stop of operations, external calls, and failures.
- Use consistent, appropriate levels: debug, info, warn, error.
- Log structured, contextual data (identifiers, timing) — never raw secrets, tokens, or personal data.
- Logs are for diagnosis, not control flow; never depend on log output for correctness.
- Keep messages actionable: state what happened and, where possible, what to do.

## Error Handling Rules

- Handle errors deliberately; never silently swallow them.
- Fail fast on programmer errors; degrade gracefully on expected operational errors.
- Catch narrowly — only errors you can meaningfully handle — and let others propagate.
- Add context when re-raising so the failure can be traced to its source.
- Always release resources on failure paths; leave the system in a consistent state.
- Return clear, user-safe error messages; keep internal details out of external responses.

## Documentation Rules

- Every module, public function, and class has a short description of its purpose and contract.
- Comments explain **why**, not **what** the code already shows.
- Update documentation in the same change that alters behavior, structure, or configuration.
- Keep READMEs and guides current; outdated docs are treated as defects.
- Prefer clear code and names over comments that compensate for unclear code.

## Security Rules

- Never hardcode credentials, tokens, or keys; never commit them to version control.
- Treat all external input as untrusted: validate, sanitize, and enforce boundaries.
- Apply least privilege to access, permissions, and dependencies.
- Keep dependencies minimal and updated; review them for known vulnerabilities.
- Never log or expose sensitive data; encrypt secrets in transit and at rest.
- Confirm and gate irreversible or outward-facing actions.
