import glob, re, os
base="C:/workspace/study/src/content/docs/notes/itpe"
for subj in ["04-computer-system","06-security","07-latest-tech","01-it-strategy"]:
    print("==",subj)
    for p in sorted(glob.glob(os.path.join(base,subj,"*.md"))):
        name=os.path.basename(p)
        if not re.match(r'^0(79|8[0-9]|9[01])',name): continue
        with open(p,encoding='utf-8') as f: c=f.read()
        has7 = "## Ⅰ." in c
        print(f"  {name}: 7frame={has7}")
PY