# 009 Packaging and Release Progress

Feature: `009-packaging-and-release`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## State

Status: `done`

## Summary

Feature 009 prepares the repository for a credible developer-preview package and first public release workflow. Implementation and local verification are complete, and human closure approval was received.

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
- [x] local verification evidence
- [x] package build verification evidence
- [x] review artifact

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

## Verification Evidence

Passed:

```sh
python scripts/verify_release_candidate.py
# PASS: feature registry JSON
# PASS: unit tests
# PASS: basic demo
# PASS: integration tests
# PASS: editable install
# PASS: editable install with dev extra
# PASS: package build
# Release candidate verification completed.
```

The verifier executed:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python -m pip install -e .
python -m pip install -e .[dev]
python -m build
```

Observed test and build results:

- Unit discovery: `Ran 23 tests in 0.007s`, `OK (skipped=2)`.
- Integration discovery: `Ran 2 tests in 0.000s`, `OK (skipped=2)`.
- Package build created `langchain_dynamic_tool_router-0.1.0.dev0.tar.gz` and `langchain_dynamic_tool_router-0.1.0.dev0-py3-none-any.whl`.
- Setuptools emitted deprecation warnings for `project.license` table format and license classifier usage. The build still passed; cleanup is a recommended follow-up before a non-preview release.

## Manual Checks

- Package metadata is accurate.
- README release section does not claim PyPI publication.
- Release checklist does not create tags without maintainer approval.
- `v0.1.0-dev` notes clearly state developer-preview limitations.

## Review Artifact

Created:

```text
progress/review_009-packaging-and-release.md
```

## Next Valid Lifecycle Action

Closed after human approval:

```text
FEATURE: 009-packaging-and-release
MODE: SHIP
STATE CHANGE: review -> done
```

## Accepted Limitations

- No PyPI publish.
- No git tag.
- No GitHub Release.
- Setuptools license metadata deprecation warning is documented as a non-blocking follow-up for a future non-preview release.
