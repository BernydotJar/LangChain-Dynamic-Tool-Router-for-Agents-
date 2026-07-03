import unittest

from tool_policy_router import InMemoryAuditLog, Principal, ToolPolicy, ToolPolicyRouter, ToolRequestContext


class ToolPolicyRouterTest(unittest.TestCase):
    def context(self, **overrides):
        principal = Principal(
            user_id=overrides.pop("user_id", "user_1"),
            tenant_id=overrides.pop("tenant_id", "tenant_1"),
            plan=overrides.pop("plan", "pro"),
            roles=overrides.pop("roles", {"analyst"}),
            permissions=overrides.pop("permissions", {"crm:read"}),
        )
        return ToolRequestContext(
            principal=principal,
            request_id="req_1",
            available_mcp_servers=overrides.pop("available_mcp_servers", {"crm-mcp"}),
            state=overrides.pop("state", {}),
        )

    def test_allows_matching_policy(self):
        router = ToolPolicyRouter(
            policies={
                "crm_lookup": ToolPolicy(
                    allowed_tenants={"tenant_1"},
                    allowed_plans={"pro"},
                    required_permissions={"crm:read"},
                    required_mcp_servers={"crm-mcp"},
                )
            }
        )

        decision = router.authorize_tool("crm_lookup", self.context())

        self.assertTrue(decision.authorized)
        self.assertEqual(decision.reason, "authorized")

    def test_denies_missing_permission(self):
        router = ToolPolicyRouter(
            policies={"crm_delete": ToolPolicy(required_permissions={"crm:delete"})},
            fallback_tool_name="not_authorized",
        )

        decision = router.authorize_tool("crm_delete", self.context())

        self.assertFalse(decision.authorized)
        self.assertEqual(decision.reason, "missing permissions: crm:delete")
        self.assertEqual(decision.fallback_tool_name, "not_authorized")

    def test_denies_missing_mcp_server(self):
        router = ToolPolicyRouter(
            policies={"github_search": ToolPolicy(required_mcp_servers={"github-mcp"})}
        )

        decision = router.authorize_tool(
            "github_search",
            self.context(available_mcp_servers={"crm-mcp"}),
        )

        self.assertFalse(decision.authorized)
        self.assertEqual(decision.reason, "missing MCP servers: github-mcp")

    def test_unknown_tool_denied_by_default(self):
        router = ToolPolicyRouter()

        decision = router.authorize_tool("unknown", self.context())

        self.assertFalse(decision.authorized)
        self.assertEqual(decision.reason, "no policy matched")

    def test_custom_condition_can_use_context_state(self):
        router = ToolPolicyRouter(
            policies={
                "billing_tool": ToolPolicy(
                    condition=lambda context: context.state.get("billing_enabled") is True
                )
            }
        )

        self.assertFalse(router.authorize_tool("billing_tool", self.context()).authorized)
        self.assertTrue(
            router.authorize_tool("billing_tool", self.context(state={"billing_enabled": True})).authorized
        )

    def test_records_audit_event_for_decisions(self):
        audit_log = InMemoryAuditLog()
        router = ToolPolicyRouter(
            policies={"search_docs": ToolPolicy(allowed_plans={"enterprise"})},
            audit_log=audit_log,
        )

        router.authorize_tool("search_docs", self.context(plan="free"))

        events = audit_log.events()
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].action, "authorize")
        self.assertFalse(events[0].allowed)
        self.assertEqual(events[0].tenant_id, "tenant_1")


if __name__ == "__main__":
    unittest.main()
