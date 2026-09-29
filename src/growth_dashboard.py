from __future__ import annotations

import json
from pathlib import Path


PROFILE_PATH = Path(__file__).resolve().parent.parent / "config" / "app_profile_template.json"


def load_profile(path: str | Path = PROFILE_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def get_growth_recommendations(profile: dict) -> list[str]:
    app_type = profile.get("app_type", "general")
    levers = {
        "social": [
            "Add one-tap share moments after meaningful milestones.",
            "Reward both inviter and invitee for successful activation.",
            "Use social proof to show the network is active.",
        ],
        "saas": [
            "Reduce onboarding friction before the first share prompt.",
            "Create a powerful team or workspace invite loop.",
            "Tie invite rewards to successful team activation.",
        ],
        "marketplace": [
            "Trigger invites when trust or value is established.",
            "Offer referral rewards for successful transactions.",
            "Focus on new-user conversion and repeat transactions.",
        ],
        "gaming": [
            "Reward social share after milestone unlocks.",
            "Highlight social competition and squad play.",
            "Drive invites around leaderboards and co-op moments.",
        ],
        "content": [
            "Invite people to save, share, or remix strong content moments.",
            "Reward referrals tied to engagement, not vanity installs.",
            "Focus on creator-to-audience network loops.",
        ],
        "productivity": [
            "Trigger invites after the user experiences meaningful workflow gains.",
            "Promote team-based sharing and workspace collaboration.",
            "Optimise retention before scaling referral loops.",
        ],
    }
    return levers.get(app_type, [
        "Reduce friction before the share moment.",
        "Improve activation and retention before pushing invites harder.",
        "Test high-value, low-friction referral experiences.",
    ])


def main() -> None:
    profile = load_profile()
    print(f"App type: {profile.get('app_type', 'general')}")
    print(f"Primary growth loop: {profile.get('primary_growth_loop', 'referral')}")
    print(f"Recommended first experiment: {profile.get('first_experiment', 'share prompt timing')}")
    print("\nSuggested growth levers:")
    for i, lever in enumerate(get_growth_recommendations(profile), start=1):
        print(f"{i}. {lever}")


if __name__ == "__main__":
    main()
