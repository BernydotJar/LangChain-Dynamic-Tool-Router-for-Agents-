# Tasks: 010 Release Candidate Polish

Feature: `010-release-candidate-polish`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Register Feature 010 as `spec_ready`.
- [x] Update `progress/current.md`.
- [x] Update `progress/history.md`.

## Phase 2: Approval Gate

- [x] Wait for explicit human approval.
- [x] Move Feature 010 from `spec_ready` to `approved` only after approval.
- [x] Do not implement before approval.

## Phase 3: Implementation Candidates

Implementation scope should be confirmed after approval. Candidate tasks:

- [x] Inspect README for release-candidate consistency.
- [x] Inspect CHANGELOG for `0.1.0.dev0` readiness.
- [x] Inspect package metadata.
- [x] Inspect release checklist.
- [x] Inspect developer-preview release notes.
- [x] Inspect demo guide command consistency.
- [x] Inspect architecture and security-model cross-links.
- [x] Inspect verification script documentation.
- [x] Apply small documentation or metadata fixes only where necessary.

## Phase 4: Verification Candidates

Run after implementation:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```

Manual checks:

- [x] README commands are consistent.
- [x] Demo guide commands are consistent.
- [x] Release notes and checklist are consistent.
- [x] Known boundaries are stated consistently.
- [x] No accidental release action was performed.
- [x] No runtime behavior changed unless explicitly approved.

## Phase 5: Review

Create:

- [x] `progress/review_010-release-candidate-polish.md`

Move Feature 010 to `review`, not `done`, after verification.
