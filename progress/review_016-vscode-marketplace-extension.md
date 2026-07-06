# Review: 016 VS Code Marketplace Extension

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Status: `review`

## Summary

Feature 016 added a VS Code extension scaffold for Runtime Tool Authorization developer-preview workflows.

The extension provides local Command Palette commands for policy initialization, policy validation, authorized-tool preview, demo execution, and audit viewing.

## Review Scope

Included:

- VS Code extension manifest.
- TypeScript extension entrypoint.
- Local command workflow.
- VSIX packaging path.
- Extension-local README and changelog.
- Extension-local MIT license.
- Manual test checklist.
- Root `.gitignore` updates for generated local artifacts.

Excluded:

- Public Marketplace publish.
- Marketplace paid install gating.
- Hosted service integration.
- Telemetry.
- Remote policy management.
- Production authorization claims.

## Files Added Or Updated

- `vscode-extension/package.json`
- `vscode-extension/package-lock.json`
- `vscode-extension/tsconfig.json`
- `vscode-extension/src/extension.ts`
- `vscode-extension/README.md`
- `vscode-extension/CHANGELOG.md`
- `vscode-extension/LICENSE`
- `vscode-extension/.vscodeignore`
- `docs/vscode-extension-manual-test.md`
- `.gitignore`
- `feature_list.json`
- `progress/016-vscode-marketplace-extension.md`
- `specs/016-vscode-marketplace-extension/tasks.md`

## Verification Evidence

Local packaging verification passed:

```sh
cd vscode-extension
npm install
# added 286 packages; found 0 vulnerabilities

npm run compile
# tsc -p ./ passed

npx @vscode/vsce package
# packaged runtime-tool-authorization-0.0.1.vsix

code --install-extension runtime-tool-authorization-0.0.1.vsix --force
# installed successfully

code --list-extensions --show-versions | rg 'bernydotjar.runtime-tool-authorization'
# bernydotjar.runtime-tool-authorization@0.0.1
```

Manual command validation passed:

```text
- Initialize Policy: PASS
- Validate Policy: PASS
- Preview Authorized Tools: PASS
- Run Demo: PASS
- Open Audit Viewer: PASS
```

Run demo evidence included:

```text
Injected tools: search_docs, fetch_customer_record, not_authorized
search_docs: [{'title': 'Plan limits', 'snippet': 'Search result for retention policy'}]
LangGraph state tools: search_docs, not_authorized
Audit export: /var/folders/.../tool_policy_router_example/runtime_audit_export.json
```

## Observations

- `Validate Policy` fails with `ENOENT` if `tool_policies.json` does not exist in the active workspace root. This is expected before running `Initialize Policy`.
- `Open Audit Viewer` shows a clear not-found message if `runtime_audit_export.json` does not exist in the active workspace root. This is acceptable developer-preview behavior.
- The repository root should be opened directly with `code .` from `LangChain-Dynamic-Tool-Router-for-Agents-` for the cleanest test path.

## Review Checklist

- [x] Extension scaffold exists.
- [x] Manifest has command contributions.
- [x] TypeScript entrypoint registers commands.
- [x] Policy initialization works.
- [x] Policy validation works.
- [x] Tool preview works.
- [x] Demo execution works.
- [x] Audit viewer opens and handles missing audit file clearly.
- [x] VSIX packaging works locally.
- [x] VSIX installs locally.
- [x] Extension appears in installed-extension list.
- [x] Generated local artifacts are ignored.
- [x] Public publish has not been run.

## Remaining Publish Gate

Before public publish:

- Confirm Marketplace publisher id.
- Confirm extension name availability.
- Review Marketplace README rendering.
- Confirm Marketplace auth path.
- Explicitly approve `vsce publish`.

## Recommendation

Approve Feature 016 for closure after human review of this artifact.

Do not publish until explicit publish approval is given.
