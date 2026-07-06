# VS Code Extension Manual Test Checklist

Feature: `016-vscode-marketplace-extension`

Use this checklist after local VSIX install and before moving Feature 016 from `in_progress` to `review`.

## Preconditions

Run from the repository root:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix --force
code --list-extensions --show-versions | rg 'bernydotjar.runtime-tool-authorization'
```

Expected installed extension:

```text
bernydotjar.runtime-tool-authorization@0.0.1
```

## Test Workspace

Open the repository root in VS Code.

```sh
code .
```

Open Command Palette:

```text
Cmd+Shift+P
```

## Manual Tests

### 1. Initialize Policy

Command:

```text
Runtime Tool Auth: Initialize Policy
```

Expected result:

- If `tool_policies.json` does not exist, the extension creates it in the workspace root.
- VS Code shows an information message that the starter policy was created.
- The file contains `version`, `fallback_tool_name`, and `policies`.

Pass criteria:

```text
PASS: starter policy created or existing policy detected without error.
```

### 2. Validate Policy

Command:

```text
Runtime Tool Auth: Validate Policy
```

Expected result:

- Output channel `Runtime Tool Authorization` opens.
- Output shows policy validation.
- VS Code shows an information message that validation passed.

Pass criteria:

```text
PASS: policy validation passed.
```

### 3. Preview Authorized Tools

Command:

```text
Runtime Tool Auth: Preview Authorized Tools
```

Expected result:

- Output channel lists configured tools.
- Default starter policy should show:
  - `search_docs`
  - `fetch_customer_record`
  - `delete_customer_record`
- Output includes allowed plans and required permissions when present.

Pass criteria:

```text
PASS: policy tools and gates are visible in the output channel.
```

### 4. Run Demo

Command:

```text
Runtime Tool Auth: Run Demo
```

Expected result:

- VS Code opens terminal `Runtime Tool Auth Demo`.
- Terminal runs:

```sh
python examples/basic_agent/run_example.py
```

- Demo output shows injected tools and audit export path.

Pass criteria:

```text
PASS: demo terminal opens and basic agent demo completes.
```

### 5. Open Audit Viewer

Command:

```text
Runtime Tool Auth: Open Audit Viewer
```

Expected result:

- VS Code opens webview `Runtime Tool Auth Audit Viewer`.
- If `runtime_audit_export.json` exists, it renders formatted JSON.
- If the file does not exist, the webview shows a clear not-found message.

Pass criteria:

```text
PASS: audit viewer opens and renders JSON or a clear not-found message.
```

## Failure Handling

If any command fails:

1. Copy the VS Code notification text.
2. Copy the `Runtime Tool Authorization` output channel content.
3. Copy terminal output if the failure happened during `Run Demo`.
4. Do not move Feature 016 to `review`.

## Review Gate

Move Feature 016 to `review` only after all five manual command tests pass.

Required evidence:

```text
Manual command validation passed:
- Initialize Policy: PASS
- Validate Policy: PASS
- Preview Authorized Tools: PASS
- Run Demo: PASS
- Open Audit Viewer: PASS
```
