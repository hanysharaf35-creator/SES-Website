#!/usr/bin/env python3
"""
Restructure Arabic HTML to match English HTML structure exactly
"""

# Read the pasted Arabic translations
with open('/home/ubuntu/upload/pasted_content.txt', 'r', encoding='utf-8') as f:
    arabic_translations = f.read()

# Read current Arabic HTML
with open('/home/ubuntu/SES-Website/index-ar.html', 'r', encoding='utf-8') as f:
    arabic_html = f.read()

# Read English HTML for structure reference
with open('/home/ubuntu/SES-Website/index.html', 'r', encoding='utf-8') as f:
    english_html = f.read()

print("Files loaded successfully")
print(f"Arabic HTML length: {len(arabic_html)} characters")
print(f"English HTML length: {len(english_html)} characters")
print(f"Arabic translations length: {len(arabic_translations)} characters")

