from __future__ import annotations


def calculate_viral_coefficient(
    invites_per_user: float,
    invite_conversion_rate: float,
    activation_rate: float,
    retention_rate: float,
) -> float:
    """Compute a simple viral coefficient approximation.

    K = invites_per_user * invite_conversion_rate * activation_rate * retention_rate
    """
    return invites_per_user * invite_conversion_rate * activation_rate * retention_rate


def growth_status(k_value: float) -> str:
    if k_value >= 1.0:
        return "Strong growth potential"
    if k_value >= 0.5:
        return "Promising but needs stronger retention or sharing"
    return "Weak viral loop; prioritise activation and referral flow"


def identify_bottleneck(
    invites_per_user: float,
    invite_conversion_rate: float,
    activation_rate: float,
    retention_rate: float,
) -> str:
    values = {
        "invites_per_user": invites_per_user,
        "invite_conversion_rate": invite_conversion_rate,
        "activation_rate": activation_rate,
        "retention_rate": retention_rate,
    }

    weakest_metric = min(values, key=values.get)
    mapping = {
        "invites_per_user": "sharing frequency",
        "invite_conversion_rate": "invite conversion",
        "activation_rate": "activation after invite",
        "retention_rate": "retention after activation",
    }
    return mapping[weakest_metric]


def main() -> None:
    invites_per_user = 1.4
    invite_conversion_rate = 0.28
    activation_rate = 0.62
    retention_rate = 0.82

    k_value = calculate_viral_coefficient(
        invites_per_user,
        invite_conversion_rate,
        activation_rate,
        retention_rate,
    )

    print(f"Viral coefficient (K): {k_value:.2f}")
    print(f"Status: {growth_status(k_value)}")
    print(f"Primary bottleneck: {identify_bottleneck(invites_per_user, invite_conversion_rate, activation_rate, retention_rate)}")
    print("Recommended action: improve onboarding, reward loops, and share friction")


if __name__ == "__main__":
    main()
