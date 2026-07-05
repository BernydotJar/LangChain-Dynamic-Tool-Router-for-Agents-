# History

## 001-dynamic-tool-router

- Created the initial standalone Python package structure.
- Added harness-style feature registry, specs, docs, ADR, and progress files.
- Implemented policy routing, runtime injection, audit logging, fallback routing, and adapters.
- Added examples, tests, and admin dashboard artifact.
- Verified with unit tests and the basic example.
- Closed as `done` after approval.

## 002-persistent-policy-and-audit-store

- Added file-backed policy configuration and audit persistence.
- Implemented `FilePolicyStore`, `PolicyBundle`, and `FileAuditStore`.
- Added JSON policy example and JSON Lines audit sample.
- Updated the basic example to load policy from JSON and persist/export audit events.
- Added tests for policy loading, invalid policy rejection, audit persistence, audit export, and fallback behavior.
- Closed as `done` after verification and approval.

## 003-langchain-langgraph-real-integration-tests

- Added optional real LangChain and LangGraph integration coverage.
- Added dependency-gated tests for `langchain_core.tools.tool` and `langgraph.graph.StateGraph`.
- Added shared integration fixtures for JSON-loaded policy, fallback routing, and `FileAuditStore`.
- Closed as `done` after verification and approval.

## 004-sellable-developer-preview

- Reframed the project from MVP-only work into SHIP-mode productization.
- Added Runtime Tool Authorization product identity.
- Rewrote README for developer-preview positioning.
- Added product docs for positioning, security model, policy format, audit format, demo guide, dashboard notes, and release notes.

## SHIP-001-developer-preview-release

- Created the SHIP epic for the commercial developer-preview release.
- Defined Wave 1, Wave 2, and Wave 3 tracks.
- Captured the product identity: Runtime Tool Authorization for AI Agents.
- Captured the commercial message: Never expose every tool. Expose the right tool.

## 005-readme-3-landing-page

- Created README 3.0 landing-page artifacts.
- Preserved Feature 004 as active during spec gate.
- Closed as `done` after README verification and review artifact creation.

## 006-github-trust-signals

- Added GitHub trust-signal work for repository credibility.
- Preserved harness evidence, governance files, and developer-preview boundaries.
- Closed as `done` after verification and review artifact creation.

## 007-architecture-mermaid-diagrams

- Created `docs/architecture.md` as canonical architecture documentation.
- Added terminal-native and Mermaid diagrams for system architecture, request lifecycle, policy decision flow, before/after tool exposure, audit lifecycle, MCP-style filtering, and adapter boundaries.
- Updated product positioning and security docs with architecture cross-references.
- Closed as `done` after verification and approval.

## 008-demo-experience

- Added guided local demo at `examples/demo_experience/run_demo.py`.
- Updated `docs/demo-guide.md` with guided demo command and expected output shape.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, and integration test discovery.
- Closed as `done` after approval.

## 009-packaging-and-release

- Added release-candidate verification through `scripts/verify_release_candidate.py`.
- Fixed verifier behavior for `PYTHONPATH=src` and dev-extra build setup.
- Verified registry JSON, unit tests, examples, integration discovery, editable install, dev-extra install, and package build.
- Recorded setuptools license metadata warnings as non-blocking follow-up.
- Closed as `done` after approval.

## 010-release-candidate-polish

- Aligned README roadmap, documentation index, release checklist, release notes, and CHANGELOG.
- Added guided demo execution to release-candidate verification.
- Preserved no-release-action constraints: no PyPI publish, no git tag, and no GitHub Release.
- Closed as `done` after verification and approval.

## 011-security-whitepaper

- Created `docs/security-whitepaper.md`.
- Documented runtime authorization boundary, request context, policy evaluation, fallback behavior, audit evidence, local audit limitations, JSON policy limitations, adapter boundaries, MCP-style filtering, threat model, non-goals, and reviewer checklist.
- Added README discoverability and cross-linked from `docs/security-model.md`.
- Closed as `done` after verification and approval.

## 012-design-partner-kit

- Created `docs/design-partner-kit.md`.
- Documented ideal design partner profile, buyer personas, pain points, qualification criteria, discovery questions, pilot scope, demo call script, success metrics, feedback checklist, outbound message, security discussion guide, and non-goals.
- Preserved developer-preview boundaries.
- Closed as `done` after verification and approval.

## 013-pricing-and-landing-copy

- Created `docs/pricing.md`.
- Added README pricing section and link to pricing docs.
- Updated `docs/design-partner-kit.md` with the first-20 design partner offer.
- Added monetization architecture for trial, billing-backed entitlement, license validation, and grace-period behavior.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration discovery, editable install, dev-extra install, package build, and release-candidate verifier.
- Closed as `done` after approval.

## 014-stripe-entitlement-billing

- Created Stripe entitlement billing spec, design, tasks, ADR, and progress artifacts.
- Implemented mock-safe billing contracts in `src/tool_policy_router/billing.py`.
- Exported billing contracts from `src/tool_policy_router/__init__.py`.
- Created `tests/test_billing.py`.
- Created `docs/stripe-entitlement-billing.md`.
- Created `.env.example` with safe placeholders only.
- Updated README documentation index, developer-preview boundary, roadmap, and billing references.
- Implemented plan mapping, Checkout boundary, Customer Portal boundary, mock gateway, entitlement mapping, premium feature mapping, license hashing, machine fingerprint hashing, activation/deactivation store, activation limits, webhook idempotency, and payload hashing.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration discovery, editable install, dev-extra install, package build, and release-candidate verifier.
- Created `progress/review_014-stripe-entitlement-billing.md`.
- Closed as `done` after approval.
- Accepted limitations: no real provider dependency, no dependency changes, no customer data, no live charge operation, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no enterprise-readiness claim, no compliance certification claim, no guaranteed security outcome claim, and setuptools license metadata warnings remain a follow-up.

## 015-billing-provider-abstraction

- Opened Feature 015 as a SHIP-mode spec gate.
- Registered Feature 015 as `spec_ready`.
- Tied Feature 015 to SHIP-001 Wave 3: commercial readiness.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Updated README roadmap and billing language so Feature 014 is `done` and Feature 015 is `spec_ready`.
- Captured provider-agnostic direction: entitlement is core, Stripe is optional, manual license activation is valid for developer preview, and merchant-of-record/local gateway paths remain future adapters.
- No runtime provider abstraction was implemented.
- No new provider dependency was added.
- Next valid lifecycle action is explicit approval for `spec_ready -> in_progress`.
