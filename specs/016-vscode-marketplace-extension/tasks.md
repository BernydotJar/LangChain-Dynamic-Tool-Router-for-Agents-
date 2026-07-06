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
- [x] Create ADR.
- [x] Create progress artifact.

## Phase 2: Extension Scaffold

- [x] Create `vscode-extension/package.json`.
- [x] Create `vscode-extension/tsconfig.json`.
- [x] Create `vscode-extension/src/extension.ts`.
- [x] Create `vscode-extension/README.md`.
- [x] Create `vscode-extension/CHANGELOG.md`.
- [x] Create `vscode-extension/.vscodeignore`.

## Phase 3: Commands

- [x] Add Initialize Policy command.
- [x] Add Validate Policy command.
- [x] Add Preview Authorized Tools command.
- [x] Add Run Demo command.
- [x] Add Open Audit Viewer command.

## Phase 4: Packaging Readiness

- [x] Document `npm install`.
- [x] Document `npm run compile`.
- [x] Document `npx @vscode/vsce package`.
- [x] Document local VSIX install command.
- [x] Do not publish automatically.

## Phase 5: Local Verification

Run locally:

```sh
cd vscode-extension
npm install
npm run compile
npx @vscode/vsce package
code --install-extension runtime-tool-authorization-0.0.1.vsix
```

- [x] `npm install` passed.
- [x] `npm run compile` passed.
- [x] `npx @vscode/vsce package` passed.
- [x] `code --install-extension runtime-tool-authorization-0.0.1.vsix --force` passed.
- [x] `code --list-extensions --show-versions` confirmed `bernydotjar.runtime-tool-authorization@0.0.1`.
- [ ] User confirms commands work in VS Code.

## Phase 6: Marketplace Publish Gate

- [ ] Confirm publisher id.
- [ ] Confirm extension name availability.
- [ ] Confirm README renders correctly.
- [ ] Confirm no SVG icon or unsupported README images.
- [ ] Confirm Marketplace auth path.
- [ ] Run `vsce publish` only after local verification.
