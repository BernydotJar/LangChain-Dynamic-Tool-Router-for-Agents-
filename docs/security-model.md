# Security Model

## Summary

Dynamic Tool Router is a request-time authorization and routing layer for agent tools.

It controls which tools are exposed to an agent/tool surface for a given user, tenant, plan, role, permission set, context, and MCP-style server availability.

It is not a complete security boundary by itself.

## Trust Boundaries

- The application owns authenticated identity and must build `Principal` from trusted server-side session data.
- The LLM must not be allowed to set `user_id`, `tenant_id`, `plan`, `roles`, or `permissions`.
- Tools must be registered server-side in `ToolRegistry`.
- The agent receives only the routed list of tools for the current request.
- Applications must not bypass the router and hand raw privileged tools directly to the agent.

## What The Router Protects

The router helps reduce accidental or unauthorized tool exposure by:

- evaluating policy before tool injection,
- withholding tools that are not authorized,
- routing denied tools to a fallback tool when configured,
- recording allow, deny, invoke, and fallback events,
- supporting persistent local audit evidence,
- validating JSON policy configuration before use.

## Policy Controls

Policies can restrict tools by:

- user id,
- tenant id,
- plan,
- roles,
- permissions,
- available MCP servers,
- custom request condition in code-backed policies.

JSON-loaded policies intentionally do not support arbitrary callable conditions in the developer preview.

## Audit Events

The router records:

- authorization decisions,
- denials and fallback mapping,
- tool invocations through `AuditedTool`,
- locally persisted JSON Lines events through `FileAuditStore`,
- JSON exports for demos and review.

Audit metadata intentionally avoids raw tool arguments by default. Applications can add a custom audit sink later if they need redacted argument capture.

## What The Router Does Not Protect

Dynamic Tool Router does not provide:

- process sandboxing,
- network isolation,
- secret management,
- encryption at rest,
- tamper-proof audit logs,
- admin authentication,
- hosted policy enforcement,
- enterprise IAM integration,
- compliance guarantees,
- protection from malicious tool implementations.

## Threat Model For Developer Preview

### In Scope

- Developer accidentally injecting tools that a user should not see.
- Tenant or plan using a tool outside its configured entitlement.
- Missing permission for a sensitive tool.
- Need to preserve audit evidence of routing decisions.
- Need to avoid forcing LangChain/LangGraph into the core package.

### Out Of Scope

- Attacker with filesystem access modifying audit files.
- Malicious Python code inside a registered tool.
- Secrets embedded in tool implementations.
- Runtime escape from an agent framework.
- Admin dashboard authentication.
- Multi-node distributed policy consistency.

## Fallback Behavior

Fallback behavior makes denied tools explicit and safe for demos. It does not secure the underlying denied tool. The denied tool must still be withheld from the agent's authorized tool surface.

## Local Audit Caveat

Feature 002 adds `FileAuditStore` for local JSON Lines persistence and JSON export. This is durable enough for local demos, tests, and simple single-process deployments, but it is not tamper-proof and does not provide compliance retention controls.

Anyone with write access to the audit path can modify or delete local audit files.

## Static Dashboard Caveat

The dashboard example is static and unauthenticated. It is for visualization only, not production administration.

## Policy Validation Caveat

JSON policy validation catches schema and value errors. It does not prove that a policy is correct, complete, least-privilege, or compliant.

## Safe Product Language

Use:

```text
Auth0-style authorization for AI agent tools.
```

Do not claim:

```text
Auth0 replacement.
Enterprise IAM.
Compliance-ready governance.
Tamper-proof audit.
Production security boundary.
```

## Production Hardening Candidates

- Hosted policy API.
- Auth-provider integration.
- Admin authentication.
- Tamper-resistant audit sink.
- Policy versioning and approvals.
- Retention and redaction controls.
- Distributed policy cache.
- MCP server discovery and trust policy.
