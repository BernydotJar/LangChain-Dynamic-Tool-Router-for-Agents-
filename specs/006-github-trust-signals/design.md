# Design: 006 GitHub Trust Signals

Feature: `006-github-trust-signals`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Design Intent

Trust files should make the repo feel like a serious open-source infrastructure project while remaining honest about developer-preview maturity.

## Files

- `SECURITY.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `CODE_OF_CONDUCT.md`
- `LICENSE` if absent
- README trust-signal section

## Trust Principles

1. Be explicit about scope.
2. Make local verification easy.
3. Explain the harness workflow.
4. Avoid unsupported security claims.
5. Make design-partner evaluation easier.

## README Placement

Add a compact section near Documentation or Verification:

```text
## Trust & Project Governance

- SECURITY.md
- CONTRIBUTING.md
- CHANGELOG.md
- CODE_OF_CONDUCT.md
- Harness SDLC evidence
```

## Security Framing

Security language must distinguish:

- routing authorization,
- tool visibility,
- local audit evidence,
- non-goals such as sandboxing, IAM replacement, compliance, and tamper-proof audit.

## Contributor Framing

Contributors must run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

## Release Framing

Changelog starts at developer-preview milestones rather than pretending a production release exists.
