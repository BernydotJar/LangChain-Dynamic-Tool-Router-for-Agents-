import json
import tempfile
import unittest
from pathlib import Path

from tool_policy_router import (
    AuditEvent,
    FileAuditStore,
    FilePolicyStore,
    Principal,
    ToolRequestContext,
)


class FilePolicyStoreTest(unittest.TestCase):
    def write_policy(self, payload):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "tool_policies.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def context(self, **overrides):
        principal = Principal(
            user_id=overrides.pop("user_id", "user_1"),
            tenant_id=overrides.pop("tenant_id", "tenant_1"),
            plan=overrides.pop("plan", "pro"),
            roles=overrides.pop("roles", {"member"}),
            permissions=overrides.pop("permissions", {"docs:search"}),
        )
        return ToolRequestContext(principal=principal, request_id="req_1")

    def valid_policy_payload(self):
        return {
            "version": 1,
            "default_allow": False,
            "fallback_tool_name": "not_authorized",
            "policies": {
                "search_docs": {
                    "allowed_plans": ["pro", "enterprise"],
                    "required_permissions": ["docs:search"],
                    "reason": "authorized",
                },
                "admin_delete": {
                    "allowed_plans": ["enterprise"],
                    "required_roles": ["admin"],
                },
                "not_authorized": {
                    "allowed_plans": ["free", "pro", "enterprise"],
                },
            },
        }

    def test_policy_json_loads_into_router_compatible_bundle(self):
        bundle = FilePolicyStore(self.write_policy(self.valid_policy_payload())).load()

        self.assertEqual(bundle.fallback_tool_name, "not_authorized")
        self.assertFalse(bundle.default_allow)
        self.assertIn("search_docs", bundle.policies)
        self.assertEqual(bundle.policies["search_docs"].allowed_plans, frozenset({"pro", "enterprise"}))
        self.assertEqual(bundle.policies["search_docs"].required_permissions, frozenset({"docs:search"}))

    def test_invalid_policy_json_is_rejected_clearly(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "broken.json"
        path.write_text("{not-json", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "invalid policy JSON"):
            FilePolicyStore(path).load()

    def test_unsupported_version_is_rejected(self):
        path = self.write_policy({"version": 2, "policies": {}})

        with self.assertRaisesRegex(ValueError, "unsupported policy config version"):
            FilePolicyStore(path).load()

    def test_unknown_policy_field_is_rejected(self):
        payload = self.valid_policy_payload()
        payload["policies"]["search_docs"]["condition"] = "unsafe"

        with self.assertRaisesRegex(ValueError, "unknown fields"):
            FilePolicyStore(self.write_policy(payload)).load()

    def test_invalid_set_field_is_rejected(self):
        payload = self.valid_policy_payload()
        payload["policies"]["search_docs"]["allowed_plans"] = "pro"

        with self.assertRaisesRegex(ValueError, "allowed_plans"):
            FilePolicyStore(self.write_policy(payload)).load()

    def test_fallback_behavior_works_with_loaded_policy(self):
        router = FilePolicyStore(self.write_policy(self.valid_policy_payload())).create_router()

        result = router.route(["search_docs", "admin_delete"], self.context())

        self.assertEqual(result.allowed_tool_names, ("search_docs", "not_authorized"))
        self.assertEqual(result.denied[0].tool_name, "admin_delete")
        self.assertEqual(result.denied[0].fallback_tool_name, "not_authorized")


class FileAuditStoreTest(unittest.TestCase):
    def make_store(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        return FileAuditStore(Path(directory.name) / "audit.jsonl")

    def context(self):
        return ToolRequestContext(
            principal=Principal(
                user_id="user_1",
                tenant_id="tenant_1",
                plan="pro",
            ),
            request_id="req_1",
        )

    def test_audit_events_persist_to_local_file(self):
        store = self.make_store()
        event = AuditEvent.create(
            action="authorize",
            tool_name="search_docs",
            allowed=True,
            reason="authorized",
            context=self.context(),
        )

        store.record(event)

        persisted = store.to_dicts()
        self.assertEqual(len(persisted), 1)
        self.assertEqual(persisted[0]["event_id"], event.event_id)
        self.assertEqual(persisted[0]["action"], "authorize")
        self.assertTrue(persisted[0]["allowed"])

    def test_audit_export_returns_and_writes_persisted_events(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        audit_path = Path(directory.name) / "audit.jsonl"
        export_path = Path(directory.name) / "audit_export.json"
        store = FileAuditStore(audit_path)
        event = AuditEvent.create(
            action="invoke",
            tool_name="search_docs",
            allowed=True,
            reason="invoked",
            context=self.context(),
        )
        store.record(event)

        exported = store.export_json(export_path)

        self.assertEqual(exported[0]["action"], "invoke")
        exported_file = json.loads(export_path.read_text(encoding="utf-8"))
        self.assertEqual(exported_file[0]["tool_name"], "search_docs")


if __name__ == "__main__":
    unittest.main()
