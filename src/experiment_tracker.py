from __future__ import annotations

import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_growth_metrics.csv"


def load_metrics(path: str | Path = DATA_PATH) -> dict:
    metrics = {}
    with open(path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            if row.get("metric"):
                metrics[row["metric"]] = float(row["value"])
    return metrics


def calculate_viral_coefficient(metrics: dict) -> float:
    return (
        metrics.get("invites_per_user", 0.0)
        * metrics.get("invite_conversion_rate", 0.0)
        * metrics.get("activation_rate", 0.0)
        * metrics.get("retention_rate", 0.0)
    )


def growth_score(metrics: dict) -> float:
    k = calculate_viral_coefficient(metrics)
    invite_conversion = metrics.get("invite_conversion_rate", 0.0)
    activation = metrics.get("activation_rate", 0.0)
    retention = metrics.get("retention_rate", 0.0)
    return round((k * 30) + (invite_conversion * 40) + (activation * 20) + (retention * 10), 2)


def summarize(metrics: dict) -> dict:
    k = calculate_viral_coefficient(metrics)
    return {
        "viral_coefficient": round(k, 2),
        "growth_score": growth_score(metrics),
        "status": "Strong growth potential" if k >= 1.0 else "Needs product loop optimisation",
        "primary_bottleneck": "retention after activation" if metrics.get("retention_rate", 0) < 0.8 else "share conversion",
    }


def main() -> None:
    metrics = load_metrics()
    summary = summarize(metrics)

    print("Viral growth dashboard")
    print("=" * 30)
    print(f"Invites / active user: {metrics.get('invites_per_user', 0):.2f}")
    print(f"Invite conversion: {metrics.get('invite_conversion_rate', 0):.2%}")
    print(f"Activation rate: {metrics.get('activation_rate', 0):.2%}")
    print(f"Retention rate: {metrics.get('retention_rate', 0):.2%}")
    print(f"Viral coefficient (K): {summary['viral_coefficient']:.2f}")
    print(f"Growth score: {summary['growth_score']}")
    print(f"Status: {summary['status']}")
    print(f"Primary bottleneck: {summary['primary_bottleneck']}")


if __name__ == "__main__":
    main()
