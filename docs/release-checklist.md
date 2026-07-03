# Release Checklist

This checklist is for developer-preview releases of Dynamic Tool Router.

## Release Candidate

Current target:

```text
v0.1.0-dev
```

Package version:

```text
0.1.0.dev0
```

## Preconditions

- Feature registry is valid JSON.
- README reflects current behavior.
- Security boundary is accurate.
- Changelog is updated.
- Release notes are updated.
- License is present.
- Contributing and security policy files are present.

## Required Verification

Run:

```sh
python -m json.tool feature_list.json
PYTHONPATH=src python -m unittest discover -s tests
python examples/basic_agent/run_example.py
PYTHONPATH=src python -m unittest discover -s tests/integration
```

## Packaging Verification

Install/editable check:

```sh
python -m pip install -e .
```

Build check, if the `build` module is available:

```sh
python -m build
```

If `build` is not available, install the dev extra or build package:

```sh
python -m pip install -e .[dev]
python -m build
```

## Manual Review

- README first screen communicates the product category.
- Quickstart still matches actual demo output.
- Security docs do not overclaim production readiness.
- Changelog accurately reflects shipped work.
- `pyproject.toml` package metadata is accurate.
- Optional LangChain/LangGraph tests skip explicitly if dependencies are absent.

## Tagging Decision

Do not tag until the maintainer approves:

```text
git tag v0.1.0-dev
git push origin v0.1.0-dev
```

## GitHub Release Draft

Title:

```text
v0.1.0-dev — Runtime Tool Authorization for AI Agents
```

Description should include:

- developer-preview status,
- what works locally,
- security boundaries,
- installation steps,
- verification commands,
- known limitations,
- next roadmap item.
