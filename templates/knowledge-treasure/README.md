# knowledge-treasure template

Use this template for Treasures that must search and cite knowledge context before answering.

## Good Fit

- policy and process Q&A
- domain research with references
- support knowledge helpers

## Required Extra Inputs

Add at least one knowledge source path used by your Treasure, for example:

- `knowledge/`
- `source/references/`
- `source/assets/`

## Customize

1. Copy and rename this directory to a hyphenated Treasure ID, for example `support-policy`.
2. Update `pack.yaml` metadata and activation intent.
3. Adjust `knowledge.source_dirs` to your real data layout.
4. Tune the prompt in `runtime.steps.compose_answer`.
5. Replace `examples/smoke.md` with a domain-relevant test.

## Local Validation

```bash
treasure-furnace validate community/support-policy
treasure-furnace preview community/support-policy/SKILL.md
treasure-furnace install community/support-policy/SKILL.md --runtime-assets-dir /tmp/treasure-preview-assets
```

Use `examples/smoke.md` as the manual scenario checklist after preview or install.

## Example Treasure IDs

- `deep-search`
- `ai-sentinel-briefing`
