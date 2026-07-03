# Review: 008 Demo Experience

Feature: `008-demo-experience`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

State change:

```text
in_progress -> review
```

## Summary

Feature 008 added a guided local demo experience for Runtime Tool Authorization for AI Agents.

The demo uses the current developer-preview implementation to show request context, JSON policy loading, allowed tool exposure, denied tool behavior, fallback behavior, audit evidence, and the LangChain/LangGraph adapter boundaries without introducing external service dependencies or runtime capability changes.

## Files Changed

- `examples/demo_experience/run_demo.py`
- `docs/demo-guide.md`
- `feature_list.json`
- `specs/008-demo-experience/tasks.md`
- `progress/008-demo-experience.md`
- `progress/current.md`
- `progress/history.md`
- `progress/review_008-demo-experience.md`

## Demo Assessment

The guided demo command is:

```sh
python examples/demo_experience/run_demo.py
```

It demonstrates:

- product identity and slogan,
- request context,
- tenant/user/role/plan/permission inputs,
- available MCP-style server context,
- JSON policy loading,
- candidate tool surface,
- allowed tool surface,
- denied destructive tool path,
- fallback tool behavior,
- audit event output,
- JSON audit export,
- LangChain-style adapter boundary,
- LangGraph-style adapter boundary.

The compact demo remains available:

```sh
python examples/basic_agent/run_example.py
```

## Verification Commands

```sh
python -m json.tool feature_list.json
```

Result:

```text
passed; JSON is valid and Feature 008 is registered as review
```

```sh
PYTHONPATH=src python -m unittest discover -s tests
```

Result:

```text
ss.....................
----------------------------------------------------------------------
Ran 23 tests in 0.007s

OK (skipped=2)
```

```sh
python examples/basic_agent/run_example.py
```

Result:

```text
passed; printed injected tools, LangGraph state tools, audit events, and audit export path
```

```sh
python examples/demo_experience/run_demo.py
```

Result:

```text
passed; printed request context, JSON policy loading, allowed/denied/fallback paths,
LangChain-style boundary, LangGraph-style boundary, audit events, and audit export path
```

```sh
PYTHONPATH=src python -m unittest discover -s tests/integration
```

Result:

```text
ss
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK (skipped=2)
```

## Product Claim Check

Claims remain grounded in current developer-preview behavior:

- local JSON policy loading exists,
- runtime tool injection exists,
- fallback behavior exists,
- local audit evidence exists,
- LangChain-style and LangGraph-style adapter boundaries exist,
- optional real-framework integration tests remain dependency-gated.

The review found no production-readiness, compliance, hosted IAM, SaaS, PyPI publish, git tag, or GitHub Release claim.

## Runtime Code Check

No runtime code changes were made.

Changed implementation content is limited to demo/docs/progress artifacts.

## Known Limitations

- The guided demo is local and dependency-light.
- The guided demo uses adapter boundaries rather than requiring LangChain/LangGraph packages.
- Optional integration tests skip explicitly when optional framework dependencies are absent.
- Audit files remain local and are not tamper-proof.
- No hosted policy API, auth-provider integration, SaaS admin workflow, real MCP discovery, compliance guarantee, PyPI publish, git tag, or GitHub Release is included.

## Recommendation

Move Feature 008 from `review` to `done` only after human closure approval.
