# DR-4 MVP Blueprint

This note distills the DR-4 eight-model report into one executable blueprint for the AI Sentinel Treasure.

## One-line thesis

Four-tier source management + rule-first signal filtering + structured LLM scoring + event-centric memory + 5-minute mobile briefing is the shortest path to a paid AI intelligence service that feels meaningfully better than raw link aggregation.

## The five most important actions

1. Lock the first 30 high-quality sources before chasing coverage breadth.
2. Build the triage pipeline as `rules -> structured scoring -> human review for top signals`.
3. Produce a real daily brief fast, even before the long-term corpus is complete.
4. Convert daily outputs into event items so the system accumulates memory.
5. Audit scoring drift and noisy "everything is important" behavior every month.

## Working architecture

### Collection

- Tier 1: official announcements, research pages, top conferences
- Tier 2: authority media and analyst reports
- Tier 3: technical communities and GitHub trend signals
- Tier 4: social early signals with strict filtering

### Triage

- Rules do the first pass.
- LLM extracts structured evidence and scores it.
- Human review only touches the top slice during MVP.

### Output

- one lead story
- 3-4 industry updates
- 1-2 technical frontier items
- one tool worth testing
- quick hits
- trend radar

### Memory

- evidence chunk
- event item
- trend item

## Biggest risks

1. LLMs over-score noisy items as "important".
2. Daily quality becomes inconsistent without human spot checks.
3. The system collects knowledge but never surfaces historical context back into the brief.

## Paid-value principle

The product becomes worth paying for only when all three are present at once:

- trustworthy sources
- structured and reusable outputs
- trend insight beyond raw summaries

## China-market reminder

Source legality, traceability, and compliance-safe wording are product features, not afterthoughts.
