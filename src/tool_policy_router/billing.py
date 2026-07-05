from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Mapping, Protocol


PREMIUM_FEATURES_BY_PLAN: dict[str, frozenset[str]] = {
    "solo": frozenset({"policy_profiles", "audit_export"}),
    "team": frozenset({"policy_profiles", "audit_export", "team_config", "team_seats"}),
    "design_partner": frozenset(
        {
            "policy_profiles",
            "audit_export",
            "team_config",
            "team_seats",
            "design_partner_support",
        }
    ),
    "enterprise": frozenset(
        {
            "policy_profiles",
            "audit_export",
            "team_config",
            "team_seats",
            "design_partner_support",
            "hosted_policy_api_future",
            "hosted_audit_export_future",
        }
    ),
}

DEFAULT_SEAT_LIMITS: dict[str, int] = {
    "solo": 1,
    "team": 1,
    "design_partner": 5,
    "enterprise": 0,
}

PREMIUM_ENABLED_STATUSES = frozenset({"trialing", "active"})
PREMIUM_DISABLED_STATUSES = frozenset({"canceled", "unpaid", "missing", "incomplete", "incomplete_expired"})
GRACE_PERIOD_STATUSES = frozenset({"past_due"})


@dataclass(frozen=True)
class BillingPlan:
    """A product-facing billing plan mapped to a Stripe price ID by configuration."""

    name: str
    stripe_price_env_var: str
    monthly_price_usd: int
    seat_limit: int
    trial_period_days: int = 30


@dataclass(frozen=True)
class BillingConfig:
    """Environment-derived billing configuration without secret values."""

    price_ids_by_plan: Mapping[str, str]
    success_url: str
    cancel_url: str
    portal_return_url: str | None = None

    def price_id_for_plan(self, plan: str) -> str:
        try:
            return self.price_ids_by_plan[plan]
        except KeyError as exc:
            raise ValueError(f"unsupported billing plan: {plan}") from exc


@dataclass(frozen=True)
class CheckoutRequest:
    plan: str
    email: str
    success_url: str | None = None
    cancel_url: str | None = None


@dataclass(frozen=True)
class CheckoutSessionRequest:
    price_id: str
    email: str
    success_url: str
    cancel_url: str
    trial_period_days: int = 30
    mode: str = "subscription"


@dataclass(frozen=True)
class CheckoutSessionResult:
    checkout_url: str
    provider_session_id: str


@dataclass(frozen=True)
class PortalSessionRequest:
    stripe_customer_id: str
    return_url: str


@dataclass(frozen=True)
class PortalSessionResult:
    portal_url: str
    provider_session_id: str


class StripeCheckoutGateway(Protocol):
    """Minimal gateway boundary for Stripe or a test double."""

    def create_checkout_session(self, request: CheckoutSessionRequest) -> CheckoutSessionResult:
        ...

    def create_portal_session(self, request: PortalSessionRequest) -> PortalSessionResult:
        ...


@dataclass(frozen=True)
class SubscriptionRecord:
    customer_id: str
    stripe_subscription_id: str
    plan: str
    status: str
    seat_limit: int
    trial_ends_at: datetime | None = None
    current_period_ends_at: datetime | None = None
    grace_until: datetime | None = None


@dataclass(frozen=True)
class Entitlement:
    status: str
    plan: str | None
    premium_enabled: bool
    features: frozenset[str] = field(default_factory=frozenset)
    seat_limit: int = 0
    trial_ends_at: datetime | None = None
    current_period_ends_at: datetime | None = None
    grace_until: datetime | None = None
    reason: str = "missing entitlement"

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "plan": self.plan,
            "premium_enabled": self.premium_enabled,
            "features": sorted(self.features),
            "seat_limit": self.seat_limit,
            "trial_ends_at": isoformat_or_none(self.trial_ends_at),
            "current_period_ends_at": isoformat_or_none(self.current_period_ends_at),
            "grace_until": isoformat_or_none(self.grace_until),
            "reason": self.reason,
        }


@dataclass(frozen=True)
class LicenseActivation:
    license_key_hash: str
    machine_fingerprint_hash: str
    user_label: str
    activated_at: datetime
    last_seen_at: datetime


@dataclass(frozen=True)
class LicenseActivationResult:
    allowed: bool
    reason: str
    activation: LicenseActivation | None = None


@dataclass(frozen=True)
class WebhookEventRecord:
    provider: str
    provider_event_id: str
    event_type: str
    payload_hash: str
    processed_at: datetime


class InMemoryWebhookEventStore:
    """Small idempotency store for tests and developer-preview contracts."""

    def __init__(self) -> None:
        self._events: dict[str, WebhookEventRecord] = {}

    def record_once(self, record: WebhookEventRecord) -> bool:
        if record.provider_event_id in self._events:
            return False
        self._events[record.provider_event_id] = record
        return True

    def has_seen(self, provider_event_id: str) -> bool:
        return provider_event_id in self._events


class InMemoryLicenseActivationStore:
    """Activation-limit helper for developer-preview tests."""

    def __init__(self) -> None:
        self._activations: dict[str, list[LicenseActivation]] = {}

    def activate(
        self,
        *,
        license_key_hash: str,
        machine_fingerprint_hash: str,
        user_label: str,
        seat_limit: int,
        now: datetime | None = None,
    ) -> LicenseActivationResult:
        now = now or utc_now()
        activations = self._activations.setdefault(license_key_hash, [])
        for activation in activations:
            if activation.machine_fingerprint_hash == machine_fingerprint_hash:
                refreshed = LicenseActivation(
                    license_key_hash=license_key_hash,
                    machine_fingerprint_hash=machine_fingerprint_hash,
                    user_label=activation.user_label,
                    activated_at=activation.activated_at,
                    last_seen_at=now,
                )
                index = activations.index(activation)
                activations[index] = refreshed
                return LicenseActivationResult(True, "activation refreshed", refreshed)

        if seat_limit > 0 and len(activations) >= seat_limit:
            return LicenseActivationResult(False, "activation limit reached")

        activation = LicenseActivation(
            license_key_hash=license_key_hash,
            machine_fingerprint_hash=machine_fingerprint_hash,
            user_label=user_label,
            activated_at=now,
            last_seen_at=now,
        )
        activations.append(activation)
        return LicenseActivationResult(True, "activation created", activation)

    def deactivate(self, *, license_key_hash: str, machine_fingerprint_hash: str) -> bool:
        activations = self._activations.get(license_key_hash, [])
        kept = [
            activation
            for activation in activations
            if activation.machine_fingerprint_hash != machine_fingerprint_hash
        ]
        changed = len(kept) != len(activations)
        self._activations[license_key_hash] = kept
        return changed

    def count(self, license_key_hash: str) -> int:
        return len(self._activations.get(license_key_hash, []))


class MockStripeGateway:
    """Test double that records Checkout and Portal requests without network calls."""

    def __init__(self) -> None:
        self.checkout_requests: list[CheckoutSessionRequest] = []
        self.portal_requests: list[PortalSessionRequest] = []

    def create_checkout_session(self, request: CheckoutSessionRequest) -> CheckoutSessionResult:
        self.checkout_requests.append(request)
        index = len(self.checkout_requests)
        return CheckoutSessionResult(
            checkout_url=f"https://checkout.stripe.test/session/{index}",
            provider_session_id=f"cs_test_{index}",
        )

    def create_portal_session(self, request: PortalSessionRequest) -> PortalSessionResult:
        self.portal_requests.append(request)
        index = len(self.portal_requests)
        return PortalSessionResult(
            portal_url=f"https://billing.stripe.test/session/{index}",
            provider_session_id=f"bps_test_{index}",
        )


def build_checkout_session_request(config: BillingConfig, request: CheckoutRequest) -> CheckoutSessionRequest:
    return CheckoutSessionRequest(
        price_id=config.price_id_for_plan(request.plan),
        email=request.email,
        success_url=request.success_url or config.success_url,
        cancel_url=request.cancel_url or config.cancel_url,
        trial_period_days=30,
    )


def create_checkout_session(
    *, gateway: StripeCheckoutGateway, config: BillingConfig, request: CheckoutRequest
) -> CheckoutSessionResult:
    return gateway.create_checkout_session(build_checkout_session_request(config, request))


def create_portal_session(
    *, gateway: StripeCheckoutGateway, stripe_customer_id: str, return_url: str
) -> PortalSessionResult:
    return gateway.create_portal_session(
        PortalSessionRequest(stripe_customer_id=stripe_customer_id, return_url=return_url)
    )


def entitlement_from_subscription(
    subscription: SubscriptionRecord | None,
    *,
    now: datetime | None = None,
    grace_period: timedelta = timedelta(hours=72),
) -> Entitlement:
    now = now or utc_now()
    if subscription is None:
        return Entitlement(status="missing", plan=None, premium_enabled=False)

    status = subscription.status
    plan = subscription.plan
    features = PREMIUM_FEATURES_BY_PLAN.get(plan, frozenset())
    seat_limit = subscription.seat_limit or DEFAULT_SEAT_LIMITS.get(plan, 0)

    if status in PREMIUM_ENABLED_STATUSES:
        return Entitlement(
            status=status,
            plan=plan,
            premium_enabled=True,
            features=features,
            seat_limit=seat_limit,
            trial_ends_at=subscription.trial_ends_at,
            current_period_ends_at=subscription.current_period_ends_at,
            grace_until=subscription.grace_until,
            reason="subscription allows premium access",
        )

    if status in GRACE_PERIOD_STATUSES:
        grace_until = subscription.grace_until or now + grace_period
        premium_enabled = now <= grace_until
        return Entitlement(
            status=status,
            plan=plan,
            premium_enabled=premium_enabled,
            features=features if premium_enabled else frozenset(),
            seat_limit=seat_limit if premium_enabled else 0,
            trial_ends_at=subscription.trial_ends_at,
            current_period_ends_at=subscription.current_period_ends_at,
            grace_until=grace_until,
            reason="within grace period" if premium_enabled else "grace period expired",
        )

    if status in PREMIUM_DISABLED_STATUSES:
        return Entitlement(
            status=status,
            plan=plan,
            premium_enabled=False,
            trial_ends_at=subscription.trial_ends_at,
            current_period_ends_at=subscription.current_period_ends_at,
            grace_until=subscription.grace_until,
            reason="subscription does not allow premium access",
        )

    return Entitlement(
        status=status,
        plan=plan,
        premium_enabled=False,
        trial_ends_at=subscription.trial_ends_at,
        current_period_ends_at=subscription.current_period_ends_at,
        grace_until=subscription.grace_until,
        reason=f"unsupported subscription status: {status}",
    )


def hash_license_key(license_key: str, *, pepper: str) -> str:
    if not license_key:
        raise ValueError("license_key is required")
    if not pepper:
        raise ValueError("pepper is required")
    return hashlib.sha256(f"{pepper}:{license_key}".encode("utf-8")).hexdigest()


def hash_machine_fingerprint(machine_fingerprint: str, *, pepper: str) -> str:
    if not machine_fingerprint:
        raise ValueError("machine_fingerprint is required")
    if not pepper:
        raise ValueError("pepper is required")
    return hashlib.sha256(f"{pepper}:{machine_fingerprint}".encode("utf-8")).hexdigest()


def payload_hash(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def build_webhook_event_record(
    *, provider_event_id: str, event_type: str, payload: bytes, processed_at: datetime | None = None
) -> WebhookEventRecord:
    if not provider_event_id:
        raise ValueError("provider_event_id is required")
    if not event_type:
        raise ValueError("event_type is required")
    return WebhookEventRecord(
        provider="stripe",
        provider_event_id=provider_event_id,
        event_type=event_type,
        payload_hash=payload_hash(payload),
        processed_at=processed_at or utc_now(),
    )


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def isoformat_or_none(value: datetime | None) -> str | None:
    return value.isoformat() if value else None
