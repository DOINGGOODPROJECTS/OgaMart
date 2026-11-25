import itertools
_n = itertools.count()
def uid(p='g'): return f'{p}{next(_n)}'
def hexrgb(c):
    c = c.lstrip('#'); c = ''.join(ch*2 for ch in c) if len(c) == 3 else c; return [int(c[i:i+2], 16) for i in (0, 2, 4)]
def mix(c, t, f): a, b = hexrgb(c), hexrgb(t); return '#%02X%02X%02X' % tuple(int(x + (y - x) * f) for x, y in zip(a, b))
def dk(c, f=0.25): return mix(c, '#000000', f)
def lt(c, f=0.3): return mix(c, '#FFFFFF', f)
def lg(c, horiz=True, a=0.28, b=0.22):
    i = uid('lg'); x2, y2 = ('1', '0') if horiz else ('0', '1')
    return i, f'<linearGradient id="{i}" x1="0" y1="0" x2="{x2}" y2="{y2}"><stop offset="0" stop-color="{lt(c, a)}"/><stop offset="0.45" stop-color="{c}"/><stop offset="1" stop-color="{dk(c, b)}"/></linearGradient>'
def rg(c, a=0.35, b=0.3):
    i = uid('rg'); return i, f'<radialGradient id="{i}" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="{lt(c, a)}"/><stop offset="0.5" stop-color="{c}"/><stop offset="1" stop-color="{dk(c, b)}"/></radialGradient>'
def grad_fill(c, kind='h', **k):
    i, d = (lg(c, kind == 'h', **k) if kind in 'hv' else rg(c, **k)); return f'url(#{i})', d
def txt(x, y, s, size, col='#fff', w=700, anchor='middle', font='Poppins, Arial, sans-serif'):
    s = str(s).replace('&amp;', '&').replace('&', '&amp;')
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" fill="{col}" text-anchor="{anchor}">{s}</text>'
NS = 'xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
def svg(body, vb, w, h): return f'<svg {NS} viewBox="{vb}" width="{w}" height="{h}">{body}</svg>'
def shadow(cx, cy, rx, ry, o=0.18): return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#000" opacity="{o}"/>'
