import re

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

for m in re.finditer(r'(.{0,100}width:\s*9[68]0px.{0,100})', html, re.I):
    print("Match:", m.group(1).replace('\n', ' '))
