from common import *
import math
W_ = '#FFFFFF'
GLYPH = {
 'home': 'M50 22 L80 48 H72 V78 H58 V60 H42 V78 H28 V48 H20Z', 'store': 'M24 40 L30 24 H70 L76 40 V44 Q70 50 63 44 Q56 50 50 44 Q44 50 37 44 Q30 50 24 44Z M28 50 V78 H72 V50 M42 78 V60 H58 V78',
 'map': 'M20 30 L40 22 L60 30 L80 22 V70 L60 78 L40 70 L20 78Z M40 22 V70 M60 30 V78', 'people': 'M38 44 a10 10 0 1 0 0.1 0Z M62 46 a8 8 0 1 0 0.1 0Z M20 78 Q22 56 38 56 Q54 56 56 78Z M54 64 Q58 58 64 58 Q78 58 80 78 H58',
 'missions': 'M30 20 H70 V80 H30Z M38 34 h24 M38 46 h24 M38 58 h16', 'shop': 'M26 36 H74 L70 80 H30Z M38 36 V30 a12 12 0 0 1 24 0 V36', 'settings': 'M50 36 a14 14 0 1 0 0.1 0Z',
 'restock': 'M28 56 a22 22 0 0 1 40 -14 L72 34 V50 H56 L64 44 a14 14 0 0 0 -28 10Z M72 46 a22 22 0 0 1 -40 14 L28 68 V52 H44 L36 58 a14 14 0 0 0 28 -10Z', 'change_product': 'M26 34 H66 L58 26 M74 66 H34 L42 74',
 'move': 'M50 18 L60 30 H54 V46 H70 V40 L82 50 L70 60 V54 H54 V70 H60 L50 82 L40 70 H46 V54 H30 V60 L18 50 L30 40 V46 H46 V30 H40Z', 'upgrade': 'M50 18 L76 48 H60 V80 H40 V48 H24Z',
 'details': 'M50 20 a30 30 0 1 0 0.1 0Z', 'assign': 'M40 36 a10 10 0 1 0 0.1 0Z M22 76 Q24 54 40 54 Q56 54 58 76Z M62 48 l6 6 l12 -14', 'train': 'M50 26 L82 40 L50 54 L18 40Z M30 46 V62 Q50 74 70 62 V46',
 'manage': 'M24 76 V56 H36 V76Z M44 76 V40 H56 V76Z M64 76 V26 H76 V76Z', 'enter': 'M34 22 H70 V78 H34 M20 50 H54 L46 42 M54 50 L46 58', 'collect': 'M50 30 a20 20 0 1 0 0.1 0Z',
 'customize': 'M26 74 L60 40 L66 46 L32 80 L24 82Z M62 30 a10 10 0 0 1 14 14 l-6 6 l-14 -14Z', 'interact': 'M22 28 H78 V62 H48 L34 76 V62 H22Z', 'profile': 'M50 26 a12 12 0 1 0 0.1 0Z M26 78 Q28 52 50 52 Q72 52 74 78Z',
 'request': 'M50 20 a30 30 0 1 0 0.1 0Z', 'talk': 'M20 30 H66 V58 H42 L30 70 V58 H20Z M70 40 H80 V66 H74 V74 L66 66 H52', 'hire': 'M40 36 a10 10 0 1 0 0.1 0Z M22 76 Q24 54 40 54 Q56 54 58 76Z M70 42 V62 M60 52 H80',
 'skills': 'M50 18 L58 40 L82 40 L62 54 L70 78 L50 64 L30 78 L38 54 L18 40 L42 40Z', 'story': 'M22 26 Q36 22 50 30 Q64 22 78 26 V76 Q64 72 50 80 Q36 72 22 76Z M50 30 V80',
 'negotiate': 'M18 50 L34 34 L50 42 L66 34 L82 50 L66 66 L58 58 M18 50 L34 66 L42 58 M42 58 L50 66 M50 50 L58 58', 'partner': 'M30 40 a8 8 0 1 0 0.1 0Z M70 40 a8 8 0 1 0 0.1 0Z M16 74 Q18 54 30 54 Q42 54 44 74Z M56 74 Q58 54 70 54 Q82 54 84 74Z',
 'discount': 'M24 24 H52 L80 52 L52 80 L24 52Z', 'build': 'M22 78 H78 M30 78 V48 L50 30 L70 48 V78 M62 26 L76 18 M60 34 L80 24', 'rotate': 'M30 56 a20 20 0 1 1 8 16 M30 56 L22 46 M30 56 L40 48',
 'preview': 'M14 50 Q50 18 86 50 Q50 82 14 50Z M50 40 a10 10 0 1 0 0.1 0Z', 'cancel': 'M30 30 L70 70 M70 30 L30 70', 'expand': 'M24 40 V24 H40 M60 24 H76 V40 M76 60 V76 H60 M40 76 H24 V60', 'performance': 'M20 74 L40 52 L54 62 L80 30 M66 30 H80 V44',
 'lock': 'M32 46 H68 V78 H32Z M38 46 V36 a12 12 0 0 1 24 0 V46', 'check': 'M26 52 L42 68 L76 32', 'ad': 'M22 30 H78 V70 H22Z M44 40 V60 L60 50Z', 'coin': 'M50 22 a28 28 0 1 0 0.1 0Z',
 'happiness': 'M50 20 a30 30 0 1 0 0.1 0Z', 'trust': 'M50 20 Q66 28 78 28 Q78 64 50 80 Q22 64 22 28 Q34 28 50 20Z', 'growth': 'M22 76 H78 M30 70 V58 M44 70 V46 M58 70 V36 M72 70 V24',
 'inventory': 'M22 30 H78 V46 H22Z M26 46 V78 H74 V46 M42 56 H58', 'checkout': 'M22 66 H78 V78 H22Z M30 66 V36 H54 V66 M60 50 H74 V66', 'employees': 'M50 26 a10 10 0 1 0 0.1 0Z M32 76 Q34 50 50 50 Q66 50 68 76Z M50 50 L46 60 L50 68 L54 60Z',
 'equipment': 'M30 18 H70 V82 H30Z M30 46 H70 M38 30 V38 M38 56 V66', 'store_size': 'M18 78 V40 L36 28 L36 40 L54 28 L54 40 L72 28 V78Z', 'customer_exp': 'M50 76 L22 48 a14 14 0 0 1 28 -18 a14 14 0 0 1 28 18Z', 'operations': 'M50 30 a20 20 0 1 0 0.1 0Z',
 'gem': 'M30 30 H70 L82 44 L50 80 L18 44Z M18 44 H82 M38 30 L34 44 L50 80 L66 44 L62 30', 'xp': 'M50 18 L58 40 L82 40 L62 54 L70 78 L50 64 L30 78 L38 54 L18 40 L42 40Z', 'cart': 'M18 26 H28 L38 64 H72 L80 36 H32 M42 74 a4 4 0 1 0 0.1 0Z M68 74 a4 4 0 1 0 0.1 0Z',
 'residential': 'M20 50 L50 24 L80 50 M28 44 V78 H72 V44 M44 78 V60 H56 V78', 'commercial': 'M22 78 V34 H50 V78 M50 46 H78 V78 M30 44 H42 M30 56 H42 M58 56 H70', 'food': 'M34 20 V50 M28 20 V40 a6 6 0 0 0 12 0 V20 M34 50 V80 M62 20 Q76 30 70 52 H62 V80',
 'entertainment': 'M22 34 H78 V72 H22Z M22 34 L34 22 M42 34 L54 22 M62 34 L74 22', 'community': 'M50 22 L80 38 H20Z M26 42 V70 M40 42 V70 M60 42 V70 M74 42 V70 M20 74 H80', 'infrastructure': 'M38 20 L28 80 M62 20 L72 80 M50 26 V34 M50 46 V56 M50 68 V78', 'decoration': 'M50 20 a12 12 0 1 0 0.1 0Z M50 44 V80 M50 60 Q36 52 32 62 M50 66 Q64 58 68 68',
 'operations_m': 'M28 36 H72 L68 78 H32Z', 'service': 'M30 56 a20 20 0 0 1 40 0 M24 56 H76 M50 32 V28', 'business': 'M24 36 H76 V76 H24Z M40 36 V28 H60 V36 M24 52 H76', 'neighborhood': 'M18 78 V48 L32 38 L46 48 V78 M54 78 V36 L68 24 L82 36 V78', 'character': 'M50 26 a12 12 0 1 0 0.1 0Z M26 78 Q28 52 50 52 Q72 52 74 78Z',
 'theme': 'M50 20 a30 30 0 1 0 0.1 0Z', 'outfit': 'M30 28 L42 22 H58 L70 28 L80 44 L70 50 V78 H30 V50 L20 44Z', 'floor': 'M20 60 L50 44 L80 60 L50 76Z M20 60 V66 L50 82 L80 66 V60', 'wall': 'M20 24 H80 V76 H20Z M20 41 H80 M20 58 H80 M40 24 V41 M60 41 V58 M40 58 V76',
 'celebration': 'M24 78 L40 34 L66 60Z M52 28 L56 18 M66 34 L76 28 M70 48 L80 50', 'signage': 'M30 26 H70 V54 H30Z M50 54 V80 M40 80 H60', 'lighting': 'M50 20 a18 18 0 0 1 10 33 V62 H40 V53 A18 18 0 0 1 50 20Z M42 70 H58 M44 78 H56',
}
FILLED = {'home', 'store', 'upgrade', 'move', 'skills', 'xp', 'discount', 'trust', 'customer_exp', 'outfit', 'celebration', 'gem', 'check_f'}
ICONCOL = {'nav': '#24503B', 'action': '#3B7DD8', 'building': '#7B3AA8', 'upgrade': '#F28C28', 'mission': '#1E8C4E', 'cosmetic': '#E2435E', 'indicator': '#E8B62C', 'misc': '#24503B'}
def glyph(name, col=W_, sw=7):
    d = GLYPH[name]; fill = col if name in FILLED or name in ('profile', 'people', 'employees', 'character', 'partner', 'hire', 'assign', 'residential') else 'none'
    extra = ''
    if name == 'settings': extra = ''.join(f'<rect x="45" y="14" width="10" height="16" rx="3" fill="{col}" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45)) + f'<circle cx="50" cy="50" r="22" fill="{col}"/><circle cx="50" cy="50" r="9" fill="#000" fill-opacity="0.25"/>'; return extra
    if name in ('details', 'request'): return f'<circle cx="50" cy="50" r="30" fill="none" stroke="{col}" stroke-width="{sw}"/>' + (f'<path d="M50 44 V66" stroke="{col}" stroke-width="{sw+1}" stroke-linecap="round"/><circle cx="50" cy="33" r="5" fill="{col}"/>' if name == 'details' else f'<path d="M40 40 a10 10 0 1 1 14 9 q-4 2 -4 8" stroke="{col}" stroke-width="{sw}" fill="none" stroke-linecap="round"/><circle cx="50" cy="66" r="4.5" fill="{col}"/>')
    if name in ('collect', 'coin'): return f'<circle cx="50" cy="50" r="28" fill="{col}"/>' + txt(50, 62, '₦', 34, '#000', 800).replace('fill="#000"', 'fill="#000" fill-opacity="0.3"')
    if name == 'happiness': return f'<circle cx="50" cy="50" r="30" fill="{col}"/><circle cx="40" cy="44" r="4" fill="#000" fill-opacity=".35"/><circle cx="60" cy="44" r="4" fill="#000" fill-opacity=".35"/><path d="M36 58 Q50 72 64 58" stroke="#000" stroke-opacity=".35" stroke-width="5" fill="none" stroke-linecap="round"/>'
    if name == 'operations': return ''.join(f'<rect x="46" y="16" width="8" height="14" rx="2" fill="{col}" transform="rotate({a} 50 50)"/>' for a in range(0, 360, 60)) + f'<circle cx="50" cy="50" r="20" fill="none" stroke="{col}" stroke-width="{sw+2}"/>'
    if name == 'theme': return f'<path d="M50 20 a30 30 0 1 0 0 60 a8 8 0 0 0 4 -14 a6 6 0 0 1 6 -10 h8 a12 12 0 0 0 12 -12 a30 30 0 0 0 -30 -24Z" fill="{col}"/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="{c}"/>' for x, y, c in [(36, 40, '#E2435E'), (50, 32, '#E8B62C'), (64, 40, '#3B7DD8'), (34, 56, '#4CC38A')])
    if name == 'discount': return f'<path d="{d}" fill="{col}"/><circle cx="36" cy="36" r="5" fill="#000" fill-opacity=".3"/>' + txt(56, 62, '%', 24, '#000', 800).replace('fill="#000"', 'fill="#000" fill-opacity="0.3"')
    return f'<path d="{d}" fill="{fill}" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'
def badge(name, col, shape='circle', size=100):
    f, d = grad_fill(col, 'v', a=.3, b=.25)
    if shape == 'circle': b = f'<circle cx="50" cy="54" r="44" fill="{dk(col,.35)}"/><circle cx="50" cy="50" r="44" fill="{f}"/><ellipse cx="50" cy="28" rx="30" ry="14" fill="#fff" opacity="0.18"/>'
    else: b = f'<rect x="6" y="10" width="88" height="88" rx="22" fill="{dk(col,.35)}"/><rect x="6" y="6" width="88" height="88" rx="22" fill="{f}"/><ellipse cx="50" cy="24" rx="34" ry="12" fill="#fff" opacity="0.18"/>'
    return d + b + f'<g transform="translate(50 50) scale(0.62) translate(-50 -50)">{glyph(name)}</g>', '0 0 100 100'
def button(col, state='normal', w=320, h=100, label=None):
    if state == 'disabled': col = '#A8A39A'
    f, d = grad_fill(col, 'v', a=.25, b=.2); off = 6 if state == 'pressed' else 0
    o = d + (f'<rect x="0" y="10" width="{w}" height="{h-10}" rx="26" fill="{dk(col,.35)}"/>' if state != 'pressed' else '') + f'<rect x="0" y="{off}" width="{w}" height="{h-10}" rx="26" fill="{f}"/><rect x="14" y="{off+8}" width="{w-28}" height="{(h-10)*0.32}" rx="14" fill="#fff" opacity="0.2"/>'
    if label: o += txt(w / 2, off + (h - 10) / 2 + 12, label, 34, '#fff', 800)
    return o, f'0 0 {w} {h}'
def panel(kind):
    if kind == 'card': return '<rect x="0" y="6" width="200" height="200" rx="28" fill="#D9D2C5"/><rect x="0" y="0" width="200" height="200" rx="28" fill="#FFFDF8"/>', '0 0 200 206'
    if kind == 'dialog': return '<rect x="0" y="8" width="200" height="200" rx="32" fill="#1A3A2B"/><rect x="0" y="0" width="200" height="200" rx="32" fill="#24503B"/><rect x="10" y="10" width="180" height="180" rx="24" fill="#FFFDF8"/>', '0 0 200 208'
    if kind == 'speech': return '<rect x="0" y="0" width="200" height="160" rx="30" fill="#fff" stroke="#D9D2C5" stroke-width="4"/><path d="M40 156 L30 196 L80 158" fill="#fff" stroke="#D9D2C5" stroke-width="4"/><rect x="34" y="150" width="50" height="10" fill="#fff"/>', '-4 -4 208 204'
    if kind == 'topbar': return '<rect x="0" y="0" width="200" height="80" rx="40" fill="#000" opacity="0.35"/>', '0 0 200 80'
    if kind == 'progress_frame': return '<rect x="0" y="0" width="200" height="40" rx="20" fill="#1A3A2B"/><rect x="5" y="5" width="190" height="30" rx="15" fill="#0F241A"/>', '0 0 200 40'
    if kind == 'progress_fill': return '<defs><linearGradient id="pf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FCE08A"/><stop offset="1" stop-color="#E8B62C"/></linearGradient></defs><rect x="0" y="0" width="200" height="30" rx="15" fill="url(#pf)"/><rect x="10" y="4" width="180" height="8" rx="4" fill="#fff" opacity="0.35"/>', '0 0 200 30'
    if kind == 'toast': return '<rect x="0" y="6" width="200" height="90" rx="45" fill="#0F241A" opacity="0.5"/><rect x="0" y="0" width="200" height="90" rx="45" fill="#24503B"/>', '0 0 200 96'
def coin(frame=0):
    sx = abs(math.cos(frame * math.pi / 6)); f, d = grad_fill('#F5C542', 'r', a=.45, b=.25)
    return d + f'<g transform="translate(50 50) scale({max(.12,sx)} 1)"><circle r="40" fill="#C9971A"/><circle r="36" fill="{f}"/><circle r="28" fill="none" stroke="#C9971A" stroke-width="3"/>' + (txt(0, 13, '₦', 36, '#B07A0F', 800) if sx > .3 else '') + '</g>', '0 0 100 100'
def xp_star():
    f, d = grad_fill('#4CC38A', 'r', a=.4); return d + f'<path d="{GLYPH["xp"]}" fill="{f}" stroke="#1E8C4E" stroke-width="4" stroke-linejoin="round"/>' + txt(50, 60, 'XP', 16, '#fff', 800), '10 10 80 80'
def gem():
    return '<path d="M30 30 H70 L82 44 L50 80 L18 44Z" fill="#3BB0D9"/><path d="M18 44 H82 L50 80Z" fill="#2A8FBA"/><path d="M38 30 L34 44 H66 L62 30Z" fill="#8FDCF2"/>', '10 20 80 66'
def confetti_piece(i):
    c = ['#E2435E', '#E8B62C', '#4CC38A', '#3B7DD8', '#F28C28', '#7B3AA8'][i]
    return [f'<rect x="10" y="20" width="20" height="10" rx="2" fill="{c}"/>', f'<circle cx="20" cy="25" r="8" fill="{c}"/>', f'<path d="M10 30 L20 12 L30 30Z" fill="{c}"/>', f'<path d="M6 25 q7 -10 14 0 t14 0" stroke="{c}" stroke-width="4" fill="none"/>', f'<rect x="16" y="10" width="8" height="28" rx="2" fill="{c}"/>', f'<path d="M20 12 l4 9 h9 l-7 6 l3 9 l-9 -5 l-9 5 l3 -9 l-7 -6 h9z" fill="{c}"/>'][i], '0 0 40 50'
def burst(frame):
    s = 0.5 + frame * 0.18; o = f'<g transform="translate(100 100) scale({s})" opacity="{1 - frame*0.12}">' + ''.join(f'<path d="M0 0 L{90*math.cos(math.radians(a-5))} {90*math.sin(math.radians(a-5))} L{90*math.cos(math.radians(a+5))} {90*math.sin(math.radians(a+5))}Z" fill="#FCE08A"/>' for a in range(0, 360, 20)) + '<circle r="40" fill="#F5C542"/></g>'
    return o, '0 0 200 200'
def levelup():
    b, _ = burst(2); return b + '<path d="M30 120 H170 L160 150 H40Z" fill="#C8412E"/>' + txt(100, 143, 'LEVEL UP!', 22, '#FFF2B8', 800) + '<path d="M100 60 L118 96 H82Z" fill="#fff"/>', '0 0 200 200'
def dust(frame):
    s = 0.6 + frame * 0.2; op = 0.9 - frame * 0.2
    return ''.join(f'<circle cx="{100+dx*s}" cy="{110+dy*s*0.6}" r="{r*s}" fill="#C9B79C" opacity="{op}"/>' for dx, dy, r in [(-50, 10, 24), (-20, -10, 30), (20, -6, 28), (54, 12, 22), (0, 20, 26)]), '0 0 200 200'
def payment(frame):
    y = 60 - frame * 12; op = 1 - frame * 0.2
    return f'<g opacity="{op}"><rect x="40" y="{y}" width="120" height="50" rx="25" fill="#1E8C4E"/>' + txt(100, y + 34, '+₦250', 24, '#fff', 800) + '</g>', '0 0 200 120'
def bubble(kind):
    o = '<path d="M10 10 H90 V70 H46 L30 88 V70 H10Z" fill="#fff" stroke="#D9D2C5" stroke-width="3" stroke-linejoin="round"/>'
    g = {'happy': '<circle cx="50" cy="40" r="20" fill="#F5C542"/><circle cx="43" cy="35" r="3" fill="#2B2118"/><circle cx="57" cy="35" r="3" fill="#2B2118"/><path d="M40 45 Q50 55 60 45" stroke="#2B2118" stroke-width="3" fill="none"/>',
         'angry': '<circle cx="50" cy="40" r="20" fill="#E2452F"/><path d="M40 32 l8 4 M60 32 l-8 4" stroke="#2B2118" stroke-width="3"/><path d="M40 50 Q50 42 60 50" stroke="#2B2118" stroke-width="3" fill="none"/>',
         'sad': '<circle cx="50" cy="40" r="20" fill="#6FB3D9"/><circle cx="43" cy="36" r="3" fill="#2B2118"/><circle cx="57" cy="36" r="3" fill="#2B2118"/><path d="M40 50 Q50 42 60 50" stroke="#2B2118" stroke-width="3" fill="none"/><path d="M42 40 q-2 6 0 8" stroke="#3B7DD8" stroke-width="3"/>',
         'love': '<path d="M50 58 L32 40 a10 10 0 0 1 18 -12 a10 10 0 0 1 18 12Z" fill="#E2435E"/>', 'question': txt(50, 56, '?', 40, '#3B7DD8', 800), 'exclaim': txt(50, 56, '!', 40, '#C8412E', 800),
         'money': txt(50, 54, '₦', 34, '#1E8C4E', 800), 'zzz': txt(50, 52, 'Zzz', 24, '#7B3AA8', 800), 'idea': '<circle cx="50" cy="36" r="14" fill="#F5C542"/><rect x="44" y="48" width="12" height="10" fill="#8E979F"/>',
         'shopping': '<path d="M36 30 H64 L62 58 H38Z" fill="#E8B62C"/><path d="M44 30 a6 6 0 0 1 12 0" stroke="#8B6A4A" stroke-width="3" fill="none"/>', 'time': '<circle cx="50" cy="40" r="18" fill="none" stroke="#C8412E" stroke-width="4"/><path d="M50 30 V40 L58 46" stroke="#C8412E" stroke-width="4" fill="none"/>'}[kind]
    return o + g, '6 6 88 86'
def arrow(frame=0):
    dy = [0, 6, 10, 6][frame]
    return f'<g transform="translate(0 {dy})"><path d="M50 90 L20 54 H38 V10 H62 V54 H80Z" fill="#E8B62C" stroke="#fff" stroke-width="5" stroke-linejoin="round"/></g>', '10 0 80 110'
def ring(frame=0):
    s = 1 + frame * 0.08; op = 1 - frame * 0.22
    return f'<circle cx="60" cy="60" r="{40*s}" fill="none" stroke="#E8B62C" stroke-width="6" opacity="{op}"/><circle cx="60" cy="60" r="40" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="10 8"/>', '0 0 120 120'
REL = [('stranger', '#9AA3A8', 0), ('acquaintance', '#6FB3D9', 1), ('friendly', '#4CC38A', 2), ('trusted', '#E8B62C', 3), ('close_ally', '#E2435E', 4)]
def rel_badge(name, col, n):
    o = f'<path d="M50 10 L84 24 V52 Q84 78 50 92 Q16 78 16 52 V24Z" fill="{dk(col,.3)}"/><path d="M50 6 L84 20 V48 Q84 74 50 88 Q16 74 16 48 V20Z" fill="{col}"/>'
    o += f'<path d="M50 62 L34 46 a8 8 0 0 1 16 -10 a8 8 0 0 1 16 10Z" fill="#fff" opacity="{0.35 + n*0.16}"/>' + ''.join(f'<circle cx="{50+(i-(n-1)/2)*10}" cy="74" r="3" fill="#fff"/>' for i in range(n))
    return o, '10 0 80 96'
