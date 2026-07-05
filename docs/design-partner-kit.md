# Design Partner Kit

Runtime Tool Authorization for AI Agents

Never expose every tool. Expose the right tool.

## Executive Summary

Runtime Tool Authorization is a developer-preview authorization layer for AI agents that controls which tools are visible, injectable, invokable, denied, routed to fallback behavior, and recorded as audit evidence per request.

This design partner kit is for teams evaluating whether runtime tool authorization belongs in their agent infrastructure before they build or scale multi-tenant agentic systems.

It is designed for structured, non-production evaluation conversations. It is not a production rollout plan, compliance claim, IAM replacement, sandbox, or hosted enterprise control plane.

## Design Partner Offer

We are accepting 20 design partners to shape the runtime authorization layer for AI agents.

Founding design partner terms:

- `$49/month` flat for up to 5 users.
- First 20 design partners only.
- Founding price locked for 12 months.
- Non-production pilot only.
- Best fit for teams building real LangChain, LangGraph, MCP-style, or internal agent tooling.

The offer is intentionally simple: install and evaluate the developer-preview package, map one real non-production workflow into request context plus policy, review fallback behavior and audit evidence, then decide whether the model belongs in the partner's agent infrastructure roadmap.

Commercial use should be gated through a billing-backed entitlement layer, not marketplace install gating. See `docs/pricing.md`.

## Ideal Design Partner Profile

A strong design partner is building or operating agentic workflows where tool access changes by request, user, tenant, role, plan, permission, workflow state, or available MCP-style server surface.

Good-fit teams usually have at least one of these conditions:

- multiple tenants or customer accounts,
- internal users with different roles and permissions,
- plan-based or tier-based access to tools,
- agents connected to sensitive business systems,
- LangChain, LangGraph, MCP-style, or comparable tool orchestration,
- a need for explicit allow, deny, fallback, and invoke evidence,
- concern that prompt-only tool control is too weak for real product workflows.

## Buyer Personas And Evaluator Roles

| Role | What they evaluate |
|---|---|
| CTO / VP Engineering | Whether the architecture fills a real infrastructure gap and can become production-hardened later. |
| AI Platform Lead | Whether runtime tool authorization fits the team platform model. |
| Staff / Principal Engineer | Whether the policy, adapter, audit, and fallback model is technically credible. |
| Security Reviewer | Whether claims are bounded and evidence is inspectable. |
| Product Lead | Whether the design supports role, plan, tenant, and workflow-specific agent behavior. |

## Target Pain Points

The kit is intended for teams experiencing these problems:

1. Every agent receives too many tools.
2. Tool access is filtered manually in application code.
3. Tool visibility does not vary cleanly by tenant, role, plan, or permission.
4. Unsafe or unavailable tools do not have consistent fallback behavior.
5. Tool authorization decisions are not recorded as reviewable evidence.
6. Security posture relies too heavily on prompts or conventions.
7. Agent framework configuration is static while product authorization is dynamic.

## Design Partner Qualification Criteria

A design partner should be able to answer most of these questions:

- Which agent workflows are you building?
- Which tools can the agent currently access?
- Which tools should vary by tenant, user, role, plan, or permission?
- Which tools are sensitive enough to require deny/fallback behavior?
- What audit evidence would reviewers expect?
- Are you evaluating this in a non-production environment?
- Are you willing to provide feedback on policy shape, adapter shape, and audit evidence?

## Discovery Questions

Use these questions in a first design partner call.

### Architecture Fit

- What agent framework or orchestration layer are you using?
- Do agents receive tools statically or dynamically?
- Where do user, tenant, plan, role, and permission context come from?
- Do you already use MCP-style servers or server-scoped tool catalogs?

### Authorization Fit

- Which tools should be available to all users?
- Which tools should be gated by plan, role, permission, or tenant?
- What should happen when a user asks for an unavailable tool?
- Do you need a safe fallback tool or a hard deny path?

### Audit Fit

- Which decisions need to be recorded?
- Who reviews authorization events?
- What evidence format is useful for your team?
- Do you need local proof-of-concept evidence before considering a database or hosted audit sink?

### Pilot Fit

- What non-production workflow could test the model safely?
- What sample tools can be used without touching sensitive production systems?
- What would make the pilot successful?
- What would make the pilot a bad fit?

## Pilot Scope Template

```text
Design Partner Pilot

Team:
Use case:
Agent framework:
Pilot environment:
Pilot duration:
Commercial plan: Design Partner, $49/month flat for up to 5 users
Founding price lock: 12 months

Request context dimensions:
- user:
- tenant:
- plan:
- roles:
- permissions:
- workflow state:
- available MCP-style servers:

Candidate tools:
- tool 1:
- tool 2:
- tool 3:

Authorization rules to test:
- rule 1:
- rule 2:
- rule 3:

Fallback behavior:
Audit evidence expected:
Success criteria:
Out-of-scope items:
```

## Safe Non-Production Evaluation Scenarios

Start with scenarios that exercise authorization behavior without touching production systems.

Example scenarios:

1. Analyst can search docs but cannot delete customer records.
2. Pro-plan user can fetch CRM records but free-plan user cannot.
3. Admin can access a sensitive tool while analyst receives fallback behavior.
4. Tenant A receives a different tool surface than Tenant B.
5. Missing MCP-style server removes a tool from the allowed surface.
6. Denied tool request records an audit event with reason and fallback metadata.

## Demo Call Script

Use this structure for a 20-30 minute technical call.

### 0-3 min: Problem Framing

Explain the product question:

```text
Which tools is this user, tenant, plan, role, and request allowed to use right now?
```

### 3-8 min: Architecture Walkthrough

Show the request lifecycle:

1. app resolves request context,
2. router evaluates policy,
3. router exposes authorized tool surface,
4. agent receives only routed tools,
5. audit store records allow, deny, fallback, and invoke evidence.

### 8-15 min: Guided Demo

Run:

```sh
python examples/demo_experience/run_demo.py
```

Point out:

- request context,
- JSON policy loading,
- allowed tool surface,
- denied tool behavior,
- fallback behavior,
- audit evidence.

### 15-22 min: Partner Scenario Mapping

Ask the partner to map one real workflow into:

- request context,
- candidate tools,
- policy rules,
- fallback behavior,
- audit evidence.

### 22-30 min: Pilot Framing

Agree on:

- one non-production scenario,
- expected policy behavior,
- expected audit evidence,
- feedback format,
- next decision point.

### Commercial Close

Use this only after technical fit is clear:

```text
We are accepting 20 design partners to shape the runtime authorization layer for AI agents.
The design partner plan is $49/month flat for up to 5 users, locked for 12 months.
The pilot stays non-production and focuses on proving whether request-time tool authorization belongs in your agent infrastructure roadmap.
```

## Success Metrics

A design partner evaluation is successful if it produces clear answers to these questions:

- Can the partner express their tool authorization model as request context plus policy?
- Does the allowed tool surface match expected tenant, role, plan, and permission behavior?
- Does fallback behavior reduce unsafe tool exposure without pretending to secure the underlying tool?
- Is audit evidence useful enough for engineering and security review?
- Are the current developer-preview limitations acceptable for continued evaluation?
- What production-hardening work would be required before real deployment?

## Feedback Checklist

Collect feedback in these categories:

- policy format clarity,
- request context dimensions,
- adapter fit for the partner framework,
- fallback semantics,
- audit event usefulness,
- documentation clarity,
- demo clarity,
- missing security boundaries,
- production-hardening requirements,
- design partner willingness to continue.

## Suggested Outbound Message

```text
Hi <name>,

I am building Runtime Tool Authorization for AI Agents: a developer-preview layer that controls which tools an agent can see and use per request, tenant, role, plan, permission, and available MCP-style tool surface.

The problem it targets is simple: most agent frameworks make tool access easy to configure but harder to govern dynamically in multi-tenant products.

I am accepting 20 design partners to review the architecture, run the local demo, and map one non-production agent workflow into a policy + fallback + audit model.

Founding design partners get a $49/month flat plan for up to 5 users, locked for 12 months.

This is not a production IAM product yet. The goal is structured technical feedback on whether this belongs in real agent infrastructure.

Would you be open to a 30-minute technical design partner conversation?
```

## Security Discussion Guide

Use precise language.

Say:

- runtime authorization layer,
- controlled tool surface,
- local audit evidence,
- developer-preview boundary,
- not a sandbox,
- not an IAM replacement,
- not tamper-proof,
- requires production hardening before enterprise use.

Do not say:

- production-ready,
- enterprise-ready,
- compliant,
- certified,
- prevents prompt injection,
- secures all tools,
- replaces IAM,
- tamper-proof audit.

## Non-Goals And Boundaries

This design partner kit does not claim:

- production readiness,
- enterprise readiness,
- compliance certification,
- IAM replacement,
- sandboxing,
- tamper-proof audit,
- hosted control plane availability,
- prompt-injection prevention,
- security of individual tool implementations.

## What To Bring To A Design Partner Call

Ask the partner to bring:

- one agent workflow,
- three to five candidate tools,
- user roles or permissions,
- one tenant or plan distinction,
- one tool that should be denied or routed to fallback,
- one audit question a reviewer would ask.

## Next Step Template

```text
Recommended next step:

- Map one non-production agent workflow into request context + policy.
- Run the guided demo locally.
- Compare expected vs actual allowed tool surface.
- Review audit evidence.
- Decide whether to continue to a deeper technical pilot.
```
