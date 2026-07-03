# 003-langchain-langgraph-real-integration-tests Tasks

## Spec-Gate Tasks

- [x] Confirm Feature 001 is `done`.
- [x] Confirm Feature 002 is `done`.
- [x] Create requirements spec.
- [x] Create design spec.
- [x] Create task list.
- [x] Create ADR.
- [x] Create progress artifact.
- [x] Create documentation stub.
- [x] Register Feature 003 as `spec_ready`.
- [x] Validate `feature_list.json`.

## Implementation Tasks

- [ ] Move Feature 003 from `spec_ready` to `approved` only after explicit approval.
- [ ] Move Feature 003 from `approved` to `in_progress` before implementation.
- [ ] Inspect current LangChain and LangGraph APIs before writing integration code.
- [ ] Add skip-safe LangChain integration test or executable example.
- [ ] Add skip-safe LangGraph integration test or executable example.
- [ ] Use JSON-loaded policies in integration coverage.
- [ ] Use `FileAuditStore` in integration coverage.
- [ ] Verify unauthorized fallback behavior in integration coverage.
- [ ] Keep core package importable without framework dependencies.
- [ ] Document optional dependency/run commands.

## Verification Tasks

- [ ] Run `PYTHONPATH=src python -m unittest discover -s tests`.
- [ ] Run `python examples/basic_agent/run_example.py`.
- [ ] Run `PYTHONPATH=src python -m unittest discover -s tests/integration`.
- [ ] Record skipped optional-dependency tests if applicable.
- [ ] Record exact verification output in progress and review artifacts.

## Review Tasks

- [ ] Create `progress/review_003-langchain-langgraph-real-integration-tests.md`.
- [ ] Document changed files.
- [ ] Document known limitations.
- [ ] Document SHIP-mode gaps.
- [ ] Move Feature 003 to `review` only after implementation and verification pass.
- [ ] Move Feature 003 to `done` only after explicit closure approval.

## Stop Conditions

- Approval is missing.
- A hard LangChain/LangGraph runtime dependency is required for core users.
- Package installation is required without explicit approval.
- Real framework APIs cannot be inspected or verified.
- Existing Feature 001 or Feature 002 tests regress.
