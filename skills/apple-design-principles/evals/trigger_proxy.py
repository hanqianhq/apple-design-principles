"""Lexical trigger proxy: how well does a description separate should-trigger
from should-not-trigger queries? Threshold-free (reports AUC).

This is NOT how an agent decides to load a skill (that is a model judgment);
it only shows whether the description contains the vocabulary users actually type.
Usage: python3 trigger_proxy.py OLD_SKILL.md NEW_SKILL.md
"""
import json, re, sys, pathlib

STOP = set("a an the and or for of to in on with our is it this that these my me can you please do how what are as be by at from your so just also".split())

def desc(path):
    t = pathlib.Path(path).read_text(encoding="utf-8")
    fm = t.split("---")[1]
    m = re.search(r"description:\s*>?-?\s*\n?(.*?)(\n[a-z_]+:|\Z)", fm, re.S)
    return " ".join(m.group(1).split())

def feats(s):
    s = s.lower()
    en = {w for w in re.findall(r"[a-z][a-z\-]+", s) if w not in STOP and len(w) > 2}
    en = {w[:-1] if w.endswith("s") else w for w in en}           # crude plural folding
    zh = set()
    for run in re.findall(r"[\u4e00-\u9fff]+", s):
        zh |= {run[i:i+2] for i in range(len(run) - 1)}
    return en | zh

def score(q, d):
    fq = feats(q)
    return len(fq & feats(d)) / (len(fq) ** 0.5 or 1)

def auc(pos, neg):
    pairs = [(p > n) + 0.5 * (p == n) for p in pos for n in neg]
    return sum(pairs) / len(pairs)

qs = json.load(open(pathlib.Path(__file__).with_name("trigger-queries.json"), encoding="utf-8"))["queries"]
rows, out = [], {}
for label, path in (("old", sys.argv[1]), ("new", sys.argv[2])):
    d = desc(path)
    sc = {q["id"]: round(score(q["query"], d), 3) for q in qs}
    pos = [sc[q["id"]] for q in qs if q["should_trigger"]]
    neg = [sc[q["id"]] for q in qs if not q["should_trigger"]]
    out[label] = {"description_chars": len(d), "auc": round(auc(pos, neg), 3),
                  "zero_overlap_positives": [q["id"] for q in qs if q["should_trigger"] and sc[q["id"]] == 0],
                  "scores": sc}
print(json.dumps(out, ensure_ascii=False, indent=1))
