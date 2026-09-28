import glob
import re
import os

nums = [181, 182, 186, 187, 188, 189, 194, 199, 200, 201, 204]
for num in nums:
    matches = glob.glob(f'src/content/docs/notes/itpe/02-software-engineering/{num}_*.md')
    if not matches:
        continue
    f = matches[0]
    content = open(f, encoding='utf-8').read()
    fname = os.path.basename(f)
    blocks = re.findall(r'```(?:text)?\n(.*?)```', content, re.DOTALL)
    for i, b in enumerate(blocks):
        lines = b.split('\n')
        wides = [l for l in lines if len(l.rstrip()) > 80]
        if wides:
            print(f"{fname} Block {i+1} ({len(wides)} lines, max {max(len(l) for l in wides)}):")
            for l in wides:
                print(f"  [LEN {len(l)}] {l}")
