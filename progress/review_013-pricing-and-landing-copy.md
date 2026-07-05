# Review: 013 Pricing And Landing Copy

Feature: `013-pricing-and-landing-copy`

Mode: SHIP

State: `review`

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Commercial Readiness

## Summary

Feature 013 added commercial pricing, design partner pricing, and monetization architecture for Runtime Tool Authorization for AI Agents.

The feature moved to `review` after release-candidate verification completed successfully.

## Files Changed

Primary documentation:

- `docs/pricing.md`
- `README.md`
- `docs/design-partner-kit.md`

Lifecycle and harness artifacts:

- `feature_list.json`
- `specs/013-pricing-and-landing-copy/tasks.md`
- `progress/013-pricing-and-landing-copy.md`
- `progress/current.md`
- `progress/history.md`
- `progress/review_013-pricing-and-landing-copy.md`

## Accepted Pricing

Public launch:

- 30-day free trial.
- Solo: `$9/month`.
- Team: `$19/user/month`.

Design partner:

- First 20 design partners.
- `$49/month` flat for up to 5 users.
- Founding price locked for 12 months.

Enterprise:

- Custom future/custom scope.

## Accepted Monetization Architecture

Use this model:

```text
public install -> 30-day trial -> Stripe billing -> entitlement backend -> license/API validation -> premium features enabled or disabled
```

Payment enforcement should happen through a billing-backed entitlement layer, not marketplace install gating.

## Verification Evidence

Required verification passed:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
python examples/demo_experience/run_demo.py
PYTHONPATH=src python -m unittest discover -s tests/integration
python scripts/verify_release_candidate.py
```

`python scripts/verify_release_candidate.py` completed with:

- unit tests: PASS, ran 23 tests, skipped 2
- basic demo: PASS
- guided demo: PASS
- integration tests: PASS, ran 2 tests, skipped 2
- editable install: PASS
- editable install with dev extra: PASS
- package build: PASS

The verifier ended with:

```text
Release candidate verification completed.
```

## Manual Checks

Accepted manual checks:

- README link to `docs/pricing.md` resolves.
- `docs/pricing.md` exists.
- `docs/design-partner-kit.md` includes the design partner offer.
- Pricing preserves developer-preview maturity.
- Enterprise section is explicitly future/custom scope.
- No production-readiness claim was introduced.
- No enterprise-readiness claim was introduced.
- No compliance certification claim was introduced.
- No guaranteed security outcome claim was introduced.
- No runtime behavior changed.
- No dependency changes were introduced.
- No release action was performed.

## Constraints Preserved

- No runtime code changed.
- No dependencies changed.
- No PyPI publish occurred.
- No git tag was created.
- No GitHub Release was created.
- No production-readiness claim was introduced.
- No enterprise-readiness claim was introduced.
- No compliance certification claim was introduced.
- No guaranteed security outcome claim was introduced.

## Known Non-Blocking Follow-Up

Setuptools emitted license metadata deprecation warnings during package build. The package build completed successfully, but the license metadata warning remains a follow-up item for a later feature.

## Next Valid Lifecycle Action

Human closure approval:

```text
APPROVAL TO CLOSE
FEATURE: 013-pricing-and-landing-copy
MODE: SHIP
STATE CHANGE: review -> done
```
