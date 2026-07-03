# 008 Demo Experience Progress

Feature: `008-demo-experience`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## State

Status: `done`

State change completed:

```text
FEATURE: 008-demo-experience
MODE: SHIP
STATE CHANGE: spec_ready -> approved -> in_progress -> review -> done
```

Feature 008 is closed after explicit human approval.

## Summary

Implemented and closed a guided local demo experience for Runtime Tool Authorization for AI Agents.

The demo helps a new developer understand the developer-preview product in under three minutes without requiring LangChain, LangGraph, external services, hosted infrastructure, or runtime code changes.

## Preconditions

- Feature 001: `done`
- Feature 002: `done`
- Feature 003: `done`
- Feature 004: `done`
- Feature 005: `done`
- Feature 006: `done`
- Feature 007: `done`
- Feature 009: `done`

## Implemented Scope

- Added guided demo command: `python examples/demo_experience/run_demo.py`.
- Reused existing JSON policy file: `examples/policies/tool_policies.json`.
- Reused existing file-backed audit store and JSON export behavior.
- Demonstrated request context with tenant, user, role, plan, permissions, request ID, conversation ID, state, and available MCP-style server.
- Demonstrated JSON policy loading and policy requirements.
- Demonstrated candidate tool surface.
- Demonstrated allowed tool surface.
- Demonstrated denied tool path.
- Demonstrated fallback behavior through `not_authorized`.
- Demonstrated LangChain-style adapter boundary through `inject_into_agent_kwargs`.
- Demonstrated LangGraph-style adapter boundary through `LangGraphToolRouterMiddleware`.
- Demonstrated audit evidence and local audit export path.
- Updated `docs/demo-guide.md` with the guided demo command and expected output shape.

## Files Changed

- `examples/demo_experience/run_demo.py`
- `docs/demo-guide.md`
- `feature_list.json`
- `specs/008-demo-experience/tasks.md`
- `progress/008-demo-experience.md`
- `progress/current.md`
- `progress/history.md`
- `progress/review_008-demo-experience.md`

## Verification

Passed:

```sh
python -m json.tool feature_list.json
# valid JSON; Feature 008 is review during verification and done after closure
```

```sh
PYTHONPATH=src python -m unittest discover -s tests
# Ran 23 tests
# OK (skipped=2)
```

```sh
python examples/basic_agent/run_example.py
# passed; printed injected tools, LangGraph state tools, audit events, and audit export path
```

```sh
python examples/demo_experience/run_demo.py
# passed; printed request context, JSON policy loading, allowed/denied/fallback paths,
# LangChain-style boundary, LangGraph-style boundary, audit events, and audit export path
```

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
# Ran 2 tests
# OK (skipped=2)
```

## Known Limitations Accepted

- The guided demo is local and dependency-light; it does not use real LangChain or LangGraph packages directly.
- Optional integration tests may skip when LangChain/LangGraph dependencies are absent.
- Audit output is local JSON/JSONL and is not tamper-proof.
- The demo does not add hosted policy management, SaaS administration, auth-provider integration, or real MCP server discovery.
- The demo does not claim production readiness, compliance readiness, or managed IAM behavior.
- No runtime `src/` code changes.
- No external services added.
- No mandatory LangChain/LangGraph dependency added.
- No PyPI publish.
- No git tag.
- No GitHub Release.

## Review Artifact

Created:

- `progress/review_008-demo-experience.md`

## Closure

Human closure approval received:

```text
APPROVAL
FEATURE: 008-demo-experience
MODE: SHIP
STATE CHANGE: review -> done
```

Feature 008 moved from `review` to `done`.
