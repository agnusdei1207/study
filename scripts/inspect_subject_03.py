import glob
import re
import os

files = sorted(glob.glob('src/content/docs/notes/itpe/03-data/*.md'))
with_rec = []
without_rec = []

fence = '```' + 'text'

for f in files:
    fname = os.path.basename(f)
    if fname == 'index.md':
        continue
    content = open(f, encoding='utf-8').read().replace('\r\n', '\n')
    rec_pos = content.find('## Ⅵ.')
    if rec_pos != -1:
        hist_pos = content.find('## 출제 이력', rec_pos)
        rec_body = content[rec_pos:hist_pos] if hist_pos != -1 else content[rec_pos:]
        has_diagram = fence in rec_body
        has_table = bool(re.search(r'\|[^\n]+\|\n\|', rec_body))
        if has_diagram and has_table:
            with_rec.append(fname)
        else:
            without_rec.append((fname, has_diagram, has_table))
    else:
        without_rec.append((fname, False, False))

print(f"Total notes: {len(files)-1}")
print(f"With rec visuals (diagram + table): {len(with_rec)}")
print(f"Without rec visuals: {len(without_rec)}")
if with_rec:
    print(f"Samples with rec: {with_rec[:5]}")
if without_rec:
    print(f"Samples without rec: {without_rec[:5]}")
