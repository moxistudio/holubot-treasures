# basic-treasure template

Use this template when you want a minimal Treasure with a single straightforward response flow.

## Good Fit

- quick helper Treasure
- summarization or rewrite assistant
- format conversion helper

## Customize

1. Copy this directory and rename it to your Treasure ID (hyphenated), for example `email-polisher`.
2. Update `pack.yaml` fields under `meta`, `activation`, and runtime prompt text.
3. Update `SKILL.md` constraints to match your domain.
4. Replace `examples/smoke.md` with your own test request and expected behavior.

## Local Validation

```bash
treasure-furnace validate community/email-polisher
treasure-furnace preview community/email-polisher/SKILL.md
treasure-furnace install community/email-polisher/SKILL.md --runtime-assets-dir /tmp/treasure-preview-assets
```

Use `examples/smoke.md` as the manual request/expected-output checklist after preview or install.

## Example Treasure IDs

- `deep-search`
- `weekly-report-helper`
