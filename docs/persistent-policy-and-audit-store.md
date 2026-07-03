# Persistent Policy and Audit Store

Feature 002 adds local file-backed persistence for the Dynamic Tool Router.

## Purpose

The Dynamic Tool Router is positioned as an RBAC and governance layer for agent tools. Local persistence is the next MVP step because teams need to:

- configure tool authorization outside application code
- review tool authorization decisions after execution
- export audit evidence for debugging and governance workflows
- keep Feature 001 runtime injection and fallback behavior intact

## MVP Behavior

- Load policy configuration from JSON.
- Validate policy configuration before constructing router inputs.
- Persist audit events to a local file.
- Export audit events into a JSON inspection format.
- Provide example policy and audit artifacts.
- Keep the static admin dashboard as an example, not a hosted admin app.

## Usage

Load policies from JSON:

```python
from tool_policy_router import FilePolicyStore

policy_store = FilePolicyStore("examples/policies/tool_policies.json")
router = policy_store.create_router()
```

Record audit events to JSON Lines:

```python
from tool_policy_router import FileAuditStore, FilePolicyStore

audit_store = FileAuditStore("audit/tool_events.jsonl")
router = FilePolicyStore("examples/policies/tool_policies.json").create_router(
    audit_log=audit_store,
)
```

Export persisted audit events to a JSON array:

```python
audit_store.export_json("audit/tool_events_export.json")
```

## Policy Limitations

JSON policies are expected to support serializable fields only:

- users
- tenants
- plans
- roles
- permissions
- required MCP servers
- reason text

Callable policy `condition` rules are not planned for JSON loading in MVP because arbitrary code in config is not safe or portable.

## Audit Behavior

`FileAuditStore` stores one audit event per line as JSON. The existing router records authorization decisions, denied decisions through `allowed=false`, fallback mappings in event metadata, and invocations through wrapped tools.

The included static example artifact is `examples/audit/sample_audit.jsonl`. Running `python examples/basic_agent/run_example.py` writes live runtime audit output to the system temp directory and prints the export path.

## Audit Limitations

Local audit files are useful for demos, tests, and single-process deployments. They do not provide:

- database durability
- multi-writer locking guarantees
- tamper-proof records
- retention policy enforcement
- privacy redaction
- enterprise compliance guarantees

Those are SHIP-mode or later feature concerns.

## Implementation Status

Implemented for MVP and ready for review after verification.
