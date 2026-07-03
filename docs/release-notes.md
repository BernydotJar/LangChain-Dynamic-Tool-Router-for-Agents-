# Release Notes

## Developer Preview

Dynamic Tool Router for Agents is a developer-preview package for runtime tool authorization in LangChain/LangGraph-style agent systems.

Positioning:

```text
Auth0-style authorization for AI agent tools.
```

This is product positioning, not a claim of parity with Auth0, Okta, OPA, or enterprise IAM platforms.

## Included

### Feature 001: Dynamic Tool Router MVP

- `ToolPolicyRouter`
- runtime tool injection
- per-user and per-tenant policy dimensions
- plan, role, permission, context, and MCP-server policy dimensions
- fallback behavior for tools not allowed by policy
- in-memory audit log
- LangChain-style adapter shape
- LangGraph-style middleware shape
- static dashboard example

### Feature 002: Persistent Policy and Audit Store

- `FilePolicyStore`
- `PolicyBundle`
- `FileAuditStore`
- JSON policy loading and validation
- JSON Lines audit persistence
- JSON audit export helper
- example policy file
- stable sample audit output

### Feature 003: LangChain/LangGraph Integration Tests

- dependency-gated LangChain integration test
- dependency-gated LangGraph integration test
- shared integration fixtures for JSON policy, fallback routing, and file-backed audit
- explicit skip behavior when optional dependencies are absent

### Feature 004: Sellable Developer Preview

- buyer-facing README direction
- product positioning documentation
- policy format documentation
- audit log format documentation
- security model documentation
- demo guide
- release notes
- SHIP-mode review gates

## Verification Targets

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Feature 004 remains in progress until local verification evidence is reported and review criteria are satisfied.

## Known Developer-Preview Limitations

- No hosted policy API.
- No billing.
- No production auth provider integration.
- No database-backed policy store.
- No tamper-proof audit sink.
- No dashboard authentication.
- No retention or redaction controls.
- No enterprise compliance guarantees.
- Optional framework integration tests may skip when LangChain/LangGraph dependencies are absent.

## Candidate Next Features

- MCP server discovery adapter.
- Admin policy editor.
- Release packaging and versioning.
- Hosted policy API.
- Tamper-resistant audit sink.
- Auth-provider integration.
