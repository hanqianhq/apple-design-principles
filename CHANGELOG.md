# Changelog

## [2.0.0] - 2026-10-09

Restructured to follow the Agent Skills standard (agentskills.io) and progressive disclosure.

### Changed
- `name` is now `apple-design-principles` (lowercase, hyphenated, matches the folder). v1 used a Chinese name, which is not valid under the spec.
- New description: English first, Chinese trigger words, out-of-scope cases, no workflow summary.
- `SKILL.md` went from 806 lines (~21k tokens) to under 150 lines (~3.4k tokens). It now holds only routing, a review checklist, a priority table, an output template, one example and an index of references.
- Former sections A–H moved to `references/`: principles, checklist-ios, philosophy, apple-style-guide, typography-zh, marketing-copy, examples, sources.
- All examples use one format: input → output → why.
- Version-sensitive numbers moved into `references/spec-snapshot.md`, each with a check date.

### Added
- Routing by interface type (Persuade / Operate / Read) × platform × task.
- `references/checklist-web.md`: WCAG 2.2 values checked against the W3C Recommendation and linked per success criterion. Target size 2.5.8 is 24×24 CSS px (AA) and 2.5.5 is 44×44 (AAA).
- `references/checklist-tool-ui.md` for SaaS and admin tools. It covers:
  - data truthfulness, plus count and pagination consistency
  - destructive actions and long tasks
  - billing transparency and permissions
  - a glossary, asset references, and whether the marketing promise matches what the product can do
- `references/platform-mapping.md`: iOS ↔ Web values and mechanisms, each marked as requirement, enhanced or convention.
- `references/ux-writing.md` covering buttons, status, empty states, errors, confirmation dialogs, notifications, settings, a glossary template and a filler-word list.
- `assets/review-report-template.md`.
- `evals/`:
  - 7 test prompts, a regex grader and 20 trigger queries
  - baseline and v2 results, with the limitations written up
- Claude Code plugin packaging (`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`).
- English and Chinese READMEs, and a CC BY 4.0 LICENSE.

### Removed
- Root-level `SKILL.md`. The skill now lives in `skills/apple-design-principles/`.

## [1.0.0]
- First release: a single-file Chinese handbook (sections A–H).
