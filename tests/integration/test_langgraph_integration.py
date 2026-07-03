from __future__ import annotations

import importlib.util
import unittest
from typing import Any, TypedDict

from tool_policy_router import CallableTool, LangGraphToolRouterMiddleware
from tests.integration.helpers import build_integration_system


LANGGRAPH_AVAILABLE = importlib.util.find_spec("langgraph") is not None


@unittest.skipUnless(
    LANGGRAPH_AVAILABLE,
    "optional dependency langgraph is not installed; install LangGraph integration dependencies to run",
)
class LangGraphIntegrationTest(unittest.TestCase):
    def test_langgraph_state_graph_uses_router_middleware_with_persistent_audit(self):
        from langgraph.graph import END, START, StateGraph

        search_tool = CallableTool("search_docs", lambda query: f"found {query}")
        workspace, audit_store, injector, context = build_integration_system(search_tool)
        self.addCleanup(workspace.cleanup)
        middleware = LangGraphToolRouterMiddleware(injector)

        class RouterState(TypedDict, total=False):
            tool_context: Any
            candidate_tool_names: list[str]
            tools: list[Any]
            tool_names: list[str]

        def route_tools(state: RouterState) -> RouterState:
            next_state = middleware.before_model(dict(state))
            next_state["tool_names"] = [tool.name for tool in next_state["tools"]]
            return next_state

        graph = StateGraph(RouterState)
        graph.add_node("route_tools", route_tools)
        graph.add_edge(START, "route_tools")
        graph.add_edge("route_tools", END)
        app = graph.compile()

        result = app.invoke(
            {
                "tool_context": context,
                "candidate_tool_names": ["search_docs", "admin_delete"],
            }
        )

        self.assertEqual(result["tool_names"], ["search_docs", "not_authorized"])
        events = audit_store.to_dicts()
        self.assertTrue(any(event["allowed"] is False and event["tool_name"] == "admin_delete" for event in events))
        self.assertTrue(any(event["tool_name"] == "not_authorized" for event in events))


if __name__ == "__main__":
    unittest.main()
