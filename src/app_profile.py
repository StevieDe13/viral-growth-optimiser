# Viral Growth Optimiser

A growth-focused starter repo for optimising an app's viral potential across acquisition, activation, referral, and retention loops.

This version includes three practical layers:

1. Tailoring to your app type through a reusable app profile
2. A growth dashboard for monitoring the right viral metrics
3. An experiment tracker for running structured growth tests

## Why this repo exists

Most apps fail to grow not because they lack distribution, but because they do not build a repeatable system where users recruit more users. This repo is designed to turn that into a measurable product loop.

## App-type tailoring

Use the app profile template to adapt the repo to your app category and growth model.

- `config/app_profile_template.json`
- `src/app_profile.py`

Supported profiles include:

- `social`
- `saas`
- `marketplace`
- `gaming`
- `content`
- `productivity`

## Dashboard

Use the dashboard to score and monitor the major growth drivers.

- `src/growth_dashboard.py`
- `data/sample_growth_metrics.csv`

This dashboard calculates:

- viral coefficient (K)
- sharing intensity
- invite conversion
- activation rate
- retention score
- experiment confidence

## Experiment tracker

Use the tracker to plan and compare experiments.

- `src/experiment_tracker.py`
- `data/experiments.csv`
- `docs/experiment-tracker.md`

This helps you record:

- hypothesis
- baseline and variant
- sample size
- primary metric
- result
- recommendation

## Quick start

### 1) Inspect the app profile

```bash
python3 src/app_profile.py
```

### 2) Run the growth dashboard

```bash
python3 src/growth_dashboard.py
```

### 3) Review experiment tracker data

```bash
python3 src/experiment_tracker.py
```

## Core viral formula

```text
K = invites_per_user × invite_conversion_rate × activation_rate × retention_rate
```

A value above 1 indicates a self-reinforcing loop. The goal is not just to grow counting users, but to improve the quality of the referral loop while protecting retention.

## Growth metrics to watch

- invites sent per active user
- friend accept rate
- activation rate after invite
- 7-day retention
- share completion rate
- repeat sharing rate
- cost per activated referral

## System design

This repo is intentionally structured so you can plug in real product data later:

- replace sample metrics with your analytics exports
- connect each experiment to a feature flag or release
- match experiments to your app profile
- update the profile as the product matures

## Sample growth profile

```text
App type: general-purpose product
Primary growth loop: referral + onboarding
Main bottleneck: activation after invite
Recommendation: reduce sign-up friction and improve first-week retention
```

## Next steps

- add real event tracking from Amplitude, Mixpanel, GA4, or PostHog
- connect experiments to a live dashboard
- estimate the impact of each growth driver using cohort analysis
- iterate on the app profile as you learn which growth loop works best

## License

MIT
