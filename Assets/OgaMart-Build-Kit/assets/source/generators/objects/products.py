# 48 product icons, realistic flat-shaded, drawn in a 100x100 box centred on (50, 50), base on y=92
from common import *
def bag(label, col, txtcol='#fff', w=46, h=64, window=None, sub=''):
    f, d = grad_fill(col); x = 50 - w / 2; y = 92 - h
    o = d + shadow(50, 93, w / 2 + 4, 4)
    o += f'<path d="M{x+3} {y+8} Q{x} {y+4} {x+4} {y} L{x+w-4} {y} Q{x+w} {y+4} {x+w-3} {y+8} L{x+w} {y+h-4} Q{x+w} {y+h} {x+w-4} {y+h} L{x+4} {y+h} Q{x} {y+h} {x} {y+h-4}Z" fill="{f}"/>'
    o += f'<path d="M{x+4} {y+1} L{x+w-4} {y+1} L{x+w-4} {y+6} L{x+4} {y+6}Z" fill="{dk(col, .3)}"/>' + ''.join(f'<path d="M{x+6+i*4} {y+1} v5" stroke="{lt(col, .3)}" stroke-width="1"/>' for i in range(int((w - 10) / 4)))
    if window: o += f'<rect x="{x+8}" y="{y+h*0.42}" width="{w-16}" height="{h*0.3}" rx="4" fill="{window}"/><rect x="{x+10}" y="{y+h*0.44}" width="{(w-16)*0.3}" height="{h*0.08}" rx="2" fill="#fff" opacity="0.5"/>'
    o += txt(50, y + h * 0.32, label, 9 if len(label) < 8 else 7, txtcol)
    if sub: o += txt(50, y + h * 0.9, sub, 6, txtcol, 600)
    o += f'<path d="M{x+4} {y+10} L{x+4} {y+h-6}" stroke="#fff" stroke-width="3" opacity="0.25" stroke-linecap="round"/>'
    return o
def bottle(label, col, cap, liquid=None, w=26, h=78, glass=False):
    x = 50 - w / 2; y = 92 - h; f, d = grad_fill(liquid or col)
    o = d + shadow(50, 93, w / 2 + 3, 3)
    body = f'M{x+w*0.36} {y} h{w*0.28} v{h*0.12} C{x+w*0.7} {y+h*0.2} {x+w} {y+h*0.24} {x+w} {y+h*0.34} V{y+h-3} Q{x+w} {y+h} {x+w-3} {y+h} H{x+3} Q{x} {y+h} {x} {y+h-3} V{y+h*0.34} C{x} {y+h*0.24} {x+w*0.3} {y+h*0.2} {x+w*0.36} {y+h*0.12}Z'
    o += f'<path d="{body}" fill="{f}" {"fill-opacity=\"0.9\"" if glass else ""}/>'
    o += f'<rect x="{x+w*0.33}" y="{y-6}" width="{w*0.34}" height="8" rx="2" fill="{cap}"/>'
    o += f'<rect x="{x}" y="{y+h*0.46}" width="{w}" height="{h*0.3}" fill="{col if liquid else lt(col, .85)}"/>' + txt(50, y + h * 0.65, label, 7 if len(label) < 6 else 5.5, '#fff' if liquid else dk(col, .4))
    o += f'<path d="M{x+4} {y+h*0.36} V{y+h-6}" stroke="#fff" stroke-width="3" opacity="0.35" stroke-linecap="round"/>'
    return o
def carton(label, col, top='#FFFFFF', w=34, h=66):
    x = 50 - w / 2; y = 92 - h; f, d = grad_fill(col)
    o = d + shadow(50, 93, w / 2 + 6, 3)
    o += f'<path d="M{x} {y+12} L{x+w*0.5} {y} L{x+w} {y+12}Z" fill="{dk(top, .08)}"/><rect x="{x+w*0.4}" y="{y-4}" width="{w*0.2}" height="6" fill="{top}"/>'
    o += f'<rect x="{x}" y="{y+12}" width="{w}" height="{h-12}" fill="{top}"/><rect x="{x}" y="{y+h*0.38}" width="{w}" height="{h*0.62}" fill="{f}"/>'
    o += f'<rect x="{x+w*0.7}" y="{y+12}" width="{w*0.3}" height="{h-12}" fill="#000" opacity="0.12"/>' + txt(50 - w * 0.1, y + h * 0.66, label, 7)
    return o
def box(label, col, w=50, h=62, art=None, txtcol='#fff'):
    x = 50 - w / 2; y = 92 - h; f, d = grad_fill(col)
    o = d + shadow(50, 93, w / 2 + 4, 3) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{f}"/><path d="M{x} {y} l6 -6 h{w} l-6 6z" fill="{lt(col, .25)}"/><path d="M{x+w} {y} l6 -6 v{h} l-6 6z" fill="{dk(col, .3)}"/>'
    o += (art or '') + txt(50, y + 16, label, 9 if len(label) < 8 else 7, txtcol)
    return o
def can(label, col, w=34, h=40, lid='#C9C9CE'):
    x = 50 - w / 2; y = 92 - h; f, d = grad_fill(col)
    return (d + shadow(50, 93, w / 2 + 3, 3) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}"/><ellipse cx="50" cy="{y}" rx="{w/2}" ry="4" fill="{lid}"/><ellipse cx="50" cy="{y}" rx="{w/2-3}" ry="2.6" fill="{dk(lid, .15)}"/>'
            f'<ellipse cx="50" cy="{y+h}" rx="{w/2}" ry="4" fill="{dk(col, .3)}"/><path d="M{x} {y+6} h{w} M{x} {y+h-6} h{w}" stroke="{lid}" stroke-width="1.5"/>' + txt(50, y + h * 0.6, label, 7))
def jar(label, col, lid, w=40, h=48):
    x = 50 - w / 2; y = 92 - h; f, d = grad_fill(col)
    return (d + shadow(50, 93, w / 2 + 3, 3) + f'<rect x="{x}" y="{y+8}" width="{w}" height="{h-8}" rx="8" fill="{f}" fill-opacity="0.95"/><rect x="{x+4}" y="{y}" width="{w-8}" height="10" rx="2" fill="{lid}"/>'
            f'<rect x="{x}" y="{y+h*0.42}" width="{w}" height="{h*0.32}" fill="#F4E9D8"/>' + txt(50, y + h * 0.64, label, 7, dk(col, .4)) + f'<path d="M{x+5} {y+14} v{h-24}" stroke="#fff" stroke-width="3" opacity="0.35" stroke-linecap="round"/>')
def fruit(col, r=12, cx=50, cy=80, stem='#3E7D4A', leaf=True, shape='round'):
    f, d = grad_fill(col, 'r')
    if shape == 'round': b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{f}"/>'
    elif shape == 'oval': b = f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*1.25}" fill="{f}"/>'
    elif shape == 'pepper': b = f'<path d="M{cx-r*0.8} {cy-r*0.6} C{cx-r} {cy+r*0.6} {cx-r*0.3} {cy+r*1.5} {cx+r*0.1} {cy+r*1.6} C{cx+r*0.4} {cy+r*1.2} {cx+r} {cy+r*0.4} {cx+r*0.8} {cy-r*0.6} Q{cx} {cy-r} {cx-r*0.8} {cy-r*0.6}Z" fill="{f}"/>'
    o = d + b + f'<path d="M{cx} {cy-r*(1.25 if shape == "oval" else 1)} q1 -5 4 -6" stroke="{stem}" stroke-width="2" fill="none"/>'
    if leaf: o += f'<path d="M{cx+2} {cy-r-3} q8 -6 12 0 q-6 4 -12 0z" fill="#4E9A4F"/>'
    return o
def pile(col, n=5, leaf=True, **k):
    pos = [(36, 82), (64, 82), (50, 82), (43, 66), (57, 66), (50, 52)][:n]
    return shadow(50, 93, 30, 4) + ''.join(fruit(col, cx=x, cy=y, leaf=leaf and (i == len(pos) - 1), **k) for i, (x, y) in enumerate(pos))
def plantain():
    o = shadow(50, 92, 32, 4)
    for i, dy in enumerate((0, -7, -14)):
        f, d = grad_fill('#E3C233' if i else '#D9B42C', 'v')
        o += d + f'<path d="M14 {78+dy} C24 {96+dy} 70 {98+dy} 88 {70+dy} L86 {66+dy} C70 {88+dy} 32 {88+dy} 18 {72+dy}Z" fill="{f}"/><path d="M86 {66+dy} l6 -4" stroke="#5B4030" stroke-width="3"/><circle cx="{40+i*8}" cy="{86+dy}" r="1.4" fill="#5B4030"/>'
    return o
def yam():
    f, d = grad_fill('#8C6A4A', 'v')
    return d + shadow(50, 93, 36, 4) + f'<path d="M12 80 C10 64 30 58 50 60 C70 62 92 66 90 80 C88 92 60 94 46 92 C28 92 14 90 12 80Z" fill="{f}"/>' + ''.join(f'<path d="M{x} {y} q3 2 6 0" stroke="#5B4030" stroke-width="1.4" fill="none"/>' for x, y in [(24, 72), (40, 80), (58, 70), (72, 82), (34, 86), (64, 86)]) + '<ellipse cx="88" cy="76" rx="4" ry="7" fill="#F4E9D8"/>'
def eggs():
    o = shadow(50, 93, 40, 4) + '<path d="M8 74 H92 L88 92 H12Z" fill="#C9B79C"/><path d="M8 74 H92" stroke="#A8957A" stroke-width="2"/>'
    for r in range(2):
        for i in range(5):
            f, d = grad_fill('#F1DCC0', 'r'); o += d + f'<ellipse cx="{18+i*16}" cy="{70-r*10+ (4 if r else 0)}" rx="7" ry="9" fill="{f}"/>'
    return o
def bread():
    f, d = grad_fill('#C98A4B', 'v')
    return d + shadow(50, 93, 40, 4) + f'<path d="M10 90 V60 C10 40 30 34 50 34 C70 34 90 40 90 60 V90Z" fill="{f}"/>' + ''.join(f'<path d="M{26+i*16} 44 q6 8 2 18" stroke="#8C5A2E" stroke-width="2.4" fill="none"/>' for i in range(4)) + '<path d="M16 58 C18 46 30 40 42 40" stroke="#fff" stroke-width="3" opacity="0.3" fill="none"/>'
def baguette():
    o = shadow(50, 93, 40, 4)
    for i, a in enumerate((-30, -18)):
        f, d = grad_fill('#D9A05B', 'v'); o += d + f'<g transform="rotate({a} 50 70)"><rect x="6" y="{62+i*10}" width="88" height="14" rx="7" fill="{f}"/>' + ''.join(f'<path d="M{18+j*16} {64+i*10} l8 10" stroke="#9A6430" stroke-width="2"/>' for j in range(5)) + '</g>'
    return o
def chicken():
    o = shadow(50, 93, 40, 4) + '<rect x="8" y="58" width="84" height="34" rx="4" fill="#E8EEF2"/>'
    f, d = grad_fill('#F2C8A0', 'r')
    o += d + f'<path d="M20 86 C14 70 30 60 50 62 C72 64 86 70 80 84 Z" fill="{f}"/><path d="M76 74 l12 -8 q4 0 2 4 l-10 8" fill="{f}"/><path d="M24 74 l-12 -8 q-4 0 -2 4 l10 8" fill="{f}"/>'
    return o + '<rect x="8" y="58" width="84" height="34" rx="4" fill="#BFE3F2" opacity="0.35"/><rect x="30" y="80" width="40" height="10" rx="2" fill="#3B7DD8"/>' + txt(50, 88, 'FROZEN', 7)
def fish():
    f, d = grad_fill('#9FB3C2', 'v')
    return d + shadow(50, 93, 40, 4) + f'<path d="M10 74 C30 54 66 56 80 72 L94 62 L92 86 L80 78 C64 92 30 92 10 74Z" fill="{f}"/><circle cx="22" cy="72" r="3" fill="#1A1A1A"/><path d="M36 64 q6 10 0 20 M48 62 q6 12 0 24" stroke="#7E92A0" stroke-width="1.6" fill="none"/>'
def icecream():
    f, d = grad_fill('#F7B7C8')
    return d + shadow(50, 93, 30, 4) + f'<path d="M22 52 H78 L72 92 H28Z" fill="{f}"/><ellipse cx="50" cy="52" rx="28" ry="7" fill="#F4F1EA"/><ellipse cx="50" cy="50" rx="24" ry="5" fill="#8C5A3C"/>' + txt(50, 78, 'ICE', 9, '#B8324A')
def pastry():
    f, d = grad_fill('#D9A05B', 'r')
    return d + shadow(50, 93, 36, 4) + f'<path d="M12 88 C12 60 30 50 50 50 C70 50 88 60 88 88Z" fill="{f}"/>' + ''.join(f'<path d="M{20+i*12} 86 q-2 -10 2 -16" stroke="#A86A30" stroke-width="2" fill="none"/>' for i in range(6))
def doughnut():
    f, d = grad_fill('#C98A4B', 'r')
    return d + shadow(50, 93, 34, 4) + f'<ellipse cx="50" cy="74" rx="34" ry="18" fill="{f}"/><ellipse cx="50" cy="70" rx="30" ry="14" fill="#E2435E"/><ellipse cx="50" cy="70" rx="9" ry="5" fill="#8C5A2E"/>' + ''.join(f'<rect x="{x}" y="{y}" width="5" height="2" rx="1" fill="{c}" transform="rotate({x*3} {x} {y})"/>' for x, y, c in [(30, 66, '#F5C542'), (40, 76, '#4CC38A'), (64, 64, '#3B7DD8'), (68, 74, '#fff'), (34, 72, '#fff'), (56, 78, '#F5C542')])
def flowers():
    o = shadow(50, 93, 26, 4) + '<path d="M36 92 L44 60 H56 L64 92Z" fill="#E8D9B5"/><path d="M40 70 h20" stroke="#E2435E" stroke-width="3"/>'
    for x, y, c in [(36, 40, '#E2435E'), (50, 30, '#F5C542'), (64, 40, '#E2435E'), (44, 52, '#7B3AA8'), (58, 50, '#F28C28')]:
        o += f'<path d="M50 62 L{x} {y}" stroke="#3E7D4A" stroke-width="2"/>' + ''.join(f'<circle cx="{x+5*__import__("math").cos(a)}" cy="{y+5*__import__("math").sin(a)}" r="4.5" fill="{c}"/>' for a in [i * 1.2566 for i in range(5)]) + f'<circle cx="{x}" cy="{y}" r="3" fill="#F4E9D8"/>'
    return o
def notebook():
    return shadow(50, 93, 36, 4) + '<rect x="18" y="30" width="54" height="62" rx="3" fill="#3B7DD8"/><rect x="18" y="30" width="8" height="62" fill="#2C5FA8"/><rect x="34" y="44" width="30" height="12" rx="2" fill="#fff"/>' + ''.join(f'<rect x="{74+i*6}" y="36" width="4" height="56" rx="1" fill="{c}"/><path d="M{74+i*6} 92 l2 6 l2 -6" fill="#F4D7A8"/>' for i, c in enumerate(['#F5C542', '#E2435E']))
def soap():
    return box('SOAP', '#6FB3D9', 56, 30) 
def tissue():
    return shadow(50, 93, 36, 4) + ''.join(f'<rect x="{12+i*26}" y="54" width="24" height="38" rx="6" fill="#F4F1EA" stroke="#D9D2C5"/><ellipse cx="{24+i*26}" cy="73" rx="5" ry="5" fill="#D9D2C5"/>' for i in range(3)) + '<rect x="10" y="64" width="80" height="10" fill="#4CC38A" opacity="0.9"/>'
def snacks_chin():
    return bag('CHIN-CHIN', '#F28C28', window='#E8B062', sub="SOFIA'S")
def onion(): return pile('#B5653E', 5, r=12)
def watermelon():
    f, d = grad_fill('#3E7D4A', 'r')
    return d + shadow(50, 93, 36, 4) + f'<ellipse cx="50" cy="70" rx="38" ry="22" fill="{f}"/>' + ''.join(f'<path d="M{20+i*12} 52 q4 18 0 36" stroke="#2A5A34" stroke-width="3" fill="none"/>' for i in range(6))
def pineapple():
    f, d = grad_fill('#D9A030', 'r')
    return d + shadow(50, 93, 22, 4) + f'<ellipse cx="50" cy="70" rx="20" ry="24" fill="{f}"/>' + ''.join(f'<path d="M{34+i*8} 50 l8 40 M{66-i*8} 50 l-8 40" stroke="#A8761C" stroke-width="1.2"/>' for i in range(4)) + '<path d="M50 48 l-12 -24 l10 14 l2 -20 l4 20 l10 -14z" fill="#4E9A4F"/>'
def cabbage():
    f, d = grad_fill('#8DC26F', 'r')
    return d + shadow(50, 93, 32, 4) + f'<circle cx="50" cy="66" r="28" fill="{f}"/><path d="M30 54 q20 -10 40 0 M28 70 q22 14 44 0 M50 40 v52" stroke="#6AA04E" stroke-width="2" fill="none"/>'
def carrot():
    o = shadow(50, 93, 32, 4)
    for i, a in enumerate((-20, 0, 20)):
        f, d = grad_fill('#F28C28', 'v'); o += d + f'<g transform="rotate({a} 50 92)"><path d="M42 40 h16 l-6 52 h-4z" fill="{f}"/><path d="M44 52 h6 M46 66 h6 M47 78 h5" stroke="#C9661A" stroke-width="1.2"/><path d="M46 40 l-6 -14 M50 40 v-16 M54 40 l6 -14" stroke="#4E9A4F" stroke-width="3"/></g>'
    return o
def banana():
    o = shadow(50, 93, 32, 4)
    for i in range(4):
        f, d = grad_fill('#F5D23A', 'v'); o += d + f'<path d="M30 {40+i*3} C24 {66+i*4} 46 {92} 80 {80-i*3} L78 {76-i*3} C52 {84-i*2} 36 {66+i*3} 36 {40+i*3}Z" fill="{f}"/>'
    return o + '<path d="M30 36 h8 v6 h-8z" fill="#5B4030"/>'
def rice(): return bag('RICE', '#F4F1EA', '#24503B', 54, 70, window='#FBF8F2', sub='5 KG')
CATALOG = {
 # bakery
 'bread_loaf': bread, 'baguette': baguette, 'bread_bag': lambda: bag('BREAD', '#F5E9C8', '#C8412E', window='#D9A05B'), 'meat_pie': pastry, 'doughnut': doughnut,
 'cake_slice': lambda: shadow(50, 93, 30, 4) + '<path d="M16 88 L84 88 L84 62 L16 50Z" fill="#F4E1B8"/><path d="M16 50 L84 62 L84 56 L16 44Z" fill="#E2435E"/><path d="M16 66 L84 76" stroke="#E2435E" stroke-width="3"/><circle cx="40" cy="44" r="5" fill="#C8412E"/>',
 # eggs/dairy
 'eggs_tray': eggs, 'milk_carton': lambda: carton('MILK', '#3B7DD8'), 'yogurt': lambda: can('YOGURT', '#F7B7C8', 40, 34, '#FFFFFF'), 'butter': lambda: box('BUTTER', '#F5D23A', 56, 26, txtcol='#8C5A2E'), 'cheese': lambda: shadow(50, 93, 36, 4) + '<path d="M12 88 L88 88 L88 60 L12 74Z" fill="#F5C542"/><path d="M12 74 L88 60 L60 48Z" fill="#F9DC7A"/><circle cx="40" cy="80" r="4" fill="#D9A82A"/><circle cx="70" cy="74" r="5" fill="#D9A82A"/>',
 'powdered_milk': lambda: can('MILK', '#24503B', 44, 54, '#E8B62C'),
 # drinks
 'water_bottle': lambda: bottle('WATER', '#6FB3D9', '#3B7DD8', glass=True), 'soda_bottle': lambda: bottle('COLA', '#C8412E', '#C8412E', liquid='#3A1F14'), 'orange_soda': lambda: bottle('ORANGE', '#F28C28', '#1E6B45', liquid='#F28C28'),
 'juice_carton': lambda: carton('JUICE', '#F28C28', '#F5D23A'), 'malt_drink': lambda: can('MALT', '#7A3B1E'), 'energy_drink': lambda: can('POWER', '#1E6B45', 28, 54),
 # snacks
 'chin_chin': snacks_chin, 'plantain_chips': lambda: bag('CHIPS', '#E8B62C', '#24503B', window='#F5D23A'), 'biscuits': lambda: box('BISCUIT', '#C8412E', 60, 34), 'groundnuts': lambda: jar('NUTS', '#C9963E', '#C8412E'), 'sweets': lambda: jar('SWEETS', '#E2435E', '#3B7DD8'),
 # fruit & veg
 'tomatoes': lambda: pile('#D63A2A', 6), 'peppers': lambda: pile('#E2452F', 5, r=9, shape='pepper', leaf=False), 'onions': onion, 'plantain': plantain, 'yam': yam, 'oranges': lambda: pile('#F28C28', 6), 'mangoes': lambda: pile('#F2B233', 5, shape='oval', r=11),
 'bananas': banana, 'pineapple': pineapple, 'watermelon': watermelon, 'cabbage': cabbage, 'carrots': carrot,
 # pantry / local specialty
 'garri': lambda: bag('GARRI', '#F4F1EA', '#1E6B45', 50, 66, window='#F4E9D8', sub='2 KG'), 'rice': rice, 'beans': lambda: bag('BEANS', '#8C5A3C', window='#C9963E'),
 'palm_oil': lambda: bottle('PALM OIL', '#C8412E', '#F5C542', liquid='#C8412E', w=32), 'cooking_oil': lambda: bottle('OIL', '#F5C542', '#24503B', liquid='#F2C230', w=32), 'tomato_paste': lambda: can('TOMATO', '#C8412E', 34, 30),
 'noodles': lambda: bag('NOODLES', '#E8B62C', '#C8412E', 56, 34), 'seasoning_cubes': lambda: box('CUBES', '#C8412E', 46, 30), 'spices': lambda: jar('SPICE', '#D9731A', '#2B2118', 30, 44), 'sugar': lambda: bag('SUGAR', '#F4F1EA', '#3B7DD8', window='#FBF8F2'),
 # frozen
 'frozen_chicken': chicken, 'frozen_fish': fish, 'ice_cream': icecream, 'frozen_peas': lambda: bag('PEAS', '#3B7DD8', window='#7BB343'),
 # household
 'detergent': lambda: box('WASH', '#3B7DD8', 48, 58, '<circle cx="50" cy="68" r="12" fill="#6FB3D9"/>'), 'soap_bar': soap, 'toilet_tissue': tissue, 'toothpaste': lambda: box('SMILE', '#F4F1EA', 64, 22, txtcol='#3B7DD8'), 'bleach': lambda: bottle('BLEACH', '#F4F1EA', '#3B7DD8', w=32),
 # premium / special
 'wine_bottle': lambda: bottle('WINE', '#5B1A2E', '#2B2118', liquid='#5B1A2E', w=22, h=84), 'chocolate': lambda: box('CHOCO', '#5B3A28', 58, 26), 'imported_cheese': lambda: shadow(50, 93, 36, 4) + '<circle cx="50" cy="74" r="28" fill="#F5D23A"/><path d="M50 74 L78 74 A28 28 0 0 0 64 50Z" fill="#F9E38A"/><circle cx="40" cy="80" r="4" fill="#D9A82A"/>',
 'flowers': flowers, 'school_supplies': notebook,
}
CATEGORY = {'bakery': ['bread_loaf', 'baguette', 'bread_bag', 'meat_pie', 'doughnut', 'cake_slice'], 'eggs_dairy': ['eggs_tray', 'milk_carton', 'yogurt', 'butter', 'cheese', 'powdered_milk'],
            'drinks': ['water_bottle', 'soda_bottle', 'orange_soda', 'juice_carton', 'malt_drink', 'energy_drink'], 'snacks': ['chin_chin', 'plantain_chips', 'biscuits', 'groundnuts', 'sweets', 'doughnut'],
            'fruit_veg': ['tomatoes', 'peppers', 'onions', 'plantain', 'yam', 'oranges', 'mangoes', 'bananas', 'pineapple', 'watermelon', 'cabbage', 'carrots'],
            'household': ['detergent', 'soap_bar', 'toilet_tissue', 'toothpaste', 'bleach'], 'frozen': ['frozen_chicken', 'frozen_fish', 'ice_cream', 'frozen_peas'],
            'premium': ['wine_bottle', 'chocolate', 'imported_cheese', 'flowers'], 'local_specialty': ['garri', 'palm_oil', 'yam', 'plantain', 'chin_chin', 'spices'],
            'pantry': ['rice', 'beans', 'cooking_oil', 'tomato_paste', 'noodles', 'seasoning_cubes', 'sugar'], 'misc': ['school_supplies']}
