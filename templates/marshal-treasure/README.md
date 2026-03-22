# marshal-treasure template

Use this template for production Treasures that run as a multi-step pipeline.

## Good Fit

- reporting Treasures (for example `weekly-report`)
- workflow orchestration with staged outputs
- operations summaries that require stable formatting

## Customize

1. Copy and rename to a hyphenated Treasure ID, for example `weekly-report-helper`.
2. Update `pack.yaml` metadata and activation hints.
3. Tailor each runtime step:
   - collection
   - outline or analysis
   - final output
4. Align `SKILL.md` constraints to your governance and quality requirements.
5. Replace `examples/smoke.md` with your production-like input sample.

## Local Validation

```bash
treasure-furnace validate community/weekly-report-helper
treasure-furnace preview community/weekly-report-helper/SKILL.md
treasure-furnace install community/weekly-report-helper/SKILL.md --runtime-assets-dir /tmp/treasure-preview-assets
```

Use `examples/smoke.md` as the manual production-like check after preview or install.

## Example Treasure IDs

- `weekly-report`
- `ops-digest`
