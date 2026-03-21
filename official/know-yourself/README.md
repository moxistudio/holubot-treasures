# Know Yourself

## Overview

`know-yourself` is an official, user-initiated self-discovery treasure.  
It provides lightweight quiz and reflection flows to help users build clearer self-understanding without turning the experience into a heavy assessment.

This treasure is designed for chat-side personal insight:
- users start it intentionally
- responses remain practical and human
- any profile/memory writeback is gated by explicit consent

## Best For

- "I want to understand my style before a new role/project."
- "Give me a quick MBTI-like check and explain what it means in real life."
- "Summarize what my answers say about communication and decision habits."

## Inputs

- Natural language user request.
- Optional user answers from quiz/reflection rounds.
- Optional prior memory context for continuity (read-only unless user explicitly consents to write).

## Outputs

- Lightweight quiz prompts (short rounds).
- Reflection-guided conversation prompts.
- A concise self-discovery summary (strengths, blind spots, suggested next steps).
- Consent prompt before any profile or long-memory write.

## Tooling

- `llm_call`
- `query_long_memory`
- `send_to_user`

## Quick Try

Prompt examples:
- `我想更了解自己，先从一个轻量测试开始。`
- `给我 6 个问题，看看我的沟通风格。`
- `根据刚才我的回答，帮我写一段“我是什么样的人”的总结。`

## Limitations

- Not a medical/clinical diagnosis tool.
- Accuracy depends on user-provided context and honesty.
- Does not auto-write profile/memory without explicit user consent.
- P0 focuses on lightweight interaction and summary, not deep psychometrics.
