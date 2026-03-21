# AI Sentinel

**Steer the frontier signal pipeline** for subscription-grade intelligence delivery. This shell shows the marshal worker choreography for signal collection, triage, and briefing, but the associated knowledge base content is maintained externally and intentionally excluded from this staging package.

## Overview

- **Type:** Marshal / subscription intelligence Treasure
- **Lane:** Large
- **Pricing:** Paid (subscription or managed engagement)
- **Status:** Official slot reserved, market shell only, KB in a separate repository

## Best For

1. Demonstrating how HoluBot can coordinate multi-worker signal capture and triaging before producing structured intelligence briefs.
2. Validating subscription-first workflows that monitor trending events, tag them, and push daily updates.
3. Conveying the guardrails for evidence, sources, and next actions without delivering the proprietary knowledge store.

## Inputs

- Streaming sources from `source_collector` (e.g., news APIs, RSS, monitoring hooks)
- Internal notes from on-call analysts or research collaborators

## Outputs

- `signals.json`: curated alerts with confidence metadata
- `daily_brief.md`: narrative summary of top signals plus next-action recommendations
- `daily_brief.json`: structured brief for integrations

## Tooling

- `source_collector`
- `structured_worker`
- `structured_writer`
- `sync_worker`
- `send_to_user`

## Quick Try

```bash
treasure-furnace install https://github.com/<org>/holubot-treasures/tree/main/official/ai-sentinel
treasure-furnace run ai-sentinel --example smoke
```

> This will spin up the workers without a live KB; use your team-managed knowledge repo when integrating the full pipeline.

## Limitations

- No bundled knowledge base; integration teams must wire their own KB artifact or reference data.
- Subscription pricing and gating are handled separately; this shell only validates behavior.
