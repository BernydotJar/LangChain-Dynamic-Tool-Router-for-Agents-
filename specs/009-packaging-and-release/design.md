# Design: 009 Packaging and Release

Feature: `009-packaging-and-release`

Mode: SHIP

Epic: `SHIP-001-developer-preview-release`

## Design Intent

Feature 009 should make the repository installable and release-ready without pretending the project is production stable or already published.

## Packaging Strategy

Use `pyproject.toml` with setuptools because the repository is a lightweight Python package and already supports editable install semantics.

Package metadata should communicate:

- developer-preview maturity,
- Python version support,
- MIT license,
- README as long description,
- no hard LangChain/LangGraph runtime dependency,
- optional integration extras for future work.

## Version Strategy

Use an explicit developer-preview version:

```text
0.1.0.dev0
```

This supports the commercial story without implying production stability.

## Release Documentation

Add:

- `docs/release-checklist.md`
- `docs/v0.1.0-dev-release-notes.md`

The release checklist should distinguish:

- local verification,
- docs review,
- security boundary review,
- optional dependency behavior,
- packaging build verification,
- tag/release decision.

## README Update

Add a compact Packaging & Release section linking to release docs and showing local build commands.

## Verification

The minimum local verification remains:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

If `build` is installed, run:

```sh
python -m build
```

If `build` is not installed, document that build verification is pending.
