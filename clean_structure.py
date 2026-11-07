import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Let's inspect the main HTML body structure (excluding long inline data)
# Strip scripts and images data to inspect the structure easily
body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL | re.IGNORECASE)
if body_match:
    body = body_match.group(1)
    # clean out base64 data for printing
    clean_body = re.sub(r'data:image/[^;]+;base64,[a-zA-Z0-9+/=]+', 'DATA_IMAGE', body)
    
    # Save a lightweight skeleton of the HTML so we can inspect it without 22MB of base64
    with open('index_clean_structure.html', 'w', encoding='utf-8') as f_out:
        f_out.write(clean_body)
    print('Clean body written! Size:', len(clean_body))
