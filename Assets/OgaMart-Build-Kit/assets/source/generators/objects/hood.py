# neighborhood buildings, front view, realistic flat-shaded. ground at y=H
from common import *
import random, math
def window(x, y, w, h, kind='glass', lit=False, frame='#F4F1EA', bars=False):
    gl = '#FFE7A3' if lit else '#9CC6DA'; f, d = grad_fill(gl, 'v', a=.35, b=.25)
    o = d + f'<rect x="{x-3}" y="{y-3}" width="{w+6}" height="{h+6}" fill="{frame}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}"/>'
    if kind == 'louvre': o += ''.join(f'<path d="M{x} {y+i*h/6} h{w}" stroke="{dk(gl,.3)}" stroke-width="2"/>' for i in range(1, 6))
    else: o += f'<path d="M{x+w/2} {y} v{h} M{x} {y+h*0.45} h{w}" stroke="{frame}" stroke-width="3"/><path d="M{x+4} {y+4} l{w*0.3} 0 l-{w*0.2} {h*0.6}z" fill="#fff" opacity="0.3"/>'
    if bars: o += ''.join(f'<path d="M{x+i*w/5} {y} v{h}" stroke="#3A3F44" stroke-width="2"/>' for i in range(1, 5))
    o += f'<rect x="{x-5}" y="{y+h+2}" width="{w+10}" height="5" fill="{dk(frame,.15)}"/>'
    return o
def awning(x, y, w, c1, c2='#F4F1EA', n=8):
    o = f'<path d="M{x} {y} H{x+w} L{x+w+10} {y+34} H{x-10}Z" fill="{c1}"/>' + ''.join(f'<path d="M{x+i*w/n} {y} L{x-10+i*(w+20)/n} {y+34} L{x-10+(i+1)*(w+20)/n} {y+34} L{x+(i+1)*w/n} {y}Z" fill="{c2}"/>' for i in range(0, n, 2))
    o += ''.join(f'<path d="M{x-10+i*(w+20)/n} {y+34} a{(w+20)/n/2} 8 0 0 0 {(w+20)/n} 0" fill="{c1 if i%2 else c2}"/>' for i in range(n))
    return o
def door(x, y, w, h, kind='glass', col='#5E3A26'):
    if kind == 'glass': return f'<rect x="{x-4}" y="{y-4}" width="{w+8}" height="{h+4}" fill="#8E979F"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#7FA9BE"/><path d="M{x+w/2} {y} v{h}" stroke="#8E979F" stroke-width="4"/><path d="M{x+6} {y+8} l14 0 l-10 60z" fill="#fff" opacity="0.3"/>'
    if kind == 'roller': return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#B4BBC2"/>' + ''.join(f'<path d="M{x} {y+i*8} h{w}" stroke="#8E979F" stroke-width="2"/>' for i in range(int(h / 8)))
    return f'<rect x="{x-4}" y="{y-4}" width="{w+8}" height="{h+4}" fill="{dk(col,.3)}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}"/><rect x="{x+8}" y="{y+10}" width="{w-16}" height="{h*0.35}" fill="{dk(col,.15)}"/><rect x="{x+8}" y="{y+h*0.55}" width="{w-16}" height="{h*0.35}" fill="{dk(col,.15)}"/><circle cx="{x+w-10}" cy="{y+h/2}" r="3" fill="#E8B62C"/>'
def signboard(x, y, w, text, bg, fg='#fff', h=40, icon=None):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{dk(bg,.3)}"/><rect x="{x+3}" y="{y+3}" width="{w-6}" height="{h-6}" rx="4" fill="{bg}"/>' + txt(x + w / 2 + (10 if icon else 0), y + h * 0.66, text, min(h * 0.5, w / max(6, len(text)) * 1.5), fg, 800)
    if icon: o += f'<g transform="translate({x+18} {y+h/2})">{icon}</g>'
    return o
ICON = {'cup': '<path d="M-9 -6 h14 v8 a7 7 0 0 1 -14 0z" fill="#fff"/><path d="M5 -3 a4 4 0 0 1 0 7" stroke="#fff" stroke-width="2" fill="none"/>', 'bread': '<path d="M-10 6 v-6 a10 8 0 0 1 20 0 v6z" fill="#fff"/>',
        'apple': '<circle r="8" fill="#fff"/><path d="M0 -8 l3 -4" stroke="#fff" stroke-width="2"/>', 'fork': '<path d="M-4 -10 v20 M-8 -10 v6 a4 4 0 0 0 8 0 v-6 M6 -10 v20" stroke="#fff" stroke-width="2.4" fill="none"/>',
        'flower': ''.join(f'<circle cx="{5*math.cos(a*1.2566)}" cy="{5*math.sin(a*1.2566)}" r="4" fill="#fff"/>' for a in range(5)), 'film': '<rect x="-10" y="-8" width="20" height="16" rx="2" fill="#fff"/><path d="M-6 -8 v16 M6 -8 v16" stroke="#333" stroke-width="2"/>',
        'cross': '<path d="M-3 -10 h6 v7 h7 v6 h-7 v7 h-6 v-7 h-7 v-6 h7z" fill="#fff"/>', 'shirt': '<path d="M-10 -6 l6 -4 h8 l6 4 l-3 5 l-3 -2 v12 h-8 v-12 l-3 2z" fill="#fff"/>', 'bolt': '<path d="M2 -10 l-8 12 h6 l-2 8 l8 -12 h-6z" fill="#fff"/>',
        'dumbbell': '<path d="M-10 0 h20" stroke="#fff" stroke-width="3"/><rect x="-12" y="-6" width="4" height="12" fill="#fff"/><rect x="8" y="-6" width="4" height="12" fill="#fff"/>', 'bed': '<path d="M-10 6 v-12 M-10 2 h20 v4 M-6 -2 h14 v4" stroke="#fff" stroke-width="2.4" fill="none"/>',
        'cart': '<path d="M-10 -6 h4 l3 10 h10 l3 -8 h-14" stroke="#fff" stroke-width="2.4" fill="none"/><circle cx="-1" cy="7" r="2" fill="#fff"/><circle cx="7" cy="7" r="2" fill="#fff"/>', 'box': '<rect x="-9" y="-7" width="18" height="14" fill="#fff"/><path d="M-9 -2 h18" stroke="#333"/>',
        'truck': '<rect x="-11" y="-6" width="13" height="10" fill="#fff"/><path d="M2 -2 h6 l3 4 v2 h-9z" fill="#fff"/><circle cx="-6" cy="6" r="2.4" fill="#fff"/><circle cx="6" cy="6" r="2.4" fill="#fff"/>', 'book': '<path d="M-10 -7 q5 -2 10 1 q5 -3 10 -1 v14 q-5 -2 -10 1 q-5 -3 -10 -1z" fill="#fff"/>',
        'pepper': '<path d="M-4 -6 c-4 8 0 16 6 16 c2 -6 2 -12 -2 -16z" fill="#fff"/>', 'cookie': '<circle r="8" fill="#fff"/><circle cx="-3" cy="-2" r="1.5" fill="#333"/><circle cx="3" cy="2" r="1.5" fill="#333"/>', 'crown': '<path d="M-10 6 v-12 l5 6 l5 -8 l5 8 l5 -6 v12z" fill="#fff"/>'}
# building specs: (title, wall, accent, icon, kind)
SPEC = {
 'coffee_shop': ('COFFEE', '#E9D8BE', '#6B4226', 'cup', 'shop'), 'bakery': ('BAKERY', '#F4E1B8', '#C8412E', 'bread', 'shop'), 'fruit_shop': ('FRUIT SHOP', '#E7F0D8', '#3E7D4A', 'apple', 'stall'),
 'restaurant': ('RESTAURANT', '#F2D9C4', '#B8324A', 'fork', 'shop'), 'flower_shop': ('FLOWERS', '#F9E1EA', '#E2435E', 'flower', 'shop'), 'cinema': ('CINEMA', '#3A3F5C', '#E8B62C', 'film', 'cinema'),
 'school': ('SCHOOL', '#F5E9C8', '#3B7DD8', 'book', 'school'), 'shopping_mall': ('MALL', '#DCE1E6', '#7B3AA8', 'cart', 'mall'), 'residential': ('', '#E9D2B4', '#8C4B32', None, 'house'),
 'supermarket_branch': ('OGAMART', '#F4F1EA', '#24503B', 'cart', 'super'), 'warehouse': ('WAREHOUSE', '#B4BBC2', '#F28C28', 'box', 'warehouse'), 'delivery_center': ('DELIVERY', '#E6E9EC', '#F28C28', 'truck', 'warehouse'),
 'clothing_store': ('FASHION', '#F2E6F4', '#7B3AA8', 'shirt', 'shop'), 'pharmacy': ('PHARMACY', '#E8F5EE', '#1E8C4E', 'cross', 'shop'), 'electronics_store': ('ELECTRONICS', '#E3E8F2', '#3B7DD8', 'bolt', 'shop'),
 'fitness_center': ('FITNESS', '#E6E9EC', '#E2435E', 'dumbbell', 'mall'), 'hotel': ('HOTEL', '#EFE3D0', '#C9A23A', 'bed', 'hotel'),
 'brooks_store': ("BROOKS MART", '#DCD3E8', '#2B3A55', 'crown', 'super'), 'sofia_snacks': ("SOFIA'S SNACKS", '#FCE3C8', '#F28C28', 'cookie', 'shop'), 'pepper_food_spot': ("AUNTIE PEPPER", '#F9D6CC', '#D62828', 'pepper', 'stall'),
}
LEVEL_FLOORS = {'shop': (1, 2, 3), 'stall': (1, 1, 2), 'cinema': (1, 2, 2), 'school': (1, 2, 3), 'mall': (2, 3, 4), 'house': (1, 2, 4), 'super': (1, 2, 3), 'warehouse': (1, 1, 2), 'hotel': (2, 4, 6)}
LEVEL_W = {'shop': (260, 300, 340), 'stall': (240, 280, 320), 'cinema': (340, 380, 420), 'school': (360, 420, 480), 'mall': (440, 500, 560), 'house': (240, 280, 320), 'super': (360, 420, 480), 'warehouse': (380, 420, 460), 'hotel': (300, 340, 380)}
FH = 110
def building(key, level, sign=True):  # level 0 basic,1 established,2 premium
    title, wall, acc, icon, kind = SPEC[key]; nf = LEVEL_FLOORS[kind][level]; W = LEVEL_W[kind][level]
    H = 40 + nf * FH + (50 if kind != 'house' else 70); r = random.Random(hash((key, level)) & 0xffff)
    base = H; top = H - nf * FH - 20
    o = shadow(W / 2, H + 4, W / 2 + 20, 10, 0.15)
    wcol = wall if level else mix(wall, '#B8A487', 0.25)
    f, d = grad_fill(wcol, 'h', a=.12, b=.14); o += d
    glass = level == 2 and kind in ('mall', 'hotel', 'super', 'cinema', 'shop')
    # roof
    if kind == 'house' or (level == 0 and kind in ('shop', 'stall', 'super')):
        zinc = '#9AA3A8' if level < 2 else '#8C3B2E'; rc = uid('rf')
        o += f'<clipPath id="{rc}"><path d="M-16 {top+20} L{W/2} {top-50} L{W+16} {top+20}Z"/></clipPath><path d="M-16 {top+20} L{W/2} {top-50} L{W+16} {top+20}Z" fill="{zinc}"/>'
        o += ''.join(f'<path d="M{-16+i*(W+32)/22} {top-60} V{top+24}" stroke="{dk(zinc,.15)}" stroke-width="2" clip-path="url(#{rc})"/>' for i in range(23))
        o += f'<path d="M{W/2} {top-50} L{W+16} {top+20} L{W/2} {top+20}Z" fill="#000" opacity="0.1"/>'
        o += f'<rect x="-16" y="{top+16}" width="{W+32}" height="8" fill="{dk(zinc,.25)}"/>'
        if level == 0: o += f'<path d="M{W*0.2} {top-10} l40 -6" stroke="#8B6A4A" stroke-width="4"/><rect x="{W*0.6}" y="{top-30}" width="16" height="10" fill="#B5653E" transform="rotate(-20 {W*0.6} {top-30})"/>'
    else:
        o += f'<rect x="-8" y="{top}" width="{W+16}" height="24" fill="{dk(wcol,.2)}"/><rect x="-8" y="{top}" width="{W+16}" height="6" fill="{lt(wcol,.2)}"/>'
        if kind in ('warehouse',): o += f'<path d="M-8 {top} Q{W/2} {top-60} {W+8} {top}Z" fill="#8E979F"/>' + ''.join(f'<path d="M{x} {top} Q{W/2} {top-60+abs(x-W/2)*0.0} {x} {top}" />' for x in [])
        if level == 2 and kind in ('mall', 'hotel'): o += f'<rect x="{W/2-50}" y="{top-30}" width="100" height="30" fill="{acc}"/>' + txt(W / 2, top - 9, '★ ★ ★' if kind == 'hotel' else title[:10], 14, '#fff')
        if kind != 'warehouse' and level >= 1: o += f'<rect x="{W*0.75}" y="{top-26}" width="40" height="26" fill="#3A6EA5"/><rect x="{W*0.75+4}" y="{top-36}" width="32" height="12" rx="6" fill="#3A6EA5"/>'
    o += f'<rect x="0" y="{top+20}" width="{W}" height="{H-top-20}" fill="{f}"/>'
    if glass:
        o += f'<rect x="12" y="{top+30}" width="{W-24}" height="{H-top-110}" fill="#7FB3CF"/>' + ''.join(f'<path d="M{12+i*(W-24)/8} {top+30} v{H-top-110}" stroke="#DCE6EC" stroke-width="3"/>' for i in range(9)) + ''.join(f'<path d="M12 {top+30+j*FH} h{W-24}" stroke="#DCE6EC" stroke-width="5"/>' for j in range(nf)) + f'<path d="M20 {top+40} l60 0 l-40 {nf*FH-40}z" fill="#fff" opacity="0.2"/>'
    else:
        for fl in range(1, nf):
            y = base - 40 - fl * FH; n = max(2, int(W / 90))
            for i in range(n):
                wx = 24 + i * (W - 48) / n + ((W - 48) / n - 50) / 2
                o += window(wx, y + 20, 50, 56, 'louvre' if level == 0 else 'glass', lit=r.random() < 0.25, bars=level == 0)
            if level >= 1 and kind in ('house', 'hotel'): o += f'<rect x="10" y="{y+80}" width="{W-20}" height="6" fill="{dk(wcol,.25)}"/>' + ''.join(f'<path d="M{14+i*12} {y+86} v-22" stroke="{dk(wcol,.35)}" stroke-width="2"/>' for i in range(int((W - 20) / 12)))
            o += f'<path d="M0 {y+FH} H{W}" stroke="{dk(wcol,.1)}" stroke-width="3"/>'
    # ground floor
    gy = base - 40 - FH + 10
    if kind in ('shop', 'super', 'mall', 'cinema', 'hotel'):
        o += window(20, gy + 30, W * 0.32, 70, lit=level == 2) + window(W - 20 - W * 0.32, gy + 30, W * 0.32, 70, lit=level == 2)
        o += door(W / 2 - 30, gy + 26, 60, base - gy - 26, 'glass' if level else 'wood', acc)
        if kind == 'cinema': o += ''.join(f'<rect x="{30+i*(W-60)/3}" y="{gy+36}" width="{(W-60)/3-16}" height="60" fill="#1F1B18"/><rect x="{34+i*(W-60)/3}" y="{gy+40}" width="{(W-60)/3-24}" height="52" fill="{["#E2435E","#3B7DD8","#E8B62C"][i]}"/>' for i in (0, 2))
        if kind in ('shop', 'super'): o += awning(10, gy - 4, W - 20, acc)
    elif kind == 'stall':
        o += f'<rect x="10" y="{gy+40}" width="{W-20}" height="{base-gy-40}" fill="{dk(wcol,.35)}"/><rect x="0" y="{base-60}" width="{W}" height="60" fill="#8B5A3C"/>' + ''.join(f'<path d="M0 {base-60+i*15} h{W}" stroke="#6E4630" stroke-width="2"/>' for i in range(4))
        import products as P
        goods = ['tomatoes', 'peppers', 'oranges', 'plantain', 'yam', 'mangoes'] if key == 'fruit_shop' else ['peppers', 'tomatoes', 'onions', 'yam', 'spices', 'palm_oil']
        o += ''.join(f'<g transform="translate({40+i*(W-80)/5} {base-56}) scale(0.5) translate(-50 -92)">{P.CATALOG[g]()}</g>' for i, g in enumerate(goods))
        o += awning(0, gy - 4, W, acc, n=10)
        if key == 'pepper_food_spot': o += f'<g transform="translate({W-60} {base-90})"><ellipse cx="0" cy="0" rx="26" ry="6" fill="#3A3F44"/><path d="M-26 0 h52 v20 a8 8 0 0 1 -8 8 h-36 a8 8 0 0 1 -8 -8z" fill="#4A5056"/><path d="M-8 -6 q-4 -10 0 -18 M6 -6 q4 -10 0 -18" stroke="#C9C1B4" stroke-width="2.4" fill="none"/></g>'
    elif kind == 'school':
        o += door(W / 2 - 40, gy + 30, 80, base - gy - 30, 'wood', '#3B7DD8') + ''.join(window(30 + i * (W - 60) / 4 + (0 if i < 2 else 90), gy + 36, 54, 56) for i in range(4) if True)
        o += f'<path d="M{W/2} {top-10} v-70" stroke="#8E979F" stroke-width="4"/><rect x="{W/2}" y="{top-80}" width="44" height="28" fill="#1E8C4E"/><rect x="{W/2+14.6}" y="{top-80}" width="14.6" height="28" fill="#fff"/>'
    elif kind == 'house':
        o += door(W / 2 - 26, gy + 30, 52, base - gy - 30, 'wood', '#5E3A26') + window(30, gy + 36, 60, 60, 'louvre' if level == 0 else 'glass', bars=True) + window(W - 90, gy + 36, 60, 60, 'louvre' if level == 0 else 'glass', bars=True)
        if level >= 1: o += f'<rect x="{W-60}" y="{top-40}" width="44" height="40" rx="6" fill="#2C5FA8"/><rect x="{W-56}" y="{top-48}" width="36" height="10" rx="4" fill="#2C5FA8"/>'
        if level == 0: o += f'<path d="M30 {gy+20} h{W-60}" stroke="#7FA9BE" stroke-width="2"/>' + ''.join(f'<rect x="{40+i*30}" y="{gy+20}" width="18" height="24" fill="{c}"/>' for i, c in enumerate(['#E2435E', '#F5C542', '#3B7DD8']))
    elif kind == 'warehouse':
        o += door(30, gy + 20, W * 0.4, base - gy - 20, 'roller') + door(W - 30 - W * 0.4, gy + 20, W * 0.4, base - gy - 20, 'roller' if level else 'roller') + f'<rect x="0" y="{base-8}" width="{W}" height="8" fill="#F5C542"/>' + ''.join(f'<path d="M{i*24} {base-8} l12 8" stroke="#2B2B2B" stroke-width="5"/>' for i in range(int(W / 24) + 1))
    # sign
    if title and sign:
        sw = min(W - 40, 40 + len(title) * 16)
        sy = top + 28 if kind not in ('shop', 'super') or nf == 1 else gy - 52
        if kind == 'house': sy = None
        if sy is not None: o += signboard(W / 2 - sw / 2, sy if nf > 1 else gy - 48, sw, title, acc, icon=ICON.get(icon), h=38 if level else 32)
    if level == 0: o += ''.join(f'<path d="M{r.uniform(10,W-30)} {r.uniform(top+40,base-20)} q8 4 14 0" stroke="{dk(wcol,.3)}" stroke-width="1.6" fill="none" opacity="0.6"/>' for _ in range(6))
    if level == 2: o += ''.join(f'<circle cx="{20+i*(W-40)/9}" cy="{top+24}" r="3" fill="#FFE7A3"/>' for i in range(10)) + f'<rect x="-20" y="{base-6}" width="{W+40}" height="10" fill="#C9C1B4"/>'
    o += f'<rect x="-10" y="{base-4}" width="{W+20}" height="8" fill="#8E8476"/>'
    return o, f'-40 {top-110} {W+80} {H-top+130}'
def ogamart(style):
    lv = {'corner_shop': 0, 'traditional': 0, 'modern_mini': 1, 'neighborhood': 1, 'premium': 2, 'superstore': 2, 'mega_market': 2}[style]
    import store as S
    b, vb = building('supermarket_branch', lv, sign=False)
    x0, y0, w, h = map(float, vb.split())
    if style in ('superstore', 'mega_market'):
        b2, vb2 = building('shopping_mall', 2 if style == 'mega_market' else 1, sign=False); b = b2; vb = vb2; x0, y0, w, h = map(float, vb.split())
    sg, svb = S.sign(style); sx0, sy0, sw, sh = map(float, svb.split()); sc = (w - 120) / sw * 0.7
    W = w - 80
    if lv == 0: sc *= 0.85
    top = y0 + 110
    return b + f'<g transform="translate({W/2 - sw*sc/2} {top - sh*sc + 14}) scale({sc})">{sg}</g>', vb
def construction(stage):
    W, H = 360, 360; o = shadow(W / 2, H + 4, W / 2 + 10, 8) + f'<rect x="0" y="{H-20}" width="{W}" height="20" fill="#9C8466"/>'
    nf = stage + 1
    for f in range(nf): o += f'<rect x="30" y="{H-20-(f+1)*90}" width="{W-60}" height="90" fill="#B9B0A2"/>' + ''.join(f'<rect x="{50+i*70}" y="{H-20-(f+1)*90+20}" width="40" height="50" fill="#5A5148"/>' for i in range(4))
    for f in range(nf + 1):
        y = H - 20 - f * 90; o += f'<path d="M14 {y} H{W-14}" stroke="#D9A030" stroke-width="5"/>'
    o += ''.join(f'<path d="M{x} {H-20} V{H-20-nf*90-20}" stroke="#8E979F" stroke-width="5"/>' for x in (14, W / 2, W - 14))
    o += ''.join(f'<path d="M14 {H-20-f*90} L{W/2} {H-20-(f+1)*90}" stroke="#8E979F" stroke-width="2"/>' for f in range(nf))
    o += f'<path d="M{W-40} {H-20} V30 M{W-40} 40 H{W-280}" stroke="#F2B233" stroke-width="10"/><path d="M{W-40} 40 L{W-20} 60 M{W-40} 30 L{W-60} 50" stroke="#F2B233" stroke-width="4"/><path d="M{W-240} 40 v80" stroke="#444" stroke-width="2"/><rect x="{W-256}" y="120" width="32" height="20" fill="#B5653E"/>'
    o += f'<rect x="20" y="{H-50}" width="80" height="30" fill="#F5C542"/>' + ''.join(f'<path d="M{20+i*16} {H-50} l16 30" stroke="#2B2B2B" stroke-width="5"/>' for i in range(5)) + txt(W / 2, H - 26, 'UNDER CONSTRUCTION', 12, '#2B2B2B')
    return o, f'-20 -10 {W+40} {H+30}'
def plot(kind):
    W, H = 360, 140; col = {'commercial': '#C9B79C', 'residential': '#9DBF7A', 'locked': '#9C9C9C'}[kind]
    o = f'<path d="M30 20 H{W-30} L{W} {H} H0Z" fill="{col}"/><path d="M30 20 H{W-30} L{W} {H} H0Z" fill="none" stroke="#F4F1EA" stroke-width="4" stroke-dasharray="14 10"/>'
    o += f'<path d="M{W/2} {H/2+20} v-60" stroke="#8B6A4A" stroke-width="5"/><rect x="{W/2-50}" y="{H/2-60}" width="100" height="40" rx="4" fill="#F4F1EA"/>' + txt(W / 2, H / 2 - 34, {'commercial': 'FOR BUSINESS', 'residential': 'FOR HOMES', 'locked': 'LOCKED'}[kind], 11, '#24503B')
    if kind == 'locked': o += f'<g transform="translate({W/2} {H/2+50})"><rect x="-16" y="-10" width="32" height="26" rx="4" fill="#E8B62C"/><path d="M-10 -10 v-8 a10 10 0 0 1 20 0 v8" stroke="#E8B62C" stroke-width="5" fill="none"/></g>'
    return o, f'-10 -50 {W+20} {H+60}'
def park(level):
    W = 420 + level * 60; H = 260; o = f'<ellipse cx="{W/2}" cy="{H-40}" rx="{W/2}" ry="60" fill="#7FB35A"/><ellipse cx="{W/2}" cy="{H-44}" rx="{W/2-20}" ry="50" fill="#8DC26F"/>'
    o += f'<path d="M{W/2-30} {H} Q{W/2} {H-60} {W/2+40} {H-100}" stroke="#E8D9B5" stroke-width="22" fill="none"/>'
    import env
    for x, k in [(60, 'mango'), (W - 70, 'palm')] + ([(W / 2 + 100, 'round')] if level >= 1 else []):
        t, tvb = env.tree(k); tx0, ty0, tw, th = map(float, tvb.split()); s = 150 / th
        o += f'<g transform="translate({x - tw*s/2} {H-60-th*s}) scale({s}) translate({-tx0} {-ty0})">{t}</g>'
    b, bvb = env.bench(); o += f'<g transform="translate({W/2-120} {H-110}) scale(0.6)">{b}</g>'
    if level >= 1: fb, fvb = env.fountain(); o += f'<g transform="translate({W/2-40} {H-150}) scale(0.7)">{fb}</g>'
    if level >= 2: o += ''.join(f'<g transform="translate({40+i*60} {H-30}) scale(0.4)">{env.flowerbed()[0]}</g>' for i in range(int(W / 60)))
    return o, f'-10 -40 {W+20} {H+50}'
def farm(level):
    W = 460; H = 300; o = f'<rect x="0" y="120" width="{W}" height="{H-120}" fill="#9DBF7A"/>'
    for r in range(4): o += f'<path d="M0 {170+r*30} Q{W/2} {160+r*30} {W} {170+r*30}" stroke="#7A5A3A" stroke-width="12" fill="none"/>' + ''.join(f'<circle cx="{20+i*30}" cy="{164+r*30}" r="7" fill="{["#4E9A4F","#D63A2A","#F28C28","#4E9A4F"][r]}"/>' for i in range(15))
    o += f'<path d="M260 120 L330 60 L400 120Z" fill="#B8324A"/><rect x="270" y="120" width="120" height="60" fill="#C8412E"/><rect x="310" y="136" width="40" height="44" fill="#F4F1EA"/><path d="M310 136 l40 44 M350 136 l-40 44" stroke="#C8412E" stroke-width="4"/>'
    if level >= 1: o += '<rect x="420" y="40" width="30" height="140" fill="#B4BBC2"/><ellipse cx="435" cy="40" rx="15" ry="8" fill="#8E979F"/>'
    if level >= 2: o += '<path d="M30 40 h160 v80 h-160z" fill="#DCEFF7" opacity="0.8"/><path d="M30 40 l80 -30 l80 30" fill="#C9E4EF"/>' + ''.join(f'<path d="M{30+i*20} 40 v80" stroke="#fff"/>' for i in range(9))
    o += ''.join(f'<path d="M{i*24} {H-20} v-26 M{i*24-12} {H-34} h24" stroke="#8B6A4A" stroke-width="4"/>' for i in range(int(W / 24) + 1))
    return o, f'-10 0 {W+20} {H+10}'
