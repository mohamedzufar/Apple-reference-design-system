from pathlib import Path
from html.parser import HTMLParser
import sys
ROOT = Path(__file__).resolve().parents[2]
class RefParser(HTMLParser):
    def __init__(self): super().__init__(); self.refs=[]; self.ids=[]; self.anchors=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.append(d['id'])
        if tag.lower() == 'a' and d.get('href', '').startswith('#') and len(d['href']) > 1:
            self.anchors.append(d['href'][1:])
        for key in ('href','src'):
            val=d.get(key,'')
            if val and not val.startswith(('http://','https://','mailto:','tel:','data:','#','javascript:')):
                self.refs.append(val.split('#')[0].split('?')[0])
errors=[]; pages=list(ROOT.rglob('*.html'))
for page in pages:
    parser=RefParser()
    try: parser.feed(page.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{page.relative_to(ROOT)}: HTML parse error: {e}'); continue
    duplicates=sorted({x for x in parser.ids if parser.ids.count(x)>1})
    if duplicates: errors.append(f'{page.relative_to(ROOT)}: duplicate ids {duplicates}')
    for anchor in parser.anchors:
        if anchor not in parser.ids: errors.append(f'{page.relative_to(ROOT)}: missing in-page anchor #{anchor}')
    for ref in parser.refs:
        if not ref: continue
        target=(page.parent/ref).resolve()
        if not target.exists(): errors.append(f'{page.relative_to(ROOT)}: missing local reference {ref}')
if not (ROOT/'index.html').exists(): errors.append('root index.html missing')
if not (ROOT/'docs/skills/APPLE-DESIGN-SYSTEM-SKILL-V1.0-FINAL.md').exists(): errors.append('v1.0 final skill missing')
print(f'Checked {len(pages)} HTML pages.')
if errors:
    print('FAIL:')
    print('\n'.join(errors)); sys.exit(1)
print('PASS: no duplicate IDs, missing local files, or broken in-page anchors found.')
