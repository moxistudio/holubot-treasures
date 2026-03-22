# Smoke Test

```bash
treasure-furnace validate https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel
treasure-furnace preview https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel
treasure-furnace install https://github.com/moxistudio/holubot-treasures/tree/main/official/ai-sentinel --runtime-assets-dir /tmp/ai-sentinel-preview
```

After preview or install, validate the package with one or more of the following prompts.

## Scenario A: Daily Brief

```text
给我一份 AI 哨兵日报，聚焦过去 72 小时 AI Agent 和大模型产品动态。
我只想看最重要的 1 条头条、3 条行业动态、1 条技术前沿和本周趋势雷达。
请明确标注来源、置信度，以及哪些信息仍待验证。
```

## Scenario B: Entity Watch

```text
帮我跟踪 OpenAI 最近一周的重要动作。
我不想看泛泛新闻，只看真正影响产品路线、开发者生态或商业竞争格局的变化。
如果有 PR 噪音请直接过滤掉。
```

## Scenario C: Trend Radar

```text
AI 安全这个方向最近是在升温、分化还是降温？
请结合近期事件给出判断，并说明这和 Agent 安全、模型对齐或政策侧有什么关系。
```

## Manual Acceptance Checks

- 输出是否先给结论，再给依据，而不是一大串原始链接。
- 今日头条是否包含 `What's new / Why it matters / 来源 / 置信度`。
- 是否把纯 PR、重复转载、信息过薄的内容剔除或降权。
- 是否对未核实内容明确标记 `待验证`。
- 是否保持手机端 3-5 分钟可读，不出现大段无结构长文。
- 是否在有条件时提示“与你最近关注相关”。
