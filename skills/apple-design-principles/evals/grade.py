#!/usr/bin/env python3
"""Regex grader for evals/evals.json.

Usage: python3 grade.py <iteration-dir>
Expects <iteration-dir>/<config>/<eval-name>.md for each config (e.g. without_skill, old_skill, new_skill).
Writes <iteration-dir>/grading.json and prints a markdown summary.

Check types:
  regex_any          pass if any pattern matches
  regex_all          pass if every pattern matches
  regex_none_in_final pass if no pattern matches, ignoring lines that quote the original draft
                     (lines quoting drafts or meta-commentary: 改前 / Before / Current / 原稿 / 原文 / 改了什么 / 不出现 ...)
Regex checks are a coarse proxy: they confirm a topic is addressed, not that it is addressed well.
"""
import json, re, sys
from pathlib import Path

QUOTE_LINE = re.compile(r"(改前|Before|Current|原稿|原文|现在是|改了什么|不出现|不用「|avoid)")

def run_check(chk, text):
    pats = chk["patterns"]
    t = chk["type"]
    if t == "regex_any":
        hits = [p for p in pats if re.search(p, text)]
        return bool(hits), hits
    if t == "regex_all":
        miss = [p for p in pats if not re.search(p, text)]
        return not miss, (["missing: " + m for m in miss] or ["all matched"])
    if t == "regex_none_in_final":
        final = "\n".join(l for l in text.splitlines() if not QUOTE_LINE.search(l))
        hits = [p for p in pats if re.search(p, final)]
        return not hits, (["found: " + h for h in hits] or ["none found"])
    raise ValueError(t)

def main(it_dir):
    it = Path(it_dir)
    evals = json.load(open(Path(__file__).with_name("evals.json")))["evals"]
    configs = sorted(p.name for p in it.iterdir() if p.is_dir())
    out = {"iteration": it.name, "configs": {}}
    for c in configs:
        res = {}
        for e in evals:
            f = it / c / f"{e['name']}.md"
            if not f.exists():
                continue
            text = f.read_text()
            rows = []
            for chk in e["checks"]:
                ok, ev = run_check(chk, text)
                rows.append({"text": chk["id"], "passed": ok, "evidence": "; ".join(ev)[:200]})
            res[e["name"]] = {"passed": sum(r["passed"] for r in rows), "total": len(rows), "expectations": rows}
        tp = sum(v["passed"] for v in res.values()); tt = sum(v["total"] for v in res.values())
        out["configs"][c] = {"evals": res, "passed": tp, "total": tt, "pass_rate": round(tp / tt, 3) if tt else None}
    (it / "grading.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    names = [e["name"] for e in evals]
    print("| eval | " + " | ".join(configs) + " |")
    print("|---|" + "---|" * len(configs))
    for n in names:
        cells = []
        for c in configs:
            r = out["configs"][c]["evals"].get(n)
            cells.append(f"{r['passed']}/{r['total']}" if r else "-")
        print(f"| {n} | " + " | ".join(cells) + " |")
    print("| **total** | " + " | ".join(f"**{out['configs'][c]['passed']}/{out['configs'][c]['total']} ({out['configs'][c]['pass_rate']:.0%})**" for c in configs) + " |")

if __name__ == "__main__":
    main(sys.argv[1])
