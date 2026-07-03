from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .audit import AuditEvent
from .contracts import ToolPolicy
from .policy import ToolPolicyRouter


_TOP_LEVEL_FIELDS = {"version", "default_allow", "fallback_tool_name", "policies"}
_POLICY_FIELDS = {
    "allowed_users",
    "allowed_tenants",
    "allowed_plans",
    "required_roles",
    "required_permissions",
    "required_mcp_servers",
    "reason",
}
_SET_FIELDS = {
    "allowed_users",
    "allowed_tenants",
    "allowed_plans",
    "required_roles",
    "required_permissions",
    "required_mcp_servers",
}


@dataclass(frozen=True)
class PolicyBundle:
    """Validated router configuration loaded from a policy file."""

    policies: dict[str, ToolPolicy]
    fallback_tool_name: str | None = None
    default_allow: bool = False
    version: int = 1

    def create_router(self, *, audit_log: Any | None = None) -> ToolPolicyRouter:
        return ToolPolicyRouter(
            policies=self.policies,
            fallback_tool_name=self.fallback_tool_name,
            default_allow=self.default_allow,
            audit_log=audit_log,
        )


class FilePolicyStore:
    """Loads dependency-free JSON policy configuration from disk."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    def load(self) -> PolicyBundle:
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid policy JSON: {exc.msg}") from exc

        if not isinstance(raw, dict):
            raise ValueError("policy config must be a JSON object")

        unknown_top_level = set(raw) - _TOP_LEVEL_FIELDS
        if unknown_top_level:
            raise ValueError(f"unknown policy config fields: {', '.join(sorted(unknown_top_level))}")

        version = raw.get("version")
        if version != 1:
            raise ValueError("unsupported policy config version: expected 1")

        default_allow = raw.get("default_allow", False)
        if not isinstance(default_allow, bool):
            raise ValueError("default_allow must be a boolean")

        fallback_tool_name = raw.get("fallback_tool_name")
        if fallback_tool_name is not None and not isinstance(fallback_tool_name, str):
            raise ValueError("fallback_tool_name must be a string or null")

        policies_raw = raw.get("policies")
        if not isinstance(policies_raw, dict):
            raise ValueError("policies must be a JSON object")

        policies: dict[str, ToolPolicy] = {}
        for tool_name, policy_raw in policies_raw.items():
            if not isinstance(tool_name, str) or not tool_name:
                raise ValueError("policy tool names must be non-empty strings")
            policies[tool_name] = self._load_policy(tool_name, policy_raw)

        return PolicyBundle(
            policies=policies,
            fallback_tool_name=fallback_tool_name,
            default_allow=default_allow,
            version=version,
        )

    def create_router(self, *, audit_log: Any | None = None) -> ToolPolicyRouter:
        return self.load().create_router(audit_log=audit_log)

    def _load_policy(self, tool_name: str, raw: Any) -> ToolPolicy:
        if not isinstance(raw, dict):
            raise ValueError(f"policy for {tool_name!r} must be a JSON object")

        unknown_fields = set(raw) - _POLICY_FIELDS
        if unknown_fields:
            raise ValueError(
                f"unknown fields for policy {tool_name!r}: {', '.join(sorted(unknown_fields))}"
            )

        values: dict[str, Any] = {}
        for field_name in _SET_FIELDS:
            if field_name in raw:
                values[field_name] = self._load_string_set(tool_name, field_name, raw[field_name])

        if "reason" in raw:
            reason = raw["reason"]
            if not isinstance(reason, str) or not reason:
                raise ValueError(f"reason for policy {tool_name!r} must be a non-empty string")
            values["reason"] = reason

        return ToolPolicy(**values)

    def _load_string_set(self, tool_name: str, field_name: str, value: Any) -> set[str] | None:
        if value is None and field_name.startswith("allowed_"):
            return None
        if not isinstance(value, list):
            raise ValueError(f"{field_name} for policy {tool_name!r} must be a list of strings")
        if not all(isinstance(item, str) and item for item in value):
            raise ValueError(f"{field_name} for policy {tool_name!r} must contain only non-empty strings")
        return set(value)


class FileAuditStore:
    """JSON Lines audit sink compatible with ToolPolicyRouter."""

    def __init__(self, path: str | Path, *, reset: bool = False) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if reset:
            self.path.write_text("", encoding="utf-8")
        elif not self.path.exists():
            self.path.touch()

    def record(self, event: AuditEvent) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event.to_dict(), sort_keys=True))
            handle.write("\n")

    def events(self) -> tuple[AuditEvent, ...]:
        return tuple(AuditEvent(**event_dict) for event_dict in self.to_dicts())

    def to_dicts(self) -> list[dict[str, Any]]:
        events: list[dict[str, Any]] = []
        for line_number, line in enumerate(self.path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid audit JSON on line {line_number}: {exc.msg}") from exc
            if not isinstance(event, dict):
                raise ValueError(f"invalid audit event on line {line_number}: expected object")
            events.append(event)
        return events

    def export_json(self, path: str | Path | None = None) -> list[dict[str, Any]]:
        events = self.to_dicts()
        if path is not None:
            output_path = Path(path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(events, indent=2, sort_keys=True), encoding="utf-8")
        return events

    def clear(self) -> None:
        self.path.write_text("", encoding="utf-8")
