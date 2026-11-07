from bs4 import BeautifulSoup
import re

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

container = soup.find('div', class_='container')
if container:
    print("Children of .container:")
    for child in container.find_all(recursive=False):
        print(f"Tag: <{child.name}> id='{child.get('id')}' class='{child.get('class')}'")
        # print child's children summary
        sub_children = [f"<{c.name} class='{c.get('class')}'>" for c in child.find_all(recursive=False)]
        print("  Direct children:", sub_children[:10])
