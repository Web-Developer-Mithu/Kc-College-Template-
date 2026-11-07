from bs4 import BeautifulSoup

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

container = soup.find('div', class_='container')
if container:
    for i, child in enumerate(container.find_all(recursive=False)):
        if child.name not in ['script', 'style']:
            print(f"{i}: <{child.name}> id='{child.get('id')}' class='{child.get('class')}'")

print("\n--- Let's inspect div#contents and other main sections ---")
for contents in soup.find_all('div', id='contents'):
    print("Found #contents:")
    for sub in contents.find_all(recursive=False):
        print(f"  <{sub.name}> class='{sub.get('class')}' id='{sub.get('id')}'")
        for subsub in sub.find_all(recursive=False):
            print(f"    <{subsub.name}> class='{subsub.get('class')}' id='{subsub.get('id')}'")

footer = soup.find('footer') or soup.find(class_=lambda c: c and 'footer' in c)
if footer:
    print(f"\nFooter: <{footer.name}> class='{footer.get('class')}'")
