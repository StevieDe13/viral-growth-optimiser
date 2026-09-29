# Viral Growth Optimiser

A starter repository for diagnosing, experimenting with, and improving an app's viral growth loop.

This repo is designed to help you turn product growth from a vague goal into an observable system: track the right metrics, model your viral coefficient, and run structured experiments around referrals, invites, retention, and network effects.

## Why this repo exists

Most apps fail to grow because they focus only on acquisition and ignore the mechanics that make growth self-reinforcing.

This project gives you a simple framework for:

- measuring the referral loop,
- spotting the highest-leverage growth bottlenecks,
- quantifying the viral coefficient,
- prioritising experiments that improve retention and sharing.

## Core growth idea

The viral coefficient K is the number of new users brought in by each existing user. If K is above 1, growth compounds.

A practical formula:

K = invites_per_user × invite_conversion × activation_rate × retention_rate

This repo helps you model that while keeping the focus on product decisions rather than vanity metrics.

## Repository structure

- `src/viral_growth_score.py` — calculates viral growth metrics and flags weak points
- `docs/viral-growth-playbook.md` — product strategy guide for growth experiments
- `data/sample_growth_metrics.csv` — sample dataset for quick testing and analysis

## Quick start

```bash
python3 src/viral_growth_score.py
```

This will print a basic snapshot of your growth health using default values.

## Metrics to monitor

- Invites sent per active user
- Invite conversion rate
- User activation rate after invite
- 7-day retention rate
- Repeat sharing rate
- Referral completion rate
- Cost per activated referral

## Growth levers to test

1. Reduce friction before the share prompt appears
2. Reward the right side of the exchange, not just the inviter
3. Increase emotional share moments inside the product
4. Improve onboarding for invite recipients
5. Make the invitation feel useful, not spammy
6. Focus on retention before scaling acquisition

## Example output

```text
Viral coefficient (K): 1.38
Status: Strong growth potential
Primary bottleneck: retention after activation
Recommended action: improve onboarding and 7-day stickiness
```

## Next steps

- replace the sample numbers with your real product metrics
- add cohort-based dashboards and experiment logs
- connect this to analytics tooling such as Mixpanel, GA4, Amplitude, or PostHog
- iterate the model to fit your app's true growth engine

## License

MIT
