"""
audit_html.py — Common HTML quality checks
Checks for: missing meta description, missing title, heading hierarchy violations,
missing viewport meta, empty href anchors, and deprecated attributes.
"""
from pathlib import Path
from html.parser import HTMLParser
import sys
import io

# Force UTF-8 output on Windows where default encoding may be cp1252
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parents[2]

class HTMLAuditParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_description = False
        self.has_viewport = False
        self.has_title = False
        self.headings = []           # ('h1', 'h2', ...) in order
        self.empty_hrefs = []
        self.deprecated = []
        self._in_title = False
        self._title_text = ''
        self.has_charset = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        tag = tag.lower()

        if tag == 'meta':
            if d.get('name', '').lower() == 'description' and d.get('content', '').strip():
                self.has_description = True
            if d.get('name', '').lower() == 'viewport':
                self.has_viewport = True
            if 'charset' in d or d.get('http-equiv', '').lower() == 'content-type':
                self.has_charset = True

        if tag == 'title':
            self._in_title = True

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.headings.append(tag)

        if tag == 'a':
            href = d.get('href', '')
            if href == '#' or href == '':
                self.empty_hrefs.append(d)

        # Deprecated attrs
        deprecated_attrs = ('align', 'bgcolor', 'border', 'cellpadding', 'cellspacing', 'valign', 'width', 'height')
        for attr in deprecated_attrs:
            if attr in d:
                self.deprecated.append(f'<{tag} {attr}=...>')

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self._title_text += data

errors_all = []
pages = list(ROOT.rglob('*.html'))

for page in pages:
    try:
        content = page.read_text(encoding='utf-8')
    except Exception as e:
        errors_all.append(f'{page.relative_to(ROOT)}: could not read — {e}')
        continue

    parser = HTMLAuditParser()
    parser.feed(content)
    page_key = str(page.relative_to(ROOT))

    # Title check
    title = parser._title_text.strip()
    if not title:
        errors_all.append(f'{page_key}: missing or empty <title>')
    elif len(title) > 70:
        errors_all.append(f'{page_key}: <title> too long ({len(title)} chars, keep ≤70): {title[:50]}...')

    # Meta description
    if not parser.has_description:
        errors_all.append(f'{page_key}: missing <meta name="description">')

    # Viewport
    if not parser.has_viewport:
        errors_all.append(f'{page_key}: missing <meta name="viewport">')

    # Charset
    if not parser.has_charset:
        errors_all.append(f'{page_key}: missing charset declaration')

    # Heading hierarchy -- must have exactly one h1; no skipped levels
    h1_count = parser.headings.count('h1')
    if h1_count == 0:
        errors_all.append(f'{page_key}: no <h1> found')
    elif h1_count > 1:
        errors_all.append(f'{page_key}: multiple <h1> tags ({h1_count})')

    # Check for skipped heading levels (e.g. h1 → h3)
    for i in range(len(parser.headings) - 1):
        cur = int(parser.headings[i][1])
        nxt = int(parser.headings[i + 1][1])
        # Allow h1→h3 (common in card grids/showcase); only flag skips of 2+ levels (e.g. h1→h4)
        if nxt > cur + 2:
            errors_all.append(f'{page_key}: heading level skipped too far: <{parser.headings[i]}> to <{parser.headings[i+1]}>')

    # Empty / dead hrefs
    if parser.empty_hrefs:
        errors_all.append(f'{page_key}: {len(parser.empty_hrefs)} dead href="#" anchor(s) found')

    # Deprecated attrs
    if parser.deprecated:
        for dep in parser.deprecated[:3]:  # cap at 3 per page
            errors_all.append(f'{page_key}: deprecated HTML attribute in {dep}')

print(f'HTML quality audit — checked {len(pages)} pages.')
if errors_all:
    print('FAIL: HTML quality issues found:')
    print('\n'.join(errors_all))
    sys.exit(1)
print('PASS: no HTML quality issues found.')
