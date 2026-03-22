# Event Item Schema

## Modeling principle

Use event-centric memory, not a loose pile of snippets.

## Three asset layers

### Evidence Chunk

- immutable source fragment
- keeps source, quote, time, and retrieval reference

### Event Item

- the main unit for retrieval, filtering, and timeline reasoning
- can be updated as new evidence arrives

### Trend Item

- a higher-level conclusion supported by multiple event items
- better suited to weekly or monthly synthesis

## Event Item fields

- entry_id
- parent_id
- version
- event_date
- publish_date
- effective_date
- expiry_date
- title
- summary
- key_quotes
- semantic_tags
- topic_vector
- companies
- people
- technologies
- products
- related_entries
- trend_ids
- source_url
- source_tier
- multi_source_count
- importance_score
- confidence
- freshness_score

## Time handling

Track both:

- valid time: when the fact is true in the world
- transaction time: when the fact was written into memory

Freshness should decay by event type, because policy, funding, research, and security events age differently.

## Condensation rules

- monthly: cluster Event Items into Trend Items
- quarterly: summarize Trend Items into a narrative about acceleration, slowdown, and divergence
