from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .contracts import ToolRequestContext


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    timestamp: str
    action: str
    tool_name: str
    allowed: bool
    reason: str
    user_id: str
    tenant_id: str
    request_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        action: str,
        tool_name: str,
        allowed: bool,
        reason: str,
        context: ToolRequestContext,
        metadata: dict[str, Any] | None = None,
    ) -> "AuditEvent":
        return cls(
            event_id=str(uuid4()),
            timestamp=datetime.now(timezone.utc).isoformat(),
            action=action,
            tool_name=tool_name,
            allowed=allowed,
            reason=reason,
            user_id=context.principal.user_id,
            tenant_id=context.principal.tenant_id,
            request_id=context.request_id,
            metadata=metadata or {},
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class InMemoryAuditLog:
    """Small audit sink suitable for MVP tests, demos, and embedding."""

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def record(self, event: AuditEvent) -> None:
        self._events.append(event)

    def events(self) -> tuple[AuditEvent, ...]:
        return tuple(self._events)

    def to_dicts(self) -> list[dict[str, Any]]:
        return [event.to_dict() for event in self._events]

    def clear(self) -> None:
        self._events.clear()
