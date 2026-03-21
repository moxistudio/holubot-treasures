# Smoke Example: Weekly Report

## Input

```text
请写“给老板看的汇报版”周报。
本周素材：
- A 客户：提案二轮收口，客户确认主线方向，待法务走合同补充条款
- B 项目：投放素材过审，排期已锁定，下周一上线
- C 项目：预算未最终确认，影响下周投放节奏
```

## Expected Lane

`large`（Marshal weekly worker control plane）

## Expected Output Style

- 仅输出一个版本：老板汇报版
- 固定四段：本周总结 / 已完成事项 / 进行中事项 / 下周计划
- 事项按客户/项目归组，不按周一到周五流水账
- 风险项至少体现来源与影响，最好附待协调动作
- 信息不足处使用“待补充”

## Non-Goals

- 不生成多个口径版本混排
- 不在缺证据时虚构数据或结果
- 不把“沟通/开会/跟进”直接当成果输出
