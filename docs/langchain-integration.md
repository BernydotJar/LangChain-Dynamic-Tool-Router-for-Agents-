# LangChain And LangGraph Integration

The MVP intentionally avoids hard dependencies on LangChain and LangGraph.

Feature 003 adds optional dependency-gated integration tests under `tests/integration`. These tests exercise real LangChain/LangGraph import paths when the packages are installed and skip clearly when they are absent.

## LangChain-Style Injection

Use `RuntimeToolInjector.inject_into_agent_kwargs()` before constructing or invoking an agent.

```python
agent_kwargs = injector.inject_into_agent_kwargs(
    {"model": model},
    context,
    candidate_tool_names=["basic_search", "crm_lookup", "admin_delete"],
)
```

The returned dictionary has a request-specific `tools` list.

## LangGraph-Style Middleware

Use `LangGraphToolRouterMiddleware.before_model()` to enrich a state dictionary.

```python
state = middleware.before_model({
    "tool_context": context,
    "candidate_tool_names": ["basic_search", "admin_delete"],
})
```

The returned state includes a `tools` key containing only allowed tools plus the configured fallback tool when a candidate was denied.

## Tool Compatibility

Tools can be:

- `CallableTool` instances,
- objects with `name` and `invoke()`,
- callable objects with a `name` attribute.

Invocation auditing is captured by wrapping returned tools in `AuditedTool`.
