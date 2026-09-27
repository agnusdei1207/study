"""Report structural gaps in ITPE topic notes without changing content.

This checks required sections and diagrams. It cannot judge whether a diagram
accurately explains the topic; that still needs editorial review.
"""

from collections import Counter
from pathlib import Path
import argparse
import re


ROOT = Path(__file__).resolve().parents[1] / "src/content/docs/notes/itpe"
SECOND_ANSWER = "## 2~4교시 25점 답안"
INSIGHT_LABELS = ("본질", "메커니즘", "통찰")
ROMAN_SECTION = re.compile(r"^#{2,3}\s+([ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ])\.\s*(.+)$", re.M)
TEXT_DIAGRAM = re.compile(r"^```text\s*$", re.M)


def section(text: str, start: str, end: str | None = None) -> str:
    if start not in text:
        return ""
    value = text.split(start, 1)[1]
    return value.split(end, 1)[0] if end and end in value else value


def roman_parts(answer: str) -> list[tuple[str, str, str]]:
    matches = list(ROMAN_SECTION.finditer(answer))
    return [
        (match.group(1), match.group(2), answer[match.end() : matches[i + 1].start() if i + 1 < len(matches) else len(answer)])
        for i, match in enumerate(matches)
    ]


def audit(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    findings = []
    recall = section(text, "## 30초 인출", "<details>")
    recall_lines = [line for line in recall.splitlines() if re.match(r"^\s*-\s+", line)]
    recall_labels = {
        line.lstrip("- ").replace("**", "").split(":", 1)[0].strip()
        for line in recall_lines
    }
    if len(recall_lines) != 3:
        findings.append("30초 인출: 본질·메커니즘·통찰 3줄 아님")
    for label in INSIGHT_LABELS:
        if label not in recall_labels:
            findings.append(f"30초 인출: {label} 없음")
    insight = next((line for line in recall.splitlines() if re.match(r"-\s*(?:\*\*)?통찰", line)), "")
    if insight and not re.search(r"한계\s*:.*→\s*방안\s*:", insight):
        findings.append("30초 통찰: 한계→방안 표시 없음")

    if "## 1교시 예상문제" in text or "## 1교시 10점 답안" in text:
        findings.append("1교시 중복 답안 남음")
    second = section(text, SECOND_ANSWER, "## 출제 이력")
    if not second:
        return findings + ["25점 답안 없음"]
    second_parts = roman_parts(second)
    ordered = [number for number, _, _ in second_parts]
    if ordered != ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ"]:
        findings.append("25점 Ⅰ→Ⅱ→Ⅲ→Ⅳ→Ⅴ→Ⅵ 순서 아님")
    by_number = {number: (title, body) for number, title, body in second_parts}
    overview = by_number.get("Ⅰ", ("", ""))
    if "개요" not in overview[0] or not all(f"| {word} |" in overview[1] for word in ("정의", "목적")):
        findings.append("25점 Ⅰ 개요·정의·목적 누락")
    if re.search(r"^```(?:text|mermaid)\s*$", overview[1], re.M):
        findings.append("25점 Ⅰ 중복 도해 남음")
    characteristics = by_number.get("Ⅱ", ("", ""))
    if "특징" not in characteristics[0] and "특성" not in characteristics[0]:
        findings.append("25점 Ⅱ 특징 제목 없음")
    if not characteristics[1].strip():
        findings.append("25점 Ⅱ 특징 내용 없음")
    core = by_number.get("Ⅲ", ("", ""))[1]
    if not TEXT_DIAGRAM.search(core):
        findings.append("25점 Ⅲ text 도해 없음")
    extension = by_number.get("Ⅳ", ("", ""))[1]
    if not (TEXT_DIAGRAM.search(extension) or re.search(r"^\|[^\n]+\|\s*$", extension, re.M)):
        findings.append("25점 Ⅳ 표·도해 없음")
    limits = by_number.get("Ⅴ", ("", ""))
    if "한계" not in limits[0] or "방안" not in limits[0]:
        findings.append("25점 Ⅴ 한계와 방안 제목 없음")
    limit_table = [line.strip() for line in limits[1].splitlines() if line.lstrip().startswith("|")]
    required_header = re.compile(r"^\|\s*한계\s*\|\s*방안\s*\|$")
    valid_limit_table = (
        len(limit_table) >= 3
        and required_header.fullmatch(limit_table[0])
        and re.fullmatch(r"\|\s*:?-{3,}:?\s*\|\s*:?-{3,}:?\s*\|", limit_table[1])
        and all(line.count("|") == 3 for line in limit_table[2:])
        and not any(required_header.fullmatch(line) for line in limit_table[2:])
    )
    if not valid_limit_table:
        findings.append("25점 Ⅴ 한계·방안 대응 없음")
    proposal = by_number.get("Ⅵ", ("", ""))
    if "제언" not in proposal[0] or not proposal[1].strip():
        findings.append("25점 Ⅵ 제언 없음")
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subject", help="Only audit one subject directory")
    parser.add_argument("--summary", action="store_true", help="Hide per-file findings")
    args = parser.parse_args()
    totals = Counter()
    for directory in sorted(path for path in ROOT.iterdir() if path.is_dir()):
        if args.subject and directory.name != args.subject:
            continue
        files = sorted(directory.glob("*.md"))
        problems = [(path, audit(path)) for path in files if path.name != "index.md"]
        counts = Counter(issue for _, issues in problems for issue in issues)
        totals.update(counts)
        print(f"{directory.name}: {len(problems)} notes; {sum(bool(issues) for _, issues in problems)} with gaps")
        for issue, count in sorted(counts.items()):
            print(f"  {issue}: {count}")
        if not args.summary:
            for path, issues in problems:
                if issues:
                    print(f"  {path.name}: {', '.join(issues)}")
    print("TOTAL", dict(sorted(totals.items())))


if __name__ == "__main__":
    main()
