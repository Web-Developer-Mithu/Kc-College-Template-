with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
print("Length of index.html:", len(html))

# Let's find all occurrences of <div class="...sixteen columns..." or id="left-content"
for m in re.finditer(r'<div[^>]+id=[\'"]([^\'"]+)[\'"]', html):
    print("div id:", m.group(1))

# Check occurrences of right-content or sidebar or footer
for keyword in ['right', 'sidebar', 'footer', 'widget', 'bottom', 'copyright']:
    matches = re.findall(rf'<[^>]+(?:class|id)=[\'"][^\'"]*{keyword}[^\'"]*[\'"][^>]*>', html, re.I)
    print(f"Keyword '{keyword}' matches count: {len(matches)}")
    for sample in matches[:5]:
        print("  ", sample[:120])
