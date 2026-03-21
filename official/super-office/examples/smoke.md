# Smoke Test: super-office

## Scenario A: Attachment reading + template fill

Input:
`帮我读一下这个合同摘要，再把甲方信息填进这个 docx 模板。`

Expected lane:
`nimbus` (medium-lane office execution)

Expected behavior:
- routes to `read_document` then `fill_template` style execution guidance
- requests missing `template_ref/template_path/template_uri` or `field_map` if absent
- returns a practical next-step list, not vague chat advice

## Scenario B: Spreadsheet handling + deliverable generation

Input:
`按这个 cell_map 更新预算表，然后生成一版 xlsx 报告。`

Expected behavior:
- validates sheet inputs (`workbook ref/path`, `cell_map`)
- uses `fill_sheet` and `generate_report` scope for xlsx output
- provides output path or actionable fallback

## Scenario C: Out-of-scope request guard

Input:
`直接给我生成一版 PPT 演示文稿。`

Expected behavior:
- clearly states PPT generation is unsupported in current P0 scope
- offers closest supported alternatives (docx/xlsx deliverable or markdown draft)

Not promised in P0:
- PPT generation
- guaranteed perfect visual layout replication across all templates
