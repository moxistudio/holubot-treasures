# Super Office

## Overview

`super-office` is an official medium-lane Office treasure for practical document execution:
- read and extract from attachments
- fill templates
- handle spreadsheets with structured maps
- generate docx/xlsx deliverables

It is designed for requests like "help me sort this attachment" or "fill this template and produce a final file" without requiring a multi-worker pipeline.

## Best For

- Attachment reading and quick extraction.
- DOCX template filling from structured fields.
- Spreadsheet cell updates from explicit mapping.
- Report deliverable generation in `docx` or `xlsx`.

## Inputs

- File references through `file_ref`, `path`, or `uri`.
- For template filling:
  - `template_ref` / `template_path` / `template_uri`
  - `field_map`
  - optional `mode` (`table_row2`)
- For sheet filling:
  - workbook reference/path
  - `cell_map`
- For report generation:
  - `report_type` (`docx` or `xlsx`)
  - template or source reference + structured data map

## Outputs

- Action decision and readiness status.
- Clear missing-input guidance when contracts are incomplete.
- Deliverable summary with output path when available.

## Tooling

- `read_document`
- `fill_template`
- `fill_sheet`
- `generate_report`
- `llm_call`
- `send_to_user`
- MCP dependency: `office-fill-mcp`

## Quick Try

Prompt examples:
- `读下这个附件，帮我提取关键结论。`
- `用这个模板和字段表帮我生成一版 docx。`
- `按这个 cell_map 更新 xlsx 并给我输出文件路径。`
- `基于模板和数据，生成 xlsx 报告。`

## Limitations

- Current P0/PB scope is document reading, template filling, sheet filling, and docx/xlsx report generation.
- PPT generation is not promised in this package.
- Complex layout fidelity depends on template quality and Office tool behavior.
- Missing refs/maps will stop execution and return explicit next-step requirements.
