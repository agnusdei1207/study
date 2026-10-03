"""Find `**` bold markers that CommonMark would leave unrendered (flanking rules)."""
import re, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src/content/docs/notes/itpe"

def is_punct(c): return unicodedata.category(c).startswith(("P", "S"))
def is_ws(c): return c == "" or c.isspace()

def scan_line(line):
    line = re.sub(r"`[^`]*`", lambda m: "\0" * len(m.group()), line)  # mask inline code
    toks = []
    for m in re.finditer(r"\*{2,}", line):
        s, e = m.start(), m.end()
        b = line[s - 1] if s else ""
        a = line[e] if e < len(line) else ""
        lf = not is_ws(a) and (not is_punct(a) or is_ws(b) or is_punct(b))
        rf = not is_ws(b) and (not is_punct(b) or is_ws(a) or is_punct(a))
        toks.append((s, e - s, lf, rf))
    stack, bad = [], []
    for t in toks:
        s, n, lf, rf = t
        if n != 2:
            bad.append((s, "3+ asterisks")); continue
        if rf and stack:
            stack.pop(); continue
        if lf:
            stack.append(t); continue
        bad.append((s, "unflanked"))
    bad += [(t[0], "unclosed") for t in stack]
    return bad

def check(path):
    out, fence = [], False
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.lstrip().startswith("```"):
            fence = not fence; continue
        if fence or line.startswith("---") and i < 3: continue
        if re.match(r"^#{1,6}\s.*\*\*", line):
            out.append((i, "bold in heading", line.strip()[:80]))
        for pos, why in scan_line(line):
            out.append((i, why, line.strip()[max(0, pos - 25): pos + 30]))
    return out

if __name__ == "__main__":
    total = 0
    targets = [Path(a) for a in sys.argv[1:]] or sorted(ROOT.rglob("*.md"))
    for p in targets:
        for i, why, ctx in check(p):
            total += 1
            print(f"{p.relative_to(ROOT.parent) if ROOT in p.parents else p}:{i}: {why}: {ctx}")
    print(f"TOTAL {total}", file=sys.stderr)
