with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('id="right-content"')
print("Pos of right-content in index.html:", pos)
if pos != -1:
    print(html[pos-200:pos+1000])

clean_pos = open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore').read().find('right-content')
print("Pos in clean:", clean_pos)
