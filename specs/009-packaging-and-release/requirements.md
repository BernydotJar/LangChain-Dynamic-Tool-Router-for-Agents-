# Requirements: 009 Packaging and Release

Feature: `009-packaging-and-release`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Objective

Prepare the project for a credible developer-preview package and first public release workflow.

## Business Goal

Make the project easier to install, evaluate, tag, and present to CTOs, engineering leaders, design partners, and early users.

## Functional Requirements

1. Add Python packaging metadata.
2. Define a developer-preview version.
3. Preserve editable local install with `python -m pip install -e .`.
4. Add package build instructions.
5. Add release checklist.
6. Add release notes for `v0.1.0-dev`.
7. Update README with packaging/release guidance.
8. Avoid publishing to PyPI in this feature.
9. Avoid creating GitHub releases or tags through this feature unless explicitly requested.
10. Preserve existing tests and examples.

## Non-Goals

- No PyPI publish.
- No GitHub Release creation.
- No automated release workflow.
- No paid packaging or billing integration.
- No production stability claim.

## Acceptance Criteria

- `pyproject.toml` exists and supports editable install.
- Package version is defined.
- Build instructions are documented.
- Release checklist exists.
- README links packaging/release docs.
- `python -m json.tool feature_list.json` passes.
- Unit tests pass.
- Basic example passes.
- Integration tests pass or skip explicitly.
