# 002-persistent-policy-and-audit-store Tasks

## Spec-Gate Tasks

- [x] Create requirements spec.
- [x] Create design spec.
- [x] Create implementation task list.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Create documentation stub.
- [x] Register Feature 002 as `spec_ready`.
- [x] Validate `feature_list.json`.

## Implementation Tasks

- [ ] Move Feature 002 from `spec_ready` to `approved` only after explicit approval.
- [ ] Move Feature 002 from `approved` to `in_progress` before code edits.
- [ ] Add policy-store model or bundle type if needed.
- [ ] Implement `FilePolicyStore`.
- [ ] Implement deterministic JSON policy validation.
- [ ] Add conversion from JSON policy records to `ToolPolicy`.
- [ ] Implement `FileAuditStore`.
- [ ] Add audit export helper.
- [ ] Add example policy JSON.
- [ ] Add example persisted audit output or export path.
- [ ] Update admin dashboard sample/documentation for persisted data.
- [ ] Preserve existing in-memory audit behavior.
- [ ] Preserve existing fallback behavior.
- [ ] Preserve existing adapter behavior.

## Test Tasks

- [ ] Test valid policy loading.
- [ ] Test invalid JSON policy rejection.
- [ ] Test unsupported version rejection.
- [ ] Test unknown policy field rejection.
- [ ] Test invalid set/list field rejection.
- [ ] Test audit event persistence.
- [ ] Test audit export helper.
- [ ] Test fallback behavior with loaded policies.
- [ ] Test existing Feature 001 unit suite remains passing.

## Verification Tasks

- [ ] Run `PYTHONPATH=src python -m unittest discover -s tests`.
- [ ] Run `python examples/basic_agent/run_example.py`.
- [ ] Record exact command results in progress and review artifacts.

## Review Tasks

- [ ] Create `progress/review_002-persistent-policy-and-audit-store.md`.
- [ ] Document changed files.
- [ ] Document known limitations.
- [ ] Document SHIP-mode gaps.
- [ ] Move Feature 002 to `review` only after implementation and verification pass.
- [ ] Move Feature 002 to `done` only after explicit closure approval.

## Stop Conditions

- Approval is missing.
- A database or hosted API is required.
- A new dependency is required without explicit approval.
- Existing public APIs require breaking changes.
- Real auth provider integration is requested.
