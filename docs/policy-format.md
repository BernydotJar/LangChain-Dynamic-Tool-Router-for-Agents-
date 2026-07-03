# Policy Format

Dynamic Tool Router can load policy configuration from JSON for local developer-preview use.

## Example

```json
{
  "version": 1,
  "fallback_tool_name": "not_authorized",
  "policies": {
    "search_docs": {
      "allowed_plans": ["free", "pro", "enterprise"]
    },
    "fetch_customer_record": {
      "allowed_plans": ["pro", "enterprise"],
      "required_permissions": ["records:read"]
    },
    "delete_customer_record": {
      "allowed_plans": ["enterprise"],
      "required_permissions": ["records:delete"]
    }
  }
}
```

## Top-Level Fields

| Field | Type | Required | Description |
|---|---:|---:|---|
| `version` | integer | yes | Policy file schema version. Developer preview supports `1`. |
| `fallback_tool_name` | string | no | Tool returned when a requested/visible tool is denied. |
| `policies` | object | yes | Mapping of tool name to policy object. |

## Policy Fields

| Field | Type | Description |
|---|---:|---|
| `allowed_user_ids` | array of strings | Users allowed to access this tool. |
| `allowed_tenant_ids` | array of strings | Tenants allowed to access this tool. |
| `allowed_plans` | array of strings | Plans allowed to access this tool. |
| `required_roles` | array of strings | Roles required to access this tool. |
| `required_permissions` | array of strings | Permissions required to access this tool. |
| `allowed_mcp_servers` | array of strings | MCP-style server identifiers allowed for this tool. |

Exact field support should match the current `ToolPolicy` model. Unknown fields are rejected to avoid silent configuration drift.

## Validation Behavior

The file-backed policy store should reject:

- invalid JSON,
- unsupported schema versions,
- missing `policies`,
- unknown top-level fields,
- unknown policy fields,
- non-list values for set-like fields,
- non-string values inside set-like fields.

## Unsupported In JSON Developer Preview

JSON policy files do not support callable Python `condition` rules. Code-backed policies can still use richer behavior, but JSON policies remain deterministic and serializable.

## Recommended Policy Design

Prefer additive least-privilege policy:

```text
start with no tools
allow by plan
narrow by role / permission
narrow by tenant / MCP server when needed
record audit events for every decision
```

## Product Caveat

This format is developer-preview configuration, not a hosted policy administration API. Production deployments should add versioning, review workflow, policy signing, and operational controls before enterprise use.
