from bs4 import BeautifulSoup
import re

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read()[:500000], 'html.parser')

print("Top tags inside body:")
for child in soup.children:
    if child.name:
        classes = child.get('class', [])
        id_ = child.get('id', '')
        print(f"<{child.name} id='{id_}' class='{' '.join(classes)}'>")

print("\nDirect divs in body or main container:")
for div in soup.find_all('div', recursive=False):
    print(div.get('id'), div.get('class'))

# Let's see containers
print("\nContainers:")
for c in soup.find_all(class_=re.compile(r'container|wrapper|main|header|nav|row')):
    print(c.name, c.get('id'), c.get('class'))
