# Deep Search

## Overview

`deep-search` 是官方研究型 Treasure 样板，面向“需要联网调研和结构化结论”的中事任务。它基于 SDR v2 提供六种路由模式：`flash`、`quick`、`standard`、`deep`、`pro`、`status`，可以在速度、深度和跟踪能力之间做平衡。

## Lane

- Recommended lane: `medium`
- Route family: Nimbus research chain
- Not for hotpath: 默认不参与聊天热路径激活

## Dependencies

- Built-in tools:
  - `sdr_flash`
  - `sdr_research`
  - `sdr_status`
  - `llm_call`
  - `send_to_user`
- Runtime assumptions:
  - 可用的 SDR 检索与研究后端
  - 研究任务状态查询能力（`job_id`）

## Simplest Invocation

最短调用示例：

```text
/research 帮我快速梳理一下 2026 年 3 月 AI Agent 基础设施趋势，给出结论和来源
```

或自然语言触发：

```text
帮我深度研究一下某行业最近一周的关键变化
```

## Output Style

默认输出为结构化研究答复，优先包含：

1. 一句话结论或当前状态
2. 关键发现
3. 关键来源
4. 待验证
5. 任务编号与产物文件（若存在）
6. 下一步建议

## Limitations

- 该 Treasure 侧重“研究组织与来源呈现”，不保证外部信息绝对真值。
- 当请求是状态查询但未提供 `job_id` 时，只会提示补充，不会臆造进度。
- `flash` 模式为短答，不覆盖深度尽调所需的全部维度。
- 不直接暴露上游 JSON、内部步骤或调度细节。
