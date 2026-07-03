# Design: 010 Release Candidate Polish

Feature: `010-release-candidate-polish`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Design Intent

Feature 010 is a low-risk release-candidate polish pass. It should make the repository feel more coherent, reviewable, and ready for a later release decision without changing runtime behavior.

## Design Principle

Polish the release surface, not the runtime surface.

The implementation phase should focus on:

- wording consistency,
- command consistency,
- docs navigation,
- release checklist clarity,
- version metadata consistency,
- review evidence,
- known-boundary clarity.

## Repository Surfaces To Inspect Later

Implementation should inspect and update only where necessary:

- `README.md`
- `CHANGELOG.md`
- `pyproject.toml`
- `docs/release-checklist.md`
- `docs/v0.1.0-dev-release-notes.md`
- `docs/demo-guide.md`
- `docs/architecture.md`
- `docs/security-model.md`
- `docs/product-positioning.md`
- `scripts/verify_release_candidate.py`

## Expected Shape

The repository should tell one consistent story:

```text
Runtime Tool Authorization for AI Agents
        |
        v
clone -> install -> run demo -> inspect audit -> review docs -> understand boundaries
```

## Review Lens

A reviewer should be able to answer:

1. What is the project?
2. What version/maturity is it?
3. How do I install it locally?
4. How do I run the basic demo?
5. How do I run the guided demo?
6. How do I verify the release candidate locally?
7. What docs explain policy, audit, architecture, demo, and security model?
8. What is intentionally not included?

## Constraints

- Keep changes small and reviewable.
- Prefer docs and metadata edits over runtime edits.
- Preserve all completed feature history.
- Preserve existing feature numbering.
- Keep Feature 010 in `review` after implementation until human closure approval.
