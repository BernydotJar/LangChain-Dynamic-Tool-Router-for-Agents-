# Tasks: 016 VS Code Marketplace Extension

Feature: `016-vscode-marketplace-extension`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution Readiness

## Phase 1: Spec Gate

- [x] Register Feature 016 as `in_progress` after user approval to continue.
- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.
- [ ] Create ADR.
- [ ] Create progress artifact.

## Phase 2: Extension Scaffold

- [ ] Create `vscode-extension/package.json`.
- [ ] Create `vscode-extension/tsconfig.json`.
- [ ] Create `vscode-extension/src/extension.ts`.
- [ ] Create `vscode-extension/README.md`.
- [ ] Create `vscode-extension/CHANGELOG.md`.
- [ ] Create `vscode-extension/.vscodeignore`.

## Phase 3: Commands

- [ ] Add Initialize Policy command.
- [ ] Add Validate Policy command.
- [ ] Add Preview Authorized Tools command.
- [ ] Add Run Demo command.
- [ ] Add Open Audit Viewer command.

## Phase 4: Packaging Readiness

- [ ] Document `npm install`.
- [ ] Document `npm run compile`.
- [ ] Document `npx @vscode/vsce package`.
- [ ] Document local VSIX install command.
- [ ] Do not publish automatically.

## Phase 5: Local Verification Required

To be run by the user locally:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix
```

- [ ] User confirms compile passed.
- [ ] User confirms VSIX package created.
- [ ] User confirms VSIX installed locally.
- [ ] User confirms commands work in VS Code.

## Phase 6: Marketplace Publish Gate

- [ ] Confirm publisher id.
- [ ] Confirm extension name availability.
- [ ] Confirm README renders correctly.
- [ ] Confirm no SVG icon or unsupported README images.
- [ ] Confirm Marketplace auth path.
- [ ] Run `vsce publish` only after local verification.
