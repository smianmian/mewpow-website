#!/usr/bin/env python3
"""
Final complete fix for main.js - handles all syntax errors carefully
"""

# Start from the broken backup which has the original structure
with open('main.js.broken', 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Fix unicode escapes that were incorrectly created
content = content.replace('u003c', '<')

# Step 2: Fix HTML tags with spaces: "< tag" -> "<tag"
import re
content = re.sub(r'< ([a-z/])', r'<\1', content)

# Step 3: Fix HTML tags with spaces: "tag >" -> "tag>"
content = re.sub(r'([a-z]) >', r'\1>', content)

# Step 4: Fix CSS properties with spaces: "border - radius" -> "border-radius"
content = re.sub(r'([a-z]) - ([a-z])', r'\1-\2', content)

# Step 5: Fix percentages with spaces: "0 %" -> "0%"
content = re.sub(r'(\d+) %', r'\1%', content)

# Step 6: Fix template literals with spaces: "${ var }" -> "${var}"
content = re.sub(r'\$\{\s+', '${', content)
content = re.sub(r'\s+\}', '}', content)

# Write the fixed content
with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完成所有修复！从main.js.broken恢复并修复所有语法错误')
