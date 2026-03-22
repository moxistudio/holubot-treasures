# holubot-treasures

`holubot-treasures` is the official GitHub-based distribution and discovery layer for HoluBot Treasures.

In P0, this repository is intentionally simple: a catalog, official starter Treasures, community submissions, templates, and a minimum validation gate so low-quality packages do not flood the ecosystem.

## What Is A Treasure?

A Treasure is a pluggable capability pack for HoluBot.

Each Treasure ships with:

- `pack.yaml` for metadata and runtime routing
- `SKILL.md` for behavior and usage constraints
- optional examples, assets, and knowledge files

## What This Repository Is For

This repository is for:

- Discovering Treasures through `catalog.yaml`
- Installing Treasures through HoluBot or `treasure-furnace`
- Reviewing official and community Treasure examples
- Contributing new Treasures with a shared template and quality baseline

This repository is not for:

- HoluBot core chat runtime development
- complex payment backend implementation
- recommendation and ranking algorithms in P0

## Quick Install (Examples)

Use hyphenated Treasure IDs from the catalog, for example `deep-search` and `weekly-report`.

```bash
# Example 1: install an official Treasure from its repository URL
treasure-furnace install https://github.com/moxistudio/holubot-treasures/tree/main/official/deep-search

# Example 2: install another official Treasure from the same repository
treasure-furnace install https://github.com/moxistudio/holubot-treasures/tree/main/official/weekly-report
```

Inside HoluBot chat (example):

```text
/install deep-search
```

## Official Treasures (P0)

- `know-yourself`
- `deep-search`
- `super-office`
- `weekly-report`
- `ai-sentinel` (kept in official planning; not prioritized in the current bundled-only demo line)

## Contribute A Treasure

Start with:

- `templates/basic-treasure/`
- `templates/knowledge-treasure/`
- `templates/marshal-treasure/`

Then follow [CONTRIBUTING.md](CONTRIBUTING.md) for structure, current P0 validation commands, and pull request expectations.

Community submission area: `community/` (see `community/README.md`).

## What `verified` Means In P0

P0 uses binary verification only:

- `verified: true`
- `verified: false`

`verified: true` means the Treasure passed minimum repository gates:

1. structure is valid
2. package can be installed
3. smoke example can run at minimum level
4. no obvious governance boundary violations

In P0, `verified` does not mean expert endorsement, perfect safety, best-in-class quality, or commercial guarantees.

## Repository Layout (P0)

```text
holubot-treasures/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── catalog.yaml
├── official/
├── community/
└── templates/
```
