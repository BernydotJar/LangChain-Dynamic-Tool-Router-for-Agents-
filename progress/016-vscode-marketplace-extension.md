# 016 VS Code Marketplace Extension Progress

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution Readiness

## State

Status: `in_progress`

## Summary

Feature 016 creates a VS Code extension scaffold for local developer-preview workflows.

The extension now compiles, packages into a VSIX, installs locally through the VS Code CLI, and is visible in the local extension list.

Feature 016 remains `in_progress` because one command behavior still needs manual validation inside VS Code before moving to `review`.

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

Created manual checklist:

```text
docs/vscode-extension-manual-test.md
```

Partial manual validation passed:

```text
- Initialize Policy: PASS
- Validate Policy: PASS
- Preview Authorized Tools: PASS
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

Observed workspace-root behavior:

- `Validate Policy` fails with `ENOENT` when `tool_policies.json` does not exist in the active VS Code workspace root.
- This is expected before `Initialize Policy` runs.
- `Open Audit Viewer` shows a clear not-found message when `runtime_audit_export.json` does not exist in the active VS Code workspace root.
- This is accepted behavior for developer-preview because the command opens the webview and explains the missing audit file clearly.
- Opening the repository root with `code .` and then running `Initialize Policy` creates `tool_policies.json` under the repo workspace.
- After that, `Validate Policy` passes.

Remaining manual validation required:

```text
- Run Demo: pending
```

Feature 016 can move to `review` only after all five manual commands pass.

## Publish Gate

Do not publish publicly until:

- compile passes,
- VSIX package is generated,
- VSIX installs locally,
- all commands are validated in VS Code,
- publisher id is confirmed,
- README rendering is reviewed,
- extension name is confirmed.

## Notes

The assistant has verified local CLI compile, package, install, and installed-extension listing through user-provided handoff evidence.

Command Palette validation is partially complete. Manual validation is still required for:

- Runtime Tool Auth: Run Demo
