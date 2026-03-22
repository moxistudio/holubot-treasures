# DR-4 Synthesis

## What this document is

This is the packaged research正文 version of the DR-4 eight-model synthesis. It captures the parts that should remain searchable inside the AI Sentinel Treasure rather than living only in an external planning folder.

## Best source contributions by topic

### Source selection and management

- Perplexity contributed the strongest concrete source inventory.
- Grok reinforced the need for executable source handling rather than broad collection.
- Kimi clarified the tiered weighting approach.

The packaged conclusion is:

- keep the source base small and high quality first
- bias toward first-party and authority sources
- revisit source drift regularly
- treat source legality and traceability as quality gates

### Triage and noise filtering

- Grok contributed the strongest executable mixed pipeline
- Perplexity sharpened the “structured feature extraction before scoring” rule
- Kimi added practical review-ratio guidance

The packaged conclusion is:

- rules first
- structured LLM scoring second
- human review for the top slice during MVP
- never let a model directly improvise importance without a rubric

### Daily brief quality

- Claude(Compass) contributed the most product-useful benchmark teardown
- ChatGPT contributed the most systematic event and brief structure

The packaged conclusion is:

- target a 3-5 minute mobile read
- structure the lead story around facts, consequence, evidence, and confidence
- keep one deep lead plus a small set of fast secondary items

### Knowledge base architecture

- ChatGPT and Kimi both converged on event-centric memory
- Claude(Compass) made the format and product implications more concrete

The packaged conclusion is:

- separate evidence chunks, event items, and trend items
- use event items as the main retrieval and reasoning unit
- compress upward into trend items over time

### Query and retrieval

- 豆包 contributed the most useful user-behavior patterns
- Kimi shaped the query architecture
- Claude(Compass) made the RAG parameter choices concrete

The packaged conclusion is:

- support natural-language question style as the default
- combine vector retrieval with keyword retrieval
- rewrite vague queries into structured search hints
- prioritize speed enough that the first answer feels instant

### Paid value and product logic

- Kimi provided the clearest “value = quality × structure × insight” framing
- 豆包 provided China-side willingness-to-pay and behavior support
- Qwen contributed the strongest compliance framing

The packaged conclusion is:

- paid value comes from filtered and reusable intelligence, not information volume
- compliance should be treated as a value signal, not just a restriction
- the knowledge base must feel cumulative to users, not like disposable summaries

## Working product thesis from DR-4

AI Sentinel should not behave like a general AI news stream. It should behave like an intelligence system that:

- sees first-party and high-value signals quickly
- filters noisy hype aggressively
- turns changes into decisions, content, and opportunity cues
- accumulates reusable memory over time

## Packaged implementation priorities

1. maintain the source registry
2. keep the scorecard and discard rules current
3. generate briefs with explicit consequence and confidence
4. convert important signals into event items
5. compress recurrent patterns into trend items
