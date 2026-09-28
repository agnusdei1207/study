import glob
import re
import os

files = sorted(glob.glob('src/content/docs/notes/itpe/02-software-engineering/*.md'))
target_files = []
for f in files:
    m = re.match(r'(\d+)', os.path.basename(f))
    if m and int(m.group(1)) >= 127:
        target_files.append(f)

print(f"Total target files (>= 127): {len(target_files)}")

for f in target_files:
    fname = os.path.basename(f)
    content = open(f, encoding='utf-8').read()
    issues = []
    
    # Check CA mentions
    if '컴퓨터시스템응용' in content:
        issues.append('CA_MENTION')
        
    # Check decorative box
    if re.search(r'\+[-=]{50,}\+', content):
        issues.append('DECORATIVE_BOX')
        
    # Check wide lines in code blocks
    blocks = re.findall(r'```(?:text)?\n(.*?)```', content, re.DOTALL)
    for b in blocks:
        lines = b.split('\n')
        max_len = max((len(l.rstrip()) for l in lines), default=0)
        if max_len > 85:
            issues.append(f'WIDE({max_len})')
            break
            
    # Check footer
    hist_pos = content.find('## 출제 이력과 검증 출처')
    if hist_pos == -1:
        hist_pos = content.find('## 출제 이력')
        issues.append('LEGACY_HIST_TITLE')
    conn_pos = content.find('## 연결 토픽')
    if hist_pos != -1 and conn_pos != -1:
        if hist_pos > conn_pos:
            issues.append('FOOTER_ORDER_INVERTED')
    elif hist_pos == -1 or conn_pos == -1:
        issues.append('MISSING_FOOTER')
        
    # Check section order
    sections = re.findall(r'## ([ⅠⅡⅢⅣⅤⅥ])\.', content)
    expected = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ']
    if sections != expected:
        issues.append(f'SECTIONS({sections})')

    # Check tree/graph files for dir-style tree
    if any(k in fname for k in ['star', 'dag', 'graph', 'tree', 'shortest_path', 'greedy']):
        if re.search(r'[├└]─', content):
            issues.append('DIR_STYLE_TREE')
            
    if issues:
        print(f"{fname}: {', '.join(issues)}")
