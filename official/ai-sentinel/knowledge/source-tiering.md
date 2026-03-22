# Source Tiering

## Default tiers

| Tier | Source class | Weight | Update cadence | Default handling |
| --- | --- | --- | --- | --- |
| Tier 1 | Official company releases, research pages, major conferences, first-party papers | 0.95-1.0 | 5-15 min | prioritize and auto-ingest |
| Tier 2 | Authority tech media, analyst reports, trusted vertical outlets | 0.80-0.95 | daily | review and ingest |
| Tier 3 | GitHub trends, technical communities, practitioner discussions | 0.60-0.80 | hourly | monitor and machine-triage |
| Tier 4 | Social signals, rumor channels, weak early signals | 0.40-0.60 | real-time | strict filter only |

## Recommended MVP source families

### Research and papers

- arXiv AI-relevant tracks
- NeurIPS, ICLR, ICML, ACL official pages

### International official vendors

- OpenAI
- Anthropic
- Google DeepMind
- Meta AI / FAIR
- Microsoft Research
- xAI
- Mistral
- Cohere

### Open ecosystem and events

- GitHub Trending
- GDELT
- Event Registry

### China local ecosystem

- 机器之心
- 新智元
- 量子位
- 36氪 AI
- 虎嗅
- 钛媒体

## Collection rules

- Start with 30-50 high-quality sources, not maximal breadth.
- Favor free or low-cost feeds in MVP.
- Review source drift every quarter.
- Keep a clear allowlist and do not let Tier 4 dominate the brief.

## Risks to watch

- English- and China-heavy coverage can miss Europe, Japan, and Korea.
- Paid sources can distort MVP cost if adopted too early.
- China deployment must favor lawful, attributable sources.
