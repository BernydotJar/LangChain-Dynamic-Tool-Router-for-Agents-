from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from .contracts import ToolRequestContext
from .policy import ToolPolicyRouter
from .tool_registry import CallableTool, ToolLike, ToolRegistry, tool_name


class AuditedTool:
    """Proxy that records invocations without requiring LangChain as a dependency."""

    def __init__(self, wrapped: ToolLike, router: ToolPolicyRouter, context: ToolRequestContext) -> None:
        self._wrapped = wrapped
        self._router = router
        self._context = context
        self.name = tool_name(wrapped)
        self.description = getattr(wrapped, "description", "")
        self.metadata = getattr(wrapped, "metadata", {})

    def invoke(self, input: Any = None, **kwargs: Any) -> Any:
        self._router.record_invocation(self.name, self._context)
        if hasattr(self._wrapped, "invoke"):
            return self._wrapped.invoke(input, **kwargs)
        if input is None:
            return self._wrapped(**kwargs)  # type: ignore[misc]
        return self._wrapped(input, **kwargs)  # type: ignore[misc]

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self._router.record_invocation(self.name, self._context)
        if callable(self._wrapped):
            return self._wrapped(*args, **kwargs)
        if hasattr(self._wrapped, "invoke"):
            if args:
                return self._wrapped.invoke(args[0], **kwargs)
            return self._wrapped.invoke(**kwargs)
        raise TypeError(f"tool {self.name!r} is not callable")


class RuntimeToolInjector:
    """Builds the request-time tool list an agent should receive."""

    def __init__(self, registry: ToolRegistry, router: ToolPolicyRouter) -> None:
        self.registry = registry
        self.router = router

    def tools_for_context(
        self,
        context: ToolRequestContext,
        candidate_tool_names: Iterable[str] | None = None,
        *,
        audited: bool = True,
    ) -> list[ToolLike]:
        names = tuple(candidate_tool_names or self.registry.names())
        route_result = self.router.route(names, context)
        tools: list[ToolLike] = []
        for name in route_result.allowed_tool_names:
            tool = self.registry.get(name)
            tools.append(AuditedTool(tool, self.router, context) if audited else tool)
        return tools

    def inject_into_agent_kwargs(
        self,
        agent_kwargs: dict[str, Any],
        context: ToolRequestContext,
        candidate_tool_names: Iterable[str] | None = None,
    ) -> dict[str, Any]:
        updated = dict(agent_kwargs)
        updated["tools"] = self.tools_for_context(context, candidate_tool_names)
        return updated


class LangGraphToolRouterMiddleware:
    """Tiny adapter for LangGraph-style state dictionaries."""

    def __init__(
        self,
        injector: RuntimeToolInjector,
        *,
        context_key: str = "tool_context",
        tools_key: str = "tools",
        candidate_tools_key: str = "candidate_tool_names",
    ) -> None:
        self.injector = injector
        self.context_key = context_key
        self.tools_key = tools_key
        self.candidate_tools_key = candidate_tools_key

    def before_model(self, state: dict[str, Any]) -> dict[str, Any]:
        if self.context_key not in state:
            raise KeyError(f"state is missing {self.context_key!r}")
        context = state[self.context_key]
        if not isinstance(context, ToolRequestContext):
            raise TypeError(f"state[{self.context_key!r}] must be ToolRequestContext")

        candidate_names = state.get(self.candidate_tools_key)
        next_state = dict(state)
        next_state[self.tools_key] = self.injector.tools_for_context(context, candidate_names)
        return next_state


def fallback_tool(message: str = "Tool is not authorized for this request.") -> CallableTool:
    return CallableTool("not_authorized", lambda *_, **__: {"error": message}, description=message)
