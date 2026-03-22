# AI Sentinel

**Steer the frontier signal pipeline** for subscription-grade AI intelligence delivery. This Treasure packages the DR-4 operating method into a marshal-style workflow: tiered source collection, structured signal triage, 5-minute daily briefing, and event-centric knowledge accumulation. The full production corpus can still be extended from your separately managed knowledge assets.

## Overview

- **Type:** Marshal / subscription intelligence Treasure
- **Lane:** Large
- **Pricing posture:** Paid subscription or managed intelligence engagement
- **Status:** Official Treasure with bundled operating scaffold; production-grade corpus remains extensible

## Best For

1. Producing a daily AI intelligence brief from tiered source monitoring without dumping raw noise on the reader.
2. Tracking a company, model family, or topic such as `OpenAI`, `AI Agent`, or `AI 安全` and judging whether the trend is heating up or cooling down.
3. Building a subscription-style signal workflow with clear evidence, confidence, and next-action traceability.
4. Bridging daily briefs with longer-lived event memory, while leaving the proprietary corpus open to external extension.

## Core Capabilities

### 1. Four-tier source management

- Tier 1: official releases, major papers, top conferences
- Tier 2: authority tech media and analyst reports
- Tier 3: technical communities and GitHub trend signals
- Tier 4: social early-signal scanning with strict filtering

### 2. Three-stage signal triage

- Rule-based coarse filter for freshness, length, duplicates, and PR noise
- Structured LLM scoring across impact, scarcity, timeliness, and verifiability
- Human-review-ready output for top signals and watchlist items

### 3. Brief generation patterns

- `daily_brief`
- `entity_watch`
- `trend_radar`
- `compare`
- `follow_up`

### 4. Event-centric knowledge scaffold

The packaged `knowledge/` folder now carries the operating scaffold distilled from the DR-4 eight-model report:

- source tiering
- triage rubric
- daily brief structure
- event item schema
- query playbook
- MVP rollout blueprint

### 5. Paid-value posture

This Treasure is designed for a subscription intelligence product where the value comes from:

- source quality
- structure and traceability
- trend-level insight instead of raw link dumping

## Inputs

- User request about AI developments, company tracking, or trend interpretation
- Streaming sources from `source_collector` such as RSS, APIs, official blogs, and monitoring hooks
- Optional user-interest memory from `query_long_memory`
- Bundled operating knowledge from `knowledge/`

## Outputs

- `signals.json`: curated alerts with structured importance scoring and verification flags
- `daily_brief.md`: mobile-friendly narrative summary of top signals and next actions
- `daily_brief.json`: structured brief for integrations and downstream rendering
- `publish_ticket`: sync-ready handoff for channels such as Telegram, Feishu, or internal dashboards

## Tooling

- `source_collector`
- `structured_worker`
- `structured_writer`
- `knowledge_search`
- `query_long_memory`
- `llm_call`
- `sync_worker`
- `send_to_user`

## Bundled Knowledge Assets

- [`knowledge/dr4-mvp-blueprint.md`](knowledge/dr4-mvp-blueprint.md)
- [`knowledge/source-tiering.md`](knowledge/source-tiering.md)
- [`knowledge/source-registry.yaml`](knowledge/source-registry.yaml)
- [`knowledge/signal-triage-rubric.md`](knowledge/signal-triage-rubric.md)
- [`knowledge/triage-scorecard.yaml`](knowledge/triage-scorecard.yaml)
- [`knowledge/daily-brief-format.md`](knowledge/daily-brief-format.md)
- [`knowledge/event-item-schema.md`](knowledge/event-item-schema.md)
- [`knowledge/sample-event-item.yaml`](knowledge/sample-event-item.yaml)
- [`knowledge/sample-trend-item.yaml`](knowledge/sample-trend-item.yaml)
- [`knowledge/query-playbook.md`](knowledge/query-playbook.md)
- [`contracts.yaml`](contracts.yaml)

## Starter Structured Assets

Beyond the markdown playbook, this package now includes machine-readable starter assets for faster integration:

- a starter source registry with tier, cadence, locale, and authority weight
- a triage scorecard with thresholds, scoring weights, and discard patterns
- sample `EventItem` and `TrendItem` records to anchor downstream schema work
- example `signals.json` and `daily_brief.md` outputs for manual QA and renderer alignment

## Quick Try

```bash
treasure-furnace validate https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel
treasure-furnace preview https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel
treasure-furnace install https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel --runtime-assets-dir /tmp/ai-sentinel-preview
```

Use [`examples/smoke.md`](examples/smoke.md) for manual production-like verification after preview or install.

If you need renderer or QA alignment, also inspect:

- [`examples/signals.sample.json`](examples/signals.sample.json)
- [`examples/daily_brief.sample.md`](examples/daily_brief.sample.md)

## Output Shape

The lead story should always answer:

1. What's new
2. Why it matters
3. Which source supports it
4. How confident the system is
5. What to watch next

The default daily format follows a 3-5 minute scan rhythm:

- editor line
- one lead story
- 3-4 industry updates
- 1-2 technical frontier notes
- one tool or product worth testing
- 3-5 quick hits
- a weekly trend radar section

## Limitations

- The bundled knowledge is an operating scaffold, not a full proprietary research corpus.
- Live source connectors, paywalls, and channel delivery credentials are still environment-dependent.
- High-value signals should still receive human review during MVP, especially when used for paid delivery.
- China-market deployment should keep emphasizing lawful sources, traceability, and compliance-safe claims.
