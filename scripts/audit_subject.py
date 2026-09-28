import glob
import re
import os
import sys

subject_dir = sys.argv[1] if len(sys.argv) > 1 else 'src/content/docs/notes/itpe/03-data'
files = sorted(glob.glob(f'{subject_dir}/*.md'))
print(f"Auditing subject dir: {subject_dir} ({len(files)} files)")

issue_counts = {}

for f in files:
    fname = os.path.basename(f)
    if fname == 'index.md':
        continue
    content = open(f, encoding='utf-8').read()
    issues = []
    
    # 1. Check CA mentions
    if '컴퓨터시스템응용' in content:
        issues.append('CA_MENTION')
        
    # 2. Check decorative box
    if re.search(r'\+[-=]{50,}\+', content):
        issues.append('DECORATIVE_BOX')
        
    # 3. Check wide lines in code blocks (> 80 chars)
    blocks = re.findall(r'```(?:text)?\n(.*?)```', content, re.DOTALL)
    for b in blocks:
        lines = b.split('\n')
        max_len = max((len(l.rstrip()) for l in lines), default=0)
        if max_len > 80:
            issues.append(f'WIDE({max_len})')
            break
            
    # 4. Check footer
    hist_pos = content.find('## 출제 이력과 검증 출처')
    if hist_pos == -1:
        hist_pos = content.find('## 출제 이력')
        if hist_pos != -1:
            issues.append('LEGACY_HIST_TITLE')
        else:
            issues.append('MISSING_HIST')
    conn_pos = content.find('## 연결 토픽')
    if hist_pos != -1 and conn_pos != -1:
        if hist_pos > conn_pos:
            issues.append('FOOTER_INVERTED')
    elif conn_pos == -1:
        issues.append('MISSING_CONN')
        
    # 5. Check section order
    sections = re.findall(r'## ([ⅠⅡⅢⅣⅤⅥ])\.', content)
    expected = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ']
    if sections != expected:
        issues.append(f'SECTIONS({",".join(sections)})')

    # 6. Check recommendation ending
    m_rec = re.search(r'## Ⅵ\. 제언\s*\n\s*(.*?)(?=\n\n|\n```)', content, re.DOTALL)
    if m_rec:
        rec_first_p = m_rec.group(1).strip()
        last_sentence = rec_first_p.split('\n')[-1].strip()
        if any(bad in last_sentence for bad in ['권장.', '바람직하다.', '필요하다.', '하여야 한다.', '요구된다.']):
            issues.append('REC_NOT_NOUN')
            
    # 7. Check tree-related topics for dir-style tree
    if any(k in fname for k in ['tree', 'b_tree', 'b_plus', 'index', 'graph', 'hierarch']):
        if re.search(r'[├└]─', content):
            issues.append('DIR_STYLE_TREE')

    if issues:
        for iss in issues:
            k = iss.split('(')[0]
            issue_counts[k] = issue_counts.get(k, 0) + 1
        print(f"{fname}: {', '.join(issues)}")

print("\n=== Issue Summary ===")
for k, v in sorted(issue_counts.items(), key=lambda x: -x[1]):
    print(f"{k}: {v} files")
