# Retrieval And Query Architecture

## Retrieval objective

The retrieval layer should make the KB feel cumulative and fast. It should not force users to remember exact keywords, and it should not feel slow enough to discourage follow-up questions.

## Recommended storage split

- SQLite for structured metadata, event records, entities, and relations
- ChromaDB for vectors

The current recommended collections are:

- evidence_chunks
- event_items
- trend_items

## Embedding and reranking

The DR-4 synthesis recommended:

- bge-large-zh-v1.5 as the practical MVP embedding model
- vector recall first
- cross-encoder rerank after recall

## Query flow

1. rewrite vague natural-language query into search hints
2. combine semantic and keyword retrieval
3. retrieve a larger candidate pool
4. rerank to the smaller answer set
5. answer with both current signals and relevant historical context

## Target parameters

- semantic plus keyword retrieval mix
- top_k around 20 before rerank
- answer context around top 3 to 5 items after rerank
- minimum score threshold around 0.70 to 0.78

## Query patterns the KB should serve

- time range
- entity tracking
- trend direction
- comparison
- follow-up from previous interest

## Memory linkage

One of the strongest product behaviors is to connect new signals to previous user focus. The KB should make it easy to say:

- this matters because it connects to what you followed last week
- this confirms or weakens a prior trend
- this is new, not just repeated noise
