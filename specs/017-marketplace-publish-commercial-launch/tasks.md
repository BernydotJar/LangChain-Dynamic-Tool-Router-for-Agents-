# Tasks: 017 Marketplace Publish And Commercial Launch

Feature: `017-marketplace-publish-commercial-launch`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

Wave: 3 - Distribution And Commercial Launch

## Phase 1: Spec And Gate

- [x] Register Feature 017 as `in_progress`.
- [x] Create requirements.
- [x] Create design.
- [x] Create tasks.

## Phase 2: Publish Readiness

- [ ] Create Marketplace publish runbook.
- [ ] Document publisher id and extension id confirmation.
- [ ] Document local package command.
- [ ] Document publish command.
- [ ] Document post-publish smoke test.
- [ ] Document unpublish / rollback notes.

## Phase 3: Commercial Access Readiness

- [ ] Create commercial launch runbook.
- [ ] Document founding customer offer.
- [ ] Document manual activation workflow.
- [ ] Document support and renewal notes.
- [ ] Document limitations and non-goals.

## Phase 4: Metadata Review

- [ ] Confirm `vscode-extension/package.json` metadata.
- [ ] Confirm extension README exists.
- [ ] Confirm extension CHANGELOG exists.
- [ ] Confirm extension LICENSE exists.
- [ ] Confirm `.vscodeignore` excludes generated artifacts.

## Phase 5: Publish Gate

- [ ] Require explicit publish approval phrase.
- [ ] Do not run public publish before approval.
- [ ] Do not move to `done` until publish gate state is documented.

## Explicit Publish Approval Phrase

```text
APPROVAL TO PUBLISH
TARGET: VS Code Marketplace
EXTENSION: bernydotjar.runtime-tool-authorization
ACTION: vsce publish
```
