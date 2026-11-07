import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's inspect CSS frameworks included
links = re.findall(r'<style[^>]*data-savepage-href=[\'"]([^\'"]+)[\'"]', content)
for l in links:
    print('CSS href:', l)

# Let's find skeleton or bootstrap or custom grid classes
print('\nSearching for container/row/col classes:')
classes = set(re.findall(r'class=[\'"]([^\'"]+)[\'"]', content))
all_classes = set()
for c in classes:
    for cls in c.split():
        all_classes.add(cls)

common_layout = [c for c in all_classes if any(k in c.lower() for k in ['container', 'column', 'grid', 'row', 'col-', 'header', 'nav', 'menu', 'wrapper', 'main', 'sidebar', 'footer', 'banner'])]
print('Sample layout classes:', sorted(common_layout)[:50])
