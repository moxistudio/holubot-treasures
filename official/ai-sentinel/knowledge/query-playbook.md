# Query Playbook

## Typical query modes

1. Time range: "上个月 AI Agent 有什么重要进展"
2. Entity watch: "OpenAI 最近在干什么"
3. Trend radar: "AI 安全是在升温还是降温"
4. Compare: "Claude 和 GPT 在 coding 上有什么差异"
5. Follow-up: "这和我上周研究的 Agent 安全有什么关系"

## Retrieval posture

- 70% semantic vector match
- 30% keyword match
- retrieve top_k=20
- rerank to top 3-5
- keep a minimum score threshold around 0.7-0.78

## Latency goal

Users care more about speed than exhaustive recall in the first pass. The practical target is under 1 second for query response startup.

## Query rewriting

Natural-language questions should be rewritten into structured search hints when needed:

- time window
- entity list
- topic list
- comparison axis
- intended audience

## Memory linkage

If the user recently cared about a topic, relevant new signals should be labeled as connected to that prior interest rather than surfaced as isolated news.
