from bs4 import BeautifulSoup
import re

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- H1, H2, H3, H4, H5, H6 headings ---")
for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    print(f"<{h.name}>: {h.get_text(strip=True)[:80]}")

print("\n--- Main navigation items ---")
nav = soup.find(id='jmenu') or soup.find(class_=lambda c: c and 'menu' in c)
if nav:
    links = nav.find_all('a')
    print(f"Nav links count: {len(links)}")
    for a in links[:15]:
        print(" ", a.get_text(strip=True))

print("\n--- Left content sections / widgets ---")
left = soup.find(id='left-content')
if left:
    for box in left.find_all(['div', 'section'], recursive=False):
        print("Left child:", box.name, box.get('id'), box.get('class'))
    # look for widgets or headings inside left
    for widget in left.find_all(class_=re.compile(r'widget|box|block|card|panel|section')):
        print(" Left sub-box:", widget.name, widget.get('id'), widget.get('class'))

print("\n--- Right content sections / widgets ---")
right = soup.find(id='right-content')
if right:
    for box in right.find_all(['div', 'section'], recursive=False):
        print("Right child:", box.name, box.get('id'), box.get('class'))
        title = box.find(['h2', 'h3', 'h4', 'h5', 'span', 'p'])
        if title:
            print("   title:", title.get_text(strip=True)[:60])
