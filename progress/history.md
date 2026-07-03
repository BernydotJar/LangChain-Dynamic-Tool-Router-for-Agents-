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
- Added futuristic terminal-native architecture diagrams to README.
- Added/updated product docs: product positioning, security model, policy format, audit log format, demo guide, admin dashboard notes, and release notes.
- Local verification is still required before moving Feature 004 to `review`.
