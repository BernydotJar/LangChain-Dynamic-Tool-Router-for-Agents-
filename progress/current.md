# Current Progress

## Active Feature

None. Feature 014 is closed as `done`.

## Current State

Feature 001 status: `done`

Feature 002 status: `done`

Feature 003 status: `done`

Feature 004 status: `done`

Feature 005 status: `done`

Feature 006 status: `done`

Feature 007 status: `done`

Feature 008 status: `done`

Feature 009 status: `done`

Feature 010 status: `done`

Feature 011 status: `done`

Feature 012 status: `done`

Feature 013 status: `done`

Feature 014 status: `done`

Feature 014 is closed after successful verification, review artifact creation, and explicit closure approval.

## Product Direction

The product is framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, audit evidence, and entitlement-backed premium access.

## SHIP Epic

Created:

- `epics/SHIP-001-developer-preview-release.md`

SHIP-001 owns the commercial developer-preview release across GitHub, LinkedIn, and early design partner conversations.

## Recently Closed

Feature 004 is closed as `done` after local verification and SHIP review artifact creation.

Feature 005 is closed as `done` after README 3.0 verification and SHIP review artifact creation.

Feature 006 is closed as `done` after trust signal verification and SHIP review artifact creation.

Feature 009 is closed as `done` after release-candidate verification and SHIP review artifact creation.

Feature 007 is closed as `done` after architecture documentation verification and SHIP review artifact creation.

Feature 008 is closed as `done` after guided demo verification and SHIP review artifact creation.

Feature 010 is closed as `done` after release-candidate polish verification and SHIP review artifact creation.

Feature 011 is closed as `done` after security whitepaper verification and SHIP review artifact creation.

Feature 012 is closed as `done` after design partner kit verification and SHIP review artifact creation.

Feature 013 is closed as `done` after pricing, monetization architecture, release-candidate verification, and SHIP review artifact creation.

Feature 014 is closed as `done` after Stripe entitlement billing implementation, release-candidate verification, SHIP review artifact creation, and closure approval.

Review artifacts:

- `progress/review_004-sellable-developer-preview.md`
- `progress/review_005-readme-3-landing-page.md`
- `progress/review_006-github-trust-signals.md`
- `progress/review_009-packaging-and-release.md`
- `progress/review_007-architecture-mermaid-diagrams.md`
- `progress/review_008-demo-experience.md`
- `progress/review_010-release-candidate-polish.md`
- `progress/review_011-security-whitepaper.md`
- `progress/review_012-design-partner-kit.md`
- `progress/review_013-pricing-and-landing-copy.md`
- `progress/review_014-stripe-entitlement-billing.md`

## Feature 014 Closed Scope

Created and updated:

- `src/tool_policy_router/billing.py`
- `src/tool_policy_router/__init__.py`
- `tests/test_billing.py`
- `docs/stripe-entitlement-billing.md`
- `.env.example`
- `README.md`
- `specs/014-stripe-entitlement-billing/tasks.md`
- `progress/014-stripe-entitlement-billing.md`
- `progress/review_014-stripe-entitlement-billing.md`

Implemented contracts:

- plan-to-price mapping,
- Checkout session creation boundary,
- Customer Portal session creation boundary,
- mock Stripe gateway,
- entitlement state mapping,
- premium feature mapping by plan,
- license key hashing,
- machine fingerprint hashing,
- license activation/deactivation store,
- activation limit enforcement,
- webhook event idempotency store,
- webhook payload hashing.

Verification passed:

- `python -m json.tool feature_list.json`
- `PYTHONPATH=src python -m unittest discover -s tests`
- `python examples/basic_agent/run_example.py`
- `python examples/demo_experience/run_demo.py`
- `PYTHONPATH=src python -m unittest discover -s tests/integration`
- `python scripts/verify_release_candidate.py`

Hard constraints preserved:

- No real Stripe SDK dependency was added.
- No dependency changes were made.
- No Stripe live secret keys were committed.
- No webhook signing secret was committed.
- No customer data was committed.
- No live payment operation was performed.
- No PyPI publish.
- No git tag.
- No GitHub Release.
- No production-readiness claim.
- No enterprise-readiness claim.
- No compliance certification claim.
- No guaranteed security outcome claim.

Known non-blocking follow-up:

- Setuptools license metadata deprecation warnings remain.

## Next Valid Lifecycle Action

Open the next feature as a new spec gate before implementation.
