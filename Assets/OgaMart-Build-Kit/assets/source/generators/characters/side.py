import sys; sys.path.insert(0, '/home/claude/rig2')
from math import sin, cos, radians
from rig2 import limb, uid, cr_path, fk, _dark, _light, pattern_def, GROUND
SX = 100
def head_side(c, y, expr='smile', pid=None):
    x = SX + 2; o = []; h, hh = c.hair, c.hair_h
    o.append(limb((x - 2, y + 52), (x - 4, y + 72), 8 * min(c.girth, 1.15), 9 * min(c.girth, 1.2), c.skin, c.skin_d, 0.45))
    back = {'bun': f'<circle cx="{x-12}" cy="{y+2}" r="14" fill="{h}"/>', 'silver_bun': f'<circle cx="{x-16}" cy="{y+12}" r="11" fill="{h}"/>',
            'puffs': f'<circle cx="{x-14}" cy="{y+6}" r="15" fill="{h}"/>', 'afro': f'<ellipse cx="{x-4}" cy="{y+22}" rx="28" ry="30" fill="{h}"/>',
            'bouffant': f'<ellipse cx="{x-6}" cy="{y+18}" rx="30" ry="28" fill="{h}"/>', 'updo': f'<path d="M{x-14} {y+12} C{x-22} {y-38} {x+14} {y-38} {x+8} {y+12}Z" fill="{h}"/>',
            'long_braids': f'<path d="M{x-18} {y+22} C{x-28} {y+60} {x-26} {y+92} {x-22} {y+104} L{x-6} {y+104} C{x-6} {y+80} {x-4} {y+50} {x-2} {y+24}Z" fill="{h}"/>'}.get(c.hairstyle, '')
    if c.headwear not in ('gele', 'helmet'): o.append(back)
    g = c.girth
    face = (f'M{x-18} {y+30} C{x-20} {y+10} {x-6} {y+4} {x+4} {y+5} C{x+16} {y+6} {x+20} {y+18} {x+20} {y+28} L{x+21} {y+33} '
            f'C{x+22} {y+36} {x+26} {y+40} {x+27} {y+43} C{x+27} {y+45} {x+24} {y+46} {x+22} {y+46} L{x+22} {y+50} C{x+23} {y+52} {x+22} {y+54} {x+20} {y+55} '
            f'C{x+21} {y+58} {x+19} {y+62} {x+12} {y+63+2*(g-1)*5} C{x+4} {y+64+(g-1)*8} {x-4} {y+58} {x-8} {y+54} C{x-14} {y+50} {x-18} {y+42} {x-18} {y+30}Z')
    cid = uid(); o.append(f'<clipPath id="{cid}"><path d="{face}"/></clipPath><path d="{face}" fill="{c.skin}"/>')
    o.append(f'<path d="M{x-20} {y+20} C{x-10} {y+30} {x-8} {y+50} {x+2} {y+70} L{x-30} {y+70}Z" fill="{c.skin_d}" opacity="0.45" clip-path="url(#{cid})"/>')
    o.append(f'<ellipse cx="{x-3}" cy="{y+38}" rx="4" ry="6.5" fill="{c.skin}"/><path d="M{x-4} {y+34} q3 4 0 8" stroke="{c.skin_d}" stroke-width="1.2" fill="none"/>')
    if expr in ('happy', 'laugh', 'blink'): o.append(f'<path d="M{x+9} {y+35} Q{x+13} {y+31.5} {x+17} {y+35}" stroke="#1A0F08" stroke-width="1.6" fill="none"/>')
    else: o.append(f'<path d="M{x+9} {y+35} Q{x+13} {y+32.5} {x+17} {y+35} Q{x+13} {y+37} {x+9} {y+35}Z" fill="#FBF6EE"/><circle cx="{x+14.5}" cy="{y+35}" r="2" fill="#2A170C"/><path d="M{x+8.5} {y+34.5} Q{x+13} {y+31.5} {x+17.5} {y+34.3}" stroke="#1A0F08" stroke-width="1.5" fill="none"/>')
    bc = c.hair if c.age != 'old' else '#E8E3D8'
    o.append(f'<path d="M{x+8} {y+28} Q{x+13} {y+26} {x+19} {y+28}" stroke="{bc}" stroke-width="{2 if c.sex == "f" else 2.8}" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{x+23} {y+45.5} Q{x+21} {y+44} {x+20} {y+45}" stroke="{c.skin_d}" stroke-width="1.2" fill="none"/>')
    if expr in ('talk', 'laugh', 'surprised'): o.append(f'<path d="M{x+18} {y+50} q3 5 4 0z" fill="#4A1A12"/>')
    o.append(f'<path d="M{x+18} {y+50} Q{x+21} {y+49} {x+22.5} {y+50} M{x+18.5} {y+53.5} Q{x+21} {y+55} {x+21.5} {y+53.5}" stroke="{c.lip}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    f = c.facial; fc = c.facial_col
    if f == 'mustache': o.append(f'<path d="M{x+14} {y+48} C{x+18} {y+45} {x+24} {y+46} {x+27} {y+50} C{x+22} {y+50} {x+18} {y+50} {x+14} {y+48}Z" fill="{fc}"/>')
    if f in ('beard_thick', 'beard_long'):
        L = 90 if f == 'beard_long' else 70
        o.append(f'<path d="M{x-6} {y+40} C{x-6} {y+58} {x+4} {y+L} {x+14} {y+L-2} C{x+22} {y+L-10} {x+24} {y+60} {x+22} {y+54} L{x+16} {y+52} C{x+10} {y+50} {x+4} {y+46} {x-6} {y+40}Z" fill="{fc}"/>')
    e = c.eyewear; ec = c.eye_col
    if e == 'oversized': o.append(f'<circle cx="{x+14}" cy="{y+35}" r="8" fill="#fff" fill-opacity="0.2" stroke="{ec}" stroke-width="2.4"/><path d="M{x+6} {y+34} H{x-3}" stroke="{ec}" stroke-width="2.2"/>')
    elif e in ('round', 'stylish', 'colorful'): o.append(f'<rect x="{x+8}" y="{y+30}" width="12" height="9" rx="{4.5 if e == "round" else 3}" fill="#fff" fill-opacity="0.2" stroke="{ec}" stroke-width="{2.4 if e == "colorful" else 1.6}"/><path d="M{x+8} {y+33} H{x-3}" stroke="{ec}" stroke-width="1.6"/>')
    elif e == 'sunglasses': o.append(f'<path d="M{x+8} {y+31} h13 v4 q0 5 -6 5 q-7 0 -7 -5z" fill="#151515"/><path d="M{x+8} {y+33} H{x-3}" stroke="#151515" stroke-width="2"/>')
    hw = c.headwear
    if hw not in ('gele', 'helmet', 'straw_hat'):
        if c.hairstyle in ('bun', 'puffs', 'updo', 'long_braids', 'silver_bun'):
            o.append(f'<path d="M{x-19} {y+38} C{x-24} {y+12} {x-8} {y+2} {x+4} {y+3} C{x+14} {y+4} {x+20} {y+12} {x+20} {y+22} C{x+12} {y+14} {x+2} {y+14} {x-6} {y+20} C{x-10} {y+26} {x-10} {y+32} {x-9} {y+40}Z" fill="{h}"/>')
        elif c.hairstyle in ('afro', 'bouffant'):
            o.append(f'<path d="M{x-20} {y+40} C{x-26} {y+4} {x-6} {y-6} {x+6} {y-4} C{x+18} {y-2} {x+22} {y+12} {x+21} {y+22} C{x+12} {y+14} {x+2} {y+14} {x-6} {y+22} L{x-10} {y+42}Z" fill="{h}"/>')
        elif c.hairstyle == 'messy':
            o.append(f'<path d="M{x-19} {y+36} L{x-24} {y+14} L{x-14} {y+12} L{x-12} {y+0} L{x-2} {y+6} L{x+4} {y-4} L{x+10} {y+6} L{x+18} {y+2} L{x+20} {y+20} C{x+12} {y+14} {x+2} {y+15} {x-4} {y+22} L{x-8} {y+36}Z" fill="{h}"/>')
        elif c.hairstyle == 'bald':
            o.append(f'<path d="M{x-18} {y+40} C{x-20} {y+30} {x-18} {y+24} {x-14} {y+22} L{x-6} {y+38}Z" fill="{h}"/>')
        else:
            o.append(f'<path d="M{x-18.5} {y+34} C{x-21} {y+10} {x-6} {y+3} {x+4} {y+4} C{x+14} {y+5} {x+19} {y+12} {x+19.5} {y+21} C{x+12} {y+14} {x+2} {y+15} {x-4} {y+22} L{x-8} {y+36}Z" fill="{h}"/>')
    col = c.head_col; cd = _dark(col)
    if hw == 'gele':
        f = f'url(#{pid})' if pid else col
        o.append(f'<path d="M{x-24} {y+30} C{x-34} {y-6} {x-10} {y-26} {x+6} {y-14} C{x+18} {y-24} {x+30} {y-4} {x+20} {y+24} C{x+10} {y+12} {x-8} {y+14} {x-24} {y+30}Z" fill="{f}"/><path d="M{x-30} {y-2} C{x-40} {y-14} {x-46} {y+2} {x-36} {y+12} C{x-32} {y+6} {x-28} {y+2} {x-24} {y+0}Z" fill="{col}"/><path d="M{x-18} {y+10} C{x-4} {y-2} {x+10} {y} {x+18} {y+10}" stroke="{cd}" stroke-width="3" fill="none"/>')
    elif hw == 'straw_hat': o.append(f'<ellipse cx="{x+2}" cy="{y+14}" rx="38" ry="7" fill="#D9B26A"/><path d="M{x-18} {y+14} C{x-18} {y-12} {x+20} {y-12} {x+20} {y+14}Z" fill="#C9A055"/><rect x="{x-18}" y="{y+6}" width="38" height="6" fill="#8C4B32"/>')
    elif hw == 'kufi': o.append(f'<path d="M{x-19} {y+16} C{x-19} {y-6} {x+21} {y-6} {x+21} {y+16}Z" fill="{col}"/><path d="M{x-19} {y+14} H{x+21}" stroke="#E8B62C" stroke-width="1.5"/>')
    elif hw == 'cap': o.append(f'<path d="M{x-19} {y+20} C{x-20} {y-2} {x+20} {y-2} {x+20} {y+20}Z" fill="{col}"/><path d="M{x+16} {y+18} Q{x+30} {y+16} {x+36} {y+20} Q{x+28} {y+24} {x+16} {y+22}Z" fill="{cd}"/>')
    elif hw == 'helmet': o.append(f'<path d="M{x-22} {y+30} C{x-24} {y-6} {x+24} {y-6} {x+24} {y+26}Z" fill="#E2435E"/><path d="M{x-16} {y+6} C{x-6} {y-2} {x+8} {y-2} {x+18} {y+8}" stroke="#F5C542" stroke-width="5" fill="none"/><path d="M{x-20} {y+18} C{x-8} {y+10} {x+10} {y+10} {x+22} {y+18}" stroke="#3B7DD8" stroke-width="5" fill="none"/><path d="M{x+18} {y+24} L{x+30} {y+24} L{x+28} {y+30} L{x+18} {y+30}Z" fill="#2B2118"/>')
    elif hw == 'fila': o.append(f'<path d="M{x-19} {y+18} C{x-18} {y-6} {x+22} {y-8} {x+22} {y+14} L{x+28} {y+6} C{x+18} {y-2} {x+2} {y-4} {x-19} {y+18}Z" fill="{col}"/>')
    if c.earrings:
        r = {'small': 2.5, 'hoop': 4, 'big': 6.5}[c.earrings]; o.append(f'<circle cx="{x-3}" cy="{y+46+r}" r="{r}" fill="none" stroke="#E8B62C" stroke-width="{1.6 if r < 5 else 2.4}"/>')
    return ''.join(o)
def torso_pts(c, y):
    g = c.girth; b = c.bust if c.sex == 'f' else 0; h = c.hip if c.sex == 'f' else 0.6; bel = c.belly; r = c.rear
    front = [(SX + 4, y + 68), (SX + 14 * g, y + 84), (SX + (16 + 8 * b) * g, y + 106), (SX + (12 + 2 * b + 6 * bel) * g, y + 124), (SX + (10 + 14 * bel) * g, y + 142), (SX + (12 + 14 * bel) * g, y + 160), (SX + 13 * g, y + 180)]
    back = [(SX - (6 + 12 * h + 8 * r) * g, y + 198), (SX - (14 + 20 * h + 22 * r) * g, y + 180), (SX - (10 + 8 * h + 6 * r) * g, y + 154), (SX - 14 * g, y + 132), (SX - 18 * g, y + 100), (SX - 14 * g, y + 78), (SX - 6, y + 68)]
    if c.outfit in ('dress', 'robe', 'agbada') or c.bottom in ('skirt', 'long_skirt'):
        return front[:5] + [(SX + 10 * g, y + 152), (SX - 16 * g, y + 152)] + back[3:]
    return front + back
def shoe_side(c, a, ft, far):
    dk = (lambda x: _dark(x)) if far else (lambda x: x)
    tip = (a[0] + 24 * cos(radians(-ft)), a[1] + 24 * sin(radians(-ft)) + 6); heel = (a[0] - 6, a[1] + 8)
    sc, sd = dk(c.shoes), dk(c.shoes_d)
    if c.shoe == 'boot':
        return f'<path d="M{heel[0]-2:.1f} {heel[1]-22:.1f} L{a[0]+8:.1f} {a[1]-14:.1f} L{a[0]+8:.1f} {a[1]-2:.1f} Q{tip[0]:.1f} {tip[1]-10:.1f} {tip[0]:.1f} {tip[1]:.1f} L{heel[0]:.1f} {heel[1]:.1f}Z" fill="{sc}"/><path d="M{heel[0]:.1f} {heel[1]:.1f} L{tip[0]:.1f} {tip[1]:.1f}" stroke="{sd}" stroke-width="3"/>'
    if c.shoe == 'sandal':
        return f'<path d="M{heel[0]:.1f} {heel[1]:.1f} L{tip[0]:.1f} {tip[1]:.1f}" stroke="{sc}" stroke-width="4" stroke-linecap="round"/><path d="M{a[0]:.1f} {a[1]+2:.1f} q6 -2 10 4" stroke="{sd}" stroke-width="2.4" fill="none"/>'
    o = f'<path d="M{heel[0]:.1f} {heel[1]-12:.1f} L{a[0]+5:.1f} {a[1]-4:.1f} Q{tip[0]:.1f} {tip[1]-8:.1f} {tip[0]:.1f} {tip[1]:.1f} L{heel[0]:.1f} {heel[1]:.1f}Z" fill="{sc}"/>'
    o += f'<path d="M{heel[0]:.1f} {heel[1]:.1f} L{tip[0]:.1f} {tip[1]:.1f}" stroke="{"#F4F1EA" if c.shoe == "sneaker" else sd}" stroke-width="{3 if c.shoe == "sneaker" else 2}" stroke-linecap="round"/>'
    if c.shoe == 'heel': o += f'<path d="M{heel[0]:.1f} {heel[1]-4:.1f} l1 8" stroke="{sd}" stroke-width="3"/>'
    if c.shoe == 'dress_shoe': o += f'<ellipse cx="{tip[0]-6:.1f}" cy="{tip[1]-4:.1f}" rx="3" ry="1.4" fill="#fff" opacity="0.7"/>'
    return o
def leg_side(c, hip, th, kn, ft, far=False):
    g = c.girth; k = fk(hip, 86, th); a = fk(k, 80, th - kn)
    dk = (lambda x: _dark(x)) if far else (lambda x: x)
    if (c.bottom == 'pants' and c.outfit not in ('dress', 'robe')) or c.outfit == 'agbada':
        o = limb(hip, k, 16 * g, 11 * g, dk(c.bot), dk(c.bot_d)) + limb(k, a, 11 * g, 8 * min(g, 1.2), dk(c.bot), dk(c.bot_d))
    else:
        mid = (k[0] * 0.6 + a[0] * 0.4 - 2.5, k[1] * 0.6 + a[1] * 0.4)
        o = limb(hip, k, 14.5 * g, 8.8 * g, dk(c.skin), dk(c.skin_d)) + limb(k, mid, 8.8 * g, 10 * g, dk(c.skin), dk(c.skin_d)) + limb(mid, a, 10 * g, 5.4 * min(g, 1.2), dk(c.skin), dk(c.skin_d))
    return o + shoe_side(c, a, ft, far), a
def arm_side(c, sh, a1, bend, far=False, hand_kind='rest', pid=None):
    g = min(c.girth, 1.4); e = fk(sh, 54, a1); w = fk(e, 48, a1 + bend)
    dk = (lambda x: _dark(x)) if far else (lambda x: x)
    o = limb(sh, e, 9.5 * g, 7.2 * g, dk(c.skin), dk(c.skin_d)) + limb(e, w, 7 * g, 5.2 * g, dk(c.skin), dk(c.skin_d))
    if c.outfit in ('agbada', 'dress', 'robe'): sc, sd = c.outfit_col, c.outfit_d
    elif c.jacket: sc, sd = c.jacket, _dark(c.jacket)
    else: sc, sd = c.top, c.top_d
    sf = f'url(#{pid})' if c.pattern and pid and not far else dk(sc)
    sl = 'wide' if c.outfit in ('agbada', 'robe') else c.sleeve
    if sl == 'short': o += limb(fk(sh, 3, a1), fk(sh, 24, a1), 10.5 * g, 9.5 * g, sf, dk(sd))
    elif sl == 'puff': o += limb(fk(sh, 2, a1), fk(sh, 20, a1), 13 * g, 11 * g, sf, dk(sd))
    elif sl == 'long': o += limb(sh, e, 11 * g, 9 * g, sf, dk(sd)) + limb(e, fk(e, 42, a1 + bend), 9 * g, 7.4 * g, sf, dk(sd))
    elif sl == 'wide': o += limb(sh, e, 12 * g, 13 * g, sf, dk(sd)) + limb(e, fk(e, 30, a1 + bend), 13 * g, 16 * g, sf, dk(sd))
    hx, hy = fk(w, 8, a1 + bend)
    if c.watch and not far: o += limb(fk(e, 40, a1 + bend), fk(e, 45, a1 + bend), 6.5, 6, '#E8B62C', '#B98A12')
    o += f'<g transform="translate({hx:.1f} {hy:.1f}) rotate({-(a1+bend):.1f})"><path d="M-6 -6 Q-7 6 -3 10 Q0 12 3 10 Q7 6 6 -6Z" fill="{dk(c.skin)}"/></g>'
    return o, (hx, hy)
# walk tables
WALK = [(24, 4, 12), (14, 22, 0), (-2, 8, 0), (-16, 4, -10), (-24, 10, -30), (-10, 42, -20), (8, 58, 0), (20, 26, 8)]
RUN = [(36, 20, 15), (20, 50, 0), (-6, 30, 0), (-28, 10, -25), (-36, 30, -40), (-14, 90, -20), (14, 110, 0), (32, 60, 10)]
BOB = [0, 4, -1, -3, 0, 4, -1, -3]
STYLE = {'normal': dict(stride=1, knee=1, arm=0.8, bob=1, lean=0, sway=0), 'sway': dict(stride=0.7, knee=0.8, arm=0.45, bob=0.7, lean=0, sway=5),
         'run': dict(stride=1, knee=1, arm=1.6, bob=1.8, lean=12, sway=0, table='run'), 'old': dict(stride=0.6, knee=0.6, arm=0.35, bob=0.5, lean=7, sway=0),
         'confident': dict(stride=1.1, knee=1, arm=1.05, bob=1, lean=-2, sway=0), 'brisk': dict(stride=0.85, knee=1.2, arm=1.0, bob=1.2, lean=3, sway=0),
         'strut': dict(stride=1.0, knee=0.9, arm=0.6, bob=0.8, lean=-3, sway=3)}
def side(c, f, style='normal'):
    fr = f; st = STYLE[style]; T = RUN if st.get('table') == 'run' else WALK
    th, kn, ft = T[f]; th2, kn2, ft2 = T[(f + 4) % 8]
    th *= st['stride']; th2 *= st['stride']; kn *= st['knee']; kn2 *= st['knee']
    if c.outfit in ('dress', 'robe') or c.bottom == 'long_skirt': th *= 0.6; th2 *= 0.6; kn *= 0.7; kn2 *= 0.7
    bob = BOB[f] * st['bob']; pid = uid('pat') if c.pattern else None
    hip = (SX, 182 + bob); sh = (SX - 2, 82 + bob)
    o = [f'<defs>{pattern_def(c, pid)}</defs>' if pid else '']
    if c.backpack:
        col = c.backpack; o.append(f'<rect x="{SX-62}" y="{70+bob}" width="48" height="90" rx="8" fill="{_dark(col)}"/><rect x="{SX-58}" y="{74+bob}" width="44" height="82" rx="7" fill="{col}"/><path d="M{SX-56} {92+bob} h40" stroke="{_dark(col)}" stroke-width="2"/>')
    if st['table'] if 'table' in st else False:
        a_far = (th * 0.9 + 10, -85); a_near = (-th * 0.9 + 10, -85)
    else:
        a_far = (th * st['arm'], -8 - max(0, th) * 0.6); a_near = (-th * st['arm'], -10 - max(0, -th) * 0.7)
    if c.stick: a_near = (-6 + th * 0.3, -40)
    far_arm, _ = arm_side(c, sh, a_far[0], a_far[1], far=True, pid=pid)
    o.append(f'<g id="arm_far" inkscape:label="arm_far">{far_arm}</g>')
    lf, ank_f = leg_side(c, hip, th2, kn2, ft2, far=True); o.append(f'<g id="leg_far" inkscape:label="leg_far">{lf}</g>')
    ln, ank_n = leg_side(c, hip, th, kn, ft); o.append(f'<g id="leg_near" inkscape:label="leg_near">{ln}</g>')
    pts = torso_pts(c, bob); td = cr_path(pts); cid = uid(); y = bob
    body = f'<clipPath id="{cid}"><path d="{td}"/></clipPath>'
    out = c.outfit; g = c.girth
    if out in ('dress', 'robe', 'agbada') or c.bottom in ('skirt', 'long_skirt'):
        hem = {'dress': 322, 'robe': 336, 'agbada': 300}.get(out, 248 if c.bottom == 'skirt' else 300)
        hp = c.hip if c.sex == 'f' else 0.7
        back = (14 + 16 * hp + 22 * c.rear) * g * (0.8 if c.sex == 'm' else 1); frontw = (14 + 6 * c.belly) * g
        hy = min(hem, ank_n[1] - 14)
        hb = min(SX - back * 0.72, min(ank_n[0], ank_f[0]) - 14); hf = max(SX + frontw + 8, max(ank_n[0], ank_f[0]) + 16)
        if out == 'agbada' or c.bottom == 'skirt': hb = SX - back * 0.9; hf = SX + frontw + 14
        f = f'url(#{pid})' if c.pattern and pid else (c.outfit_col if out else c.bot); fd = c.outfit_d if out else c.bot_d
        body += (f'<path d="M{SX-12*g} {140+y} C{SX-back*0.9} {150+y} {SX-back-2} {176+y} {SX-back} {200+y} C{SX-back+2} {236+y} {hb-2} {hem-50+y} {hb} {hem+y} '
                 f'Q{(hb+hf)/2} {hem+5+y} {hf} {hem+y} C{hf-4} {hem-60+y} {SX+frontw+2} {200+y} {SX+frontw-2} {140+y}Z" fill="{f}"/>'
                 f'<path d="M{SX-back+6} {190+y} C{SX-back+10} {236+y} {hb+6} {hem-50+y} {hb+8} {hem+y} L{hb} {hem+y} C{hb-2} {hem-50+y} {SX-back+2} {236+y} {SX-back} {200+y}Z" fill="#000" opacity="0.18"/>'
                 f'<path d="M{SX+2} {200+y} C{SX} {240+y} {(hb+hf)/2} {hem-40+y} {(hb+hf)/2} {hem+y}" stroke="#000" stroke-opacity="0.15" stroke-width="2" fill="none"/>')
        sw = 0
        if out: body += f'<path d="M{hb+1} {hem-9+y} Q{(hb+hf)/2} {hem-5+y} {hf-1} {hem-9+y}" stroke="{c.trim}" stroke-width="5" fill="none"/>'
    tfill = (f'url(#{pid})' if c.pattern and pid else c.outfit_col) if out in ('dress', 'robe') else (f'url(#{pid})' if c.pattern and pid and not out else c.top)
    body += f'<path d="{td}" fill="{tfill}"/>'
    if out == 'agbada': body += f'<path d="M{SX-34*g} {76+y} C{SX-50*g} {140+y} {SX-48*g} {220+y} {SX-40*g} {290+y} L{SX+34*g} {290+y} C{SX+40*g} {220+y} {SX+34*g} {140+y} {SX+18} {76+y}Z" fill="{c.outfit_col}"/><path d="M{SX+4} {70+y} Q{SX+20} {110+y} {SX+14} {130+y}" stroke="{c.trim}" stroke-width="3.5" fill="none"/>'
    if c.bottom == 'pants' and not out:
        hem = 176 + y
        body += f'<path d="M{SX-40} {hem} L{SX+40} {hem} L{SX+40} {215+y} L{SX-40} {215+y}Z" fill="{c.bot}" clip-path="url(#{cid})"/>'
        if c.top_kind not in ('oversized', 'overalls'): body += f'<rect x="{SX-40}" y="{hem-6}" width="80" height="7" fill="#2B1F17" clip-path="url(#{cid})"/>'
    if c.top_kind == 'overalls' or c.vest == 'overalls': body += f'<path d="M{SX-4} {108+y} L{SX+18*g} {108+y} L{SX+16*g} {180+y} L{SX-6} {180+y}Z" fill="{c.bot}" clip-path="url(#{cid})"/><path d="M{SX-2} {76+y} L{SX+6} {110+y}" stroke="{c.bot}" stroke-width="6"/>'
    if c.apron: body += f'<path d="M{SX+4} {100+y} L{SX+22*g} {100+y} L{SX+24*g} {214+y} L{SX+2} {214+y}Z" fill="{c.apron}"/>'
    if c.vest and c.vest != 'overalls': body += f'<path d="M{SX-20*g} {80+y} L{SX+16*g} {80+y} L{SX+14*g} {172+y} L{SX-18*g} {172+y}Z" fill="{c.vest}" clip-path="url(#{cid})"/>'
    if c.top_kind == 'suit': body += f'<path d="M{SX+4} {70+y} L{SX+14} {110+y} L{SX+8} {70+y}Z" fill="#F4F4F4"/>'
    if c.tie: body += f'<path d="M{SX+10} {74+y} l5 36 l-4 6 l-3 -6z" fill="{c.tie}"/>'
    if c.chain: body += f'<path d="M{SX+2} {72+y} Q{SX+16} {100+y} {SX+14} {104+y}" stroke="#E8B62C" stroke-width="2.4" fill="none"/>'
    body += f'<path d="M{SX-40} {60+y} C{SX-14} {100+y} {SX-12} {150+y} {SX-20} {215+y} L{SX-60} {215+y}Z" fill="#000" opacity="0.15" clip-path="url(#{cid})"/>'
    if c.sex == 'f' and c.bust > 0.3: body += f'<path d="M{SX+4} {118+y} Q{SX+14} {124+y} {SX+20*g} {116+y}" stroke="#000" stroke-opacity="0.2" stroke-width="1.8" fill="none" clip-path="url(#{cid})"/>'
    o.append(f'<g id="torso" inkscape:label="torso">{body}</g>')
    hs = f' transform="translate({SX} {66+bob}) scale(1.4) translate({-SX} {-66-bob})"' if c.age == 'child' else ''
    o.append(f'<g id="head" inkscape:label="head"{hs}>{head_side(c, bob - 2, "smile", pid)}</g>')
    near_arm, hp = arm_side(c, sh, a_near[0], a_near[1], pid=pid)
    o.append(f'<g id="arm_near" inkscape:label="arm_near">{near_arm}</g>')
    items = ''
    if c.handbag:
        col = c.handbag; x0, y0 = fk(fk(sh, 54, a_near[0]), 10, a_near[0] + a_near[1])
        items += f'<path d="M{x0-6:.1f} {y0:.1f} C{x0-8:.1f} {y0+16:.1f} {x0+12:.1f} {y0+16:.1f} {x0+10:.1f} {y0:.1f}" stroke="#2B2118" stroke-width="3" fill="none"/><rect x="{x0-12:.1f}" y="{y0+12:.1f}" width="30" height="24" rx="6" fill="{col}"/><rect x="{x0-12:.1f}" y="{y0+12:.1f}" width="30" height="7" rx="3.5" fill="{_dark(col)}"/>'
    if c.stick: items += f'<path d="M{hp[0]:.1f} {hp[1]-4:.1f} L{hp[0]+14+th*0.4:.1f} {GROUND:.1f}" stroke="#6B4A32" stroke-width="4" stroke-linecap="round"/><path d="M{hp[0]:.1f} {hp[1]-4:.1f} q0 -10 -9 -10" stroke="#6B4A32" stroke-width="4" fill="none" stroke-linecap="round"/>'
    if c.prop in ('basket', 'snackbox', 'box', 'clipboard', 'tablet', 'pot', 'clutch', 'shopping_bag'):
        from rig2 import prop_svg
        items += f'<g transform="translate({hp[0]+4:.1f} {hp[1]+8:.1f}) scale(0.8)">{prop_svg(c.prop, 0, 0)}</g>'
    o.append(f'<g id="props" inkscape:label="props">{items}</g>')
    inner = ''.join(o)
    tf = []
    if c.height != 1: tf.append(f'translate({SX} {GROUND}) scale({c.height}) translate({-SX} {-GROUND})')
    if st['lean']: tf.append(f'rotate({st["lean"]} {SX} {GROUND})')
    if st['sway']: tf.append(f'rotate({st["sway"] * (1 if fr % 4 < 2 else -1)} {SX} {GROUND})')
    shadow = f'<ellipse cx="{SX+4}" cy="{GROUND+3}" rx="{40*c.girth*c.height}" ry="5.5" fill="#000" opacity="0.13"/>'
    return shadow + (f'<g transform="{" ".join(tf)}">{inner}</g>' if tf else inner)
