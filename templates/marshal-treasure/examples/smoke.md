# Smoke Test: marshal-treasure

Treasure ID used in this test: `weekly-report-helper`

## Input

```text
Create this week's report from team activity logs. Keep it short and include: outcomes, in-progress, risks, next actions.
```

## Expected Checks

1. output has all requested sections
2. each section is actionable and concise
3. missing data is explicitly marked, not fabricated
4. report remains stable in structure across repeated runs

## Suggested Local Check

```bash
treasure-furnace preview community/weekly-report-helper/SKILL.md
treasure-furnace install community/weekly-report-helper/SKILL.md --runtime-assets-dir /tmp/treasure-preview-assets
```

After preview or install, use the input and checks below as your manual smoke scenario.
