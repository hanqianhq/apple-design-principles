# Apple-style Design Principles

[中文说明](README.zh-CN.md)

An [Agent Skill](https://agentskills.io) for reviewing and writing product plans, app and web UI, UX copy, and landing-page or keynote copy the way Apple tends to: focus first, then hierarchy, then detail, and every critique comes with a fix. Works in English and Chinese.

It covers:

- **Routing.** It works out whether a screen is meant to persuade (marketing), operate (app, SaaS, admin tool) or be read (docs), and which platform it targets, then applies the matching checklist and units (iOS pt + HIG, or Web CSS px + WCAG 2.2).
- **Checklists** for iOS, Web (WCAG 2.2, checked against the W3C text), and tool/SaaS UI: data truthfulness, count and pagination consistency, destructive actions, long tasks, billing transparency, permissions, glossary, asset references, and whether the marketing promise matches what the product can do.
- **UX writing**: buttons, status, empty states, errors, confirmation dialogs, notifications, settings.
- **Marketing copy**: product-page structure, headline patterns, keynote structure, Chinese–English transcreation.
- **A spec snapshot**: version-sensitive numbers (HIG sizes, WCAG values, Liquid Glass), each with the date it was checked.

## Install

### Claude Code (plugin marketplace)

```text
/plugin marketplace add hanqianhq/apple-design-principles
/plugin install apple-design-principles@apple-design-principles
```

From a shell: `claude plugin marketplace add hanqianhq/apple-design-principles`.

### Any agent, via the `skills` CLI ([vercel-labs/skills](https://github.com/vercel-labs/skills))

```bash
npx skills add hanqianhq/apple-design-principles                 # interactive
npx skills add hanqianhq/apple-design-principles -a claude-code -g # Claude Code, user-wide
npx skills add hanqianhq/apple-design-principles -a cursor -a codex
```

### Manual copy

Copy the folder `skills/apple-design-principles/` (the whole folder, not just `SKILL.md`) into one of these:

| Agent | Project | User-wide |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Cursor | `.agents/skills/` or `.cursor/skills/` | `~/.cursor/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |

```bash
git clone https://github.com/hanqianhq/apple-design-principles
cp -r apple-design-principles/skills/apple-design-principles ~/.claude/skills/
```

### Claude.ai / Claude app

Zip the `skills/apple-design-principles/` folder and upload it as a custom skill in Settings. The frontmatter uses only standard fields, so the upload is accepted.

## Try it

- "Review this settings screen like an Apple designer. Give me P0/P1/P2 issues and fixes."
- "Our pricing page feels cluttered. What should we cut?"
- "Rewrite these error messages: 'Error 500', 'Operation failed'."
- "How big should buttons be on iOS and on the web? Cite the source."
- "把这段产品介绍改成发布会风格，中英文各一版。"
- "这个后台工具页帮我按苹果式标准审一遍。"

## Structure

```text
.claude-plugin/          plugin.json, marketplace.json (Claude Code)
skills/apple-design-principles/
  SKILL.md               routing, checklist, priority table, output template, example, index
  references/            loaded on demand (principles, checklists, writing, specs, sources...)
  assets/                review report template
  evals/                 test prompts, trigger queries, grader, results
```

## Evals

`skills/apple-design-principles/evals/` holds 7 test prompts and 20 trigger queries. In the bundled run, v2.0.0 scored 53/53 on regex checks, against 42/53 for v1 and 35/53 with no skill. **Those numbers come from a single, non-blind, self-graded run.** See [evals/README.md](skills/apple-design-principles/evals/README.md) for the method and its limits.

## Sources and accuracy

Numbers from Apple HIG and WCAG 2.2 were checked against the original pages on 2026-10-09 and are linked in `references/spec-snapshot.md` and `references/sources.md`. Standards change, so check the current Apple Human Interface Guidelines and [WCAG](https://www.w3.org/TR/WCAG22/) before relying on a number.

## License

[CC BY 4.0](LICENSE). You can share and adapt the material, including commercially, as long as you give attribution.

## Disclaimer

This project is not affiliated with, endorsed by, or sponsored by Apple Inc. Apple, iPhone, iPad, Mac, Apple Watch, SF Pro, Liquid Glass and other marks are trademarks of Apple Inc., registered in the U.S. and other countries. All examples are original and use fictional products. No Apple copy or assets are reproduced; the skill only distills methods and principles, with sources cited.
