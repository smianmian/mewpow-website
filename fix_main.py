#!/usr/bin/env python3
import re

# Read the file
with open('main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix HTML tags with spaces: "< tag" -> "<tag" and "tag >" -> "tag>"
content = re.sub(r'< ([a-z/])', r'<\1', content)
content = re.sub(r'([a-z]) >', r'\1>', content)

# Fix CSS properties with spaces: "border - radius" -> "border-radius"
content = re.sub(r'([a-z]) - ([a-z])', r'\1-\2', content)

# Fix percentage with spaces: "0 %" -> "0%"
content = re.sub(r'(\d) %', r'\1%', content)

# Write back
with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed main.js successfully!")
