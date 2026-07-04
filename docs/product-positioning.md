# Product Positioning

## Product Name

Runtime Tool Authorization for AI Agents

## One-Liner

Auth0-style authorization for AI agent tools.

## Category

Runtime tool governance for LangChain and LangGraph agents.

## Buyer Problem

Agent products are moving from small static tool lists into multi-tenant systems with many tools, dynamic MCP-style tool surfaces, and request-specific permissions.

Without a routing layer, an agent may be created with tools that should not be visible for a given user, tenant, plan, role, or request context.

## Wedge

Runtime Tool Authorization provides the missing authorization layer between:

```text
agent runtime  ←→  tool catalog
```

It evaluates policy at request time and injects only the tools the current principal/context may use.

For the canonical architecture view, see [`architecture.md`](architecture.md).

## Target Buyers

### AI Platform Teams

Need shared policy primitives for agents embedded across products.

### SaaS Product Teams

Need per-tenant and per-plan tool gating before shipping agents to customers.

### Security / Governance Teams

Need audit evidence showing what tool was allowed, denied, invoked, or routed to fallback.

### Developer Tooling Teams

Need LangChain/LangGraph-compatible middleware patterns without adding a heavy dependency to the core package.

## Positioning Statement

For teams shipping multi-tenant agents, Runtime Tool Authorization is a tool authorization layer that selects, injects, denies, and audits agent tools by user, tenant, plan, permission, context, and available MCP-style tool surface.

Unlike static agent tool registration, it evaluates policy at request time and persists governance evidence.

## What This Is

- A runtime tool authorization layer.
- A policy-driven tool injector.
- A fallback router for unauthorized tools.
- A local developer-preview policy and audit store.
- A LangChain/LangGraph-compatible adapter shape.

## What This Is Not

- Not a hosted SaaS yet.
- Not an Auth0 replacement.
- Not an Okta replacement.
- Not an OPA/Rego engine.
- Not a secret manager.
- Not a sandbox.
- Not a compliance product.
- Not tamper-proof audit infrastructure.

## Core Message

```text
Never expose every tool.
Expose the right tool.
```

## Demo Promise

In under a minute, a developer should see:

1. a policy loaded from JSON,
2. an authorized tool injected,
3. an unauthorized tool denied,
4. a fallback tool returned,
5. audit events persisted and exported.

## Roadmap Narrative

```text
Developer Preview
  └─ local policy + audit + examples

Team Preview
  └─ admin policy editor + MCP discovery adapter

Enterprise Preview
  └─ hosted policy API + tamper-resistant audit + auth-provider integration
```
