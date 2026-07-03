# Design: 008 Demo Experience

Feature: `008-demo-experience`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: SHIP-001 Wave 1

## Approach

Feature 008 should turn the existing local demo into a sharper developer-preview experience without changing core runtime capabilities.

The demo should tell one concise story:

```text
An application receives a request.
The request has a user, tenant, plan, roles, permissions, context, and available tool surface.
The router loads JSON policy.
The router exposes only authorized tools.
Denied tools are withheld.
Fallback gives the agent a safe response path.
Audit events prove what happened.
LangChain-style and LangGraph-style boundaries remain dependency-light.
```

## Demo Experience Options

The implementation phase should choose one or a combination:

### CLI Script

Pros:

- one command
- easy to verify
- good for README snippets

Potential command:

```sh
python examples/demo_experience/run_demo.py
```

### Guided Terminal Walkthrough

Pros:

- teaches product concepts in order
- works well for screenshots and recorded demos
- helps CTOs and developers follow the story

Potential command:

```sh
python examples/demo_experience/walkthrough.py
```

### Recorded-Output Fixture

Pros:

- deterministic reference output
- easy to review in PRs
- useful for docs

Potential artifact:

```text
examples/demo_experience/expected_output.txt
```

## Expected Output Shape

The demo output should be scannable in a terminal:

```text
Runtime Tool Authorization for AI Agents
Never expose every tool. Expose the right tool.

1. Request context
   user=user_123 tenant=tenant_acme plan=pro roles=analyst permissions=crm:read

2. JSON policy loaded
   policy=examples/policies/tool_policies.json

3. Candidate tools
   search_docs, fetch_customer_record, delete_customer_record

4. Authorized tool surface
   search_docs, fetch_customer_record, not_authorized

5. Denied tool path
   delete_customer_record -> denied -> fallback=not_authorized

6. Framework boundaries
   LangChain-style tools=[...]
   LangGraph-style state.tools=[...]

7. Audit evidence
   authorize allow search_docs
   authorize deny delete_customer_record
   invoke search_docs
```

## Required Grounding

The implementation must use current verified behavior:

- `FilePolicyStore`
- `FileAuditStore`
- `ToolPolicyRouter`
- `RuntimeToolInjector`
- `LangGraphToolRouterMiddleware`
- `fallback_tool`
- existing JSON policy example or a new example policy approved in implementation

## Files You May Read

- `README.md`
- `docs/**`
- `examples/**`
- `src/**`
- `tests/**`
- `feature_list.json`
- `progress/**`
- `specs/008-demo-experience/**`
- `adr/008-demo-experience-strategy.md`

## Files You May Touch After Approval

Potential implementation files:

- `examples/demo_experience/**`
- `examples/basic_agent/**` if the existing demo is intentionally upgraded
- `docs/demo-guide.md`
- `README.md` only if explicitly approved in the implementation gate
- `feature_list.json`
- `progress/008-demo-experience.md`
- `progress/review_008-demo-experience.md`
- `progress/current.md`
- `progress/history.md`

## Files You Must Not Touch Without Explicit Approval

- runtime source code
- packaging/release publishing artifacts
- `.git`
- secrets or credentials
- unrelated repositories

## Risks

- Risk: demo implies production security.
  - Mitigation: use developer-preview language and link to security boundaries.
- Risk: demo becomes too verbose.
  - Mitigation: target under three minutes and keep output sections short.
- Risk: demo requires external services.
  - Mitigation: use local mock tools and local policy/audit files.
- Risk: demo changes runtime behavior.
  - Mitigation: keep changes in examples/docs unless explicitly approved.

## Verification Plan

Spec gate:

```sh
python -m json.tool feature_list.json
```

After implementation approval:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
```

Any new demo command must be run and its output captured.
