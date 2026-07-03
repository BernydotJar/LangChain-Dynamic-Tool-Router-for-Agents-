from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping


Condition = Callable[["ToolRequestContext"], bool]


@dataclass(frozen=True)
class Principal:
    """Actor requesting tool access."""

    user_id: str
    tenant_id: str
    plan: str
    roles: frozenset[str] = field(default_factory=frozenset)
    permissions: frozenset[str] = field(default_factory=frozenset)
    attributes: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "roles", frozenset(self.roles))
        object.__setattr__(self, "permissions", frozenset(self.permissions))


@dataclass(frozen=True)
class ToolRequestContext:
    """Runtime state used to decide which tools an agent may receive."""

    principal: Principal
    request_id: str | None = None
    conversation_id: str | None = None
    state: Mapping[str, Any] = field(default_factory=dict)
    available_mcp_servers: frozenset[str] = field(default_factory=frozenset)

    def __post_init__(self) -> None:
        object.__setattr__(self, "available_mcp_servers", frozenset(self.available_mcp_servers))


@dataclass(frozen=True)
class ToolPolicy:
    """Authorization rules for one tool."""

    allowed_users: frozenset[str] | None = None
    allowed_tenants: frozenset[str] | None = None
    allowed_plans: frozenset[str] | None = None
    required_roles: frozenset[str] = field(default_factory=frozenset)
    required_permissions: frozenset[str] = field(default_factory=frozenset)
    required_mcp_servers: frozenset[str] = field(default_factory=frozenset)
    condition: Condition | None = None
    reason: str = "authorized"

    def __post_init__(self) -> None:
        for name in (
            "allowed_users",
            "allowed_tenants",
            "allowed_plans",
            "required_roles",
            "required_permissions",
            "required_mcp_servers",
        ):
            value = getattr(self, name)
            if value is not None:
                object.__setattr__(self, name, frozenset(value))


@dataclass(frozen=True)
class ToolDecision:
    tool_name: str
    authorized: bool
    reason: str
    fallback_tool_name: str | None = None


@dataclass(frozen=True)
class RouteResult:
    allowed_tool_names: tuple[str, ...]
    denied: tuple[ToolDecision, ...]
    decisions: tuple[ToolDecision, ...]

    def is_allowed(self, tool_name: str) -> bool:
        return tool_name in self.allowed_tool_names
