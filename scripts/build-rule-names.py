# Copies each slop sign's short name (L1 "Decoration colour", ...) from slop-list.md into the
# report templates, so a rule tag on the report shows its name. Run after editing slop-list.md.
import json, pathlib, re

ref = pathlib.Path(__file__).resolve().parent.parent / 'skills' / 'slop-free-screens' / 'reference'
names = {}
for line in (ref / 'slop-list.md').read_text().splitlines():
    m = re.match(r'- \*\*([LWDB]\d+) · [^*]+\*\* \*\*(.+?)\*\*', line)
    if m:
        names[m.group(1)] = m.group(2).rstrip('.:').strip()
for name in ('report-template.html', 'report-template-marked.html'):
    tpl = ref / name
    html = tpl.read_text()
    html, n = re.subn(r'/\*SLOP-IDS\*/.*?/\*END\*/', lambda _: '/*SLOP-IDS*/' + json.dumps(names, ensure_ascii=False) + '/*END*/', html, flags=re.S)
    assert n == 1, f'marker not found in {name}'
    tpl.write_text(html)
print(len(names), 'rule names written to 2 templates')
