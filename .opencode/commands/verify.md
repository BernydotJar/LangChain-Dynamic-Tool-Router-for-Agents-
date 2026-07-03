# verify

MODE:
Use the mode in `feature_list.json`.

FEATURE:
Use the named or active feature.

STATE:
No state changes unless recording verification is explicitly requested.

SOURCE OF TRUTH:
- `feature_list.json`
- `specs/<feature-id>/tasks.md`
- `progress/current.md`

FILES YOU MAY READ:
- `feature_list.json`
- `specs/**`
- `progress/**`
- `src/**`
- `tests/**`
- `examples/**`

FILES YOU MAY TOUCH:
- `progress/current.md` only if recording verification was requested
- `progress/history.md` only if recording verification was requested

FILES YOU MUST NOT TOUCH:
- production source files
- test source files
- dependency manifests
- lockfiles
- environment files

DO:
- Run `PYTHONPATH=src python -m unittest discover -s tests`.
- Run `python examples/basic_agent/run_example.py`.
- Capture command results.

DON'T:
- Fix failures during verification unless explicitly asked.
- Mark features done.

OUTPUT:
- Commands run
- Pass/fail result
- Relevant output summary
- Follow-up required

STOP:
Stop after reporting verification results.
