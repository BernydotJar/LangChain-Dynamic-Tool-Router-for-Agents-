from __future__ import annotations

from .audit import AuditEvent, InMemoryAuditLog
from .contracts import RouteResult, ToolDecision, ToolPolicy, ToolRequestContext


class ToolPolicyRouter:
    """Evaluates request context against per-tool policies."""

    def __init__(
        self,
        *,
        policies: dict[str, ToolPolicy] | None = None,
        fallback_tool_name: str | None = None,
        audit_log: InMemoryAuditLog | None = None,
        default_allow: bool = False,
    ) -> None:
        self.policies = policies or {}
        self.fallback_tool_name = fallback_tool_name
        self.audit_log = audit_log or InMemoryAuditLog()
        self.default_allow = default_allow

    def authorize_tool(self, tool_name: str, context: ToolRequestContext) -> ToolDecision:
        policy = self.policies.get(tool_name)
        if policy is None:
            if self.default_allow:
                decision = ToolDecision(tool_name, True, "no policy matched; default_allow=true")
            else:
                decision = ToolDecision(
                    tool_name,
                    False,
                    "no policy matched",
                    fallback_tool_name=self.fallback_tool_name,
                )
            self._record_decision(decision, context)
            return decision

        decision = self._evaluate_policy(tool_name, policy, context)
        self._record_decision(decision, context)
        return decision

    def route(self, tool_names: list[str] | tuple[str, ...], context: ToolRequestContext) -> RouteResult:
        decisions = tuple(self.authorize_tool(name, context) for name in tool_names)
        allowed = [decision.tool_name for decision in decisions if decision.authorized]
        denied = tuple(decision for decision in decisions if not decision.authorized)

        if denied and self.fallback_tool_name and self.fallback_tool_name not in allowed:
            fallback_decision = self.authorize_tool(self.fallback_tool_name, context)
            if fallback_decision.authorized:
                allowed.append(self.fallback_tool_name)
                decisions = decisions + (fallback_decision,)

        return RouteResult(tuple(allowed), denied, decisions)

    def record_invocation(
        self,
        tool_name: str,
        context: ToolRequestContext,
        *,
        allowed: bool = True,
        reason: str = "invoked",
    ) -> None:
        self.audit_log.record(
            AuditEvent.create(
                action="invoke",
                tool_name=tool_name,
                allowed=allowed,
                reason=reason,
                context=context,
            )
        )

    def _evaluate_policy(
        self,
        tool_name: str,
        policy: ToolPolicy,
        context: ToolRequestContext,
    ) -> ToolDecision:
        principal = context.principal

        if policy.allowed_users is not None and principal.user_id not in policy.allowed_users:
            return self._deny(tool_name, "user is not allowed")

        if policy.allowed_tenants is not None and principal.tenant_id not in policy.allowed_tenants:
            return self._deny(tool_name, "tenant is not allowed")

        if policy.allowed_plans is not None and principal.plan not in policy.allowed_plans:
            return self._deny(tool_name, "plan is not allowed")

        missing_roles = policy.required_roles - principal.roles
        if missing_roles:
            return self._deny(tool_name, f"missing roles: {', '.join(sorted(missing_roles))}")

        missing_permissions = policy.required_permissions - principal.permissions
        if missing_permissions:
            return self._deny(tool_name, f"missing permissions: {', '.join(sorted(missing_permissions))}")

        missing_servers = policy.required_mcp_servers - context.available_mcp_servers
        if missing_servers:
            return self._deny(tool_name, f"missing MCP servers: {', '.join(sorted(missing_servers))}")

        if policy.condition is not None and not policy.condition(context):
            return self._deny(tool_name, "custom policy condition failed")

        return ToolDecision(tool_name, True, policy.reason)

    def _deny(self, tool_name: str, reason: str) -> ToolDecision:
        return ToolDecision(tool_name, False, reason, fallback_tool_name=self.fallback_tool_name)

    def _record_decision(self, decision: ToolDecision, context: ToolRequestContext) -> None:
        self.audit_log.record(
            AuditEvent.create(
                action="authorize",
                tool_name=decision.tool_name,
                allowed=decision.authorized,
                reason=decision.reason,
                context=context,
                metadata={"fallback_tool_name": decision.fallback_tool_name},
            )
        )
