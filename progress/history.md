# History

## 001-dynamic-tool-router

- Inspected linked GitHub repository; it contained only `.gitignore`.
- Created standalone Python package structure.
- Added harness-style feature registry, specs, docs, ADR, and progress files.
- Implemented policy routing, runtime injection, audit logging, fallback routing, and adapters.
- Added examples, tests, and admin dashboard artifact.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Human closure approval received for MVP.
- Moved feature from `review` to `done`.
- Accepted known MVP gaps: no persistent audit sink, static unauthenticated dashboard, no real LangChain/LangGraph integration tests, and no hosted policy management API.
- Recommended next feature: `002-persistent-policy-and-audit-store`.

## 002-persistent-policy-and-audit-store

- Created spec-gate artifacts for file-backed policy configuration and audit persistence.
- Registered Feature 002 as `spec_ready`.
- Preserved Feature 001 as `done`.
- Human approval received for MVP implementation.
- Moved Feature 002 to `in_progress`.
- Implemented `FilePolicyStore`, `PolicyBundle`, and `FileAuditStore`.
- Added JSON policy example and JSON Lines audit sample.
- Updated the basic example to load policy from JSON and persist/export audit events.
- Added tests for policy loading, invalid policy rejection, audit persistence, audit export, and fallback behavior.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Moved Feature 002 to `review`.
- Human closure approval received for MVP.
- Moved Feature 002 from `review` to `done`.
- Accepted known MVP limitations: JSON policies do not support callable condition rules, local audit files are not tamper-proof, no database, no hosted API, no retention policy, no redaction policy, no locking, no compliance guarantees, and dashboard remains static and unauthenticated.
- Recommended next feature: `003-langchain-langgraph-real-integration-tests`.

## 003-langchain-langgraph-real-integration-tests

- Confirmed Feature 001 is `done`.
- Confirmed Feature 002 is `done`.
- Created spec-gate artifacts for optional real LangChain/LangGraph integration coverage.
- Registered Feature 003 as `spec_ready`.
- Human approval received for MVP implementation.
- Moved Feature 003 to `in_progress`.
- Added dependency-gated LangChain integration test for `langchain_core.tools.tool`.
- Added dependency-gated LangGraph integration test for `langgraph.graph.StateGraph`.
- Added shared integration fixtures for JSON-loaded policy, fallback routing, and `FileAuditStore`.
- Documented optional integration verification and local missing-dependency skip behavior.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Verified with `python -m json.tool feature_list.json`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests/integration`.
- Moved Feature 003 to `review`.
- Human closure approval received.
- Moved Feature 003 from `review` to `done`.

## 004-sellable-developer-preview

- Reframed the next increment from MVP-only work into SHIP-mode productization.
- Registered Feature 004 as `spec_ready`.
- Preserved Feature 001 and Feature 002 as `done`.
- Preserved Feature 003 as `review`; Feature 004 implementation waited for explicit lifecycle handling.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Embedded developer-tool product principles: one-screen clarity, copy-paste quickstart, immediate demo path, futuristic text diagrams, realistic examples, security honesty, verification evidence, integration proof, and roadmap.
- Human approval received to close Feature 003 and approve Feature 004.
- Moved Feature 004 from `spec_ready` to `in_progress`.
- Rewrote README for sellable developer-preview positioning.
- Added Runtime Tool Authorization product identity to README.
- Added futuristic terminal-native architecture diagrams and Mermaid request lifecycle to README.
- Added/updated product docs: product positioning, security model, policy format, audit log format, demo guide, admin dashboard notes, and release notes.
- Local verification is still required before moving Feature 004 to `review`.

## SHIP-001-developer-preview-release

- Created the SHIP epic for the commercial developer-preview release.
- Defined Wave 1, Wave 2, and Wave 3 release tracks.
- Captured the product identity: Runtime Tool Authorization for AI Agents.
- Captured the commercial message: Never expose every tool. Expose the right tool.

## 005-readme-3-landing-page

- Created requirements, design, tasks, ADR, and progress artifacts.
- Registered Feature 005 as `spec_ready`.
- Preserved Feature 004 as the active `in_progress` feature.
- Feature 005 must not enter implementation until Feature 004 verification and review handling are complete.

## 009-packaging-and-release

- Ran `python scripts/verify_release_candidate.py`.
- Fixed the verifier to run tests with `PYTHONPATH=src` and to install the `dev` extra before `python -m build`.
- Verification passed for registry JSON, unit tests, basic demo, integration tests, editable install, dev-extra install, and package build.
- Recorded package build warnings for license metadata as a non-blocking follow-up.
- Created `progress/review_009-packaging-and-release.md`.
- Moved Feature 009 from `in_progress` to `review`.
- Human closure approval received.
- Moved Feature 009 from `review` to `done`.
- Accepted limitations: no PyPI publish, no git tag, no GitHub Release, and setuptools license metadata warning deferred as a non-blocking follow-up.

## 007-architecture-mermaid-diagrams

- Preserved existing feature numbering.
- Created SHIP-001 Wave 1 spec-gate artifacts for architecture visuals.
- Registered Feature 007 as `spec_ready`.
- Created ADR 007 for architecture visual language.
- Implementation not started; `docs/architecture.md` and README diagrams were deferred until approval.
- Human approval received for SHIP-mode implementation.
- Moved Feature 007 to `in_progress`.
- Created `docs/architecture.md` as the canonical architecture document.
- Added terminal-native and Mermaid diagrams for system architecture, request lifecycle, policy decision flow, before/after tool exposure, audit lifecycle, MCP-style filtering, and adapter boundaries.
- Updated product positioning and security docs with architecture cross-references.
- Verified with `python -m json.tool feature_list.json`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Completed manual Markdown link, Mermaid compatibility, claim grounding, and no-runtime-code-change checks.
- Created `progress/review_007-architecture-mermaid-diagrams.md`.
- Moved Feature 007 from `in_progress` to `review`.
- Human closure approval received.
- Moved Feature 007 from `review` to `done`.
- Accepted limitations: no runtime code changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, and no runtime capability change.
- Recommended next feature: `008-demo-experience` as a spec gate only.

## 008-demo-experience

- Confirmed local branch is current with `origin/main`.
- Confirmed Features 001, 002, 003, 004, 005, 006, 007, and 009 are `done`.
- Created SHIP-001 Wave 1 spec-gate artifacts for the stronger developer-preview demo experience.
- Registered Feature 008 as `spec_ready`.
- Created ADR 008 for demo experience strategy.
- Implementation not started; README, runtime code, publishing, tags, and GitHub Releases were not touched.
- Human approval received for SHIP-mode implementation.
- Moved Feature 008 from `spec_ready` to `in_progress`.
- Added guided local demo at `examples/demo_experience/run_demo.py`.
- Updated `docs/demo-guide.md` with guided demo command and expected output shape.
- Verified with `python -m json.tool feature_list.json`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Verified with `python examples/demo_experience/run_demo.py`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests/integration`.
- Created `progress/review_008-demo-experience.md`.
- Moved Feature 008 from `in_progress` to `review`.
- Human closure approval received.
- Moved Feature 008 from `review` to `done`.
- Accepted limitations: no runtime `src/` code changes, no external services, no mandatory LangChain/LangGraph dependency, no PyPI publish, no git tag, no GitHub Release, and no production-readiness claim.
- Recommended next candidate: `010-release-candidate-polish` for GitHub release readiness, or `010-design-partner-kit` for outbound selling.

## 010-release-candidate-polish

- Opened Feature 010 as a SHIP-mode spec gate.
- Registered Feature 010 as `spec_ready`.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Preserved Features 001 through 009 as `done`.
- No implementation changes were made.
- Next valid lifecycle action is explicit human approval for `spec_ready -> approved`.
- Human approval received for SHIP-mode implementation.
- Moved Feature 010 from `spec_ready` through approved implementation to `review`.
- Aligned README roadmap, documentation index, release checklist, release notes, and CHANGELOG with current developer-preview state.
- Added guided demo execution to release-candidate verification.
- Aligned architecture, security-model, product-positioning, and demo-guide language around Runtime Tool Authorization for AI Agents.
- Preserved no-release-action constraints: no PyPI publish, no git tag, and no GitHub Release.
- Preserved runtime behavior; no `src/` runtime code changes were made.
- Verified with `python -m json.tool feature_list.json`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Verified with `python examples/demo_experience/run_demo.py`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests/integration`.
- Verified with `python scripts/verify_release_candidate.py` after rerunning with network escalation for pip/build dependency resolution.
- Created `progress/review_010-release-candidate-polish.md`.
- Human closure approval received.
- Moved Feature 010 from `review` to `done`.
- Accepted limitations: no runtime code changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, and setuptools license metadata warnings remain a documented follow-up.
- No next feature was opened during the closure pass.

## 011-security-whitepaper

- Opened Feature 011 as a SHIP-mode spec gate.
- Registered Feature 011 as `spec_ready`.
- Tied Feature 011 to SHIP-001 Wave 2: make CTOs and technical reviewers trust the project.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Preserved Features 001 through 010 as `done`.
- Captured future implementation scope for `docs/security-whitepaper.md`.
- Captured required coverage for security posture, runtime authorization boundary, request context, policy evaluation, allowed and denied tool surfaces, fallback behavior, audit evidence, local audit limitations, JSON policy limitations, LangChain/LangGraph adapter boundary, MCP-style filtering, and tenant/user/role/plan/permission constraints.
- Captured threat-model topics: overexposed tools, tenant leakage, role or permission mismatch, unsafe invocation, prompt-only control weakness, audit evidence gaps, and local file tampering.
- Captured explicit non-claims: no production readiness, IAM replacement, compliance certification, tamper-proof audit, sandboxing, or hosted enterprise control plane.
- No implementation changes were made.
- `docs/security-whitepaper.md` was not created.
- Next valid lifecycle action is explicit human approval for `spec_ready -> approved`.
- Human approval received for SHIP-mode implementation.
- Moved Feature 011 from `spec_ready` to approved implementation.
- Created `docs/security-whitepaper.md`.
- Added README discoverability for the security whitepaper.
- Updated `docs/security-model.md` to cross-link the consolidated whitepaper.
- Documented security posture, trust boundary, request context model, policy evaluation model, allowed and denied tool behavior, fallback behavior, audit evidence, local audit limitations, JSON policy limitations, adapter boundaries, MCP-style filtering, tenant/user/role/plan/permission constraints, threat model, non-goals, developer-preview limitations, future hardening, and reviewer checklist.
- Preserved hard constraints: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no IAM replacement claim, no compliance certification claim, no tamper-proof audit claim, no sandboxing claim, no hosted enterprise control-plane claim, no prompt-injection prevention claim, and no claim that individual tool implementations are secured.
- Verified with `python -m json.tool feature_list.json`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Verified with `python examples/demo_experience/run_demo.py`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests/integration`.
- `python scripts/verify_release_candidate.py` passed local checks but failed install/build steps in the sandbox because network access was blocked while resolving `setuptools` and `wheel`.
- Escalation for the release-candidate verifier was rejected by the environment because the workspace is out of credits.
- Local rerun of `python scripts/verify_release_candidate.py` completed successfully.
- Release-candidate verification passed for registry JSON, unit tests, basic demo, guided demo, integration tests, editable install, editable install with dev extra, and package build.
- Setuptools license metadata deprecation warnings remain a documented non-blocking follow-up.
- Created `progress/review_011-security-whitepaper.md`.
- Moved Feature 011 from `in_progress` to `review`.
- Human closure approval received.
- Moved Feature 011 from `review` to `done`.
- Accepted limitations: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no IAM replacement claim, no compliance certification claim, no tamper-proof audit claim, no sandboxing claim, no hosted enterprise control-plane claim, and setuptools license metadata warnings remain a documented follow-up.
- No next feature was opened during the closure pass.

## 012-design-partner-kit

- Opened Feature 012 as a SHIP-mode spec gate.
- Registered Feature 012 as `spec_ready`.
- Tied Feature 012 to SHIP-001 Wave 3: design partner readiness.
- Created requirements, design, tasks, ADR, and progress artifacts.
- Preserved Features 001 through 011 as `done`.
- Captured future implementation scope for `docs/design-partner-kit.md`.
- Captured required coverage for ideal design partner profile, buyer personas, target pain points, qualification criteria, discovery questions, pilot scope, safe non-production evaluation scenarios, demo call script, success metrics, feedback checklist, outbound message, and boundaries.
- No implementation changes were made.
- `docs/design-partner-kit.md` was not created.
- Next valid lifecycle action is explicit human approval for `spec_ready -> approved`.
- Human approval received to continue from `spec_ready` into implementation.
- Moved Feature 012 to `in_progress`.
- Created `docs/design-partner-kit.md`.
- Added README discoverability for the design partner kit.
- Updated README roadmap to show Feature 010 and Feature 011 as `done` and Feature 012 as `in progress`.
- Documented ideal design partner profile, buyer personas, target pain points, qualification criteria, discovery questions, pilot scope, safe non-production evaluation scenarios, demo call script, success metrics, feedback checklist, suggested outbound message, security discussion guide, and explicit non-goals.
- Preserved hard constraints: no runtime code changes, no dependency changes, no PyPI publish, no git tag, no GitHub Release, no production-readiness claim, no enterprise-readiness claim, no compliance certification claim, and no guaranteed security outcome claim.
- Verified with `python -m json.tool feature_list.json`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests`.
- Verified with `python examples/basic_agent/run_example.py`.
- Verified with `python examples/demo_experience/run_demo.py`.
- Verified with `PYTHONPATH=src python -m unittest discover -s tests/integration`.
- Verified with `python scripts/verify_release_candidate.py`.
- Release-candidate verification passed for unit tests, basic demo, guided demo, integration tests, editable install, editable install with dev extra, and package build.
- Setuptools license metadata deprecation warnings remain a documented non-blocking follow-up.
- Created `progress/review_012-design-partner-kit.md`.
- Moved Feature 012 from `in_progress` to `review`.
- Feature 012 is not closed; next valid lifecycle action is explicit human approval for `review -> done`.
