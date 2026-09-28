import glob
import re
import os

for num in range(2, 21):
    matches = glob.glob(f'src/content/docs/notes/itpe/03-data/{num:03d}_*.md')
    if not matches:
        continue
    f = matches[0]
    content = open(f, encoding='utf-8').read()
    m_title = re.search(r'title:\s*"([^"]+)"', content)
    title = m_title.group(1) if m_title else os.path.basename(f)
    print(f"{os.path.basename(f)}: {title}")
