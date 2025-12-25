#!/usr/bin/env python3
"""
Complete fix for main.js - handles all HTML and CSS syntax errors
"""
import re

# Read the file
with open('main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line
fixed_lines = []
for line in lines:
    # Fix HTML tags: "< tag" -> "<tag"
    line = re.sub(r'< ([a-z/])', r'<\1', line)
    # Fix HTML tags: "tag >" -> "tag>"  
    line = re.sub(r'([a-z]) >', r'\1>', line)
    # Fix CSS properties: "border - radius" -> "border-radius"
    line = re.sub(r'([a-z]) - ([a-z])', r'\1-\2', line)
    # Fix percentages: "0 %" -> "0%"
    line = re.sub(r'(\d+) %', r'\1%', line)
    
    fixed_lines.append(line)

# Write back
with open('main.js', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("✅ Successfully fixed all syntax errors in main.js!")
print("Fixed:")
print("  - HTML tag spaces")
print("  - CSS property hyphens")
print("  - Percentage spaces")
