"""Report structural gaps in ITPE topic notes without changing content.

This checks required sections and diagrams. It cannot judge whether a diagram
accurately explains the topic; that still needs editorial review.
"""

from collections import Counter
from pathlib import Path
import argparse
import re


ROOT = Path(__file__).resolve().parents[1] / "src/content/docs/notes/itpe"
FIRST_ANSWER = "## 1교시 10점 답안"
SECOND_QUESTION = "## 2~4교시 예상문제"
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
    recall_labels = {
        line.lstrip("- ").replace("**", "").split(":", 1)[0].strip()
        for line in recall.splitlines()
        if line.lstrip().startswith("-")
    }
    for label in INSIGHT_LABELS:
        if label not in recall_labels:
            findings.append(f"30초 인출: {label} 없음")

    first = section(text, FIRST_ANSWER, SECOND_QUESTION)
    if not first:
        return findings + ["1교시 답안 없음"]
    parts = roman_parts(first)
    by_number = {number: (title, body) for number, title, body in parts}
    for number in ("Ⅰ", "Ⅱ", "Ⅲ"):
        if number not in by_number:
            findings.append(f"1교시 {number} 절 없음")
    if "Ⅰ" in by_number:
        title, body = by_number["Ⅰ"]
        if "개요" not in title or not all(f"| {word} |" in body for word in ("정의", "목적")):
            findings.append("1교시 Ⅰ 개요·정의·목적 누락")
    if "Ⅱ" in by_number and not TEXT_DIAGRAM.search(by_number["Ⅱ"][1]):
        findings.append("1교시 Ⅱ text 도해 없음")
    if "Ⅲ" in by_number and "제언" not in by_number["Ⅲ"][0]:
        findings.append("1교시 Ⅲ 제언 아님")

    second = section(text, SECOND_ANSWER, "## 출제 이력")
    if second:
        second_parts = roman_parts(second)
        core = next((body for number, _, body in second_parts if number == "Ⅱ"), "")
        if not TEXT_DIAGRAM.search(core):
            findings.append("25점 Ⅱ text 도해 없음")
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
