# Current Progress

## Active Feature

`013-pricing-and-landing-copy`

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

Feature 013 status: `in_progress`

Feature 013 is in implementation after approval. Pricing and monetization copy has been added, but verification is still required before review.

## Product Direction

The product is framed as:

> Runtime Tool Authorization for AI Agents.
>
> Never expose every tool. Expose the right tool.

The intended buyer is a team building multi-tenant LangChain/LangGraph agents that needs runtime tool authorization, tenant-aware policy control, fallback behavior, and audit evidence.

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

## Feature 013 Implementation

Created and updated:

- `docs/pricing.md`
- `README.md`
- `docs/design-partner-kit.md`
- `specs/013-pricing-and-landing-copy/tasks.md`
- `progress/013-pricing-and-landing-copy.md`

Implemented pricing:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.
- Design Partner: `$49/month` flat for up to 5 users.
- First 20 design partners only.
- Founding price locked for 12 months.
- Enterprise: custom future/custom scope.

Implemented monetization architecture:

```text
public install -> 30-day trial -> Stripe billing -> entitlement backend -> license/API validation -> premium features enabled or disabled
```

Decision:

- Do not rely on marketplace install gating for payment enforcement.
- Keep developer-preview local examples useful for evaluation.
- Gate commercial and team capabilities through active entitlement.
- Use a short grace period for offline developer experience.

Hard constraints preserved:

- No runtime code changes.
- No dependency changes.
- No PyPI publish.
- No git tag.
- No GitHub Release.
- No production-readiness claim.
- No enterprise-readiness claim.
- No compliance certification claim.
- No guaranteed security outcome claim.

## Next Valid Lifecycle Action

Run verification:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```

After verification passes, create `progress/review_013-pricing-and-landing-copy.md` and move Feature 013 to `review`.

Do not close Feature 013 until explicit closure approval is received.
