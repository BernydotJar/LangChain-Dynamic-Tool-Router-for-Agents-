# Tasks: 008 Demo Experience

Feature: `008-demo-experience`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Spec Gate

- [x] Confirm Features 001, 002, 003, 004, 005, 006, 007, and 009 are `done`.
- [x] Register Feature 008 as `spec_ready`.
- [x] Create requirements spec.
- [x] Create design spec.
- [x] Create task list.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Update current progress.
- [x] Update history.
- [x] Validate `feature_list.json`.

## Implementation Tasks After Approval

- [x] Move Feature 008 from `spec_ready` to `approved` only after explicit human approval.
- [x] Move Feature 008 from `approved` to `in_progress` before implementation.
- [x] Choose CLI script, guided walkthrough, recorded-output fixture, or combination.
- [x] Implement the approved demo experience.
- [x] Demonstrate request context.
- [x] Demonstrate JSON policy loading.
- [x] Demonstrate allowed tool exposure.
- [x] Demonstrate denied tool behavior.
- [x] Demonstrate fallback behavior.
- [x] Demonstrate audit event output.
- [x] Demonstrate LangChain-style boundary.
- [x] Demonstrate LangGraph-style boundary.
- [x] Keep demo local with no external service dependency.
- [x] Avoid runtime code changes unless explicitly approved.

## Verification Tasks After Approval

- [x] Run `python -m json.tool feature_list.json`.
- [x] Run `PYTHONPATH=src python -m unittest discover -s tests`.
- [x] Run `python examples/basic_agent/run_example.py`.
- [x] Run any new Feature 008 demo command.
- [x] Capture exact output in progress and review artifacts.

## Review Tasks After Approval

- [x] Create `progress/review_008-demo-experience.md`.
- [x] Document changed files.
- [x] Document verification evidence.
- [x] Document known limitations.
- [x] Move Feature 008 to `review` only after implementation and verification pass.
- [ ] Move Feature 008 to `done` only after explicit closure approval.

## Stop Conditions

- Approval is missing.
- Implementation requires runtime capability changes without explicit approval.
- Demo requires external services.
- Demo makes production-readiness or compliance claims.
- README changes are requested without explicit approval.
