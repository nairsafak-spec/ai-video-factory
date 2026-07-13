# Documentation Standards

Standards for writing and maintaining project documentation. They are technology-agnostic and apply to all docs in the repository. Documentation is part of the deliverable, not an afterthought — it is written, reviewed, and versioned alongside the code.

---

## README Standards

- Every project and significant module has a README.
- A README covers, in order: purpose, prerequisites, setup, usage, configuration, and where to find deeper docs.
- Lead with what the reader needs first; keep the top of the file scannable.
- Keep it current — an outdated README is treated as a defect.

## Markdown Style

- One top-level `#` heading per file; nest headings logically without skipping levels.
- Prefer short paragraphs, lists, and tables over dense prose.
- Use fenced code blocks with a language hint for all commands and snippets.
- Use backticks for file names, commands, and identifiers.
- Keep line length reasonable and formatting consistent across all documents.

## Architecture Documentation

- Maintain a high-level overview describing components, responsibilities, and how they interact.
- Document data flow and integration boundaries, not implementation minutiae.
- Update architecture docs in the same change that alters structure or behavior.
- Pair narrative with diagrams where they aid understanding.

## Decision Records

- Record significant technical decisions as Architecture Decision Records (ADRs).
- Each ADR states: context, the decision, alternatives considered, and consequences.
- ADRs are immutable once accepted; supersede rather than edit them.
- Number and store ADRs together so history is easy to trace.

## API Documentation

- Document every public interface: purpose, inputs, outputs, errors, and side effects.
- Keep API docs adjacent to the code and update them with every contract change.
- Include at least one usage example per endpoint or public operation.
- Clearly mark deprecated and experimental surfaces.

## Change Logs

- Maintain a changelog capturing notable changes per release.
- Group entries by type (added, changed, fixed, removed, security).
- Write entries for humans: what changed and why it matters.
- Keep an "unreleased" section updated as changes land.

## Examples

- Provide runnable, minimal examples that demonstrate real usage.
- Keep examples current and verify they work; broken examples are defects.
- Prefer small, focused examples over exhaustive ones.
- Never include real secrets or credentials in examples.

## Diagrams

- Use diagrams to clarify architecture, flows, and relationships.
- Keep diagrams simple, labeled, and focused on one idea.
- Prefer text-based, version-controllable diagram sources where possible.
- Keep diagrams in sync with the system they describe.

## Versioning

- Version documentation alongside the code it describes.
- Note the applicable version or date on docs that can drift.
- When behavior changes across versions, document the differences and migration steps.
- Archive rather than delete documentation for still-supported older versions.

## Review Process

- All documentation changes go through the same review as code.
- Reviewers check for accuracy, clarity, completeness, and consistency with these standards.
- Documentation updates ship together with the change they describe.
- Correct or remove documentation as soon as it becomes inaccurate.
