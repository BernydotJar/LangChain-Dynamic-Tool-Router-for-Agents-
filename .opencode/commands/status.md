# status

MODE:
Read-only.

FEATURE:
All features, with emphasis on the active feature if one exists.

STATE:
No state changes.

SOURCE OF TRUTH:
- `feature_list.json`
- `progress/**`
- `specs/**`

FILES YOU MAY READ:
- `feature_list.json`
- `progress/**`
- `specs/**`
- `docs/**`

FILES YOU MAY TOUCH:
- none

FILES YOU MUST NOT TOUCH:
- all files

DO:
- Summarize feature states.
- Identify the next valid command.
- Report blockers.

DON'T:
- Edit files.
- Change status.

OUTPUT:
- Current feature table
- Active feature
- Next recommended command
- Blockers

STOP:
Stop after reporting status.
