import sys, os, subprocess; sys.path.insert(0, '/home/claude/obj'); sys.path.insert(0, '/home/claude/label')
import common as C; from names import CHAR, nice
R = '/home/claude/pack2/OgaMart-GDevelop-Assets'; out = f'{R}/ui/name_tags'; os.makedirs(out, exist_ok=True); os.makedirs(f'{R}/source/ui/name_tags', exist_ok=True)
GRP = {'recurring': ('#24503B', '#E8B62C'), 'daniel_career': ('#24503B', '#E8B62C'), 'employees': ('#3B7DD8', '#FFFFFF'), 'customers': ('#7B3AA8', '#FFFFFF'), 'pedestrians': ('#5E6A73', '#FFFFFF')}
def tag(text, bg, fg, sub=None):
    w = max(180, 16.5 * len(text) + 64); h = 64 if not sub else 80
    b = f'<rect x="0" y="5" width="{w}" height="{h}" rx="{h/2}" fill="{C.dk(bg,.35)}"/><rect x="0" y="0" width="{w}" height="{h}" rx="{h/2}" fill="{bg}"/><rect x="10" y="5" width="{w-20}" height="{h*0.32}" rx="{h*0.16}" fill="#fff" opacity="0.15"/>'
    b += C.txt(w / 2, 41 if not sub else 37, text, 26, fg, 800) + (C.txt(w / 2, 64, sub, 14, fg, 600) if sub else '')
    return C.svg(b, f'-4 -4 {w+8} {h+14}', round((w + 8) * 1.5), round((h + 14) * 1.5))
def save(name, s):
    p = f'{R}/source/ui/name_tags/{name}.svg'; open(p, 'w').write(s); subprocess.run(['rsvg-convert', p, '-o', f'{out}/{name}.png'], check=True)
for g, (bg, fg) in GRP.items():
    for n in sorted(os.listdir(f'{R}/characters/{g}')): save(f'nametag_{n}', tag(CHAR[n], bg, fg))
for b in sorted(os.listdir(f'{R}/neighborhood/buildings')): save(f'buildingtag_{b}', tag(nice(b).replace(' (rival)', ''), '#FFFDF8', '#24503B'))
print(len(os.listdir(out)))
