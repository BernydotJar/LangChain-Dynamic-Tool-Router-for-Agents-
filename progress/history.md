# History

## 001-dynamic-tool-router

- Inspected linked GitHub repository; it contained only `.gitignore`.
- Created standalone Python package structure.
- Added harness-style feature registry, specs, docs, ADR, and progress files.
- Implemented policy routing, runtime injection, audit logging, fallback routing, and adapters.
- Added examples, tests, and admin dashboard artifact.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Closure approval received for MVP.
- Moved feature from `review` to `done`.
- Accepted known MVP gaps: no persistent audit sink, static unauthenticated dashboard, no real LangChain/LangGraph integration tests, and no hosted policy management API.

## 002-persistent-policy-and-audit-store

- Created spec-gate artifacts for file-backed policy configuration and audit persistence.
- Registered Feature 002 as `spec_ready`.
- Approval received for MVP implementation.
- Implemented `FilePolicyStore`, `PolicyBundle`, and `FileAuditStore`.
- Added JSON policy example and JSON Lines audit sample.
- Updated the basic example to load policy from JSON and persist/export audit events.
- Added tests for policy loading, invalid policy rejection, audit persistence, audit export, and fallback behavior.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Moved Feature 002 from `review` to `done` after closure approval.
- Accepted known MVP limitations: JSON policies do not support callable condition rules, local audit files are not tamper-proof, no database, no hosted API, no retention policy, no redaction policy, no locking, no compliance guarantees, and dashboard remains static and unauthenticated.

## 003-langchain-langgraph-real-integration-tests

- Created spec-gate artifacts for optional real LangChain/LangGraph integration coverage.
- Registered Feature 003 as `spec_ready`.
- Approval received for MVP implementation.
- Added dependency-gated LangChain integration test for `langchain_core.tools.tool`.
- Added dependency-gated LangGraph integration test for `langgraph.graph.StateGraph`.
- Added shared integration fixtures for JSON-loaded policy, fallback routing, and `FileAuditStore`.
- Documented optional integration verification and local missing-dependency skip behavior.
- Verified with unit tests, basic example, registry JSON validation, and integration test discovery.
- Moved Feature 003 from `review` to `done` after closure approval.

## 004-sellable-developer-preview

- Reframed the next increment from MVP-only work into SHIP-mode productization.
- Registered Feature 004 as `spec_ready`.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Embedded developer-tool product principles: one-screen clarity, copy-paste quickstart, immediate demo path, futuristic text diagrams, realistic examples, security honesty, verification evidence, integration proof, and roadmap.
- Approval received to close Feature 003 and approve Feature 004.
- Rewrote README for sellable developer-preview positioning.
- Added Runtime Tool Authorization product identity to README.
- Added terminal-native architecture diagrams and Mermaid request lifecycle to README.
- Added and updated product docs: product positioning, security model, policy format, audit log format, demo guide, admin dashboard notes, and release notes.

## SHIP-001-developer-preview-release

- Created the SHIP epic for the commercial developer-preview release.
- Defined Wave 1, Wave 2, and Wave 3 release tracks.
- Captured the product identity: Runtime Tool Authorization for AI Agents.
- Captured the commercial message: Never expose every tool. Expose the right tool.

## 005-readme-3-landing-page

- Created requirements, design, tasks, ADR, and progress artifacts.
- Registered Feature 005 as `spec_ready`.
- Preserved Feature 004 as the active `in_progress` feature during the spec gate.
- Feature 005 implementation waited for Feature 004 verification and review handling.
- Closed as `done` after README 3.0 verification and review artifact creation.

## 006-github-trust-signals

- Created and closed trust-signal work for repository credibility.
- Preserved harness evidence, governance files, and developer-preview boundaries.
- Closed as `done` after trust-signal verification and review artifact creation.

## 007-architecture-mermaid-diagrams

- Created SHIP-001 Wave 1 spec-gate artifacts for architecture visuals.
- Registered Feature 007 as `spec_ready`.
- Created ADR 007 for architecture visual language.
- Approval received for SHIP-mode implementation.
- Created `docs/architecture.md` as the canonical architecture document.
- Added terminal-native and Mermaid diagrams for system architecture, request lifecycle, policy decision flow, before/after tool exposure, audit lifecycle, MCP-style filtering, and adapter boundaries.
- Updated product positioning and security docs with architecture cross-references.
- Verified with registry JSON validation, unit tests, basic demo, manual Markdown link checks, Mermaid compatibility checks, claim grounding, and no-runtime-code-change checks.
- Created `progress/review_007-architecture-mermaid-diagrams.md`.
- Moved Feature 007 from `review` to `done` after closure approval.
- Accepted limitations: no runtime code changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, and no runtime capability change.

## 008-demo-experience

- Created SHIP-001 Wave 1 spec-gate artifacts for the stronger developer-preview demo experience.
- Registered Feature 008 as `spec_ready`.
- Created ADR 008 for demo experience strategy.
- Approval received for SHIP-mode implementation.
- Added guided local demo at `examples/demo_experience/run_demo.py`.
- Updated `docs/demo-guide.md` with guided demo command and expected output shape.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, and integration test discovery.
- Created `progress/review_008-demo-experience.md`.
- Moved Feature 008 from `review` to `done` after closure approval.
- Accepted limitations: no runtime `src/` code changes, no external services, no mandatory LangChain/LangGraph dependency, no PyPI publish, no git tag, no GitHub Release, and no production-readiness claim.

## 009-packaging-and-release

- Ran `python scripts/verify_release_candidate.py`.
- Fixed the verifier to run tests with `PYTHONPATH=src` and to install the `dev` extra before `python -m build`.
- Verification passed for registry JSON, unit tests, basic demo, integration tests, editable install, dev-extra install, and package build.
- Recorded package build warnings for license metadata as a non-blocking follow-up.
- Created `progress/review_009-packaging-and-release.md`.
- Moved Feature 009 from `review` to `done` after closure approval.
- Accepted limitations: no PyPI publish, no git tag, no GitHub Release, and setuptools license metadata warning deferred as a non-blocking follow-up.

## 010-release-candidate-polish

- Opened Feature 010 as a SHIP-mode spec gate.
- Registered Feature 010 as `spec_ready`.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Approval received for SHIP-mode implementation.
- Aligned README roadmap, documentation index, release checklist, release notes, and CHANGELOG with current developer-preview state.
- Added guided demo execution to release-candidate verification.
- Aligned architecture, security-model, product-positioning, and demo-guide language around Runtime Tool Authorization for AI Agents.
- Preserved no-release-action constraints: no PyPI publish, no git tag, and no GitHub Release.
- Preserved runtime behavior; no `src/` runtime code changes were made.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration tests, and release-candidate verifier.
- Created `progress/review_010-release-candidate-polish.md`.
- Moved Feature 010 from `review` to `done` after closure approval.
- Accepted limitations: no runtime code changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, and setuptools license metadata warnings remain a documented follow-up.

## 011-security-whitepaper

- Opened Feature 011 as a SHIP-mode spec gate.
- Registered Feature 011 as `spec_ready`.
- Tied Feature 011 to SHIP-001 Wave 2: make CTOs and technical reviewers trust the project.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Captured future implementation scope for `docs/security-whitepaper.md`.
- Captured security posture, runtime authorization boundary, request context, policy evaluation, allow/deny/fallback behavior, audit evidence, local audit limitations, JSON policy limitations, adapter boundaries, MCP-style filtering, tenant/user/role/plan/permission constraints, threat model, non-goals, developer-preview limitations, future hardening, and reviewer checklist.
- Approval received for SHIP-mode implementation.
- Created `docs/security-whitepaper.md`.
- Added README discoverability for the security whitepaper.
- Updated `docs/security-model.md` to cross-link the consolidated whitepaper.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration tests, and release-candidate verifier.
- Created `progress/review_011-security-whitepaper.md`.
- Moved Feature 011 from `review` to `done` after closure approval.
- Accepted limitations: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no IAM replacement claim, no compliance certification claim, no tamper-proof audit claim, no sandboxing claim, no hosted enterprise control-plane claim, and setuptools license metadata warnings remain a documented follow-up.

## 012-design-partner-kit

- Opened Feature 012 as a SHIP-mode spec gate.
- Registered Feature 012 as `spec_ready`.
- Tied Feature 012 to SHIP-001 Wave 3: design partner readiness.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Captured future implementation scope for `docs/design-partner-kit.md`.
- Captured ideal design partner profile, buyer personas, target pain points, qualification criteria, discovery questions, pilot scope, safe non-production evaluation scenarios, demo call script, success metrics, feedback checklist, outbound message, and boundaries.
- Approval received to continue from `spec_ready` into implementation.
- Created `docs/design-partner-kit.md`.
- Added README discoverability for the design partner kit.
- Documented ideal design partner profile, buyer personas, target pain points, qualification criteria, discovery questions, pilot scope, safe non-production evaluation scenarios, demo call script, success metrics, feedback checklist, suggested outbound message, security discussion guide, and explicit non-goals.
- Preserved hard constraints: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no enterprise-readiness claim, no compliance certification claim, and no guaranteed security outcome claim.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration tests, and release-candidate verifier.
- Created `progress/review_012-design-partner-kit.md`.
- Moved Feature 012 from `review` to `done` after closure approval.
- Accepted limitations: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no enterprise-readiness claim, no compliance certification claim, no guaranteed security outcome claim, and setuptools license metadata warnings remain a documented follow-up.

## 013-pricing-and-landing-copy

- Opened Feature 013 as a SHIP-mode spec gate.
- Registered Feature 013 as `spec_ready`.
- Tied Feature 013 to SHIP-001 Wave 3: commercial readiness.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Captured placement strategy: README conversion section, canonical `docs/pricing.md`, and design partner offer inside `docs/design-partner-kit.md`.
- Captured pricing strategy: 30-day free trial, `$9/month` Solo, `$19/user/month` Team, `$49/month` design partner flat plan for up to 5 users, first 20 design partners, and 12-month founding price lock.
- Captured required copy blocks for category contrast, hero, pricing CTA, design partner CTA, and premium AI developer-tool seat value anchor.
- Approval received for SHIP-mode implementation.
- Created `docs/pricing.md`.
- Added README pricing section and link to `docs/pricing.md`.
- Updated `docs/design-partner-kit.md` with the first-20 design partner offer.
- Added monetization architecture: public install, Stripe billing, entitlement backend, license validation, and grace-period behavior.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration tests, editable install, editable install with dev extra, package build, and release-candidate verifier.
- Created `progress/review_013-pricing-and-landing-copy.md`.
- Moved Feature 013 from `in_progress` to `review` after verification.
- Closure approval received.
- Moved Feature 013 from `review` to `done`.
- Accepted limitations: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no enterprise-readiness claim, no compliance certification claim, no guaranteed security outcome claim, and setuptools license metadata warnings remain a documented follow-up.

## 014-stripe-entitlement-billing

- Opened Feature 014 as a SHIP-mode spec gate.
- Registered Feature 014 as `spec_ready`.
- Tied Feature 014 to SHIP-001 Wave 3: commercial readiness.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Preserved Features 001 through 013 as `done`.
- Captured billing flow: public install, 30-day trial, Stripe Checkout, Stripe subscription, Stripe webhooks, entitlement DB, license/API validation, and premium feature gating.
- Captured Stripe products and prices: Solo `$9/month`, Team `$19/user/month`, and Design Partner `$49/month` flat for up to 5 users.
- Captured required webhook events: checkout completion, subscription created/updated/deleted, trial ending, invoice paid, and invoice payment failed.
- Captured entitlement states, API contracts, data model, license activation rules, grace-period behavior, secret-handling rules, feature flags, and test strategy.
- Approval received for SHIP-mode implementation.
- Moved Feature 014 from `spec_ready` to `in_progress`.
- Created `src/tool_policy_router/billing.py`.
- Exported billing contracts from `src/tool_policy_router/__init__.py`.
- Created `tests/test_billing.py`.
- Created `docs/stripe-entitlement-billing.md`.
- Created `.env.example` with safe placeholders only.
- Updated README documentation index, developer-preview boundary, roadmap, and billing references.
- Implemented plan-to-price mapping, Checkout session boundary, Customer Portal session boundary, mock Stripe gateway, entitlement state mapping, premium feature mapping by plan, license key hashing, machine fingerprint hashing, activation/deactivation store, activation limit enforcement, webhook idempotency, and webhook payload hashing.
- Verified with registry JSON validation, unit tests, basic demo, guided demo, integration tests, editable install, editable install with dev extra, package build, and release-candidate verifier.
- Created `progress/review_014-stripe-entitlement-billing.md`.
- Moved Feature 014 from `in_progress` to `review` after verification.
- Accepted limitations: no real Stripe SDK dependency, no dependency changes, no Stripe live secrets, no webhook signing secret, no customer data, no live payment operation, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no enterprise-readiness claim, no compliance certification claim, no guaranteed security outcome claim, and setuptools license metadata warnings remain a documented follow-up.
