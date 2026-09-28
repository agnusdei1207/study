from pathlib import Path
import re

dir_path = Path("src/content/docs/notes/itpe/02-software-engineering")
files = sorted(dir_path.glob("*.md"))

print(f"Total files: {len(files)}")
report = []

for f in files:
    if f.name == "index.md":
        continue
    text = f.read_text(encoding="utf-8")
    issues = []
    
    # 1. Check diagram block widths and decorative boxes
    blocks = re.findall(r"```text\s*\n(.*?)\n```", text, re.DOTALL)
    for i, b in enumerate(blocks):
        lines = b.splitlines()
        max_len = max((len(l) for l in lines), default=0)
        if max_len > 85:
            issues.append(f"Block {i+1} wide ({max_len} chars)")
        if any(re.match(r"^\s*\+[-=]{10,}\+\s*$", l) for l in lines):
            issues.append(f"Block {i+1} decorative box border")
        if any(re.match(r"^\s*[├└]─", l) for l in lines):
            # check how many dir tree lines
            cnt = sum(1 for l in lines if re.match(r"^\s*[├└]─", l))
            if cnt >= 3:
                issues.append(f"Block {i+1} dir-style tree ({cnt} lines)")

    # 2. Check Ⅵ proposal diagram count and table
    ans_start = text.find("## 2~4교시 25점 답안")
    if ans_start != -1:
        ans = text[ans_start:]
        sec6_match = re.search(r"## Ⅵ\.\s*제언\s*([\s\S]*?)(?=## 출제 이력|$)", ans)
        if sec6_match:
            sec6_text = sec6_match.group(1)
            sec6_diagrams = len(re.findall(r"```text\s*$", sec6_text, re.M))
            if sec6_diagrams == 0:
                issues.append("Ⅵ no diagram")
            sec6_table = bool(re.search(r"\|[^\n]+\|\r?\n\|", sec6_text))
            if not sec6_table:
                issues.append("Ⅵ no comparison table")

    # 3. Check verbal endings (다, 함/됨)
    for line in text.splitlines():
        if line.strip().startswith(("#", ">", "-", "|", "`", "*", "<")):
            continue
        if re.search(r"다\.\s*$", line.strip()):
            issues.append(f"ends with 다: '{line.strip()[:30]}'")
            break

    if issues:
        report.append((f.name, issues))

print(f"\nFiles with findings: {len(report)} / {len(files)-1}")
for name, iss in report:
    print(f"{name}: {', '.join(iss)}")
