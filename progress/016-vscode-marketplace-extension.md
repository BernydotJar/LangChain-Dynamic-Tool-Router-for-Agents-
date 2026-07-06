# 016 VS Code Marketplace Extension Progress

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution Readiness

## State

Status: `done`

## Summary

Feature 016 created a VS Code extension scaffold for local developer-preview workflows.

The extension compiles, packages into a VSIX, installs locally through the VS Code CLI, is visible in the local extension list, and passed manual Command Palette validation for the five developer-preview commands.

Feature 016 moved from `review` to `done` after closure approval.

## Created

- `specs/016-vscode-marketplace-extension/requirements.md`
- `specs/016-vscode-marketplace-extension/design.md`
- `specs/016-vscode-marketplace-extension/tasks.md`
- `adr/016-vscode-marketplace-extension.md`
- `vscode-extension/package.json`
- `vscode-extension/package-lock.json`
- `vscode-extension/tsconfig.json`
- `vscode-extension/src/extension.ts`
- `vscode-extension/README.md`
- `vscode-extension/CHANGELOG.md`
- `vscode-extension/LICENSE`
- `vscode-extension/.vscodeignore`
- `docs/vscode-extension-manual-test.md`
- `progress/review_016-vscode-marketplace-extension.md`

## Packaging Adjustments

- Added extension manifest `repository` metadata.
- Added extension-local MIT license for VSIX inclusion.
- Updated `.vscodeignore` so the packaged VSIX includes the expected README, changelog, license, manifest, and compiled output.
- Updated root `.gitignore` to ignore generated extension artifacts:
  - `vscode-extension/node_modules/`
  - `vscode-extension/out/`
  - `vscode-extension/*.vsix`
  - `/tool_policies.json`
  - `/runtime_audit_export.json`
  - `/package-lock.json`

## Extension Commands

- Runtime Tool Auth: Initialize Policy
- Runtime Tool Auth: Validate Policy
- Runtime Tool Auth: Preview Authorized Tools
- Runtime Tool Auth: Run Demo
- Runtime Tool Auth: Open Audit Viewer

## Local Verification

Passed:

```sh
cd vscode-extension
npm install
# added 286 packages; found 0 vulnerabilities
```

```sh
npm run compile
# tsc -p ./ passed
```

```sh
npx @vscode/vsce package
# packaged runtime-tool-authorization-0.0.1.vsix
```

```sh
code --install-extension runtime-tool-authorization-0.0.1.vsix --force
# Extension 'runtime-tool-authorization-0.0.1.vsix' was successfully installed.
```

```sh
code --list-extensions --show-versions | rg 'bernydotjar.runtime-tool-authorization'
# bernydotjar.runtime-tool-authorization@0.0.1
```

Notes:

- `npm install` emitted deprecation warnings for transitive dependencies `whatwg-encoding` and `prebuild-install`.
- `code --install-extension` emitted a Node `url.parse()` deprecation warning from the VS Code CLI path.
- `npx @vscode/vsce package` passed after adding repository metadata and extension-local license.
- The VSIX includes `extension/out/extension.js.map`; this is acceptable for developer-preview local packaging.

## Manual Command Test Gate

Manual validation passed:

```text
- Initialize Policy: PASS
- Validate Policy: PASS
- Preview Authorized Tools: PASS
- Run Demo: PASS
- Open Audit Viewer: PASS
```

Preview output confirmed:

```text
Tool: search_docs
  allowed_plans: free, pro, enterprise
  required_permissions: none

Tool: fetch_customer_record
  allowed_plans: pro, enterprise
  required_permissions: records:read

Tool: delete_customer_record
  allowed_plans: enterprise
  required_permissions: records:delete
```

Run Demo output confirmed:

```text
Injected tools: search_docs, fetch_customer_record, not_authorized
search_docs: [{'title': 'Plan limits', 'snippet': 'Search result for retention policy'}]
LangGraph state tools: search_docs, not_authorized
Audit export: /var/folders/.../tool_policy_router_example/runtime_audit_export.json
```

Observed workspace-root behavior:

- `Validate Policy` fails with `ENOENT` when `tool_policies.json` does not exist in the active VS Code workspace root.
- This is expected before `Initialize Policy` runs.
- `Open Audit Viewer` shows a clear not-found message when `runtime_audit_export.json` does not exist in the active VS Code workspace root.
- This is accepted behavior for developer-preview because the command opens the webview and explains the missing audit file clearly.
- Opening the repository root with `code .` and then running `Initialize Policy` creates `tool_policies.json` under the repo workspace.
- After that, `Validate Policy` passes.

## Closure

Closure approval received:

```text
APPROVAL TO CLOSE
FEATURE: 016-vscode-marketplace-extension
STATE CHANGE: review -> done
```

Feature 016 is closed as `done`.

## Publish Gate

Public Marketplace publish remains separate and has not been run.

Do not publish publicly until:

- publisher id is confirmed,
- extension name availability is confirmed,
- README rendering is reviewed,
- Marketplace auth path is confirmed,
- `vsce publish` is explicitly approved.
