---
name: New Treasure Proposal
about: Propose a new official/community Treasure for catalog onboarding.
title: "[New Treasure] <treasure-id>"
labels: ["new-treasure"]
assignees: []
---

## Treasure Basic Info

- Treasure name:
- Treasure id (hyphenated, e.g. `deep-search`):
- Target owner:
  - [ ] official
  - [ ] community
- Treasure type/category (e.g. profile/research/office/work/radar/knowledge):
- Lane:
  - [ ] small
  - [ ] medium
  - [ ] large

## Scope And Value

- What user problem does this Treasure solve?
- Why should this be listed in `holubot-treasures` now?

## Structure Checklist

- [ ] `pack.yaml` is prepared
- [ ] `SKILL.md` is prepared
- [ ] `README.md` is prepared
- [ ] `examples/smoke.md` is prepared

## Knowledge And Demo

- Includes knowledge base?
  - [ ] no
  - [ ] yes
- If yes, where is the knowledge source?
- Is this demo-ready now?
  - [ ] yes
  - [ ] no

## Validation And Verification

- Local validation command and result:
  - `python scripts/validate_catalog.py catalog.yaml`
  - `python scripts/validate_treasures.py catalog.yaml`
- Request `verified` status?
  - [ ] yes
  - [ ] no

## Extra Notes

- Dependencies, constraints, or rollout notes:
