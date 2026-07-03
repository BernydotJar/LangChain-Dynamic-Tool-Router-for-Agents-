# Security Model

This MVP is an authorization layer for agent tools, not a sandbox.

## Trust Boundaries

- The app owns authenticated identity and must build `Principal` from trusted server-side session data.
- The LLM must not be allowed to set `user_id`, `tenant_id`, `plan`, `roles`, or `permissions`.
- Tools must be registered server-side in `ToolRegistry`.
- The agent receives only the routed list of tools for the current request.

## Policy Controls

Policies can restrict tools by:

- user id
- tenant id
- plan
- roles
- permissions
- available MCP servers
- custom request condition

## Audit Events

The router records:

- authorization decisions,
- denials and fallback mapping,
- tool invocations through `AuditedTool`.

Audit metadata intentionally avoids raw tool arguments by default. Applications can add a custom audit sink later if they need redacted argument capture.

Feature 002 adds `FileAuditStore` for local JSON Lines persistence and JSON export. This is durable enough for local demos, tests, and simple single-process deployments, but it is not tamper-proof and does not provide compliance retention controls.

## MVP Limitations

- No database-backed or hosted audit backend.
- No cryptographic policy signing.
- No distributed policy store.
- No admin authentication for the static dashboard example.
- No enforcement if an application bypasses the router and gives the agent raw tools directly.
