# Commercial Launch Runbook

Feature: `017-marketplace-publish-commercial-launch`

## Purpose

This runbook defines the first commercial access path for Runtime Tool Authorization.

The Marketplace listing is a distribution channel. Commercial access should be controlled through entitlement and license state.

## Commercial Positioning

Product:

```text
Runtime Tool Authorization for AI Agents
```

Message:

```text
Never expose every tool. Expose the right tool.
```

Target buyer:

- AI platform teams,
- SaaS teams adding agentic workflows,
- teams using LangChain, LangGraph, or MCP-style tool surfaces,
- teams that need plan, tenant, role, permission, and audit-aware tool access.

## First Offer

Initial commercial offer:

```text
Founding design partner access
Flat monthly access for early teams
Manual activation during developer preview
Direct feedback loop
```

The exact commercial terms should be handled outside this repository.

## Access Model

Recommended first access model:

```text
Public extension install
  +
Manual commercial onboarding
  +
License / entitlement activation
  +
Premium feature boundary
```

## Manual Activation Workflow

1. Customer requests access.
2. Confirm customer/team identity and plan.
3. Create a license or entitlement record using the existing developer-preview contract path.
4. Record activation date, renewal date, support contact, and plan.
5. Send activation instructions.
6. Track renewal and support manually until provider-neutral automation is implemented.

## What The Free Extension Should Provide

The public extension may provide:

- local policy initialization,
- local policy validation,
- local authorized-tool preview,
- local demo execution,
- local audit viewer,
- docs and onboarding.

## What Commercial Access Should Unlock Later

Commercial access may later unlock:

- team policy templates,
- premium policy packs,
- advanced audit export flows,
- design partner support,
- commercial support SLA,
- future provider-neutral entitlement automation.

## Non-Goals

- Do not put customer data in this repository.
- Do not add remote calls to the extension in this feature.
- Do not add live provider integration in this feature.
- Do not claim Marketplace-native commercial checkout.
- Do not claim production IAM.
- Do not claim compliance certification.

## Relationship To Feature 015

Feature 015 remains the correct place to implement provider-neutral commercial automation.

Feature 017 is about distribution and launch readiness, not live provider integration.

## Launch Checklist

Before outreach:

- Marketplace publish completed.
- Marketplace listing reviewed.
- Public install smoke test passed.
- Commercial offer text approved.
- Manual activation process confirmed.
- Support contact confirmed.
- Renewal tracking method confirmed.

## Current State

Commercial launch is prepared but not active until public publish and explicit commercial approval.
