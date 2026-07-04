# Security Whitepaper

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

Runtime Tool Authorization for AI Agents is a developer-preview library for reducing agent tool exposure at request time. It evaluates policy before an agent receives tools, documents authorization decisions, and records local audit evidence for review.

This document consolidates the current security posture, boundaries, non-goals, threat assumptions, and reviewer checklist. It should be read with:

- [`security-model.md`](security-model.md)
- [`architecture.md`](architecture.md)
- [`policy-format.md`](policy-format.md)
- [`audit-log-format.md`](audit-log-format.md)
- [`demo-guide.md`](demo-guide.md)

## Executive Summary

Agent applications often start with static tool registration: create an agent, attach tools, and run. That model becomes risky in multi-tenant products where each request may have different user, tenant, plan, role, permission, context, and MCP-style tool availability.

Runtime Tool Authorization adds a request-time authorization layer between the application and the agent tool surface. The application resolves trusted identity and context, the router evaluates policy, and the agent receives only the routed tool list for that request.

The developer preview supports local JSON policies, in-process routing, fallback behavior for denied tools, local JSON Lines audit evidence, JSON audit export, and LangChain/LangGraph adapter shapes. It requires production hardening before enterprise use.

## What Runtime Tool Authorization Is

Runtime Tool Authorization is:

- a request-time authorization layer for agent tool visibility,
- a policy evaluator for user, tenant, role, plan, permission, context, and MCP-style server inputs,
- a tool injector that returns a request-specific allowed tool surface,
- a fallback router for making denied access explicit,
- a local audit evidence generator for allow, deny, fallback, and invoke decisions,
- a dependency-light adapter pattern for LangChain-style and LangGraph-style integrations.

Its purpose is to reduce accidental or unauthorized tool exposure before the agent runs.

## What Runtime Tool Authorization Is Not

Runtime Tool Authorization is not:

- a production security product,
- a replacement for IAM,
- a compliance-certified control,
- a tamper-proof audit system,
- a sandbox,
- a hosted enterprise control plane,
- a prompt injection defense,
- a way to secure the implementation of individual tools.

Applications still need authenticated identity, authorization policy governance, secure tool implementations, secrets management, logging controls, and production security operations.

## Trust Boundary

The core trust boundary is between server-side application state and the agent runtime.

Trusted inputs should come from application-controlled systems:

- authenticated user identity,
- tenant identity,
- plan or entitlement data,
- roles and permissions,
- request metadata,
- available MCP-style server names,
- server-side tool registry,
- policy configuration.

The LLM must not be trusted to set `user_id`, `tenant_id`, `plan`, `roles`, `permissions`, or available server names. Prompt text can request a tool, but the routed tool surface should be decided from trusted request context and policy, not from prompt intent alone.

The application must not bypass the router by handing raw privileged tools directly to the agent.

## Request Context Model

The request context describes who is making the request and what tool environment is available.

Current developer-preview inputs include:

- user id,
- tenant id,
- plan,
- roles,
- permissions,
- request id,
- conversation id,
- arbitrary state metadata,
- available MCP-style servers.

The request context is evaluated with policy for each candidate tool. The context should be built by the application from trusted server-side state. It should not be derived from untrusted model output.

## Policy Evaluation Model

Policy evaluation compares each candidate tool against configured rules.

Current developer-preview policy controls include:

- allowed user ids,
- allowed tenant ids,
- allowed plans,
- required roles,
- required permissions,
- allowed or required MCP-style server availability,
- code-backed condition rules when policies are constructed in Python.

JSON policy files intentionally avoid arbitrary callable conditions. This keeps local JSON configuration deterministic and reviewable, but limits expressiveness.

Policy evaluation records authorization decisions so reviewers can inspect why a tool was allowed, denied, or routed to fallback behavior.

## Allowed Tool Surface

The allowed tool surface is the list of tools returned to the agent for a specific request.

The router reduces exposure by evaluating policy before the agent receives tools. A tenant, user, role, plan, or permission set can receive a narrower tool list than the full server-side registry.

This approach is stronger than prompt-only control because unauthorized tools are not provided through the routed adapter path.

The application still owns final integration discipline. If the application passes raw privileged tools around the router, the authorization boundary is weakened.

## Denied Tool Behavior

When a candidate tool does not satisfy policy, the router withholds that tool from the allowed tool surface.

Denied decisions can be caused by:

- missing policy,
- user mismatch,
- tenant mismatch,
- plan mismatch,
- missing role,
- missing permission,
- unavailable MCP-style server,
- code-backed condition mismatch.

The denial is documented in local audit evidence. The denied tool implementation is not secured by this project; it must remain unavailable to the agent through application integration.

## Fallback Behavior

Fallback behavior can map a denied tool request to a configured fallback tool, such as `not_authorized`.

The fallback tool makes denied access explicit for demos, applications, and audit review. It should communicate that the requested tool is not authorized for the current request.

Fallback behavior does not secure the denied tool. It only helps represent denied access while the original tool remains withheld from the allowed tool surface.

Fallback misuse is possible if the fallback tool leaks sensitive detail, performs privileged work, or is treated as proof that the denied tool is safe. The fallback tool should be simple, low-privilege, and reviewed like any other tool.

## Audit Evidence Model

Runtime Tool Authorization records local audit evidence for routing and invocation review.

Current developer-preview evidence includes:

- authorization decisions,
- denied decisions,
- fallback metadata,
- audited tool invocation events,
- JSON Lines persistence through `FileAuditStore`,
- JSON export for demos and review.

The audit model documents decisions; it does not make the audit trail tamper-proof.

Audit metadata avoids raw tool arguments by default. Applications that need argument-level evidence should define redaction and retention rules before storing sensitive data.

## Local Audit Limitations

Developer-preview audit storage is local file-backed JSON Lines.

This is useful for:

- local demos,
- unit and integration tests,
- release-candidate review,
- static dashboard sample data,
- single-process developer evaluation.

It is not:

- tamper-proof,
- encrypted by default,
- retention-managed,
- compliance-certified,
- resistant to a user with filesystem write access.

Production hardening should add append-only storage, integrity controls, retention policy, redaction policy, access controls, and operational monitoring.

## JSON Policy Limitations

JSON policy files support deterministic local configuration for developer-preview use.

They intentionally do not support arbitrary callable Python condition rules. This reduces configuration ambiguity and makes policy files easier to review, but it means advanced logic must be implemented in code-backed policies or a future policy control plane.

JSON validation catches schema and value errors. It does not prove that a policy is complete, least-privilege, or suitable for a specific compliance program.

Production hardening should add policy versioning, approval workflow, signing or integrity checks, dry-run evaluation, review tooling, and operational rollback.

## Adapter Boundary For LangChain And LangGraph

The core package avoids mandatory LangChain and LangGraph runtime dependencies.

Current adapter shapes include:

- LangChain-style agent kwargs injection,
- LangGraph-style state middleware,
- plain callable wrappers,
- objects with a `name` attribute and `invoke()` method.

The adapter boundary is an integration point. It must be tested when frameworks change, because adapter integration drift can cause the application to pass tools differently than expected.

Dependency-gated integration tests cover real framework imports when optional packages are installed. If optional packages are absent, those tests skip explicitly.

## MCP-Style Tool Surface Filtering

Runtime Tool Authorization can evaluate MCP-style server availability as part of policy.

The application supplies available server names in request context. Policy can require that a server be available before a tool appears in the allowed tool surface.

This is surface filtering based on declared availability. The developer preview does not implement real MCP discovery, remote server attestation, transport security, or a managed MCP trust policy.

## Tenant/User/Role/Plan/Permission Constraints

The router can reduce exposure across common SaaS authorization dimensions:

- tenant constraints reduce cross-tenant exposure risk,
- user constraints narrow access to specific users,
- plan constraints model commercial entitlement,
- role constraints model job function or administrative scope,
- permission constraints model action-level capability.

These constraints are only as trustworthy as the request context and policy data supplied by the application. The application must source them from trusted systems and keep them out of direct LLM control.

## Threat Model

### Overexposed Tool Surfaces

Risk: an agent receives more tools than the current request should use.

Mitigation posture: the router evaluates policy before injection and returns a request-specific allowed tool surface. This reduces exposure when applications route all tool access through the authorization layer.

### Tenant Leakage Risk

Risk: a tenant receives access to tools or records intended for another tenant.

Mitigation posture: policy can restrict tools by tenant id, and audit evidence records tenant context. The application must provide trusted tenant identity and enforce tenant isolation inside tool implementations.

### Role Or Permission Mismatch

Risk: a user lacks the right role or permission for a tool but the agent still receives it.

Mitigation posture: policy can require roles and permissions before a tool is exposed. The application must source role and permission data from trusted authorization systems.

### Unsafe Tool Invocation

Risk: a tool implementation performs sensitive work after being invoked.

Mitigation posture: the router reduces which tools are exposed to the agent and records invocation evidence for wrapped tools. It does not secure tool internals, validate tool side effects, or sandbox tool execution.

### Prompt-Only Control Weakness

Risk: prompt instructions ask the model not to use sensitive tools, but the tools remain available.

Mitigation posture: the router removes unauthorized tools from the routed tool surface, reducing reliance on prompt-only control. Prompt policy should complement, not replace, runtime authorization.

### Audit Evidence Gaps

Risk: reviewers lack enough evidence to understand why a tool was available or used.

Mitigation posture: the router records allow, deny, fallback, and invoke events locally. Applications needing stronger evidence should add redaction, retention, centralized storage, and integrity controls.

### Local File Tampering Risk

Risk: anyone with filesystem write access can modify or delete local audit files.

Mitigation posture: local JSON Lines evidence is suitable for developer-preview review, not tamper-proof audit. Production hardening should add append-only or tamper-resistant storage.

### Policy Misconfiguration

Risk: a policy is valid JSON but too broad, incomplete, or inconsistent with business rules.

Mitigation posture: validation rejects malformed or unknown fields, and audit evidence helps review behavior. Policy correctness still requires human review, least-privilege design, tests, and production governance.

### Fallback Misuse

Risk: fallback behavior is treated as a security control for the denied tool or leaks sensitive information.

Mitigation posture: fallback should be low-privilege and explicit. The denied tool must remain withheld. The fallback tool should not perform privileged work.

### Adapter Integration Drift

Risk: LangChain, LangGraph, or application integration changes cause tools to bypass the expected routed path.

Mitigation posture: dependency-gated integration tests and local demos exercise adapter behavior. Production use should add compatibility tests around the exact framework versions and application integration path.

## Security Non-Goals

Runtime Tool Authorization does not provide:

- production readiness,
- IAM replacement,
- compliance certification,
- tamper-proof audit,
- sandboxing,
- hosted enterprise control plane,
- prompt injection prevention,
- secure implementation of individual tools,
- secrets management,
- network isolation,
- encryption at rest,
- admin authentication,
- distributed policy consistency.

## Developer-Preview Limitations

The current developer preview has important boundaries:

- policy configuration is local file-backed JSON or in-process Python objects,
- audit evidence is local file-backed JSON Lines,
- audit files are not tamper-proof,
- static dashboard material is not authenticated administration,
- optional LangChain/LangGraph integrations are dependency-gated,
- MCP-style filtering uses declared server availability, not real server trust validation,
- JSON policy validation does not prove least privilege,
- no hosted policy API is included,
- no production auth-provider integration is included,
- no release action implies enterprise readiness.

The project requires production hardening before enterprise use.

## Future Hardening Opportunities

Future production hardening could include:

- hosted policy API,
- auth-provider integration,
- policy versioning and approval workflow,
- policy dry-run and diff tooling,
- tamper-resistant or append-only audit sink,
- audit redaction and retention controls,
- centralized audit export,
- admin authentication,
- distributed policy cache,
- MCP discovery and trust policy,
- framework compatibility matrix,
- application-level integration tests,
- release automation with maintainer approval.

## Reviewer Checklist

Use this checklist when reviewing the developer preview:

- Does the application build request context from trusted server-side data?
- Are `user_id`, `tenant_id`, `plan`, `roles`, and `permissions` kept out of LLM control?
- Are privileged tools registered server-side and routed before agent use?
- Does the agent receive only the request-specific allowed tool surface?
- Are denied tools withheld from the agent?
- Is fallback behavior low-privilege and explicit?
- Are audit events produced for allow, deny, fallback, and invoke behavior?
- Are local audit limitations understood?
- Are JSON policy limitations understood?
- Are tenant, user, role, plan, and permission rules tested?
- Are optional LangChain/LangGraph integrations tested for the deployed framework versions?
- Are MCP-style server names sourced from trusted application state?
- Are non-goals understood before using the project in a sensitive environment?
- Is additional production hardening planned before enterprise use?
