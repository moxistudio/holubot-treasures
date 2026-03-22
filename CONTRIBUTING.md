# Contributing To holubot-treasures

Thanks for helping grow the Treasure ecosystem.

This document explains the minimum bar for a PR in P0: clear structure, installable package metadata, a usable `SKILL.md`, and a smoke example.

## Directory Structure

Use one Treasure per directory.

For community submissions, place your Treasure under:

```text
community/<your-treasure-id>/
├── pack.yaml
├── SKILL.md
├── README.md
└── examples/
    └── smoke.md
```

Use a hyphenated ID, for example `customer-brief` or `weekly-report-helper`.

## Minimum `pack.yaml` Expectations

Your `pack.yaml` should be concise but complete enough to validate and install.

Minimum expected fields in P0:

```yaml
meta:
  id: your-treasure-id
  name: Your Treasure Name
  kind: treasure
  version: 0.1.0
  description: One-line value statement
  api_version: holubot.treasure/v1

skill:
  entry: SKILL.md

runtime:
  kind: nimbus
```

Also expected in realistic submissions:

- activation hints (`trigger_keywords`, `intents`)
- tool declarations (`tools.builtin`, optional MCP dependencies)
- governance constraints (`forbidden_tools`, trust level)
- at least one runnable step or execution path

## Minimum `SKILL.md` Expectations

Your `SKILL.md` should include:

1. front matter with `name`, `description`, and tool hints
2. clear scope of what the Treasure does
3. behavioral constraints (what it must not do)
4. output style expectations for users

Keep it focused and runnable. Avoid only writing product copy or marketing text.

## Local Validation (P0 Workflow)

Current P0 checks should match CI intent and the standalone `treasure-furnace` toolchain.

Example commands:

```bash
# 1) catalog schema check
python scripts/validate_catalog.py catalog.yaml

# 2) repository treasure directory check
python scripts/validate_treasures.py catalog.yaml

# 3) package compile and manifest validation
treasure-furnace validate community/<your-treasure-id>

# 4) preview the imported behavior before install
treasure-furnace preview community/<your-treasure-id>/SKILL.md

# 5) optional install dry run into a temp runtime assets directory
treasure-furnace install community/<your-treasure-id>/SKILL.md --runtime-assets-dir /tmp/treasure-preview-assets
```

Keep `examples/smoke.md` as the manual smoke scenario reviewers should check after preview/install. There is no dedicated `smoke` subcommand in the current P0 CLI.

## Pull Request Expectations

A good PR includes:

1. one Treasure per PR
2. complete directory structure
3. passing local validation checks
4. short explanation of the user problem solved
5. whether you are requesting `verified` review

Recommended PR body checklist:

- Treasure ID:
- Treasure type: `basic` / `knowledge` / `marshal`
- Includes knowledge files: yes/no
- Local validation completed: yes/no
- Request `verified` review: yes/no

## What Will Not Be Accepted

The following are rejected in P0:

- missing `pack.yaml` or `SKILL.md`
- non-installable or structurally invalid Treasure directories
- “Treasure” submissions that are only docs with no runnable package intent
- obvious unsafe behavior (credential exfiltration, destructive file actions, hidden shell execution)
- copied proprietary content without permission
- low-effort spam or SEO-only directories

## Review Notes For `verified`

`verified` is controlled by maintainers and reflects passing the minimum quality gate.

`verified` in P0 does not imply security certification, expert endorsement, or guaranteed business outcomes.
