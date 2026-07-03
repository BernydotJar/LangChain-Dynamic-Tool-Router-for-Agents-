"""Run local developer-preview release verification.

This script is intentionally local-only. It does not publish packages,
create tags, or create GitHub releases.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Check:
    name: str
    command: list[str]
    required: bool = True


CHECKS = [
    Check(
        name="feature registry JSON",
        command=[sys.executable, "-m", "json.tool", "feature_list.json"],
    ),
    Check(
        name="unit tests",
        command=[sys.executable, "-m", "unittest", "discover", "-s", "tests"],
    ),
    Check(
        name="basic demo",
        command=[sys.executable, "examples/basic_agent/run_example.py"],
    ),
    Check(
        name="integration tests",
        command=[sys.executable, "-m", "unittest", "discover", "-s", "tests/integration"],
    ),
    Check(
        name="editable install",
        command=[sys.executable, "-m", "pip", "install", "-e", "."],
    ),
    Check(
        name="package build",
        command=[sys.executable, "-m", "build"],
        required=False,
    ),
]


def run_check(check: Check) -> bool:
    print(f"\n==> {check.name}")
    print("$ " + " ".join(check.command))

    result = subprocess.run(check.command, check=False)

    if result.returncode == 0:
        print(f"PASS: {check.name}")
        return True

    if not check.required:
        print(f"SKIP/INFO: {check.name} did not pass. Install dev extras with: python -m pip install -e .[dev]")
        return True

    print(f"FAIL: {check.name}")
    return False


def main() -> int:
    print("Dynamic Tool Router developer-preview verification")
    print("No publish, tag, or release actions will be performed.")

    passed = True
    for check in CHECKS:
        passed = run_check(check) and passed

    if passed:
        print("\nRelease candidate verification completed.")
        return 0

    print("\nRelease candidate verification failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
