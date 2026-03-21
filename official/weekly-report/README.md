# Weekly Report

## Overview

`weekly-report` 是官方 Marshal 型周报产线 Treasure 样板，用于把工作日志、项目碎片和长期记忆整理为稳定可交付周报。它先做结构化材料归组，再输出单一口径周报，适合“大事链路”而非聊天热路径。

## Lane

- Recommended lane: `large`
- Route family: Marshal worker control plane
- Default entry: 显式周报意图触发，不默认常驻聊天热路径

## Dependencies

- Built-in tools:
  - `query_work_logs`
  - `query_long_memory`
  - `knowledge_search`
  - `llm_call`
  - `send_to_user`
- Knowledge pack:
  - `knowledge/writing-guardrails.md`
- Related ecosystem expectations:
  - 典型部署会优先走低成本 CLI 后端（如 `opencode`），必要时可升档到 `codex`、`claude code`、`qwen code`、`openclaw`
  - 可预留调用 `deep-search` 与 `super-office` 作为子 Treasure（P0 样板仅保留合同占位，不在包内实现调用协议）

## Simplest Invocation

最短调用示例：

```text
请基于我这周日志写一版周报，给老板看的汇报版。
```

带最小上下文输入示例：

```text
本周做了 A 客户提案二轮收口，B 项目素材已过审待上线，C 项目预算还没确认。
请整理为带风险和下周计划的详细版周报。
```

## Output Style

稳定输出四段结构：

1. 本周总结
2. 已完成事项
3. 进行中事项
4. 下周计划

并遵循：

- 只输出一个口径版本（concise / boss / detailed）
- 优先按客户/项目归组
- 风险描述尽量含“来源 + 影响 + 待协调项”
- 信息不足时标记“待补充”

## Limitations

- 来源可追溯不等于自动真值验证，仍需人工对关键事实做最终确认。
- 若输入材料不足，输出会保留“待补充”，不会编造业务细节。
- P0 样板聚焦稳定文本产线，暂不包含完整模板填充与自动子 Treasure 编排实现。
- 质量强依赖工作日志与项目碎片的可读性和完整度。
