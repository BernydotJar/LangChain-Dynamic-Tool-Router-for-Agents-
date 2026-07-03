# 003-langchain-langgraph-real-integration-tests Design

## Approach

Feature 003 will add optional integration coverage around the existing dependency-free core:

- keep `tool_policy_router` importable without LangChain or LangGraph installed
- place real-framework tests under a separate integration test path
- skip integration tests with a clear reason when optional packages are missing
- use Feature 002 JSON policy loading for router construction
- use `FileAuditStore` in the integration scenario
- assert fallback routing for unauthorized tools
- document commands separately from core unit verification

The preferred MVP is test-first compatibility coverage. If the local environment cannot install or provide current framework packages, the fallback acceptable MVP is executable examples plus skip-safe tests that define the integration boundary.

## Files You May Read

- `feature_list.json`
- `README.md`
- `AGENTS.md`
- `RTK.md`
- `CLAUDE.md`
- `pyproject.toml`
- `src/**`
- `examples/**`
- `tests/**`
- `specs/003-langchain-langgraph-real-integration-tests/**`
- `adr/003-optional-framework-integration-tests.md`
- `progress/**`
- `docs/**`

## Files You May Touch After Approval

- `feature_list.json`
- `tests/**`
- `examples/**`
- `docs/langchain-langgraph-integration.md`
- `docs/langchain-integration.md` if cross-reference is needed
- `README.md` if a top-level integration pointer is needed
- `pyproject.toml` only if explicitly approved for optional extras
- `progress/003-langchain-langgraph-real-integration-tests.md`
- `progress/review_003-langchain-langgraph-real-integration-tests.md`
- `progress/current.md`
- `progress/history.md`

## Files You Must Not Touch

- harness-sdlc
- parent repositories
- unrelated local repositories
- `.git`
- secrets
- credentials
- deployment files
- global environment files
- shell profiles

## Proposed Test Layout

Core tests stay unchanged:

```text
tests/
  test_adapter.py
  test_policy.py
  test_store.py
  test_tool_registry.py
```

Optional framework tests should be isolated:

```text
tests/integration/
  test_langchain_integration.py
  test_langgraph_integration.py
```

Each integration test should use `unittest.skipUnless` or an equivalent import guard so missing optional dependencies produce a clear skip, not a core test failure.

## LangChain Scenario

The LangChain scenario should prove:

- a real LangChain-compatible tool object or current tool decorator shape can be registered
- `RuntimeToolInjector.tools_for_context()` returns only authorized tools plus fallback when needed
- a JSON-loaded policy controls access
- invoking an injected tool records an audit event in `FileAuditStore`

The exact LangChain API should be selected during implementation by inspecting the installed/current package docs or local environment. Do not guess a stale API during implementation.

## LangGraph Scenario

The LangGraph scenario should prove:

- `LangGraphToolRouterMiddleware.before_model()` can be used in a realistic graph/state path
- the state receives authorized tools plus fallback behavior
- JSON-loaded policy and `FileAuditStore` work during the scenario
- integration remains optional

If a full graph compile/run adds too much setup for MVP, an executable middleware compatibility test using real LangGraph state conventions is acceptable and must be documented honestly.

## Dependency Strategy

No hard runtime dependency should be added to the core package. Acceptable implementation options after approval:

- skip-safe tests that run only if packages are already installed
- documented optional dev dependency command
- optional extras in `pyproject.toml` only with explicit approval

No package installation should be performed without explicit approval.

## Risks

- Risk: LangChain/LangGraph APIs change frequently.
  - Mitigation: document tested versions and isolate integration tests from core tests.
- Risk: optional dependencies make CI slower or less reliable.
  - Mitigation: keep core tests dependency-free and create a separate integration command.
- Risk: examples imply full production agent support.
  - Mitigation: document these as compatibility examples/tests, not hosted agent infrastructure.
- Risk: missing packages could block local verification.
  - Mitigation: skip clearly and treat installed-package verification as a separate approval decision.

## Verification Plan

Spec gate:

```sh
python -m json.tool feature_list.json
```

After implementation approval:

```sh
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If optional packages are absent, record the skip count and exact skip reason in the review artifact.
