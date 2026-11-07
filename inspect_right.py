from bs4 import BeautifulSoup

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

right = soup.find(id='right-content')
if right:
    print("Right content direct children:", len(list(right.children)))
    for c in right.children:
        if c.name:
            print(f"<{c.name} class='{c.get('class')}' id='{c.get('id')}'>")
            print("  text sample:", c.get_text(strip=True)[:100])
else:
    print("No right-content found!")
