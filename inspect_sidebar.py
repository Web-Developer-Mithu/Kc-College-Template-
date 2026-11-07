from bs4 import BeautifulSoup

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

second_contents = soup.find_all('div', id='contents')[1]
print("Direct children of second #contents:")
for child in second_contents.find_all(recursive=False):
    print(child.name, child.get('id'), child.get('class'))

print("\nLeft content children:")
left = soup.find(id='left-content')
if left:
    for child in left.find_all(recursive=False):
        print(" ", child.name, child.get('id'), child.get('class'))

# Is there a right content or sidebar?
right = soup.find(id='right-content') or soup.find(class_=lambda c: c and 'four' in str(c))
print("\nSidebar / right content:", right.name if right else None, right.get('id') if right else None, right.get('class') if right else None)

# Footer inspection
footer = soup.find('footer')
if not footer:
    footer = soup.find(class_=lambda c: c and 'footer' in str(c))
print("\nFooter found:", footer.name if footer else None, footer.get('id') if footer else None, footer.get('class') if footer else None)
