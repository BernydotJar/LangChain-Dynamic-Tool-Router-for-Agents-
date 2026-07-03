# 003-langchain-langgraph-real-integration-tests Requirements

## Summary

Add real LangChain and LangGraph integration tests or executable compatibility examples that prove the Dynamic Tool Router can inject authorized tools into practical framework workflows.

## Mode

MVP

## Initial State

`pending`

## Target Spec-Gate State

`spec_ready`

## Objective

Validate the Feature 001 adapter shapes and Feature 002 persistent policy/audit stores against current LangChain and LangGraph APIs without forcing heavy framework dependencies on users of the core router.

## Business Reason

Feature 001 provided framework-agnostic adapter shapes. Feature 002 added JSON policy loading and durable local audit evidence. Feature 003 increases product credibility by showing the router works with real LangChain/LangGraph package APIs or by documenting exactly where integration boundaries sit when optional dependencies are unavailable.

## Acceptance Criteria

- [ ] Add a LangChain integration example or test.
- [ ] Add a LangGraph integration example or test.
- [ ] Keep the core library dependency-light.
- [ ] Keep LangChain/LangGraph dependencies optional where possible.
- [ ] Document how to run integration tests separately from core unit tests if dependencies are optional.
- [ ] Verify runtime tool injection from JSON-loaded policy.
- [ ] Verify fallback behavior when a tool is unauthorized.
- [ ] Verify audit persistence during the integration scenario.
- [ ] Preserve all Feature 001 and Feature 002 tests.
- [ ] Avoid breaking changes to public core APIs.

## Required Artifacts

- `specs/003-langchain-langgraph-real-integration-tests/requirements.md`
- `specs/003-langchain-langgraph-real-integration-tests/design.md`
- `specs/003-langchain-langgraph-real-integration-tests/tasks.md`
- `adr/003-optional-framework-integration-tests.md`
- `progress/003-langchain-langgraph-real-integration-tests.md`
- `docs/langchain-langgraph-integration.md`

## Non-Goals

- No hosted API.
- No dashboard rewrite.
- No MCP server discovery.
- No production auth provider integration.
- No SaaS packaging.
- No breaking changes to core public APIs.
- No forced heavy runtime dependency for users who only want the core router.
- No package installation before implementation approval.

## Spec-Gate Validation

```sh
python -m json.tool feature_list.json
```

## Implementation Verification After Approval

Core verification must continue to pass:

```sh
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

Integration verification should be separate and optional when dependencies are not installed:

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If LangChain or LangGraph packages are missing, integration tests should skip clearly rather than fail core verification.

## MVP Criteria

- real-framework import paths are exercised where dependencies are available
- skipped integration tests explain missing optional dependencies
- JSON-loaded policy is used in at least one integration scenario
- unauthorized tool fallback is verified
- `FileAuditStore` persistence is verified
- no new dependency is required for core import/use

## SHIP Criteria

- pinned compatibility matrix for supported LangChain/LangGraph versions
- CI job for optional integration dependencies
- documentation with exact package extras
- compatibility tests against multiple Python versions
- release note process for framework API changes
- real agent/graph smoke tests beyond minimal examples
