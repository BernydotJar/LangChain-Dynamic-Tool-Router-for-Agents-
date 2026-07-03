# Design: 004 Sellable Developer Preview

Feature: `004-sellable-developer-preview`

Mode: SHIP

## Design Goal

Convert the repository from an MVP implementation into a developer-preview product package that can be evaluated by buyers and technical decision makers.

This feature is primarily productization and release-readiness work, not new runtime authorization logic.

## Benchmark Principles From Successful Developer Tools

Successful developer tools and extensions tend to share these traits:

1. Immediate value in the first screen.
2. Copy-paste quickstart.
3. Clear installation path.
4. Realistic example data.
5. Strong visual/diagrammatic explanation.
6. Visible trust signals: tests, security model, limitations, release notes.
7. Progressive disclosure: simple first, advanced docs later.
8. Integration proof with the tools developers already use.
9. Honest operational boundaries.
10. A roadmap that makes the buyer believe the product can mature.

Feature 004 applies those principles without expanding into SaaS, billing, hosted APIs, or enterprise compliance.

## Product Narrative

The README and docs should consistently frame the product as:

> Auth0-style authorization for AI agent tools.

This is positioning, not a claim of feature parity with Auth0. The docs must explicitly avoid overclaiming.

## Proposed README Architecture

README sections:

1. Hero / one-liner.
2. Problem: agents are getting too many tools.
3. Product: runtime authorization and injection layer.
4. Futuristic text diagram.
5. Quickstart.
6. Demo flow.
7. Policy JSON example.
8. Audit event example.
9. LangChain/LangGraph integration note.
10. Security model summary.
11. Limitations.
12. Roadmap.
13. Harness/SDLC evidence.

## Futuristic Text Diagram Direction

Use terminal-friendly diagrams such as:

```text
┌──────────────────────────────────────────────────────────────────┐
│                    DYNAMIC TOOL ROUTER                           │
│              runtime authorization for agent tools               │
└──────────────────────────────────────────────────────────────────┘

       request context
 user ─ tenant ─ plan ─ roles ─ permissions ─ MCP servers
          │
          ▼
┌──────────────────────┐       ┌────────────────────────────┐
│  ToolPolicyRouter    │──────▶│  authorized tool surface   │
│  policy evaluation   │       │  injected at request time  │
└──────────────────────┘       └────────────────────────────┘
          │
          ├─ allow   → inject tool
          ├─ deny    → use fallback
          ├─ invoke  → record usage
          └─ audit   → persist governance trail
```

And:

```text
Before
======
Agent sees every tool it was created with.

After
=====
Agent sees only the tools this user, tenant, plan, and request may use.
```

## Documentation Design

### Product Positioning

`docs/product-positioning.md` should explain:

- target buyer,
- pain point,
- alternatives,
- why now,
- wedge use cases,
- what is intentionally not included.

### Security Model

`docs/security-model.md` should explain:

- this is authorization and routing logic,
- it is not a sandbox,
- it is not a secret manager,
- local audit files are not tamper-proof,
- dashboard is static and unauthenticated,
- policy validation reduces configuration mistakes but is not formal verification.

### Policy Format

`docs/policy-format.md` should document JSON policy fields, examples, validation behavior, and unsupported callable conditions.

### Audit Format

`docs/audit-log-format.md` should document JSONL events, exported JSON, event types, and expected fields.

### Demo Guide

`docs/demo-guide.md` should give a short local evaluation script.

### Release Notes

`docs/release-notes.md` should describe the developer preview, verification evidence, limitations, and next feature.

## File Plan

Create:

- `docs/product-positioning.md`
- `docs/security-model.md`
- `docs/policy-format.md`
- `docs/audit-log-format.md`
- `docs/demo-guide.md`
- `docs/release-notes.md`
- `progress/004-sellable-developer-preview.md`

Update during implementation:

- `README.md`
- `feature_list.json`
- `progress/current.md`
- `progress/history.md`
- existing example docs as needed

Create at review time:

- `progress/review_004-sellable-developer-preview.md`

## Lifecycle Design

Current Feature 003 is in `review` in the live repository. Feature 004 may be created as `spec_ready`, but it must not move to `approved` or `in_progress` until the team explicitly accepts the active-feature handling decision.

Recommended handling:

1. Close Feature 003 as `done` if its review evidence is accepted.
2. Move Feature 004 from `spec_ready` to `approved`.
3. Implement Feature 004 in SHIP mode.

## SHIP Review Gates

Feature 004 review must evaluate:

- product clarity,
- packaging clarity,
- documentation correctness,
- example correctness,
- security honesty,
- test evidence,
- integration dependency handling,
- remaining production gaps.

## Risks

- Overclaiming enterprise IAM parity.
- Overclaiming production security.
- Treating static dashboard as a secure admin app.
- Confusing optional integration skips with real installed integration proof.
- Making the README visually impressive but operationally vague.

## Decision

Feature 004 is a SHIP-mode productization feature. It should not introduce a hosted product, billing, database, or production auth provider. It should make the current package significantly easier to understand, trust, evaluate, and sell.
