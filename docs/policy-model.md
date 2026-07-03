# Policy Model

`ToolPolicyRouter` evaluates one `ToolPolicy` per candidate tool.

## Default Behavior

By default, unknown tools are denied:

```python
router = ToolPolicyRouter(default_allow=False)
```

This is the safer multi-tenant default. Development-only systems can opt into `default_allow=True`.

## Fallback Tool

When at least one candidate tool is denied, the router can add a fallback tool:

```python
router = ToolPolicyRouter(
    policies=policies,
    fallback_tool_name="not_authorized",
)
```

The fallback tool itself must be authorized or `default_allow=True` must be used.

## MCP Server Gating

Use `required_mcp_servers` for tools that should only appear when a server is available:

```python
ToolPolicy(required_mcp_servers={"github-mcp"})
```

The request context supplies the current server set:

```python
ToolRequestContext(..., available_mcp_servers={"github-mcp"})
```
