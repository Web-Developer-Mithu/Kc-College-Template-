with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    clean = f.read()

pos = clean.find('id="right-content"')
print("Pos of id=\"right-content\":", pos)
if pos != -1:
    print(clean[pos-300:pos+1500])
