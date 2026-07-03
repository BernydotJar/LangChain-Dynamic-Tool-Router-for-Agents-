# Basic Agent Example

Run:

```sh
python examples/basic_agent/run_example.py
```

The example creates:

- a tool registry,
- tenant and plan policies loaded from `examples/policies/tool_policies.json`,
- MCP-server availability checks,
- a fallback tool,
- LangChain-style runtime tool injection,
- LangGraph-style state injection,
- a file-backed audit log with JSON export in the system temp directory.
