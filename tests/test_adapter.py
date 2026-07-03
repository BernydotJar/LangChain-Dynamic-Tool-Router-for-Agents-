import unittest

from tool_policy_router import (
    CallableTool,
    InMemoryAuditLog,
    LangGraphToolRouterMiddleware,
    Principal,
    RuntimeToolInjector,
    ToolPolicy,
    ToolPolicyRouter,
    ToolRegistry,
    ToolRequestContext,
)


class RuntimeToolInjectorTest(unittest.TestCase):
    def make_system(self):
        registry = ToolRegistry(
            [
                CallableTool("search_docs", lambda query: f"found {query}"),
                CallableTool("admin_delete", lambda record_id: f"deleted {record_id}"),
                CallableTool("not_authorized", lambda **_: "not authorized"),
            ]
        )
        audit_log = InMemoryAuditLog()
        router = ToolPolicyRouter(
            policies={
                "search_docs": ToolPolicy(allowed_plans={"free", "pro", "enterprise"}),
                "admin_delete": ToolPolicy(
                    allowed_plans={"enterprise"},
                    required_roles={"admin"},
                    required_permissions={"records:delete"},
                ),
                "not_authorized": ToolPolicy(allowed_plans={"free", "pro", "enterprise"}),
            },
            fallback_tool_name="not_authorized",
            audit_log=audit_log,
        )
        context = ToolRequestContext(
            principal=Principal(
                user_id="user_1",
                tenant_id="tenant_1",
                plan="pro",
                roles={"member"},
                permissions={"records:read"},
            )
        )
        return registry, router, audit_log, context

    def test_injects_allowed_tools_and_fallback(self):
        registry, router, _, context = self.make_system()
        injector = RuntimeToolInjector(registry, router)

        tools = injector.tools_for_context(
            context,
            candidate_tool_names=["search_docs", "admin_delete"],
        )

        self.assertEqual([tool.name for tool in tools], ["search_docs", "not_authorized"])

    def test_wrapped_tool_records_invocation(self):
        registry, router, audit_log, context = self.make_system()
        injector = RuntimeToolInjector(registry, router)

        tools = injector.tools_for_context(context, candidate_tool_names=["search_docs"])
        self.assertEqual(tools[0].invoke("policy"), "found policy")

        events = audit_log.events()
        self.assertEqual(events[-1].action, "invoke")
        self.assertEqual(events[-1].tool_name, "search_docs")

    def test_injects_into_agent_kwargs(self):
        registry, router, _, context = self.make_system()
        injector = RuntimeToolInjector(registry, router)

        agent_kwargs = injector.inject_into_agent_kwargs({"model": "demo"}, context, ["search_docs"])

        self.assertEqual(agent_kwargs["model"], "demo")
        self.assertEqual([tool.name for tool in agent_kwargs["tools"]], ["search_docs"])

    def test_langgraph_middleware_injects_tools_into_state(self):
        registry, router, _, context = self.make_system()
        middleware = LangGraphToolRouterMiddleware(RuntimeToolInjector(registry, router))

        state = middleware.before_model(
            {
                "tool_context": context,
                "candidate_tool_names": ["search_docs", "admin_delete"],
            }
        )

        self.assertEqual([tool.name for tool in state["tools"]], ["search_docs", "not_authorized"])

    def test_registry_changes_affect_next_request(self):
        registry, router, _, context = self.make_system()
        injector = RuntimeToolInjector(registry, router)

        registry.register(CallableTool("tenant_report", lambda: "report"))
        router.policies["tenant_report"] = ToolPolicy(allowed_tenants={"tenant_1"})

        tools = injector.tools_for_context(context, candidate_tool_names=["tenant_report"])

        self.assertEqual([tool.name for tool in tools], ["tenant_report"])


if __name__ == "__main__":
    unittest.main()
