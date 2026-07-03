# SHIP Review

Feature: `009-packaging-and-release`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

State Change: `in_progress -> review`

Reviewer: Codex implementation self-check; human closure approval still required before `done`.

## Summary

Pass/Fail: Pass for SHIP review readiness.

Feature 009 has local release-candidate verification evidence for the developer-preview package. No PyPI publish, GitHub Release, or git tag was created.

## Files Changed

- `pyproject.toml`
- `README.md`
- `CHANGELOG.md`
- `docs/release-checklist.md`
- `docs/v0.1.0-dev-release-notes.md`
- `scripts/verify_release_candidate.py`
- `specs/009-packaging-and-release/requirements.md`
- `specs/009-packaging-and-release/design.md`
- `specs/009-packaging-and-release/tasks.md`
- `progress/009-packaging-and-release.md`
- `progress/current.md`
- `progress/history.md`
- `progress/review_009-packaging-and-release.md`
- `feature_list.json`

## Verification Commands

Primary verifier:

```sh
python scripts/verify_release_candidate.py
```

Manual equivalent executed by the verifier:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python -m pip install -e .
python -m pip install -e .[dev]
python -m build
```

## Verification Result

Passed:

```text
PASS: feature registry JSON
PASS: unit tests
PASS: basic demo
PASS: integration tests
PASS: editable install
PASS: editable install with dev extra
PASS: package build
Release candidate verification completed.
```

Detailed observations:

- Unit discovery: `Ran 23 tests in 0.007s`, `OK (skipped=2)`.
- Basic demo passed and printed injected tools, fallback routing, audit events, and audit export path.
- Integration discovery: `Ran 2 tests in 0.000s`, `OK (skipped=2)`.
- Editable install passed for `langchain-dynamic-tool-router==0.1.0.dev0`.
- Dev extra install passed and installed `build`.
- Package build passed and produced sdist and wheel artifacts under ignored `dist/`.

## Packaging Assessment

- Package name is configured as `langchain-dynamic-tool-router`.
- Version is `0.1.0.dev0`.
- Core dependencies remain empty.
- Optional extras are present for `integrations` and `dev`.
- Local editable install passes.
- Local package build passes.
- Setuptools emitted deprecation warnings for the license table and license classifier format. These are not blocking for the developer preview, but should be fixed before a stable release.

## Release-Readiness Assessment

Ready for human review as a developer-preview release candidate.

Not ready for unattended production release, PyPI publish, GitHub Release, or git tag creation without maintainer approval.

The release docs correctly frame this as a developer preview for Runtime Tool Authorization for AI Agents. They do not claim hosted IAM, compliance, managed SaaS, or production security readiness.

## Known Limitations

- Optional LangChain/LangGraph integration tests skip unless optional dependencies are installed.
- No package upload was performed.
- No git tag was created.
- No GitHub Release was created.
- Build emits setuptools deprecation warnings for license metadata.
- Developer preview does not imply production security, compliance readiness, or hosted IAM behavior.

## Recommendation

- Approve Feature 009 for human review.
- Keep Feature 009 at `review` until explicit closure approval.
- Before a non-preview release, update license metadata to the modern SPDX format and run verification in CI.
