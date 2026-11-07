with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    f.seek(0, 2)
    total_size = f.tell()
    print('Total size of index.html:', total_size)
    f.seek(max(0, total_size - 10000))
    tail = f.read()

print('Tail 1500 chars of index.html:')
print(tail[-1500:])
