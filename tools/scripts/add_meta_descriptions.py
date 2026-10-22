"""
add_meta_descriptions.py — One-time fixer script.
Adds missing <meta name="description"> tags to HTML files that lack them.
Run once from the project root, then delete this file.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Map of file patterns → description text
DESCRIPTIONS = {
    'dark/accessibility.html':     'Dark theme accessibility patterns and focus states for the Apple-inspired design system.',
    'light/accessibility.html':    'Light theme accessibility patterns and focus states for the Apple-inspired design system.',
    'dark/cards-carousel.html':    'Dark theme card and carousel component specimens for the Apple-inspired design system.',
    'light/cards-carousel.html':   'Light theme card and carousel component specimens for the Apple-inspired design system.',
    'dark/cookie-preferences.html':'Dark theme cookie preferences page for the Apple-inspired design system.',
    'light/cookie-preferences.html':'Light theme cookie preferences page for the Apple-inspired design system.',
    'dark/privacy-policy.html':    'Dark theme privacy policy page for the Apple-inspired design system.',
    'light/privacy-policy.html':   'Light theme privacy policy page for the Apple-inspired design system.',
    'dark/terms-of-service.html':  'Dark theme terms of service page for the Apple-inspired design system.',
    'light/terms-of-service.html': 'Light theme terms of service page for the Apple-inspired design system.',
    'dark/typography.html':        'Dark theme typography specimens for the Apple-inspired design system.',
    'light/typography.html':       'Light theme typography specimens for the Apple-inspired design system.',
    'dark/reference-patterns.html':'Dark theme reference UI patterns — navigation, carousels, feature explorers.',
}

fixed = 0
for rel_path, desc in DESCRIPTIONS.items():
    path = ROOT / rel_path
    if not path.exists():
        print(f'SKIP (not found): {rel_path}')
        continue
    content = path.read_text(encoding='utf-8')
    if 'name="description"' in content:
        print(f'OK (already has description): {rel_path}')
        continue
    # Insert after <meta charset...> or after <head>
    tag = '<meta name="description" content="' + desc + '">'
    if '<meta charset' in content:
        content = content.replace('<meta charset', tag + '<meta charset', 1)
    elif '<head>' in content:
        content = content.replace('<head>', '<head>' + tag, 1)
    else:
        print(f'SKIP (cannot find insertion point): {rel_path}')
        continue
    path.write_text(content, encoding='utf-8')
    print(f'FIXED: {rel_path}')
    fixed += 1

print(f'\nDone. Fixed {fixed} files.')
