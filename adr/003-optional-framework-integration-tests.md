# 003 Optional Framework Integration Tests

Status: proposed

## Context

The Dynamic Tool Router intentionally began as a dependency-free package with LangChain-style and LangGraph-style adapter shapes. That kept the core library small and easy to embed, but it left a credibility gap: the repository has not yet proven those shapes against real LangChain and LangGraph package APIs.

Feature 002 added JSON policy loading and local audit persistence. The next validation step should exercise those pieces in realistic framework workflows.

## Decision

Feature 003 will specify optional real-framework integration coverage:

- Core router behavior remains dependency-free.
- LangChain and LangGraph tests/examples are separated from core unit tests.
- Missing optional dependencies produce clear skips or documented compatibility boundaries.
- Integration coverage must use JSON-loaded policy and file-backed audit persistence.
- Optional dependency installation or pyproject extras require explicit implementation approval.

## Consequences

- Users who only need the core router are not forced to install LangChain or LangGraph.
- Product credibility improves through real compatibility coverage.
- CI and local verification can keep fast core tests separate from framework tests.
- Compatibility may require maintenance as framework APIs evolve.
- A skip-safe MVP is honest about local dependency availability without overstating support.

## Alternatives Considered

- Add LangChain and LangGraph as hard dependencies: rejected because it violates the core dependency-light product design.
- Keep only pseudo-integration docs: rejected as insufficient for buyer credibility.
- Build a full production agent app: rejected as outside MVP scope.
- Delay integration coverage until SaaS features exist: rejected because compatibility evidence is a prerequisite for product trust.
