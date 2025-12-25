#!/usr/bin/env python3
import re

# Read the file
with open('main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix remaining HTML entity issues
content = content.replace(' \u003e', '>')

# Write back
with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed remaining HTML entities!")
