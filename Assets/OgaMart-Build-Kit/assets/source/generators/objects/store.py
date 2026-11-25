# store interior objects. units: 100 = 0.5 m (person ~ 352 units / 1.7 m)
from common import *
import products as P
MAT = {'wood': dict(frame='#8B5A3C', shelf='#A8754E', back='#6E4630', edge='#5E3A26'),
       'metal': dict(frame='#C9CED4', shelf='#E6E9EC', back='#B4BBC2', edge='#8E979F'),
       'premium': dict(frame='#2E2A27', shelf='#4A3F37', back='#1F1B18', edge='#C9A23A')}
def prod(key, x, y, s=0.42):
    return f'<g transform="translate({x} {y}) scale({s}) translate(-50 -92)">{P.CATALOG[key]()}</g>'
def shelf_unit(cat, stock, mat='metal', W=280, H=330, tiers=4):
    m = MAT[mat]; items = P.CATEGORY[cat]; o = shadow(W / 2, H + 2, W / 2 + 6, 8)
    f, d = grad_fill(m['back'], 'v', a=.1, b=.2); o += d + f'<rect x="10" y="20" width="{W-20}" height="{H-30}" fill="{f}"/>'
    o += f'<rect x="0" y="0" width="{W}" height="22" rx="3" fill="{m["frame"]}"/><rect x="6" y="4" width="{W-12}" height="14" rx="2" fill="{"#24503B" if mat != "premium" else "#1F1B18"}"/>' + txt(W / 2, 15, cat.upper().replace('_', ' &amp; '), 10, '#E8B62C' if mat != 'wood' else '#F4F1EA')
    gap = (H - 40) / tiers; per = 5; fill = [0, 0.25, 0.5, 0.75, 1.0][stock]
    import random; r = random.Random(hash((cat, mat)) & 0xffff)
    for t in range(tiers):
        y = 20 + gap * (t + 1)
        n = round(per * fill + (0.49 if fill and t % 2 else 0)); n = min(per, max(0, n if fill < 1 else per))
        slots = list(range(per)); r2 = random.Random(t * 7 + stock); r2.shuffle(slots)
        for i in sorted(slots[:n]):
            k = items[(i + t * 2) % len(items)]; x = 30 + i * (W - 60) / (per - 1)
            o += prod(k, x - 7, y - 3, 0.5) + prod(k, x + 7, y - 1, 0.54)
        o += f'<rect x="4" y="{y-2}" width="{W-8}" height="10" fill="{m["shelf"]}"/><rect x="4" y="{y+6}" width="{W-8}" height="4" fill="{m["edge"]}"/>'
        o += ''.join(f'<rect x="{24+j*(W-60)/2}" y="{y+1}" width="16" height="6" fill="#FBF8F2"/><rect x="{26+j*(W-60)/2}" y="{y+3}" width="8" height="2" fill="#C8412E"/>' for j in range(3))
    o += f'<rect x="0" y="16" width="10" height="{H-16}" fill="{m["frame"]}"/><rect x="{W-10}" y="16" width="10" height="{H-16}" fill="{dk(m["frame"], .15)}"/><rect x="0" y="{H-14}" width="{W}" height="14" fill="{m["edge"]}"/>'
    if mat == 'premium': o += f'<rect x="10" y="22" width="{W-20}" height="3" fill="#FFE9A8" opacity="0.8"/>'
    if stock == 0: o += f'<rect x="{W/2-50}" y="{H/2-14}" width="100" height="26" rx="5" fill="#C8412E"/>' + txt(W / 2, H / 2 + 4, 'EMPTY', 13)
    return o, f'-10 -10 {W+20} {H+24}'
def fridge(stock, kind='drinks', W=160, H=360):
    items = P.CATEGORY['drinks' if kind == 'drinks' else 'eggs_dairy']; fill = [0, .25, .5, .75, 1][stock]
    f, d = grad_fill('#E6E9EC', a=.2, b=.15)
    o = d + shadow(W / 2, H + 2, W / 2 + 6, 8) + f'<rect x="0" y="0" width="{W}" height="{H}" rx="8" fill="{f}"/><rect x="0" y="0" width="{W}" height="40" rx="8" fill="#24503B"/>' + txt(W / 2, 26, 'COLD' if kind == 'drinks' else 'DAIRY', 14, '#E8B62C')
    o += f'<rect x="12" y="50" width="{W-24}" height="{H-90}" rx="4" fill="#DCEFF7"/>'
    for t in range(4):
        y = 50 + (t + 1) * (H - 90) / 4
        n = round(4 * fill)
        for i in range(n): o += prod(items[(i + t) % len(items)], 32 + i * (W - 64) / 3, y - 3, 0.5)
        o += f'<rect x="12" y="{y-2}" width="{W-24}" height="5" fill="#B4BBC2"/>'
    o += f'<rect x="12" y="50" width="{W-24}" height="{H-90}" rx="4" fill="#BFE3F2" opacity="0.28"/><path d="M24 60 L60 60 L30 {H-60}Z" fill="#fff" opacity="0.25"/><rect x="{W-24}" y="{H/2-30}" width="6" height="60" rx="3" fill="#8E979F"/>'
    o += f'<rect x="0" y="{H-34}" width="{W}" height="34" rx="6" fill="#8E979F"/>' + ''.join(f'<rect x="{20+i*14}" y="{H-24}" width="8" height="14" rx="2" fill="#6E767E"/>' for i in range(8)) + f'<rect x="10" y="44" width="{W-20}" height="4" fill="#BFF0FF" opacity="0.9"/>'
    return o, f'-10 -10 {W+20} {H+24}'
def chest_freezer(stock, W=260, H=150):
    fill = [0, .25, .5, .75, 1][stock]; items = P.CATEGORY['frozen']
    f, d = grad_fill('#F4F6F8', a=.1, b=.18)
    o = d + shadow(W / 2, H + 2, W / 2 + 8, 8) + f'<path d="M0 40 L20 0 H{W-20} L{W} 40Z" fill="#DCEFF7"/>'
    for i in range(round(8 * fill)): o += prod(items[i % 4], 30 + (i % 4) * (W - 60) / 3, 34 - (i // 4) * 12, 0.34)
    o += f'<path d="M0 40 L20 0 H{W-20} L{W} 40Z" fill="#BFE3F2" opacity="0.35" stroke="#B4BBC2" stroke-width="4"/><rect x="0" y="40" width="{W}" height="{H-40}" rx="6" fill="{f}"/><rect x="0" y="40" width="{W}" height="30" fill="#3B7DD8"/>' + txt(W / 2, 61, 'FROZEN FOODS', 13)
    o += ''.join(f'<rect x="{30+i*40}" y="{H-30}" width="24" height="10" rx="2" fill="#B4BBC2"/>' for i in range(5))
    return o, f'-10 -10 {W+20} {H+24}'
def produce_stand(stock, W=300, H=240):
    fill = [0, .25, .5, .75, 1][stock]; items = ['tomatoes', 'oranges', 'plantain', 'yam', 'peppers', 'mangoes', 'onions', 'bananas', 'cabbage']
    o = shadow(W / 2, H + 2, W / 2 + 8, 8)
    for row in range(3):
        y = 50 + row * 60
        for i in range(3):
            x = 10 + i * (W - 20) / 3; w = (W - 20) / 3 - 8; k = items[row * 3 + i]
            o += f'<path d="M{x} {y} L{x+w} {y} L{x+w-4} {y+50} L{x+4} {y+50}Z" fill="#A8754E"/>' + ''.join(f'<path d="M{x+2} {y+12+j*13} H{x+w-2}" stroke="#7F5833" stroke-width="2"/>' for j in range(3))
            if fill > row * 0.3 or stock == 4:
                o += prod(k, x + w / 2, y + 4, 0.7 * (0.6 + 0.4 * fill))
    o += f'<rect x="0" y="0" width="{W}" height="34" rx="4" fill="#3E7D4A"/>' + txt(W / 2, 23, 'FRESH FARM PRODUCE', 13, '#F5E9C8') + f'<rect x="4" y="{H-20}" width="{W-8}" height="20" fill="#7F5833"/>'
    return o, f'-10 -10 {W+20} {H+24}'
def bakery_case(stock, W=280, H=230):
    fill = [0, .25, .5, .75, 1][stock]; items = P.CATEGORY['bakery']
    o = shadow(W / 2, H + 2, W / 2 + 8, 8) + f'<rect x="0" y="100" width="{W}" height="{H-100}" rx="6" fill="#8B5A3C"/><rect x="10" y="114" width="{W-20}" height="{H-130}" rx="4" fill="#A8754E"/>'
    o += f'<path d="M6 100 L20 20 H{W-20} L{W-6} 100Z" fill="#FFF7E8"/>'
    for t in range(2):
        for i in range(round(5 * fill)): o += prod(items[(i + t * 3) % 6], 46 + i * (W - 92) / 4, 58 + t * 40, 0.36)
        o += f'<rect x="12" y="{60+t*40}" width="{W-24}" height="4" fill="#D9D2C5"/>'
    o += f'<path d="M6 100 L20 20 H{W-20} L{W-6} 100Z" fill="#BFE3F2" opacity="0.25" stroke="#C9CED4" stroke-width="4"/><path d="M30 30 L60 30 L36 96Z" fill="#fff" opacity="0.35"/>' + txt(W / 2, 165, 'FRESH BAKERY', 14, '#F5E9C8')
    return o, f'-10 -10 {W+20} {H+24}'
def checkout(kind, W=300, H=220):
    o = shadow(W / 2, H + 2, W / 2 + 8, 8)
    if kind == 'manual':
        o += f'<rect x="0" y="90" width="{W}" height="{H-90}" rx="6" fill="#8B5A3C"/><rect x="0" y="82" width="{W}" height="16" rx="4" fill="#5E3A26"/><rect x="10" y="110" width="{W-20}" height="{H-130}" fill="#A8754E"/>'
        o += '<rect x="190" y="30" width="80" height="56" rx="6" fill="#2B2118"/><rect x="198" y="36" width="64" height="26" rx="2" fill="#5FBF8E"/>' + txt(230, 54, '₦ 2,450', 10, '#123') + ''.join(f'<rect x="{200+i*14}" y="{68+j*8}" width="10" height="5" rx="1" fill="#C9C1B4"/>' for i in range(4) for j in range(2))
        o += prod('bread_loaf', 60, 86, .5) + prod('milk_carton', 110, 86, .5) + txt(W / 2, 160, 'PAY HERE', 16, '#F5E9C8')
    elif kind == 'automatic':
        o += f'<rect x="0" y="96" width="{W}" height="{H-96}" rx="6" fill="#C9CED4"/><rect x="0" y="84" width="{W}" height="16" rx="3" fill="#2B2B2B"/>' + ''.join(f'<path d="M{10+i*18} 86 v12" stroke="#444" stroke-width="2"/>' for i in range(10))
        o += '<rect x="200" y="20" width="70" height="66" rx="6" fill="#2B2B2B"/><rect x="206" y="26" width="58" height="36" rx="3" fill="#3B7DD8"/>' + txt(235, 48, 'SCAN', 10) + '<rect x="214" y="70" width="42" height="10" rx="3" fill="#C8412E" opacity="0.9"/><rect x="216" y="72" width="38" height="4" fill="#FF6B6B"/>'
        o += prod('soda_bottle', 50, 86, .45) + prod('cooking_oil', 90, 86, .45) + f'<rect x="10" y="116" width="{W-20}" height="34" rx="4" fill="#24503B"/>' + txt(W / 2, 139, 'AUTO CHECKOUT', 14, '#E8B62C')
    elif kind == 'express':
        W2 = 200; o = shadow(W2 / 2, H + 2, W2 / 2 + 8, 8) + f'<rect x="0" y="96" width="{W2}" height="{H-96}" rx="6" fill="#E6E9EC"/><rect x="0" y="86" width="{W2}" height="14" rx="3" fill="#2B2B2B"/>'
        o += '<rect x="120" y="30" width="62" height="56" rx="6" fill="#2B2B2B"/><rect x="126" y="36" width="50" height="28" rx="2" fill="#5FBF8E"/>' + f'<rect x="10" y="110" width="{W2-20}" height="34" rx="4" fill="#F28C28"/>' + txt(W2 / 2, 133, 'EXPRESS ≤5', 14)
        o += f'<rect x="80" y="-30" width="40" height="36" rx="4" fill="#F28C28"/>' + txt(100, -6, '⚡', 16) + '<path d="M100 6 v24" stroke="#8E979F" stroke-width="3"/>'
        return o, f'-10 -40 {W2+20} {H+54}'
    elif kind == 'self_service':
        W2 = 140; o = shadow(W2 / 2, H + 2, W2 / 2 + 6, 8) + f'<rect x="20" y="20" width="{W2-40}" height="{H-20}" rx="10" fill="#2B2B2B"/><rect x="28" y="30" width="{W2-56}" height="70" rx="4" fill="#3B7DD8"/>' + txt(W2 / 2, 60, 'SELF', 12) + txt(W2 / 2, 76, 'CHECKOUT', 9)
        o += f'<rect x="0" y="120" width="{W2}" height="16" rx="3" fill="#8E979F"/><rect x="{W2/2-14}" y="106" width="28" height="10" rx="3" fill="#C8412E"/><rect x="{W2/2-22}" y="150" width="44" height="26" rx="3" fill="#444"/><rect x="{W2/2-14}" y="156" width="28" height="4" fill="#5FBF8E"/>'
        return o, f'-10 -10 {W2+20} {H+24}'
    return o, f'-10 -10 {W+20} {H+24}'
def queue_barrier(W=240, H=110):
    o = ''
    for x in (12, W - 12):
        o += shadow(x, H, 16, 4) + f'<rect x="{x-4}" y="10" width="8" height="{H-14}" fill="#C9CED4"/><ellipse cx="{x}" cy="{H-4}" rx="14" ry="5" fill="#8E979F"/><circle cx="{x}" cy="10" r="7" fill="#E6E9EC"/>'
    o += f'<path d="M12 24 Q{W/2} 34 {W-12} 24" stroke="#24503B" stroke-width="8" fill="none"/><path d="M12 24 Q{W/2} 34 {W-12} 24" stroke="#E8B62C" stroke-width="2" fill="none"/>'
    return o, f'-10 -10 {W+20} {H+20}'
def storage_rack(full=True, W=280, H=360):
    o = shadow(W / 2, H + 2, W / 2 + 6, 8)
    for t in range(3):
        y = 40 + t * 110
        if full:
            for i in range(3): o += f'<rect x="{20+i*82}" y="{y+20}" width="74" height="70" fill="#C9A06A"/><path d="M{20+i*82} {y+40} h74 M{57+i*82} {y+20} v20" stroke="#A47648" stroke-width="2"/><rect x="{30+i*82}" y="{y+56}" width="30" height="16" fill="#F4F1EA"/>'
        o += f'<rect x="0" y="{y+90}" width="{W}" height="10" fill="#F28C28"/>'
    o += f'<rect x="0" y="0" width="12" height="{H}" fill="#3B7DD8"/><rect x="{W-12}" y="0" width="12" height="{H}" fill="#2C5FA8"/>' + ''.join(f'<circle cx="6" cy="{20+i*24}" r="2" fill="#1E3F72"/>' for i in range(15))
    return o, f'-10 -10 {W+20} {H+24}'
def pallet(load=True, W=220, H=170):
    o = shadow(W / 2, H + 2, W / 2 + 6, 6) + f'<rect x="0" y="{H-30}" width="{W}" height="10" fill="#B8915E"/><rect x="0" y="{H-10}" width="{W}" height="10" fill="#A47648"/>' + ''.join(f'<rect x="{x}" y="{H-20}" width="24" height="10" fill="#8B6A4A"/>' for x in (6, W / 2 - 12, W - 30))
    if load:
        for r in range(2):
            for i in range(3): o += f'<rect x="{6+i*70}" y="{H-30-(r+1)*54}" width="66" height="54" fill="{"#C9A06A" if (i+r)%2 else "#BC9460"}"/><path d="M{6+i*70} {H-30-(r+1)*54+18} h66" stroke="#A47648" stroke-width="2"/>'
        o += f'<rect x="4" y="{H-140}" width="{W-8}" height="110" fill="#BFE3F2" opacity="0.18"/>'
    return o, f'-10 -10 {W+20} {H+20}'
def display_table(key='mangoes', W=240, H=150):
    o = shadow(W / 2, H + 2, W / 2 + 6, 6) + f'<rect x="10" y="60" width="12" height="{H-60}" fill="#5E3A26"/><rect x="{W-22}" y="60" width="12" height="{H-60}" fill="#5E3A26"/>'
    o += prod(key, 70, 60, .7) + prod(key, 130, 60, .7) + prod(key, 180, 60, .6) + f'<rect x="0" y="56" width="{W}" height="14" rx="3" fill="#8B5A3C"/><rect x="{W/2-30}" y="74" width="60" height="22" rx="3" fill="#FBF8F2"/>' + txt(W / 2, 90, 'SPECIAL', 11, '#C8412E')
    return o, f'-10 -10 {W+20} {H+20}'
def promo_stand(W=130, H=260):
    o = shadow(W / 2, H + 2, W / 2, 6) + f'<rect x="{W/2-5}" y="120" width="10" height="{H-130}" fill="#8E979F"/><ellipse cx="{W/2}" cy="{H-6}" rx="40" ry="8" fill="#6E767E"/>'
    o += f'<rect x="0" y="0" width="{W}" height="130" rx="8" fill="#C8412E"/><rect x="8" y="8" width="{W-16}" height="114" rx="4" fill="#E2452F"/>' + txt(W / 2, 46, 'PROMO', 20, '#FFF2B8', 800) + txt(W / 2, 80, '-20%', 30, '#fff', 800) + txt(W / 2, 108, 'THIS WEEK', 11, '#FFF2B8')
    return o, f'-10 -10 {W+20} {H+20}'
def end_cap(key='chin_chin', W=150, H=260):
    o = shadow(W / 2, H + 2, W / 2 + 4, 6) + f'<rect x="0" y="40" width="{W}" height="{H-40}" fill="#F28C28"/><rect x="0" y="0" width="{W}" height="44" rx="4" fill="#24503B"/>' + txt(W / 2, 28, "SOFIA'S SNACKS" if key == 'chin_chin' else 'HOT DEAL', 11, '#E8B62C')
    for t in range(3):
        y = 100 + t * 60
        for i in range(3): o += prod(key, 30 + i * 45, y, .42)
        o += f'<rect x="4" y="{y}" width="{W-8}" height="8" fill="#D9731A"/>'
    return o, f'-10 -10 {W+20} {H+20}'
def lamp(kind, on=True):
    glow = f'<radialGradient id="glw"><stop offset="0" stop-color="#FFF4C2" stop-opacity="0.9"/><stop offset="1" stop-color="#FFF4C2" stop-opacity="0"/></radialGradient>'
    if kind == 'pendant': o = f'<path d="M60 0 V40" stroke="#2B2B2B" stroke-width="2"/><path d="M30 70 L44 40 H76 L90 70Z" fill="#24503B"/><ellipse cx="60" cy="70" rx="30" ry="6" fill="{"#FFF4C2" if on else "#C9C1B4"}"/>'
    elif kind == 'led_panel': o = f'<rect x="0" y="20" width="120" height="16" rx="3" fill="#E6E9EC"/><rect x="6" y="30" width="108" height="6" rx="2" fill="{"#FFFDF2" if on else "#C9CED4"}"/>'
    elif kind == 'chandelier': o = '<path d="M60 0 V24" stroke="#C9A23A" stroke-width="3"/><path d="M20 40 Q60 70 100 40" stroke="#C9A23A" stroke-width="4" fill="none"/>' + ''.join(f'<path d="M{x} {y} v-10" stroke="#C9A23A" stroke-width="3"/><ellipse cx="{x}" cy="{y-14}" rx="5" ry="7" fill="{"#FFF4C2" if on else "#E6E9EC"}"/>' for x, y in [(20, 44), (40, 54), (60, 58), (80, 54), (100, 44)])
    else: o = '<path d="M60 0 V30" stroke="#2B2B2B" stroke-width="2"/><circle cx="60" cy="50" r="18" fill="{}"/><path d="M48 32 h24 l-4 8 h-16z" fill="#8E979F"/>'.format('#FFF4C2' if on else '#E6E9EC')
    g = f'<defs>{glow}</defs><ellipse cx="60" cy="110" rx="70" ry="70" fill="url(#glw)" opacity="0.7"/>' if on else ''
    return g + o, '-20 -10 160 200'
def sign(style):
    S = {'corner_shop': ('#C8412E', '#FFF2B8', 'OGAMART', 'Corner Shop'), 'traditional': ('#8B5A3C', '#F5E9C8', 'OGAMART', 'Groceries & Provisions'), 'modern_mini': ('#24503B', '#FFFFFF', 'OGAMART', 'Mini Market'),
         'neighborhood': ('#24503B', '#E8B62C', 'OGAMART', 'Supermarket'), 'premium': ('#1F1B18', '#C9A23A', 'OGAMART', 'Premium Foods'), 'superstore': ('#3B7DD8', '#FFFFFF', 'OGAMART', 'Superstore'), 'mega_market': ('#7B3AA8', '#F5C542', 'OGAMART', 'MEGA MARKET')}
    bg, fg, a, b = S[style]; W = 520
    o = f'<rect x="0" y="0" width="{W}" height="120" rx="14" fill="{dk(bg, .25)}"/><rect x="6" y="6" width="{W-12}" height="108" rx="10" fill="{bg}"/>' + f'<circle cx="64" cy="60" r="40" fill="{fg}"/><path d="M44 48 h40 l-6 26 h-28z" fill="{bg}"/><circle cx="54" cy="82" r="5" fill="{bg}"/><circle cx="74" cy="82" r="5" fill="{bg}"/>'
    o += txt(300, 66, a, 50, fg, 800) + txt(300, 98, b, 18, fg, 600)
    if style == 'premium': o += f'<rect x="12" y="12" width="{W-24}" height="96" rx="8" fill="none" stroke="{fg}" stroke-width="2"/>'
    return o, f'-10 -10 {W+20} 140'
def aisle_sign(cat):
    return f'<path d="M100 0 V30" stroke="#8E979F" stroke-width="3"/><rect x="0" y="30" width="200" height="56" rx="8" fill="#24503B"/>' + txt(100, 66, cat.upper().replace('_', ' &amp; '), 15, '#E8B62C'), '-10 -10 220 106'
def price_tag(price='₦500', sale=False):
    c = '#C8412E' if sale else '#FBF8F2'; t = '#fff' if sale else '#24503B'
    return f'<rect x="0" y="0" width="120" height="60" rx="6" fill="{c}" stroke="#D9D2C5" stroke-width="2"/>' + txt(60, 40, price, 24, t, 800) + (txt(60, 14, 'SALE', 10, '#FFF2B8') if sale else ''), '-6 -6 132 72'
def doors(state):
    W, H = 320, 340; o = f'<rect x="0" y="0" width="{W}" height="{H}" fill="#8E979F"/><rect x="0" y="0" width="{W}" height="40" fill="#24503B"/>' + txt(W / 2, 27, 'WELCOME', 16, '#E8B62C') + f'<rect x="10" y="48" width="{W-20}" height="{H-48}" fill="#3A4A52"/>'
    off = {'closed': 0, 'half': 50, 'open': 120}[state]
    for s in (-1, 1):
        x = W / 2 + (s * off) + (0 if s > 0 else -(W / 2 - 14)); o += f'<rect x="{x}" y="50" width="{W/2-14}" height="{H-52}" fill="#BFE3F2" opacity="0.55" stroke="#C9CED4" stroke-width="5"/><path d="M{x+16} 70 l30 0 l-20 120z" fill="#fff" opacity="0.3"/>'
    return o + f'<rect x="-10" y="{H-6}" width="{W+20}" height="10" fill="#6E767E"/>', f'-14 -6 {W+28} {H+20}'
def cart(full=False):
    o = shadow(70, 150, 60, 6) + '<path d="M10 20 H28 L46 110 H124 L136 40 H34" stroke="#8E979F" stroke-width="6" fill="none" stroke-linejoin="round"/>' + ''.join(f'<path d="M{40+i*14} 42 L{50+i*12} 108" stroke="#B4BBC2" stroke-width="2"/>' for i in range(7)) + '<path d="M38 76 H130" stroke="#B4BBC2" stroke-width="2"/>'
    if full: o = prod('bread_bag', 60, 60, .5) + prod('cooking_oil', 86, 54, .5) + prod('milk_carton', 112, 58, .5) + prod('tomatoes', 74, 76, .4) + o
    o += '<circle cx="54" cy="136" r="10" fill="#2B2B2B"/><circle cx="116" cy="136" r="10" fill="#2B2B2B"/><path d="M46 110 L54 128 M124 110 L116 128" stroke="#8E979F" stroke-width="5"/><rect x="4" y="14" width="22" height="10" rx="4" fill="#C8412E"/>'
    return o, '-6 -10 160 170'
def basket(full=False):
    o = '<path d="M30 30 Q60 -6 90 30" stroke="#C8412E" stroke-width="6" fill="none"/>'
    if full: o += prod('bananas', 46, 44, .4) + prod('bread_bag', 70, 40, .38) + prod('eggs_tray', 84, 46, .3)
    o += shadow(60, 92, 50, 5) + '<path d="M8 36 H112 L102 88 H18Z" fill="#E2452F"/><path d="M12 50 H108 M14 64 H106 M16 76 H104" stroke="#B8324A" stroke-width="3"/>'
    return o, '-6 -10 132 110'
def plant(kind='palm'):
    o = shadow(60, 196, 40, 6) + '<path d="M28 140 H92 L84 196 H36Z" fill="#B5653E"/><rect x="24" y="134" width="72" height="12" rx="3" fill="#C97A50"/>'
    if kind == 'palm': o += ''.join(f'<path d="M60 136 Q{60+dx*0.4} {80} {60+dx} {40+abs(dx)*0.4}" stroke="#3E7D4A" stroke-width="10" fill="none" stroke-linecap="round"/>' for dx in (-50, -28, 0, 26, 48))
    else: o += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>' for x, y, r, c in [(60, 90, 40, '#3E7D4A'), (40, 104, 26, '#4E9A4F'), (82, 100, 28, '#4E9A4F'), (60, 70, 26, '#5DAE5C')])
    return o, '-10 -10 140 216'
def wall_art(kind='abstract'):
    o = '<rect x="0" y="0" width="160" height="110" fill="#8B5A3C"/><rect x="8" y="8" width="144" height="94" fill="#F4E9D8"/>'
    o += '<circle cx="50" cy="56" r="26" fill="#E8B62C"/><path d="M8 102 L60 60 L100 90 L130 70 L152 90 V102Z" fill="#3E7D4A"/><circle cx="118" cy="34" r="10" fill="#C8412E"/>'
    return o, '-6 -6 172 122'
def banner(text='GRAND OPENING', col='#C8412E'):
    o = f'<path d="M0 0 H400 L380 40 L400 80 H0 L20 40Z" fill="{col}"/>' + txt(200, 52, text, 28, '#FFF2B8', 800)
    return o, '-6 -6 412 92'
def balloons():
    import math
    o = ''
    for x, y, c in [(40, 50, '#E2435E'), (80, 34, '#E8B62C'), (120, 54, '#3B7DD8'), (60, 80, '#4CC38A'), (100, 84, '#7B3AA8')]:
        f, d = grad_fill(c, 'r'); o += d + f'<path d="M{x} {y+30} Q{x+6} {y+80} 80 200" stroke="#8E979F" stroke-width="1.4" fill="none"/><ellipse cx="{x}" cy="{y}" rx="22" ry="28" fill="{f}"/><path d="M{x-3} {y+27} l3 6 l3 -6z" fill="{c}"/>'
    return o, '0 0 160 210'
def string_lights():
    cols = ['#E2435E', '#E8B62C', '#4CC38A', '#3B7DD8', '#F28C28']
    o = '<path d="M0 10 Q100 60 200 10 Q300 60 400 10" stroke="#2B2B2B" stroke-width="2" fill="none"/>'
    import math
    for i in range(16):
        t = i / 15; x = t * 400; y = 10 + 50 * math.sin(math.pi * ((t * 2) % 1)) * 0.5 * 2 * 0.5 * 2
        y = 10 + 25 * (1 - (2 * ((t * 2) % 1) - 1) ** 2) * 1.0 + 0
        o += f'<circle cx="{x}" cy="{y+8}" r="9" fill="{cols[i%5]}" opacity="0.35"/><ellipse cx="{x}" cy="{y+8}" rx="4" ry="6" fill="{cols[i%5]}"/>'
    return o, '-14 0 428 60'
# floors & walls (seamless 256 tiles)
THEMES = {'standard': ('#E8E2D6', '#D9D2C5', '#F4EDE0', '#24503B'), 'modern': ('#EEF1F4', '#DCE1E6', '#FFFFFF', '#2E3A46'), 'tropical': ('#F2D9A6', '#E5C385', '#BFE6D2', '#1E8C6E'),
          'luxury': ('#2A2522', '#3A332E', '#1F1B18', '#C9A23A'), 'african_market': ('#C98A4B', '#B5763A', '#F4E1B8', '#C8412E'), 'holiday': ('#F4F1EA', '#E2D6C5', '#F9E7E7', '#C8412E'),
          'corner_shop': ('#C9B79C', '#B8A487', '#E8D9B5', '#C8412E'), 'premium': ('#E9E4DA', '#D8CFBF', '#F7F2E9', '#1F1B18')}
def floor(theme):
    a, b, _, acc = THEMES[theme]; o = f'<rect width="256" height="256" fill="{a}"/>'
    if theme in ('standard', 'modern', 'holiday', 'premium', 'corner_shop'):
        o += ''.join(f'<rect x="{x*64}" y="{y*64}" width="64" height="64" fill="{b if (x+y)%2 else a}"/>' for x in range(4) for y in range(4)) + ''.join(f'<path d="M{i*64} 0 V256 M0 {i*64} H256" stroke="{dk(b, .08)}" stroke-width="1.5"/>' for i in range(5))
    elif theme == 'luxury': o += ''.join(f'<path d="M{i*64} 0 V256 M0 {i*64} H256" stroke="{acc}" stroke-width="1" opacity="0.5"/>' for i in range(5)) + '<path d="M0 40 C60 60 120 20 256 80 M0 180 C80 160 160 220 256 170" stroke="#5A4E45" stroke-width="2" fill="none" opacity="0.6"/>'
    elif theme == 'tropical': o += ''.join(f'<rect x="0" y="{i*32}" width="256" height="30" fill="{b if i%2 else a}"/><path d="M{(i*53)%256} {i*32} v30" stroke="{dk(b,.15)}" stroke-width="2"/>' for i in range(8))
    else: o += ''.join(f'<rect x="{(i%4)*64+ (16 if (i//4)%2 else 0)}" y="{(i//4)*32}" width="62" height="30" fill="{b if i%3 else a}"/>' for i in range(36))
    return o, '0 0 256 256'
def wall(theme):
    a, b, c, acc = THEMES[theme]; o = f'<rect width="256" height="256" fill="{c}"/>'
    if theme == 'african_market': o += ''.join(f'<path d="M{x} 40 l16 -16 l16 16 l-16 16z" fill="{acc}" opacity="0.7"/><path d="M{x} 200 l16 -16 l16 16 l-16 16z" fill="#1E6B45" opacity="0.6"/>' for x in range(0, 256, 32)) + f'<rect y="100" width="256" height="40" fill="#E8B62C" opacity="0.6"/>'
    elif theme == 'tropical': o += ''.join(f'<path d="M{x} 256 Q{x+20} 180 {x+60} 160" stroke="#1E8C6E" stroke-width="8" fill="none" opacity="0.5"/>' for x in (0, 128))
    elif theme == 'luxury': o += f'<rect y="180" width="256" height="76" fill="{b}"/><path d="M0 180 H256" stroke="{acc}" stroke-width="4"/>' + ''.join(f'<rect x="{x+12}" y="20" width="40" height="140" fill="none" stroke="{acc}" stroke-width="1.5" opacity="0.5"/>' for x in range(0, 256, 64))
    elif theme == 'holiday': o += ''.join(f'<path d="M{x} 0 v256" stroke="#C8412E" stroke-width="10" opacity="0.18"/>' for x in range(0, 256, 32)) + '<path d="M0 30 Q64 60 128 30 Q192 60 256 30" stroke="#1E6B45" stroke-width="10" fill="none"/>'
    elif theme == 'modern': o += f'<rect y="200" width="256" height="56" fill="{acc}"/>'
    else: o += f'<rect y="190" width="256" height="66" fill="{b}"/><path d="M0 190 H256" stroke="{acc}" stroke-width="6"/>'
    return o, '0 0 256 256'
