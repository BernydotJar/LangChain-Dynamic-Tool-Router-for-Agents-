# LangChain/LangGraph Integration

Feature 003 validates the Dynamic Tool Router against real LangChain and LangGraph import paths when those optional packages are installed.

## Goal

Prove that runtime tool injection, JSON-loaded policies, fallback behavior, and file-backed audit persistence work in practical LangChain/LangGraph workflows.

## Dependency Policy

The core package should remain dependency-light. LangChain and LangGraph integration coverage should be optional:

- core unit tests should not require LangChain or LangGraph
- integration tests should live under a separate command
- missing optional packages should skip with a clear reason
- optional extras or dependency installation require explicit approval

## Verification Shape

Core verification:

```sh
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

Optional integration verification:

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
```

When `langchain_core` or `langgraph` is not installed, the integration tests skip with explicit dependency messages. This is intentional for the MVP so core users do not inherit heavy framework dependencies.

## Required Integration Behaviors

- load policies from `FilePolicyStore`
- persist audit events through `FileAuditStore`
- inject only authorized tools
- inject or expose fallback behavior for unauthorized tools
- preserve existing Feature 001 and Feature 002 APIs

## LangChain Coverage

`tests/integration/test_langchain_integration.py` imports `langchain_core.tools.tool` only inside a dependency-gated test. When available, it registers a real LangChain tool, routes it through `RuntimeToolInjector`, verifies the unauthorized fallback tool, invokes the authorized tool, and checks persisted audit events.

## LangGraph Coverage

`tests/integration/test_langgraph_integration.py` imports `langgraph.graph.StateGraph`, `START`, and `END` only inside a dependency-gated test. When available, it compiles a minimal state graph that applies `LangGraphToolRouterMiddleware`, verifies fallback injection, and checks persisted audit events.

## Local Dependency Status

During Feature 003 implementation in this environment, `langchain`, `langchain_core`, and `langgraph` were not installed. The integration tests therefore provide dependency-gated coverage and explicit skips locally.

## Current Status

Implemented for MVP and ready for review after verification.
