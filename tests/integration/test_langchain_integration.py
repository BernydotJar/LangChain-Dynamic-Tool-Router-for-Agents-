from __future__ import annotations

import importlib.util
import unittest

from tests.integration.helpers import build_integration_system


LANGCHAIN_CORE_AVAILABLE = importlib.util.find_spec("langchain_core") is not None


@unittest.skipUnless(
    LANGCHAIN_CORE_AVAILABLE,
    "optional dependency langchain_core is not installed; install LangChain integration dependencies to run",
)
class LangChainIntegrationTest(unittest.TestCase):
    def test_langchain_tool_receives_runtime_injection_and_audit_persistence(self):
        from langchain_core.tools import tool

        @tool
        def search_docs(query: str) -> str:
            """Search tenant documentation."""
            return f"found {query}"

        workspace, audit_store, injector, context = build_integration_system(search_docs)
        self.addCleanup(workspace.cleanup)

        injected = injector.tools_for_context(
            context,
            candidate_tool_names=["search_docs", "admin_delete"],
        )

        self.assertEqual([tool.name for tool in injected], ["search_docs", "not_authorized"])
        self.assertEqual(injected[0].invoke("retention"), "found retention")

        events = audit_store.to_dicts()
        self.assertTrue(any(event["action"] == "invoke" and event["tool_name"] == "search_docs" for event in events))
        self.assertTrue(any(event["allowed"] is False and event["tool_name"] == "admin_delete" for event in events))
        self.assertTrue(any(event["tool_name"] == "not_authorized" for event in events))


if __name__ == "__main__":
    unittest.main()
