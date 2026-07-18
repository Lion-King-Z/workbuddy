import re

with open('G:/锅师/深度研究/0713-0719/2026-07-14_每日窄门筛股.md', 'r', encoding='utf-8') as f:
    content = f.read()

css = '''*{margin:0;padding:0;box-sizing:border-box}
body{background:#0d1117;color:#c9d1d9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;padding:16px;max-width:900px;margin:0 auto}
h1{color:#58a6ff;font-size:1.4em;margin:20px 0 10px;border-bottom:2px solid #30363d;padding-bottom:8px}
h2{color:#f0883e;font-size:1.2em;margin:24px 0 10px;border-left:4px solid #f0883e;padding-left:10px}
h3{color:#d2a8ff;font-size:1.05em;margin:16px 0 8px}
p{margin:6px 0;line-height:1.6}
blockquote{background:#161b22;border-left:4px solid #58a6ff;padding:10px 14px;margin:10px 0;border-radius:0 6px 6px 0;font-size:.9em;color:#8b949e}
table{width:100%;border-collapse:collapse;margin:12px 0;font-size:.82em;overflow-x:auto;display:block}
th{background:#21262d;color:#f0f6fc;padding:8px 10px;text-align:center;border:1px solid #30363d;font-weight:600;white-space:nowrap}
td{padding:7px 10px;border:1px solid #30363d;text-align:center;vertical-align:middle;white-space:nowrap}
tr:nth-child(even){background:#161b22}
tr:hover{background:#1c2333}
strong{color:#f0f6fc}
code{background:#21262d;padding:1px 5px;border-radius:3px;font-size:.85em}
hr{border:none;border-top:1px solid #30363d;margin:12px 0}
.tag-buy{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#238636;color:#fff}
.tag-watch{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#d29922;color:#000}
.tag-gold{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#d2a8ff;color:#000}
.tag-new{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#d2a8ff;color:#000}
.tag-up{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#238636;color:#fff}
.tag-down{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#da3633;color:#fff}
.tag-out{display:inline-block;padding:2px 8px;border-radius:12px;font-size:.75em;font-weight:600;background:#8b949e;color:#000}
.fire{color:#f0883e}.star{color:#d2a8ff}.green{color:#3fb950}
.red{color:#f85149}.yellow{color:#d29922}.gray{color:#8b949e}
@media(max-width:640px){body{padding:10px}h1{font-size:1.2em}table{font-size:.72em}td,th{padding:5px 6px}}'''

html_out = ['<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>每日窄门筛股 — 2026-07-14 v4.6</title><style>', css, '</style></head><body>']

lines = content.split('\n')
in_table = False
in_quote = False
first_h1 = True
prev_parts = []

def fmt_cell(c):
    c = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', c)
    c = re.sub(r'`(.+?)`', r'<code>\1</code>', c)
    c = c.replace('🔥','<span class="fire">🔥</span>')
    c = c.replace('⭐','<span class="star">⭐</span>')
    c = c.replace('✅','<span class="green">✅</span>')
    c = c.replace('⚠️','<span class="yellow">⚠️</span>')
    c = c.replace('🔴','<span class="red">🔴</span>')
    c = c.replace('🟢','<span class="green">🟢</span>')
    c = c.replace('🟠','<span class="yellow">🟠</span>')
    c = c.replace('🟡','<span class="yellow">🟡</span>')
    c = c.replace('🔵','<span style="color:#58a6ff">🔵</span>')
    c = c.replace('🏆','<span class="tag-gold">🏆</span>')
    c = c.replace('💤','<span class="gray">💤</span>')
    c = c.replace('🆕','<span class="tag-new">🆕</span>')
    c = c.replace('▼','<span class="tag-down">▼</span>')
    c = c.replace('▲','<span class="tag-up">▲</span>')
    if '强力买入' in c:
        c = c.replace('强力买入','<span class="tag-buy">强力买入</span>')
    if '建议买入' in c:
        c = c.replace('建议买入','<span class="tag-buy">建议买入</span>')
    if '可买入' in c:
        c = c.replace('可买入','<span class="tag-watch">可买入</span>')
    if '观察等待' in c:
        c = c.replace('观察等待','<span class="tag-watch">观察等待</span>')
    return c

def fmt_line(l):
    l = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', l)
    l = re.sub(r'`(.+?)`', r'<code>\1</code>', l)
    l = l.replace('🔥','<span class="fire">🔥</span>')
    l = l.replace('⚠️','<span class="yellow">⚠️</span>')
    l = l.replace('💤','<span class="gray">💤</span>')
    l = l.replace('🆕','<span class="tag-new">🆕</span>')
    l = l.replace('🏆','<span class="tag-gold">🏆</span>')
    l = l.replace('✅','<span class="green">✅</span>')
    l = l.replace('🔴','<span class="red">🔴</span>')
    l = l.replace('🟢','<span class="green">🟢</span>')
    l = l.replace('🟠','<span class="yellow">🟠</span>')
    l = l.replace('🟡','<span class="yellow">🟡</span>')
    l = l.replace('🔵','<span style="color:#58a6ff">🔵</span>')
    l = l.replace('▼','<span class="tag-down">▼</span>')
    l = l.replace('▲','<span class="tag-up">▲</span>')
    return l

for line in lines:
    if line == '---' and first_h1:
        continue

    if line.startswith('# ') and first_h1:
        first_h1 = False
        html_out.append(f'<h1>{fmt_line(line[2:])}</h1>')
    elif line.startswith('## '):
        first_h1 = False
        html_out.append(f'<h2>{fmt_line(line[3:])}</h2>')
    elif line.startswith('### '):
        html_out.append(f'<h3>{fmt_line(line[4:])}</h3>')
    elif line.startswith('> '):
        if not in_quote:
            html_out.append('<blockquote>')
            in_quote = True
        html_out.append(fmt_line(line[2:]) + '<br>')
    elif line.startswith('---'):
        if in_quote:
            html_out.append('</blockquote>')
            in_quote = False
        if in_table:
            html_out.append('</table>')
            in_table = False
        html_out.append('<hr>')
    elif line.startswith('|'):
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if not in_table:
            html_out.append('<table>')
            in_table = True
        is_sep = all(p.startswith(':---') or p.startswith('---') or p.startswith('-') for p in parts if p)
        if is_sep:
            html_out.append('<thead><tr>' + ''.join(f'<th>{fmt_cell(h)}</th>' for h in prev_parts) + '</tr></thead>')
        else:
            html_out.append('<tr>' + ''.join(f'<td>{fmt_cell(c)}</td>' for c in parts) + '</tr>')
        prev_parts = parts
    else:
        if in_table:
            html_out.append('</table>')
            in_table = False
        if in_quote and not line.startswith('>') and line.strip():
            html_out.append('</blockquote>')
            in_quote = False
        if line.strip():
            html_out.append('<p>' + fmt_line(line) + '</p>')
        else:
            html_out.append('<br>')

if in_table:
    html_out.append('</table>')
if in_quote:
    html_out.append('</blockquote>')

html_out.append('</body></html>')
result = '\n'.join(html_out)

with open('G:/锅师/深度研究/0713-0719/2026-07-14_每日窄门筛股.html', 'w', encoding='utf-8') as f:
    f.write(result)
print(f'HTML generated: {len(result)} chars')
