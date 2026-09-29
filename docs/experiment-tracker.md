from __future__ import annotations

import csv
from dataclasses import dataclass, asdict
from pathlib import Path


EXPERIMENTS_PATH = Path(__file__).resolve().parent.parent / "data" / "experiments.csv"


@dataclass
class Experiment:
    name: str
    hypothesis: str
    variant: str
    baseline: float
    variant_result: float
    primary_metric: str
    status: str = "planned"

    def effect(self) -> float:
        return round(self.variant_result - self.baseline, 4)

    def decision(self) -> str:
        if self.effect() > 0:
            return "scale"
        if self.effect() < 0:
            return "pivot"
        return "hold"


def load_experiments(path: str | Path = EXPERIMENTS_PATH) -> list[Experiment]:
    experiments = []
    with open(path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            experiments.append(
                Experiment(
                    name=row.get("name", "unnamed"),
                    hypothesis=row.get("hypothesis", ""),
                    variant=row.get("variant", ""),
                    baseline=float(row.get("baseline", 0.0)),
                    variant_result=float(row.get("variant_result", 0.0)),
                    primary_metric=row.get("primary_metric", "conversion"),
                    status=row.get("status", "planned"),
                )
            )
    return experiments


def print_experiment_summary(experiments: list[Experiment]) -> None:
    print("Growth experiment tracker")
    print("=" * 30)
    for exp in experiments:
        print(f"Experiment: {exp.name}")
        print(f"  Hypothesis: {exp.hypothesis}")
        print(f"  Variant: {exp.variant}")
        print(f"  Metric: {exp.primary_metric}")
        print(f"  Delta: {exp.effect():.2%}")
        print(f"  Recommendation: {exp.decision()}")
        print()


def main() -> None:
    experiments = load_experiments()
    print_experiment_summary(experiments)


if __name__ == "__main__":
    main()
