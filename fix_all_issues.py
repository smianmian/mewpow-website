#!/usr/bin/env python3
"""
Complete and careful fix for main.js
"""
import re

with open('main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix HTML tags: "< tag" -> "<tag"
content = re.sub(r'< ([a-z/])', r'<\1', content)

# 2. Fix HTML tags: "tag >" -> "tag>"
content = re.sub(r'([a-z]) >', r'\1>', content)

# 3. Fix CSS properties: "border - radius" -> "border-radius"
content = re.sub(r'([a-z]) - ([a-z])', r'\1-\2', content)

# 4. Fix percentages: "0 %" -> "0%"
content = re.sub(r'(\d+) %', r'\1%', content)

# 5. Fix template literals: "${ var }" -> "${var}" (only in template strings)
content = re.sub(r'\$\{\s+', '${', content)
content = re.sub(r'\s+\}([`\)])', r'}\1', content)

with open('main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ 完成所有修复！')
