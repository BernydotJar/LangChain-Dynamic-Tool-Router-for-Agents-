# Tasks: 010 Release Candidate Polish

Feature: `010-release-candidate-polish`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Phase 1: Spec Gate

- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [ ] Create ADR.
- [ ] Create progress artifact.
- [ ] Register Feature 010 as `spec_ready`.
- [ ] Update `progress/current.md`.
- [ ] Update `progress/history.md`.

## Phase 2: Approval Gate

- [ ] Wait for explicit human approval.
- [ ] Move Feature 010 from `spec_ready` to `approved` only after approval.
- [ ] Do not implement before approval.

## Phase 3: Implementation Candidates

Implementation scope should be confirmed after approval. Candidate tasks:

- [ ] Inspect README for release-candidate consistency.
- [ ] Inspect CHANGELOG for `0.1.0.dev0` readiness.
- [ ] Inspect package metadata.
- [ ] Inspect release checklist.
- [ ] Inspect developer-preview release notes.
- [ ] Inspect demo guide command consistency.
- [ ] Inspect architecture and security-model cross-links.
- [ ] Inspect verification script documentation.
- [ ] Apply small documentation or metadata fixes only where necessary.

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

- [ ] README commands are consistent.
- [ ] Demo guide commands are consistent.
- [ ] Release notes and checklist are consistent.
- [ ] Known boundaries are stated consistently.
- [ ] No accidental release action was performed.
- [ ] No runtime behavior changed unless explicitly approved.

## Phase 5: Review

Create:

- [ ] `progress/review_010-release-candidate-polish.md`

Move Feature 010 to `review`, not `done`, after verification.
