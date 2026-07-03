# Demo Guide

This guide is the fastest local path to evaluate Dynamic Tool Router as a developer-preview product.

## Goal

Show that the router can:

1. load policy from JSON,
2. inject authorized tools at request time,
3. withhold tools that are not allowed,
4. route unavailable access to fallback behavior,
5. persist audit events,
6. export audit evidence,
7. demonstrate LangGraph-style state routing.

## Setup

```sh
python -m pip install -e .
```

## Run The Guided Demo

Use this command when showing the product to a new developer, CTO, or design partner:

```sh
python examples/demo_experience/run_demo.py
```

Expected output shape:

```text
Runtime Tool Authorization for AI Agents
Never expose every tool. Expose the right tool.

== 1. Request Context ==
...
== 2. JSON Policy Loading ==
...
== 3. Runtime Tool Authorization ==
Candidate tool surface: search_docs, fetch_customer_record, delete_customer_record
Allowed tool surface: search_docs, fetch_customer_record, not_authorized
Denied path: delete_customer_record -> plan is not allowed -> fallback not_authorized
...
== 7. Audit Evidence ==
1. action=authorize, tool=search_docs, allowed=True, reason=authorized
...
Audit export: /tmp/.../guided_demo_audit_export.json
```

The guided demo shows:

1. request context,
2. tenant/user/role/plan/permission policy inputs,
3. JSON policy loading,
4. allowed tool exposure,
5. denied tool behavior,
6. fallback behavior,
7. audit event output,
8. LangChain-style adapter boundary,
9. LangGraph-style adapter boundary.

It does not require LangChain, LangGraph, external services, a database, or hosted infrastructure.

## Run The Compact Demo

```sh
python examples/basic_agent/run_example.py
```

Expected output shape:

```text
Injected tools: search_docs, fetch_customer_record, not_authorized
LangGraph state tools: search_docs, not_authorized
Audit export: /tmp/.../runtime_audit_export.json
```

## What To Look For

The guided demo is optimized for comprehension. The compact demo is optimized for quick smoke verification.

### Authorized Tool

A tool allowed by policy should appear in the injected tool list.

### Tool Not Allowed By Policy

A tool that is not allowed by policy should not appear as itself. It should route to the configured fallback tool when fallback is enabled.

### Fallback Tool

The fallback tool should make unavailable access explicit without adding the original tool to the allowed tool surface.

### Persisted Audit

The demo should produce a local audit export path. Open the exported JSON to inspect allow, deny, fallback, and invoke behavior.

## Verify Core Tests

```sh
PYTHONPATH=src python -m unittest discover -s tests
```

## Verify Optional Integration Tests

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If LangChain/LangGraph optional packages are not installed, tests should skip with explicit messages instead of failing core verification.

## Manual Demo Script

Use this short narration:

```text
This is an authorization layer for agent tools.
The same agent can receive a different tool surface per user, tenant, plan, permission set, and request context.
Here the router loads JSON policy, injects allowed tools, withholds unavailable tools, returns a fallback, and persists audit evidence.
```

## Buyer Demo Frame

```text
Without Dynamic Tool Router:
  Create an agent -> give it tools -> hope every request is allowed to use them.

With Dynamic Tool Router:
  Create an agent -> evaluate request policy -> inject only authorized tools -> audit the decision.
```

## Troubleshooting

### Module import issue

Run with `PYTHONPATH=src` or install locally:

```sh
python -m pip install -e .
```

### Integration Tests Skip

This is acceptable in core developer-preview verification if optional dependencies are absent. Install LangChain/LangGraph dependencies only when you want real-framework verification.

### Audit File Not Found

Re-run the basic example and check the printed `Audit export:` path.
