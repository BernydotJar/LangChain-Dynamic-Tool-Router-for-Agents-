# 002-persistent-policy-and-audit-store Requirements

## Summary

Add file-backed policy configuration and file-backed audit logging to the Dynamic Tool Router. Feature 002 turns the Feature 001 in-memory MVP into a more realistic RBAC/governance layer where teams can load routing behavior from configuration and inspect authorization decisions after execution.

## Mode

MVP

## Initial State

`pending`

## Target Spec-Gate State

`spec_ready`

## Objective

Provide durable local policy and audit storage while preserving the Feature 001 public API where possible.

## Business Reason

Feature 001 proved runtime policy-based tool selection, fallback behavior, and LangChain/LangGraph adapter shapes. Buyers evaluating an "Auth0 for agent tools" or "RBAC layer for AI tools" need policy configuration outside application code and audit evidence that survives process exit.

## Acceptance Criteria

- [ ] Add a file-backed policy store.
- [ ] Add a file-backed audit store.
- [ ] Support loading tool policies from JSON.
- [ ] Validate policy config before use.
- [ ] Persist `authorize`, `deny`, `invoke`, and fallback-related audit events.
- [ ] Add an audit export helper.
- [ ] Add an example policy file.
- [ ] Add an example audit output artifact or sample.
- [ ] Update the admin dashboard example to document or use persisted sample data.
- [ ] Add tests for policy loading.
- [ ] Add tests for invalid policy rejection.
- [ ] Add tests for audit persistence.
- [ ] Add tests for audit export.
- [ ] Add tests proving existing fallback behavior still works.
- [ ] Preserve Feature 001 public APIs where possible.

## Required Artifacts

- `specs/002-persistent-policy-and-audit-store/requirements.md`
- `specs/002-persistent-policy-and-audit-store/design.md`
- `specs/002-persistent-policy-and-audit-store/tasks.md`
- `adr/002-file-backed-policy-and-audit-store.md`
- `progress/002-persistent-policy-and-audit-store.md`
- `docs/persistent-policy-and-audit-store.md`

## Non-Goals

- No database.
- No hosted API.
- No SaaS admin app.
- No auth provider integration.
- No real MCP server discovery.
- No cloud storage.
- No enterprise compliance claims.
- No breaking changes to existing tests/examples unless justified in design.
- No package installs or new dependencies unless separately approved.

## Validation

For the spec gate:

```sh
python -m json.tool feature_list.json
```

For implementation after approval:

```sh
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

## MVP Criteria

- local JSON policy config
- local JSONL or JSON audit persistence
- deterministic validation errors
- additive integration with `ToolPolicyRouter`
- no external service dependency
- tests and examples updated
- review artifact after implementation

## SHIP Criteria

- policy migration/versioning plan
- append reliability and corruption recovery strategy
- policy change audit trail
- authenticated admin API
- dashboard backed by real persisted data
- tenant-scoped policy bundles
- export formats reviewed for privacy and compliance needs
- real LangChain/LangGraph integration tests
