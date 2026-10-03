"""Mechanical audit of ITPE notes: structure, front matter, corruption patterns."""
import re, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1] / "src/content/docs/notes/itpe"
issues = collections.defaultdict(list)
for p in sorted(ROOT.rglob("*.md")):
    t = p.read_text(encoding="utf-8")
    rel = f"{p.parent.name}/{p.name}"
    m = re.match(r"---\n(.*?)\n---\n(.*)", t.replace("\r\n", "\n"), re.S)
    if not m: issues["no-frontmatter"].append(rel); continue
    fm, body = m.groups()
    for k in ("title:", "author:", "date:", "badge:", "keyword_grade:", "model:"):
        if k not in fm: issues[f"fm-missing {k}"].append(rel)
    g = re.search(r'text: "(.+?)"', fm); k = re.search(r'keyword_grade: "(.+?)"', fm)
    if g and k and g.group(1) != k.group(1): issues["badge!=grade"].append(rel)
    if g and g.group(1) not in ("기초", "서브", "응용"): issues["bad-badge"].append(rel)
    heads = re.findall(r"^## (.+)$", body, re.M)
    if not heads or not re.match(r"Ⅰ\.", heads[0]) or "개요" not in heads[0]: issues["first-not-개요"].append(rel)
    if not heads or "제언" not in heads[-1]: issues["last-not-제언"].append(rel)
    if len(heads) < 2 or not re.search(r"한계|문제점|해결", heads[-2] if len(heads) > 1 else ""): issues["pre-last-not-한계"].append(rel)
    if re.search(r"\*\* : - \*\*", body): issues["mangled-한계점-bullet"].append(rel)
    if re.search(r"[\t\x08\x0c\x0b\r](?!\n)", body.replace("\r\n","\n")) and re.search(r"[\x08\x0c\x0b]|\times|\tfrac|\tau", body): issues["latex-escape-corruption"].append(rel)
    if re.search(r"\t(imes|ext|heta|ilde|ext|o\b)|\x0c|\x08", body): issues["latex-escape-corruption"].append(rel)
    if "\ufffd" in t: issues["replacement-char"].append(rel)
    if re.search(r"<svg|<div|<style", body): issues["raw-html"].append(rel)
    if re.search(r"private-memory|컴퓨터시스템응용|C:\\|priority|source_status", t): issues["forbidden-public"].append(rel)
    if len(re.findall(r"\*\*", body)) < 6: issues["few-bold-keywords"].append(rel)
for k, v in sorted(issues.items()):
    subj = collections.Counter(x.split("/")[0] for x in set(v))
    print(f"{k}: {len(set(v))} {dict(subj)}")
    if len(set(v)) <= 12: print("   ", sorted(set(v)))
import json; json.dump({k: sorted(set(v)) for k, v in issues.items()}, open(sys.argv[1] if len(sys.argv) > 1 else "audit.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
