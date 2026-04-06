import re
from pathlib import Path
text = Path('index.html').read_text(encoding='utf-8')
lines = text.splitlines()
names=[]
for i,l in enumerate(lines):
    if 'capsule: true' in l:
        for j in range(i-1, max(i-30,-1), -1):
            m = re.search(r'^\s*name:\s*"([^"]+)"', lines[j])
            if m:
                names.append(m.group(1))
                break
print(len(names))
for n in names:
    print(n)
