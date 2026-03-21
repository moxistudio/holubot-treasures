# Community Treasure Submissions

This directory is the public submission area for community-built Treasures.

## Where To Submit

Create your Treasure in:

```text
community/<your-treasure-id>/
```

Use a hyphenated ID (for example `meeting-notes` or `weekly-report-helper`).

## Minimum Directory Layout

```text
community/<your-treasure-id>/
├── pack.yaml
├── SKILL.md
├── README.md
└── examples/
    └── smoke.md
```

## `verified` vs regular community Treasures

- regular community Treasure: accepted structure, visible in repo/catalog scope, not yet marked as `verified`
- `verified` community Treasure: passed the P0 minimum gate (structure, installability, smoke check, and governance baseline)

`verified` is a maintainer decision and is binary in P0.

## Submission Flow

1. Fork the repository.
2. Add your Treasure under `community/<your-treasure-id>/`.
3. Run local validation checks (see `CONTRIBUTING.md`).
4. Open a PR with your Treasure summary and checklist.
5. Address CI or review feedback.

## Not Accepted In `community/`

- directories without `pack.yaml` and `SKILL.md`
- non-runnable placeholder-only submissions
- hidden credential collection or destructive tool behavior
- malware, policy-violating, or deceptive content
- copyrighted material without reuse rights
