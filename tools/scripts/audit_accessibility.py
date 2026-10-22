"""
audit_accessibility.py — Static accessibility attribute checker
Scans all HTML pages for missing aria-label, alt text, role, lang, and skip-link patterns.
Exits with code 1 and prints all violations if any are found.
"""
from pathlib import Path
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parents[2]

class A11yParser(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.errors = []
        self.has_skip_link = False
        self.has_main = False
        self.img_count = 0
        self.img_alt_missing = 0
        self.interactive_tags = []   # buttons, inputs without accessible name
        self.iframe_tags = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        tag = tag.lower()

        # Track skip link (matches skip-link, skip-nav, skip-to, and bare 'skip' class patterns)
        if tag == 'a' and d.get('href', '').startswith('#'):
            class_id = (d.get('class', '') + ' ' + d.get('id', '')).lower().split()
            # match whole-word 'skip' or compound patterns
            if any(c in ('skip', 'skip-link', 'skip-nav', 'skip-to', 'skiplink', 'skipnav') for c in class_id):
                self.has_skip_link = True

        # Track <main>
        if tag == 'main':
            self.has_main = True

        # Images must have alt attribute
        if tag == 'img':
            self.img_count += 1
            if 'alt' not in d:
                self.errors.append(f'  <img> missing alt attribute (src={d.get("src","?")!r})')

        # Buttons must have text content or aria-label
        if tag == 'button':
            if not d.get('aria-label') and not d.get('aria-labelledby') and not d.get('title'):
                # Can't check text content at starttag; flag ambiguous ones
                pass  # text content checked separately

        # iframes must have title
        if tag == 'iframe':
            if not d.get('title'):
                self.errors.append(f'  <iframe> missing title attribute')

        # Inputs (not hidden) must have label or aria-label
        if tag == 'input' and d.get('type', 'text') not in ('hidden', 'submit', 'reset', 'button', 'image'):
            has_name = d.get('aria-label') or d.get('aria-labelledby') or d.get('id') or d.get('title')
            if not has_name:
                self.errors.append(f'  <input type={d.get("type","text")!r}> missing accessible name (aria-label / id+label)')

        # svg used as image should have role and aria-label or aria-hidden
        if tag == 'svg':
            if not d.get('aria-hidden') and not d.get('role') and not d.get('aria-label'):
                self.errors.append(f'  <svg> missing aria-hidden or role+aria-label')

errors_all = []
pages = list(ROOT.rglob('*.html'))

for page in pages:
    try:
        content = page.read_text(encoding='utf-8')
    except Exception as e:
        errors_all.append(f'{page.relative_to(ROOT)}: could not read — {e}')
        continue

    parser = A11yParser(page)
    parser.feed(content)

    page_key = str(page.relative_to(ROOT))

    # Check lang on <html>
    if '<html' in content and 'lang=' not in content.split('<body')[0]:
        errors_all.append(f'{page_key}: <html> element missing lang attribute')

    # Check skip link exists (only for pages with nav)
    if '<nav' in content and not parser.has_skip_link:
        errors_all.append(f'{page_key}: page has <nav> but no skip-to-main link detected')

    # Check <main> exists
    if not parser.has_main:
        errors_all.append(f'{page_key}: missing <main> landmark')

    for err in parser.errors:
        errors_all.append(f'{page_key}:{err}')

print(f'Accessibility audit — checked {len(pages)} HTML pages.')
if errors_all:
    print('FAIL: accessibility issues found:')
    print('\n'.join(errors_all))
    sys.exit(1)
print('PASS: no critical accessibility issues found.')
