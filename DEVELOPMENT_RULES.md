# Development Rules

Development workflow standards for this project. These rules are mandatory for all contributions.

## Version Control

- **Commit every change.** No work stays only in the working tree — if it exists, it is committed.
- **One logical change per commit.** Keep commits atomic; don't mix unrelated changes.
- **Write clear commit messages.** State what changed and why, in the imperative mood (e.g. "Bind brand constants to profile loader").
- **Never push broken code.** Lint, build, and test locally before pushing. A broken main branch blocks everyone.
- **Review before merge.** Every change is reviewed by another person (or a deliberate second pass) before landing on a shared branch.

## Code Quality

- **Keep files small and modular.** Split large files into focused units with a single responsibility.
- **Prefer configuration over hardcoding.** Move brand values, credentials, IDs, paths, and tunables into config files or environment variables instead of embedding them in code.
- **Avoid unnecessary dependencies.** Add a library only when it earns its weight; every dependency is a maintenance and security cost.

## Documentation

- **Update documentation when architecture changes.** If behavior, structure, or configuration changes, update the relevant docs in the same commit or PR.

## Mindset

- **Always think long-term.** Optimize for maintainability and clarity over short-term convenience. Leave the codebase easier to change than you found it.
