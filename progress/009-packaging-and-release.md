# 009 Packaging and Release Progress

Feature: `009-packaging-and-release`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## State

Status: `in_progress`

## Summary

Feature 009 prepares the repository for a credible developer-preview package and first public release workflow.

## Preconditions

- Feature 001: `done`
- Feature 002: `done`
- Feature 003: `done`
- Feature 004: `done`
- Feature 005: `done`
- Feature 006: `done`

## Scope

- [x] requirements
- [x] design
- [x] tasks
- [x] feature registry update
- [x] `pyproject.toml` updated
- [x] package version set to `0.1.0.dev0`
- [x] release checklist added
- [x] `v0.1.0-dev` release notes added
- [x] README packaging/release section added
- [x] CHANGELOG updated
- [x] release candidate verifier script added
- [ ] local verification evidence
- [ ] package build verification evidence
- [ ] review artifact

## Release Candidate Verifier

Run:

```sh
python scripts/verify_release_candidate.py
```

The script runs the local release-candidate checks without publishing packages, creating tags, or creating GitHub releases.

## Required Verification

Manual command sequence:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python -m pip install -e .
python -m pip install -e .[dev]
python -m build
```

If `python -m build` cannot run because the build package is unavailable, install the dev extra first and retry.

## Manual Checks

- Package metadata is accurate.
- README release section does not claim PyPI publication.
- Release checklist does not create tags without maintainer approval.
- `v0.1.0-dev` notes clearly state developer-preview limitations.

## Next Valid Lifecycle Action

After local verification passes, create:

```text
progress/review_009-packaging-and-release.md
```

Then move Feature 009 from `in_progress` to `review`.
