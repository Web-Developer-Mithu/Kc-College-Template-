with open('index_clean_structure.html', 'r', encoding='utf-8', errors='ignore') as f:
    clean = f.read()

pos = clean.find('right-content')
print("Snippet around right-content in clean:")
print(clean[pos-300:pos+300])
