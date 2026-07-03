# Requirements: 008 Demo Experience

Feature: `008-demo-experience`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Summary

Specify a stronger developer-preview demo experience for Runtime Tool Authorization for AI Agents.

The demo should help a new developer understand the product in under three minutes:

```text
Runtime Tool Authorization
for AI Agents

Never expose every tool.
Expose the right tool.
```

## Objective

In the implementation phase, improve the local demo so it clearly shows request-time tool authorization across policy, request context, allowed tools, denied tools, fallback behavior, audit evidence, and framework boundaries.

This spec gate does not implement demo code and does not modify the README.

## Acceptance Criteria

- [ ] Demo can be understood by a new developer in under three minutes.
- [ ] Demo clearly shows allowed tool exposure.
- [ ] Demo clearly shows denied tool behavior.
- [ ] Demo clearly shows fallback behavior.
- [ ] Demo clearly shows request context.
- [ ] Demo clearly shows tenant, user, role, plan, and permission policy.
- [ ] Demo clearly shows audit event output.
- [ ] Demo clearly shows JSON policy loading.
- [ ] Demo clearly shows LangChain-style boundary.
- [ ] Demo clearly shows LangGraph-style boundary.
- [ ] Demo defines expected demo commands.
- [ ] Demo defines expected output shape.
- [ ] Demo strategy decides whether implementation should use a CLI script, guided terminal walkthrough, recorded-output fixture, or combination.
- [ ] Claims remain grounded in developer-preview behavior.
- [ ] Runtime capability changes are avoided unless explicitly approved in the implementation gate.
- [ ] No external service dependencies are introduced.

## Non-Goals

- Do not implement demo code during this spec gate.
- Do not modify README during this spec gate.
- Do not modify runtime code during this spec gate.
- Do not publish to PyPI.
- Do not create a git tag.
- Do not create a GitHub Release.
- Do not add hosted services.
- Do not add external service dependencies.
- Do not claim production readiness.

## Required Demo Concepts

The implementation phase must show:

- allowed tool exposure
- denied tool behavior
- fallback behavior
- request context
- tenant/user/role/plan/permission policy
- audit event output
- JSON policy loading
- LangChain-style boundary
- LangGraph-style boundary

## Candidate Demo Shape

The implementation should evaluate a combination of:

- CLI script for one-command execution
- guided terminal walkthrough for human-readable narrative
- recorded-output fixture for deterministic documentation and review

The final implementation choice should be documented before code changes in the implementation-phase progress artifact.

## Spec-Gate Validation

Run:

```sh
python -m json.tool feature_list.json
```

## Implementation Verification After Approval

Expected minimum verification:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

If the implementation adds a new demo command, that command must also be run and captured in the review artifact.
