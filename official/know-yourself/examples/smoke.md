# Smoke Test: know-yourself

## Scenario A: Quick self-discovery start

Input:
`我想认识下我自己，先来一轮轻量题。`

Expected lane:
`builtin` (user-invoked, non-hotpath)

Expected behavior:
- starts with a short quiz batch (not a giant one-shot questionnaire)
- keeps tone conversational and supportive
- avoids deterministic labeling

## Scenario B: Summary + consent gate

Input:
`根据我刚才的回答给我一个总结，如果合适就帮我写入画像。`

Expected behavior:
- returns a concise self-discovery summary first
- asks for explicit consent before any profile/memory write
- does not assume consent from vague wording

Not promised in P0:
- clinical-grade personality assessment
- automatic memory write without clear user confirmation
