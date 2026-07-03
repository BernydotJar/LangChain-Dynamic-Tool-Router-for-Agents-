import unittest

from tool_policy_router import CallableTool, ToolRegistry


class ToolRegistryTest(unittest.TestCase):
    def test_register_get_unregister(self):
        registry = ToolRegistry()
        tool = CallableTool("hello", lambda name: f"hello {name}")

        registry.register(tool)
        self.assertEqual(registry.names(), ("hello",))
        self.assertEqual(registry.get("hello").invoke("Ada"), "hello Ada")

        registry.unregister("hello")
        self.assertEqual(registry.names(), ())
        with self.assertRaises(KeyError):
            registry.get("hello")

    def test_rejects_tool_without_name(self):
        registry = ToolRegistry()

        with self.assertRaises(ValueError):
            registry.register(object())  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
