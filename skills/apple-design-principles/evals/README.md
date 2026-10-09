# Evals

Method follows the agentskills.io guide "Evaluating skills": the same prompts are run with and without the skill, then graded against assertions.

## Files
- `evals.json`: 7 test prompts (iOS settings review, web landing hero, web tool / SaaS review, UX copy for empty state / error / dialog / notification, product page + keynote copy, CN localization, iOS vs Web specs). Each has `expected_output`, human-readable `assertions`, and machine-gradable `checks` (53 in total). All products are fictional.
- `trigger-queries.json`: 20 queries (10 should trigger, 10 near-miss should not), mixed Chinese and English.
- `grade.py`: regex grader. `python3 grade.py results/iteration-N` writes `grading.json` and prints a table.
- `trigger_proxy.py`: lexical trigger proxy (AUC between should / should-not queries).
- `results/iteration-1/`: baseline. `without_skill` (no skill) and `old_skill` (v1.0 single-file SKILL.md).
- `results/iteration-2/`: `new_skill` (v2.0.0) plus copies of the baselines, `grading.json`, `benchmark.md`.
- `results/trigger-judgment.md`, `results/trigger-proxy.json`: trigger test.

## Results (2026-10-09)

| Eval | v2.0.0 | v1 | no skill |
|---|---|---|---|
| iOS settings review | 8/8 | 8/8 | 5/8 |
| Web landing hero | 7/7 | 4/7 | 4/7 |
| Web tool / SaaS review | 10/10 | 8/10 | 8/10 |
| UX copy (empty / error / dialog / notification) | 8/8 | 8/8 | 6/8 |
| Product page + keynote | 7/7 | 7/7 | 5/7 |
| Localization | 5/5 | 5/5 | 4/5 |
| iOS vs Web specs | 8/8 | 2/8 | 3/8 |
| **Total** | **53/53 (100%)** | **42/53 (79%)** | **35/53 (66%)** |

## Limitations (read before quoting the numbers)
- **Not blind, not independent.** One author wrote the evals, the skill, and all 21 outputs, and knew the checks while writing. No separate model or human produced or graded the outputs; there was no agent CLI on the build machine.
- **Single run per configuration.** No variance estimate.
- **Regex checks test topic coverage, not quality.** A check passes if, for example, "2.5.8" and "24×24" appear; it cannot tell whether the advice is well written or correct in context.
- **Ceiling effect.** v2 scores 100%, so the evals no longer discriminate at the top; harder evals are needed.
- **Checks were widened after the first baseline run** (to fix false negatives), before any v2 output existed. The changes are listed in `evals.json` → `grading_changelog`.
- **Where v2 genuinely differs:** v1 had no Web / WCAG numbers (cross-platform 2/8, web hero 4/7) and no tool-UI checklist (v1 output missed undo/trash for destructive actions and background progress for long tasks). These gaps are structural, not an artifact of grading.

To get trustworthy numbers, rerun each prompt in a fresh agent session (with and without the skill installed), have a different person or model grade blind against `assertions`, and run several times.
