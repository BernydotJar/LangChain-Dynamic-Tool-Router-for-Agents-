# Claude Operating Guide

Read `AGENTS.md`, then `RTK.md`, before taking action.

## Default Behavior

- Work from `feature_list.json`.
- Select only one feature at a time.
- Keep feature work bounded to the approved spec.
- Record verification evidence before review.
- Do not mark a feature `done` without review evidence and human closure approval.

## Current Product

This repository contains a Python MVP for dynamic tool routing in LangChain/LangGraph-style agents.

The current implemented feature is:

- `001-dynamic-tool-router`

## Stop Conditions

Stop and ask for human input when:

- requested behavior exceeds the active feature scope,
- a new dependency is required,
- a schema, secret, deployment, or destructive operation is required,
- verification cannot run.
