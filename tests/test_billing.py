from datetime import datetime, timedelta, timezone
import unittest

from tool_policy_router.billing import (
    BillingConfig,
    CheckoutRequest,
    InMemoryLicenseActivationStore,
    InMemoryWebhookEventStore,
    MockStripeGateway,
    SubscriptionRecord,
    build_webhook_event_record,
    create_checkout_session,
    create_portal_session,
    entitlement_from_subscription,
    hash_license_key,
    hash_machine_fingerprint,
)


class BillingCheckoutTest(unittest.TestCase):
    def config(self):
        return BillingConfig(
            price_ids_by_plan={
                "solo": "price_solo_test",
                "team": "price_team_test",
                "design_partner": "price_design_partner_test",
            },
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )

    def test_checkout_session_uses_configured_price_and_trial(self):
        gateway = MockStripeGateway()

        result = create_checkout_session(
            gateway=gateway,
            config=self.config(),
            request=CheckoutRequest(plan="solo", email="buyer@example.com"),
        )

        self.assertEqual(result.provider_session_id, "cs_test_1")
        self.assertEqual(gateway.checkout_requests[0].price_id, "price_solo_test")
        self.assertEqual(gateway.checkout_requests[0].mode, "subscription")
        self.assertEqual(gateway.checkout_requests[0].trial_period_days, 30)
        self.assertEqual(gateway.checkout_requests[0].success_url, "https://example.com/success")

    def test_unsupported_plan_is_rejected(self):
        gateway = MockStripeGateway()

        with self.assertRaisesRegex(ValueError, "unsupported billing plan"):
            create_checkout_session(
                gateway=gateway,
                config=self.config(),
                request=CheckoutRequest(plan="unknown", email="buyer@example.com"),
            )

    def test_portal_session_is_created_through_gateway_boundary(self):
        gateway = MockStripeGateway()

        result = create_portal_session(
            gateway=gateway,
            stripe_customer_id="customer_123",
            return_url="https://example.com/billing",
        )

        self.assertEqual(result.provider_session_id, "bps_test_1")
        self.assertEqual(gateway.portal_requests[0].stripe_customer_id, "customer_123")


class EntitlementMappingTest(unittest.TestCase):
    def now(self):
        return datetime(2026, 7, 5, tzinfo=timezone.utc)

    def subscription(self, status="active", plan="team", grace_until=None):
        return SubscriptionRecord(
            customer_id="customer_123",
            stripe_subscription_id="sub_123",
            plan=plan,
            status=status,
            seat_limit=5,
            current_period_ends_at=self.now() + timedelta(days=30),
            grace_until=grace_until,
        )

    def test_trialing_subscription_enables_premium_features(self):
        entitlement = entitlement_from_subscription(self.subscription(status="trialing"), now=self.now())

        self.assertTrue(entitlement.premium_enabled)
        self.assertEqual(entitlement.plan, "team")
        self.assertIn("team_config", entitlement.features)
        self.assertEqual(entitlement.seat_limit, 5)

    def test_active_design_partner_includes_support_feature(self):
        entitlement = entitlement_from_subscription(
            self.subscription(status="active", plan="design_partner"), now=self.now()
        )

        self.assertTrue(entitlement.premium_enabled)
        self.assertIn("design_partner_support", entitlement.features)

    def test_canceled_subscription_disables_premium(self):
        entitlement = entitlement_from_subscription(self.subscription(status="canceled"), now=self.now())

        self.assertFalse(entitlement.premium_enabled)
        self.assertEqual(entitlement.features, frozenset())

    def test_missing_subscription_disables_premium(self):
        entitlement = entitlement_from_subscription(None, now=self.now())

        self.assertFalse(entitlement.premium_enabled)
        self.assertEqual(entitlement.status, "missing")

    def test_past_due_subscription_allows_grace_period(self):
        entitlement = entitlement_from_subscription(
            self.subscription(status="past_due", grace_until=self.now() + timedelta(hours=1)),
            now=self.now(),
        )

        self.assertTrue(entitlement.premium_enabled)
        self.assertEqual(entitlement.reason, "within grace period")

    def test_past_due_subscription_disables_after_grace_period(self):
        entitlement = entitlement_from_subscription(
            self.subscription(status="past_due", grace_until=self.now() - timedelta(minutes=1)),
            now=self.now(),
        )

        self.assertFalse(entitlement.premium_enabled)
        self.assertEqual(entitlement.reason, "grace period expired")


class LicenseActivationTest(unittest.TestCase):
    def test_license_and_machine_hashes_are_stable_and_distinct(self):
        license_hash = hash_license_key("license-123", pepper="pepper")
        machine_hash = hash_machine_fingerprint("machine-123", pepper="pepper")

        self.assertEqual(license_hash, hash_license_key("license-123", pepper="pepper"))
        self.assertNotEqual(license_hash, machine_hash)
        self.assertNotIn("license-123", license_hash)

    def test_license_activation_limit_is_enforced(self):
        store = InMemoryLicenseActivationStore()
        license_hash = hash_license_key("license-123", pepper="pepper")
        machine_1 = hash_machine_fingerprint("machine-1", pepper="pepper")
        machine_2 = hash_machine_fingerprint("machine-2", pepper="pepper")

        first = store.activate(
            license_key_hash=license_hash,
            machine_fingerprint_hash=machine_1,
            user_label="first",
            seat_limit=1,
        )
        second = store.activate(
            license_key_hash=license_hash,
            machine_fingerprint_hash=machine_2,
            user_label="second",
            seat_limit=1,
        )

        self.assertTrue(first.allowed)
        self.assertFalse(second.allowed)
        self.assertEqual(second.reason, "activation limit reached")

    def test_existing_activation_refreshes_without_consuming_new_seat(self):
        store = InMemoryLicenseActivationStore()
        license_hash = hash_license_key("license-123", pepper="pepper")
        machine_hash = hash_machine_fingerprint("machine-1", pepper="pepper")

        first = store.activate(
            license_key_hash=license_hash,
            machine_fingerprint_hash=machine_hash,
            user_label="first",
            seat_limit=1,
        )
        second = store.activate(
            license_key_hash=license_hash,
            machine_fingerprint_hash=machine_hash,
            user_label="first",
            seat_limit=1,
        )

        self.assertTrue(first.allowed)
        self.assertTrue(second.allowed)
        self.assertEqual(second.reason, "activation refreshed")
        self.assertEqual(store.count(license_hash), 1)

    def test_activation_can_be_deactivated(self):
        store = InMemoryLicenseActivationStore()
        license_hash = hash_license_key("license-123", pepper="pepper")
        machine_hash = hash_machine_fingerprint("machine-1", pepper="pepper")
        store.activate(
            license_key_hash=license_hash,
            machine_fingerprint_hash=machine_hash,
            user_label="first",
            seat_limit=1,
        )

        changed = store.deactivate(
            license_key_hash=license_hash,
            machine_fingerprint_hash=machine_hash,
        )

        self.assertTrue(changed)
        self.assertEqual(store.count(license_hash), 0)


class WebhookIdempotencyTest(unittest.TestCase):
    def test_webhook_event_is_recorded_once(self):
        store = InMemoryWebhookEventStore()
        record = build_webhook_event_record(
            provider_event_id="evt_123",
            event_type="invoice.paid",
            payload=b"{\"id\":\"evt_123\"}",
        )

        self.assertTrue(store.record_once(record))
        self.assertFalse(store.record_once(record))
        self.assertTrue(store.has_seen("evt_123"))

    def test_webhook_payload_hash_changes_with_payload(self):
        first = build_webhook_event_record(
            provider_event_id="evt_1",
            event_type="invoice.paid",
            payload=b"first",
        )
        second = build_webhook_event_record(
            provider_event_id="evt_2",
            event_type="invoice.paid",
            payload=b"second",
        )

        self.assertNotEqual(first.payload_hash, second.payload_hash)


if __name__ == "__main__":
    unittest.main()
