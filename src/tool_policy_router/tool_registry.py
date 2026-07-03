from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Protocol


class ToolLike(Protocol):
    name: str


@dataclass
class CallableTool:
    """Minimal LangChain-like tool wrapper for dependency-free routing."""

    name: str
    func: Callable[..., Any]
    description: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def invoke(self, input: Any = None, **kwargs: Any) -> Any:
        if input is None:
            return self.func(**kwargs)
        if kwargs:
            return self.func(input, **kwargs)
        return self.func(input)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.func(*args, **kwargs)


def tool_name(tool: ToolLike | CallableTool) -> str:
    name = getattr(tool, "name", None)
    if not name or not isinstance(name, str):
        raise ValueError("tools must expose a non-empty string 'name' attribute")
    return name


class ToolRegistry:
    """Mutable registry used for runtime tool injection."""

    def __init__(self, tools: Iterable[ToolLike] | None = None) -> None:
        self._tools: dict[str, ToolLike] = {}
        for tool in tools or ():
            self.register(tool)

    def register(self, tool: ToolLike) -> None:
        name = tool_name(tool)
        self._tools[name] = tool

    def unregister(self, name: str) -> None:
        self._tools.pop(name, None)

    def get(self, name: str) -> ToolLike:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise KeyError(f"unknown tool: {name}") from exc

    def list(self) -> tuple[ToolLike, ...]:
        return tuple(self._tools.values())

    def names(self) -> tuple[str, ...]:
        return tuple(self._tools.keys())
