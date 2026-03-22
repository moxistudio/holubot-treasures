# Signal Triage Rubric

## Why this exists

The main failure mode is simple: LLMs often think everything sounds important. This rubric exists to force structured judgment before ranking.

## The three-stage pipeline

### Stage 1: coarse filter

- source allowlist or denylist
- freshness within the requested time window, default 72 hours
- text length above 300 characters
- semantic dedupe over 0.85 merges into one event

### Stage 2: structured scoring

Score each candidate on four dimensions:

- impact
- scarcity
- timeliness
- verifiability

Do not ask the model "is this important?". Ask it to extract structured evidence first, then compute importance.

## High-priority threshold guidance

A signal is usually high priority only if at least one is true:

- it comes from a first-party source and changes product, research, policy, or distribution assumptions
- it is confirmed by at least two independent authority sources
- it materially changes what an operator, founder, or researcher should do next

## Patterns to discard or downgrade

- pure brand PR with no new capability or policy impact
- repeated funding coverage with no strategic delta
- reposted summaries that add no first-hand evidence
- weak social speculation without corroboration

## Output fields

Each selected signal should carry:

- signal_id
- title
- source_tier
- source_url
- publish_date
- importance_score
- importance_level
- impact_dimensions
- entities
- urgency
- confidence
- why_important
- next_action
- pending_verification

## Personal relevance boost

If a signal is strongly related to the user’s recent interests, it can be boosted, but the reason must be explicit and never override weak evidence.
