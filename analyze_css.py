import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Extract all style tags
styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
print(f"Total style tags: {len(styles)}")

# Search for media queries in all styles
media_queries = []
for i, s in enumerate(styles):
    mq = re.findall(r'@media[^{]+', s)
    if mq:
        print(f"Style tag {i} has media queries:")
        for m in mq:
            print("  ", m.strip())

# Check container width rules
for i, s in enumerate(styles):
    c_rules = re.findall(r'(\.container[^{]*\{[^}]*\})', s)
    if c_rules:
        print(f"Style {i} container rules:")
        for r in c_rules[:5]:
            print("  ", r.replace('\n', ' '))
