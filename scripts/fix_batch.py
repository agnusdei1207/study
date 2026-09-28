from pathlib import Path
import re

dir_path = Path("src/content/docs/notes/itpe/02-software-engineering")

def clean_file(f: Path):
    text = f.read_text(encoding="utf-8")
    orig = text
    
    # 1. Remove box header in ```text blocks
    def replace_box_header(match):
        block = match.group(1)
        # Find +-----+ \n | title | \n +-----+
        box_pattern = re.compile(r"^\s*\+[-=]{15,}\+\s*\n\s*\|\s*(.*?)\s*\|\s*\n\s*\+[-=]{15,}\+\s*\n?", re.M)
        m = box_pattern.search(block)
        if m:
            title = m.group(1).strip()
            block = box_pattern.sub(f"[{title}]\n", block, count=1)
        # Strip trailing whitespace on each line
        block_lines = [l.rstrip() for l in block.splitlines()]
        return "```text\n" + "\n".join(block_lines) + "\n```"

    text = re.sub(r"```text\s*\n(.*?)\n```", replace_box_header, text, flags=re.DOTALL)

    # 2. Fix Ⅵ proposal sentence ending
    # Find ## Ⅵ. 제언 \n\n sentence \n\n ```text
    sec6_match = re.search(r"(## Ⅵ\.\s*제언\s*\n\n)([^\n]+)(\n\n```text)", text)
    if sec6_match:
        prefix, sentence, suffix = sec6_match.groups()
        s = sentence.strip()
        s = re.sub(r"\s*고도화가 요구됨\.$", " 고도화", s)
        s = re.sub(r"\s*설계가 바람직함\.$", " 설계 체계화", s)
        s = re.sub(r"\s*적용 전략이 권장됨\.$", " 적용 전략 수립", s)
        s = re.sub(r"\s*체계화할 필요가 있음\.$", " 체계화", s)
        s = re.sub(r"\s*강화할 필요가 있음\.$", " 강화", s)
        s = re.sub(r"\s*접근이 필수적임\.$", " 접근 필수", s)
        s = re.sub(r"\s*점검할 필요가 있음\.$", " 점검 체계화", s)
        s = re.sub(r"\s*아키텍처 확립이 필요\.$", " 아키텍처 확립", s)
        s = re.sub(r"\s*유지할 필요가 있음\.$", " 유지", s)
        s = re.sub(r"\s*구축이 권장됨\.$", " 구축", s)
        s = re.sub(r"\s*도입이 시급함\.$", " 도입", s)
        s = re.sub(r"\s*강화가 필요함\.$", " 강화", s)
        s = re.sub(r"\s*확립이 요구됨\.$", " 확립", s)
        s = re.sub(r"\s*통합 관리가 권장됨\.$", " 통합 관리 체계화", s)
        s = re.sub(r"\s*추진이 필요함\.$", " 추진", s)
        s = re.sub(r"\s*선행이 요구됨\.$", " 선행 필수", s)
        s = re.sub(r"\s*체계가 권장됨\.$", " 체계 수립", s)
        text = text[:sec6_match.start()] + prefix + s + suffix + text[sec6_match.end():]

    # 3. Clean up footer (출제 이력 / 참고 자료 / 연결 토픽)
    # Check if ## 참고 자료 exists
    if "## 참고 자료" in text or "## 참고자료" in text:
        # Extract 출제 이력 lines
        history_match = re.search(r"## 출제 이력\s*\n([\s\S]*?)(?=\n## 참고\s*자료)", text)
        ref_match = re.search(r"## 참고\s*자료\s*\n([\s\S]*?)(?=\n## 연결 토픽|$)", text)
        topics_match = re.search(r"## 연결 토픽\s*\n([\s\S]*?)$", text)
        
        if history_match and ref_match:
            hist_lines = [l for l in history_match.group(1).strip().splitlines() if l.strip()]
            # filter out 컴퓨터시스템응용
            hist_lines = [l for l in hist_lines if "컴퓨터시스템응용" not in l]
            ref_lines = [l for l in ref_match.group(1).strip().splitlines() if l.strip()]
            # remove quotes in book titles if needed, clean up
            cleaned_refs = []
            for r in ref_lines:
                r_clean = r.replace('"', '')
                cleaned_refs.append(r_clean)
            
            topics_content = topics_match.group(1).strip() if topics_match else ""
            
            # Reconstruct footer
            new_footer = "## 출제 이력과 검증 출처\n\n"
            for hl in hist_lines:
                new_footer += f"{hl}\n"
            for rl in cleaned_refs:
                new_footer += f"{rl}\n"
            new_footer += "\n## 연결 토픽\n\n"
            if topics_content:
                new_footer += f"{topics_content}\n"
            else:
                new_footer += "- [소프트웨어 공학 개요](./index.md)\n"
            
            # Replace from --- before 출제 이력 or ## 출제 이력 to end
            split_pos = text.find("\n---\n\n## 출제 이력")
            if split_pos == -1:
                split_pos = text.find("\n## 출제 이력")
            
            if split_pos != -1:
                text = text[:split_pos].rstrip() + "\n\n" + new_footer

    if text != orig:
        f.write_text(text, encoding="utf-8")
        return True
    return False

if __name__ == "__main__":
    import sys
    files_to_fix = sys.argv[1:]
    for filepath in files_to_fix:
        p = Path(filepath)
        changed = clean_file(p)
        print(f"{p.name}: {'UPDATED' if changed else 'NO CHANGE'}")
