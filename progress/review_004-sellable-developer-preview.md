# SHIP Review: 004 Sellable Developer Preview

Feature: `004-sellable-developer-preview`

Mode: SHIP

Reviewer: AI-assisted review with human-provided local verification evidence

## Summary

Pass/Fail: Pass for SHIP review readiness.

Feature 004 productized the Dynamic Tool Router developer preview by adding a buyer-facing README, product positioning, demo guide, policy and audit documentation, security model, admin dashboard notes, release notes, and SHIP-mode release framing.

## State Reviewed

Feature state before review: `in_progress`

Recommended feature state after review artifact: `review`

## Files Changed

- `README.md`
- `feature_list.json`
- `progress/current.md`
- `progress/history.md`
- `progress/004-sellable-developer-preview.md`
- `progress/review_004-sellable-developer-preview.md`
- `docs/product-positioning.md`
- `docs/security-model.md`
- `docs/policy-format.md`
- `docs/audit-log-format.md`
- `docs/demo-guide.md`
- `docs/admin-dashboard.md`
- `docs/release-notes.md`
- `adr/004-ship-mode-sellable-developer-preview.md`
- `specs/004-sellable-developer-preview/requirements.md`
- `specs/004-sellable-developer-preview/design.md`
- `specs/004-sellable-developer-preview/tasks.md`
- `epics/SHIP-001-developer-preview-release.md`

## Product Readiness Assessment

The project now presents a clearer commercial identity:

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

The README now explains:

- the missing authorization layer,
- the multi-tenant agent-tool governance problem,
- runtime policy evaluation,
- authorized tool injection,
- fallback routing,
- audit persistence,
- LangChain/LangGraph compatibility,
- developer-preview boundaries.

## README Assessment

Pass.

The README now includes:

- stronger hero,
- terminal-native diagrams,
- Mermaid request lifecycle,
- quickstart,
- demo output expectations,
- policy example,
- audit example,
- documentation links,
- security summary,
- verification commands,
- SHIP roadmap,
- harness evidence.

## Documentation Assessment

Pass.

New and updated docs support developer-preview evaluation:

- product positioning,
- security model,
- policy format,
- audit log format,
- demo guide,
- admin dashboard caveats,
- release notes.

## Security Assessment

Pass with documented limitations.

The documentation avoids claiming production security, Auth0 parity, compliance readiness, tamper-proof audit, dashboard authentication, or enterprise IAM replacement.

Known security limitations remain explicit:

- local audit files are not tamper-proof,
- static dashboard is unauthenticated,
- no hosted policy API,
- no production auth-provider integration,
- no compliance guarantees,
- no sandboxing.

## Verification Evidence

Human-provided local verification output confirmed:

```sh
python -m json.tool feature_list.json
# passed; valid JSON printed

PYTHONPATH=src python -m unittest discover -s tests
# Ran 23 tests in 0.008s
# OK (skipped=2)

python examples/basic_agent/run_example.py
# passed
# demonstrated injected tools, search_docs invocation, LangGraph state tools, audit events, denied delete_customer_record fallback, and audit export

PYTHONPATH=src python -m unittest discover -s tests/integration
# Ran 2 tests in 0.000s
# OK (skipped=2)
```

## Integration Dependency Status

LangChain/LangGraph integration tests remain dependency-gated. Local run skipped 2 tests, consistent with Feature 003 behavior.

## Known Limitations

- Developer preview only.
- No hosted SaaS backend.
- No billing.
- No production auth-provider integration.
- No database-backed policy store.
- No tamper-proof audit sink.
- No authenticated admin dashboard.
- No retention or redaction controls.
- Optional real-framework tests may skip if dependencies are absent.

## SHIP-Mode Gaps

- Need README 3.0 final landing-page polish under Feature 005.
- Need architecture/Mermaid diagram expansion.
- Need demo experience hardening.
- Need GitHub trust signals such as CONTRIBUTING, SECURITY, CHANGELOG, license review, and release packaging.
- Need release versioning and packaging strategy.

## Recommendation

Move Feature 004 from `in_progress` to `review`.

Do not close as `done` until human closure approval is recorded.

Recommended next feature after closure: `005-readme-3-landing-page`.
