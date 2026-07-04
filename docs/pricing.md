# Pricing And Monetization

Runtime Tool Authorization for AI Agents should be sold as agent infrastructure, not as a cheap editor extension.

## Core Positioning

Your AI agent should not see every tool.

Most agent frameworks ask:

```text
Which tools should the agent use?
```

Runtime Tool Authorization asks:

```text
Which tools is this user, tenant, role, plan, and request allowed to use right now?
```

For less than the cost of one premium AI developer-tool seat, add runtime tool authorization to your agent stack.

## Public Launch Pricing

Start free for 30 days.

Then:

| Plan | Price | Buyer | Use Case |
|---|---:|---|---|
| Solo | `$9/month` | Individual AI engineer, consultant, technical founder | Local or developer-preview evaluation of runtime tool authorization. |
| Team | `$19/user/month` | Engineering teams building agent products | Multi-user evaluation for tenant, role, plan, permission, and request-aware tool access. |
| Design Partner | `$49/month` flat for up to 5 users | First 20 qualified design partners | Non-production pilot with direct feedback loop and founding price lock. |
| Enterprise | Custom | Larger teams and security reviewers | Future/custom scope such as production hardening, SSO, hosted policy APIs, compliance workflows, audit retention, and security review. |

## Design Partner Offer

We are accepting 20 design partners to shape the runtime authorization layer for AI agents.

Design partner terms:

- `$49/month` flat for up to 5 users.
- First 20 design partners only.
- Founding price locked for 12 months.
- Non-production evaluation only.
- Best fit for teams already building LangChain, LangGraph, MCP-style, or internal agent tooling.

## How Users Can Try It And Then Pay

Do not rely on an editor marketplace to enforce payment.

Use this flow instead:

```text
1. User installs the extension, package, or local demo.
2. User starts a 30-day trial from the product website.
3. Stripe creates the customer and subscription trial.
4. Your backend creates a license entitlement.
5. User signs in or pastes a license key into the extension/demo.
6. The extension/demo calls your entitlement API.
7. If entitlement is active or trialing, premium features are enabled.
8. If entitlement is expired, canceled, or missing, premium features are disabled or downgraded.
```

The product should remain installable and useful enough to evaluate, but premium behavior should require entitlement validation.

## Recommended Billing Architecture

### 1. Public install, gated premium capability

The package or extension can be publicly installable.

Premium capabilities should be gated by entitlement:

- policy bundle export,
- multi-tenant policy profiles,
- saved team configuration,
- hosted audit export,
- design partner support workflow,
- team license seats,
- future hosted policy API access.

Developer-preview local examples can remain free.

### 2. Stripe as the billing system

Use Stripe for:

- Checkout or Payment Links,
- 30-day subscription trial,
- recurring monthly billing,
- plan changes,
- cancellation,
- customer portal,
- webhook events.

Important events to handle:

- subscription created,
- trial ending soon,
- subscription updated,
- invoice payment succeeded,
- invoice payment failed,
- subscription canceled or paused.

### 3. Entitlement backend

Create a minimal entitlement service.

Suggested data model:

```text
customers
- id
- email
- stripe_customer_id
- created_at

subscriptions
- id
- customer_id
- stripe_subscription_id
- plan
- status
- trial_ends_at
- current_period_ends_at
- seat_limit

licenses
- id
- customer_id
- license_key_hash
- status
- plan
- seat_limit
- expires_at

license_activations
- id
- license_id
- machine_fingerprint_hash
- user_label
- activated_at
- last_seen_at
```

The extension or demo should never trust local state alone. It should periodically call:

```text
GET /v1/entitlements/me
```

Expected response shape:

```json
{
  "status": "active",
  "plan": "team",
  "seat_limit": 5,
  "trial_ends_at": null,
  "features": [
    "policy_profiles",
    "team_config",
    "audit_export"
  ]
}
```

### 4. Grace period

Use a short grace period for developer experience.

Recommended behavior:

```text
Online and active: premium enabled.
Offline with recently valid entitlement: premium enabled for 72 hours.
Expired, canceled, or over grace period: premium disabled with upgrade CTA.
```

This avoids breaking demos during travel, conferences, or local development.

### 5. License key rules

Use license keys for developer-preview simplicity.

Rules:

- Store only hashed license keys on your backend.
- Do not hard-code secrets in the extension.
- Do not rely on client-side checks as the source of truth.
- Allow users to rotate license keys.
- Limit activations by plan.
- Keep free local examples available.

## Recommended Product Gating

Free trial should include enough value to prove the category:

- local policy loading,
- request-time authorization demo,
- fallback behavior,
- audit evidence export,
- LangChain/LangGraph adapter examples.

Paid plans should unlock commercial usage patterns:

| Feature | Free Trial | Solo | Team | Design Partner | Enterprise |
|---|---:|---:|---:|---:|---:|
| Local demo | yes | yes | yes | yes | yes |
| JSON policy examples | yes | yes | yes | yes | yes |
| Basic audit export | yes | yes | yes | yes | yes |
| Multiple saved policy profiles | trial | yes | yes | yes | custom |
| Team seat management | no | no | yes | yes | custom |
| Design partner support | no | no | no | yes | custom |
| Hosted policy API | no | no | no | no | future/custom |
| SSO | no | no | no | no | future/custom |
| Compliance workflow | no | no | no | no | future/custom |
| Audit retention | no | no | no | no | future/custom |

## Payment Copy

Short version:

```text
Start free for 30 days.
Then $9/month for solo builders or $19/user/month for teams.
```

Design partner version:

```text
We are accepting 20 design partners to shape the runtime authorization layer for AI agents.
Founding design partners get a $49/month flat plan for up to 5 users, locked for 12 months.
```

Value anchor:

```text
For less than the cost of one premium AI developer-tool seat, add runtime tool authorization to your agent stack.
```

## What Not To Claim Yet

Do not claim current support for:

- production readiness,
- enterprise readiness,
- compliance certification,
- IAM replacement,
- sandboxing,
- prompt-injection prevention,
- guaranteed security outcomes,
- hosted policy API availability,
- SSO availability,
- audit retention availability.

Enterprise copy may describe these as future/custom scope only.

## Implementation Recommendation

Start with the simplest paid architecture:

```text
Stripe Checkout + webhook receiver + entitlement table + license key validation endpoint.
```

Do not build a complex account portal first. Use Stripe's customer portal for billing self-management and keep your backend focused on entitlements.

## Minimum Paid MVP

The first monetized version only needs:

- a pricing page,
- Stripe Checkout links,
- a webhook handler,
- an entitlement database,
- a license key screen,
- a validation endpoint,
- a 72-hour grace period,
- upgrade CTA when entitlement is missing or expired.

That is enough to let people use it first, then charge money when the trial ends.
