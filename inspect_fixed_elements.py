import re

with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find inline styles with width
inline_widths = re.findall(r'style=[\'"][^\'"]*width:\s*([0-9]+px)[^\'"]*[\'"]', html)
print(f"Total inline widths in px: {len(inline_widths)}")
from collections import Counter
print("Most common inline widths:", Counter(inline_widths).most_common(20))

# Find tables with width attribute or style
tables = re.findall(r'<table[^>]*>', html)
print(f"Total tables: {len(tables)}")
for t in tables[:10]:
    print("Table:", t)

# Find iframes
iframes = re.findall(r'<iframe[^>]*>', html)
print(f"Total iframes: {len(iframes)}")
for ifr in iframes[:10]:
    print("iframe:", ifr[:100])

# Find images with fixed width attributes
img_fixed = re.findall(r'<img[^>]+(?:width=[\'"][0-9]+[\'"]|style=[\'"][^\'"]*width:[^;\'"]+[\'"])[^>]*>', html)
print(f"Images with width: {len(img_fixed)}")
for img in img_fixed[:10]:
    print("Image:", img[:120])
