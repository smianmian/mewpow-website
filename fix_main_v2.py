#!/usr/bin/env python3
import re

# Read the broken file
with open('main.js.broken', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken unicode escapes back to proper HTML tags
# u003c -> <
content = content.replace('u003c', '<')

# Now fix the original issues:
# Fix HTML tags with extra spaces: "< tag" -> "<tag" and "tag >" -> "tag>"
content = re.sub(r'< ([a-z/])', r'<\1', content)
content = re.sub(r'([a-z]) >', r'\1>', content)

# Fix CSS properties with spaces: "border - radius" -> "border-radius"
content = re.sub(r'([a-z]) - ([a-z])', r'\1-\2', content)

# Fix percentage with spaces: "0 %" -> "0%", "90 %" -> "90%", etc.
content = re.sub(r'(\d+) %', r'\1%', content)

# Write the fixed content
with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully fixed main.js!")
