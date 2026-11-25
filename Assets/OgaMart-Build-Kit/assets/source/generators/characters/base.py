# jointed 2D character rig: front view (idle/gestures) + side view (walk). svg strings.
from math import sin, cos, radians, hypot, pi
_id = [0]
def uid(p='c'): _id[0] += 1; return f'{p}{_id[0]}'
def P(x, y): return f'{x:.1f} {y:.1f}'
def capsule_d(ax, ay, bx, by, r1, r2):
    dx, dy = bx - ax, by - ay; L = hypot(dx, dy) or 1e-6; ux, uy = dx / L, dy / L; nx, ny = -uy, ux
    return (f'M{P(ax+nx*r1, ay+ny*r1)} L{P(bx+nx*r2, by+ny*r2)} A{r2:.1f} {r2:.1f} 0 0 0 {P(bx-nx*r2, by-ny*r2)} '
            f'L{P(ax-nx*r1, ay-ny*r1)} A{r1:.1f} {r1:.1f} 0 0 0 {P(ax+nx*r1, ay+ny*r1)} Z')
def limb(a, b, r1, r2, col, shade, k=0.5):
    """tapered capsule with a soft shade strip on the screen-right side (light from top-left)"""
    d = capsule_d(a[0], a[1], b[0], b[1], r1, r2); cid = uid()
    dx, dy = b[0] - a[0], b[1] - a[1]; L = hypot(dx, dy) or 1; nx, ny = -dy / L, dx / L
    if nx < 0: nx, ny = -nx, -ny
    off = 1 - k
    sd = capsule_d(a[0] + nx * r1 * (1 + off), a[1] + ny * r1 * (1 + off), b[0] + nx * r2 * (1 + off), b[1] + ny * r2 * (1 + off), r1, r2)
    return f'<clipPath id="{cid}"><path d="{d}"/></clipPath><path d="{d}" fill="{col}"/><path d="{sd}" fill="{shade}" clip-path="url(#{cid})"/>'
def cr_path(pts, closed=True):
    """catmull-rom through points -> smooth cubic path"""
    n = len(pts); s = f'M{P(*pts[0])}'
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = pts[(i - 1) % n] if closed or i > 0 else pts[0]; p1 = pts[i]; p2 = pts[(i + 1) % n]; p3 = pts[(i + 2) % n] if closed or i + 2 < n else pts[-1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        s += f' C{P(*c1)} {P(*c2)} {P(*p2)}'
    return s + (' Z' if closed else '')
def sym(cx, prof):
    """symmetric outline from (y, halfwidth) list, top to bottom"""
    right = [(cx + hw, y) for y, hw in prof]; left = [(cx - hw, y) for y, hw in reversed(prof)]
    return right + left
def fk(origin, length, ang):  # ang: degrees, 0 = straight down, + = toward screen-right
    return (origin[0] + length * sin(radians(ang)), origin[1] + length * cos(radians(ang)))

# ---------------- character definition ----------------
class Char:
    def __init__(self, **k):
        self.__dict__.update(dict(skin='#9A5E36', skin_d='#7A4526', skin_h='#B57548', lip='#7E3B2E', hair='#1B110B', hair_h='#3A2618',
            top='#F2B705', top_d='#C99400', top_h='#FFD24D', bottom='pants', bot='#2F4A7A', bot_d='#22385E', shoes='#E2435E', shoes_d='#B42D45',
            sex='f', bust=1.0, hip=1.0, belly=0.0, waist=1.0, hairstyle='bun', sleeve='short', shoe='flat', earrings=True, height=1.0, glasses=None))
        self.__dict__.update(k)

# ---------------- FRONT VIEW ----------------
CX = 100
def head_front(c, mouth='smile', blink=False, hy=0):
    o = []
    y0 = hy
    # hair behind head
    if c.hairstyle == 'bun': o.append(f'<circle cx="{CX}" cy="{y0-4}" r="15" fill="{c.hair}"/><circle cx="{CX-4}" cy="{y0-8}" r="6" fill="{c.hair_h}" opacity="0.5"/>')
    if c.hairstyle == 'puffs': o.append(f'<circle cx="{CX-24}" cy="{y0+6}" r="14" fill="{c.hair}"/><circle cx="{CX+24}" cy="{y0+6}" r="14" fill="{c.hair}"/>')
    # neck
    o.append(limb((CX, y0 + 52), (CX, y0 + 72), 8, 9, c.skin, c.skin_d, 0.45))
    o.append(f'<path d="M{CX-8} {y0+58} Q{CX} {y0+66} {CX+8} {y0+58} L{CX+8} {y0+54} L{CX-8} {y0+54}Z" fill="{c.skin_d}" opacity="0.7"/>')
    # ears
    for s in (-1, 1): o.append(f'<ellipse cx="{CX+s*20.5}" cy="{y0+38}" rx="3.6" ry="6.5" fill="{c.skin}"/><path d="M{CX+s*20.5} {y0+34} q{s*2} 4 0 8" stroke="{c.skin_d}" stroke-width="1.2" fill="none"/>')
    # face shape
    prof = [(y0 + 8, 0.1), (y0 + 12, 13), (y0 + 22, 19.5), (y0 + 36, 20.5), (y0 + 48, 16.5), (y0 + 57, 10), (y0 + 62, 4)]
    face = cr_path(sym(CX, prof)); cid = uid()
    o.append(f'<clipPath id="{cid}"><path d="{face}"/></clipPath><path d="{face}" fill="{c.skin}"/>')
    o.append(f'<path d="M{CX+10} {y0+8} C{CX+30} {y0+20} {CX+24} {y0+52} {CX+6} {y0+64} L{CX+30} {y0+64} L{CX+30} {y0+8}Z" fill="{c.skin_d}" opacity="0.45" clip-path="url(#{cid})"/>')
    o.append(f'<ellipse cx="{CX-11}" cy="{y0+45}" rx="5" ry="3" fill="#E07A5F" opacity="0.18"/><ellipse cx="{CX+11}" cy="{y0+45}" rx="5" ry="3" fill="#E07A5F" opacity="0.14"/>')
    # eyes
    for s in (-1, 1):
        ex = CX + s * 8.5; ey = y0 + 36
        if blink: o.append(f'<path d="M{ex-5} {ey} q5 2 10 0" stroke="#2A1810" stroke-width="1.6" fill="none" stroke-linecap="round"/>')
        else:
            o.append(f'<path d="M{ex-5.5} {ey} Q{ex} {ey-4.4} {ex+5.5} {ey} Q{ex} {ey+3.4} {ex-5.5} {ey}Z" fill="#FBF6EE"/>')
            o.append(f'<circle cx="{ex+0.3}" cy="{ey-0.2}" r="2.9" fill="#3B2314"/><circle cx="{ex+0.3}" cy="{ey-0.2}" r="1.4" fill="#120A06"/><circle cx="{ex+1.3}" cy="{ey-1.2}" r="0.8" fill="#fff"/>')
            o.append(f'<path d="M{ex-5.8} {ey} Q{ex} {ey-5} {ex+5.8} {ey-0.4}" stroke="#1A0F08" stroke-width="{1.6 if c.sex == "f" else 1.2}" fill="none" stroke-linecap="round"/>')
            if c.sex == 'f': o.append(f'<path d="M{ex+s*5.6} {ey-0.6} l{s*1.8} -1.4" stroke="#1A0F08" stroke-width="1.2" stroke-linecap="round"/>')
        o.append(f'<path d="M{ex-6} {ey-7} Q{ex} {ey-10.5 if c.sex == "f" else -9.5 + ey - ey} {ex+6} {ey-7.5}" stroke="{c.hair}" stroke-width="{2 if c.sex == "f" else 2.8}" fill="none" stroke-linecap="round"/>'.replace(f'Q{ex} {-9.5}', f'Q{ex} {ey-9.5}'))
    # nose
    o.append(f'<path d="M{CX-1} {y0+38} Q{CX-2} {y0+45} {CX-4.5} {y0+47} Q{CX-3} {y0+50} {CX} {y0+49.5} Q{CX+3} {y0+50} {CX+4.5} {y0+47}" stroke="{c.skin_d}" stroke-width="1.4" fill="none" stroke-linecap="round"/>')
    o.append(f'<ellipse cx="{CX-0.5}" cy="{y0+46.5}" rx="2.4" ry="1.6" fill="{c.skin_h}" opacity="0.6"/>')
    # mouth
    my = y0 + 54.5
    if mouth == 'open':
        o.append(f'<path d="M{CX-6} {my} Q{CX} {my-2} {CX+6} {my} Q{CX} {my+7} {CX-6} {my}Z" fill="#4A1A12"/><path d="M{CX-4.5} {my+0.4} Q{CX} {my-0.8} {CX+4.5} {my+0.4} L{CX+4} {my+1.6} L{CX-4} {my+1.6}Z" fill="#fff"/>')
        o.append(f'<path d="M{CX-6.5} {my} Q{CX-3} {my-3} {CX} {my-1.6} Q{CX+3} {my-3} {CX+6.5} {my}" stroke="{c.lip}" stroke-width="1.8" fill="none"/>')
    elif mouth == 'smile':
        o.append(f'<path d="M{CX-6.5} {my-0.5} Q{CX-3} {my-2.6} {CX} {my-1.4} Q{CX+3} {my-2.6} {CX+6.5} {my-0.5} Q{CX} {my+1.2} {CX-6.5} {my-0.5}Z" fill="{c.lip}"/>')
        o.append(f'<path d="M{CX-6.5} {my-0.5} Q{CX} {my+5} {CX+6.5} {my-0.5} Q{CX} {my+1.4} {CX-6.5} {my-0.5}Z" fill="{c.lip}" opacity="0.85"/><path d="M{CX-6.5} {my-0.4} Q{CX} {my+2.4} {CX+6.5} {my-0.4}" stroke="#3B140C" stroke-width="0.9" fill="none"/>')
    else:
        o.append(f'<path d="M{CX-5.5} {my} Q{CX} {my-2} {CX+5.5} {my}" stroke="{c.lip}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    if c.glasses: o.append(f'<g fill="#fff" fill-opacity="0.18" stroke="{c.glasses}" stroke-width="1.8"><rect x="{CX-16}" y="{y0+31}" width="13" height="10" rx="4"/><rect x="{CX+3}" y="{y0+31}" width="13" height="10" rx="4"/></g><path d="M{CX-3} {y0+35} h6" stroke="{c.glasses}" stroke-width="1.6"/>')
    # hair front
    if c.hairstyle in ('bun', 'puffs'):
        o.append(f'<path d="M{CX-20} {y0+30} C{CX-24} {y0+8} {CX-8} {y0+2} {CX} {y0+3} C{CX+10} {y0+2} {CX+24} {y0+8} {CX+20} {y0+30} C{CX+16} {y0+18} {CX+8} {y0+14} {CX} {y0+15} C{CX-8} {y0+14} {CX-16} {y0+18} {CX-20} {y0+30}Z" fill="{c.hair}"/>')
        o.append(f'<path d="M{CX-14} {y0+12} q10 -6 22 -3" stroke="{c.hair_h}" stroke-width="1.5" fill="none" opacity="0.8"/><path d="M{CX-2} {y0+5} q8 2 14 8" stroke="{c.hair_h}" stroke-width="1.2" fill="none" opacity="0.6"/>')
    elif c.hairstyle == 'short':
        o.append(f'<path d="M{CX-20.5} {y0+30} C{CX-22} {y0+6} {CX-8} {y0+2} {CX} {y0+2} C{CX+10} {y0+2} {CX+22} {y0+6} {CX+20.5} {y0+30} L{CX+19} {y0+24} C{CX+14} {y0+15} {CX+6} {y0+13} {CX} {y0+13.5} C{CX-6} {y0+13} {CX-14} {y0+15} {CX-19} {y0+24}Z" fill="{c.hair}"/>')
        o.append(''.join(f'<circle cx="{CX+dx}" cy="{y0+dy}" r="0.9" fill="{c.hair_h}"/>' for dx, dy in [(-12, 9), (-6, 6), (2, 5), (9, 7), (14, 11), (-15, 15), (-3, 9), (6, 10)]))
    if c.earrings and c.sex == 'f':
        for s in (-1, 1): o.append(f'<circle cx="{CX+s*21}" cy="{y0+50}" r="4" fill="none" stroke="#E8B62C" stroke-width="1.6"/>')
    return ''.join(o)

def torso_front(c, sh_lift=0):
    w = c.waist; b = c.bust if c.sex == 'f' else 0; h = c.hip; bel = c.belly
    if c.sex == 'f':
        prof = [(68 - sh_lift, 9), (74 - sh_lift, 26), (80 - sh_lift, 33), (96, 33 + 3 * b), (110, 32 + 4 * b), (124, 26 * w + 2 * bel), (138, 24 * w + 4 * bel), (156, 30 * h + 3 * bel), (172, 37 * h), (186, 38 * h)]
    else:
        prof = [(68 - sh_lift, 10), (74 - sh_lift, 30), (80 - sh_lift, 36), (100, 34), (120, 30 + 4 * bel), (140, 28 + 6 * bel), (160, 28 + 4 * bel), (176, 29), (186, 29)]
    return prof
def shirt_front(c, prof, hem):
    pts = [p for p in prof if p[0] <= hem] + [(hem, [hw for y, hw in prof if y <= hem][-1] + 1.5)]
    d = cr_path(sym(CX, pts)); cid = uid()
    o = f'<clipPath id="{cid}"><path d="{d}"/></clipPath><path d="{d}" fill="{c.top}"/>'
    o += f'<path d="M{CX+14} 60 C{CX+44} 90 {CX+44} 150 {CX+30} {hem+6} L{CX+60} {hem+6} L{CX+60} 60Z" fill="{c.top_d}" clip-path="url(#{cid})"/>'
    o += f'<path d="M{CX-26} 84 Q{CX-30} 100 {CX-26} 118" stroke="{c.top_h}" stroke-width="5" fill="none" opacity="0.5" clip-path="url(#{cid})" stroke-linecap="round"/>'
    if c.sex == 'f' and c.bust > 0.3:
        o += f'<path d="M{CX-28} 114 Q{CX-15} 124 {CX-2} 116 M{CX+2} 116 Q{CX+15} 124 {CX+28} 114" stroke="{c.top_d}" stroke-width="1.8" fill="none" clip-path="url(#{cid})" stroke-linecap="round"/>'
    # collar
    o += f'<path d="M{CX-9} 66 L{CX} 82 L{CX+9} 66" stroke="{c.top_d}" stroke-width="2" fill="{c.skin}"/><path d="M{CX-9} 66 L{CX-4} 86 L{CX} 82 M{CX+9} 66 L{CX+4} 86 L{CX} 82" stroke="{c.top_d}" stroke-width="1.2" fill="{c.top}"/>'
    return o

def arm_front(c, side, a_up, a_low, hand='rest', sh_lift=0):
    # side: -1 = screen-left, +1 = screen-right; angles measured from down, positive outward
    sx = CX + side * (31 if c.sex == 'f' else 34); sy = 80 - sh_lift
    ang1 = side * a_up; e = fk((sx, sy), 54 * c.height, ang1); ang2 = side * (a_up + a_low); w = fk(e, 48 * c.height, ang2)
    hd = fk(w, 13, ang2)
    o = limb((sx, sy), e, 9.5, 7.2, c.skin, c.skin_d) + limb(e, w, 7, 5.2, c.skin, c.skin_d)
    # sleeve
    if c.sleeve == 'short': o += limb(fk((sx, sy), 3, ang1), fk((sx, sy), 24, ang1), 10, 9, c.top, c.top_d)
    elif c.sleeve == 'long': o += limb((sx, sy), e, 11, 8.8, c.top, c.top_d) + limb(e, fk(e, 42, ang2), 8.6, 7.2, c.top, c.top_d)
    o += hand_svg(c, w, ang2, side, hand)
    return o
def hand_svg(c, w, ang, side, kind):
    hx, hy = fk(w, 9, ang)
    rot = -ang
    if kind == 'open':  # waving palm
        g = (f'<ellipse cx="0" cy="0" rx="7" ry="8.5" fill="{c.skin}"/>' + ''.join(f'<rect x="{x-1.9}" y="-17" width="3.8" height="{h}" rx="1.9" fill="{c.skin}"/>' for x, h in [(-4.8, 12), (-1.6, 14), (1.6, 13.5), (4.8, 11)]) +
             f'<rect x="{-side*7-2}" y="-7" width="4" height="10" rx="2" fill="{c.skin}" transform="rotate({side*35} {-side*7} -2)"/><path d="M-4 3 q4 2 8 0" stroke="{c.skin_d}" stroke-width="1" fill="none"/>')
        rot = 180 - ang
    elif kind == 'point':
        g = f'<ellipse cx="0" cy="0" rx="6.5" ry="7.5" fill="{c.skin}"/><rect x="-1.9" y="2" width="3.8" height="15" rx="1.9" fill="{c.skin}"/><path d="M-5 -2 q5 3 10 0" stroke="{c.skin_d}" stroke-width="1.1" fill="none"/>'
    elif kind == 'thumb':
        g = f'<rect x="-6.5" y="-6" width="13" height="12" rx="5" fill="{c.skin}"/><rect x="-1.8" y="-16" width="4.2" height="12" rx="2.1" fill="{c.skin}"/><path d="M-6 0 h12 M-6 3 h12" stroke="{c.skin_d}" stroke-width="0.9"/>'
        rot = 180 - ang
    elif kind == 'palmup':
        g = f'<ellipse cx="0" cy="0" rx="8" ry="6" fill="{c.skin}"/><path d="M-7 -2 q7 -4 14 0" stroke="{c.skin_d}" stroke-width="1" fill="none"/><rect x="5" y="-5" width="9" height="4" rx="2" fill="{c.skin}"/>'
        rot = 0
    elif kind == 'fist':
        g = f'<rect x="-6.5" y="-6" width="13" height="12" rx="5" fill="{c.skin}"/><path d="M-6 0 h12" stroke="{c.skin_d}" stroke-width="0.9"/>'
    else:  # relaxed
        g = f'<path d="M-6 -6 Q-7 6 -3 10 Q0 12 3 10 Q7 6 6 -6Z" fill="{c.skin}"/><path d="M-2 0 v8 M1.5 0 v8" stroke="{c.skin_d}" stroke-width="0.9"/>'
    return f'<g transform="translate({hx:.1f} {hy:.1f}) rotate({rot:.1f})">{g}</g>'

def legs_front(c, spread=0):
    o = []; hipw = 13 if c.sex == 'm' else 14 * c.hip
    for s in (-1, 1):
        hp = (CX + s * hipw, 182); k = (CX + s * (12 + spread), 266); an = (CX + s * (11 + spread), 342)
        if c.bottom in ('pants',):
            o.append(limb(hp, k, 17 * (c.hip if c.sex == 'f' else 1), 11, c.bot, c.bot_d) + limb(k, an, 11, 8, c.bot, c.bot_d))
        else:
            mid = ((k[0] * 0.6 + an[0] * 0.4), (k[1] * 0.6 + an[1] * 0.4))
            o.append(limb(hp, k, 15.5 * c.hip, 8.8, c.skin, c.skin_d) + limb(k, mid, 8.8, 10.2, c.skin, c.skin_d) + limb(mid, an, 10.2, 5.4, c.skin, c.skin_d))
        o.append(shoe_front(c, an, s))
    return ''.join(o)
def shoe_front(c, an, s):
    x, y = an
    if c.shoe == 'sneaker': return f'<path d="M{x-9} {y-2} Q{x-10} {y+12} {x} {y+13} Q{x+10} {y+12} {x+9} {y-2}Z" fill="{c.shoes}"/><path d="M{x-10} {y+10} Q{x} {y+15} {x+10} {y+10}" stroke="#F4F1EA" stroke-width="3" fill="none"/>'
    return f'<path d="M{x-7} {y-1} Q{x-9} {y+11} {x} {y+12} Q{x+9} {y+11} {x+7} {y-1}Z" fill="{c.shoes}"/><path d="M{x-6} {y+3} Q{x} {y+6} {x+6} {y+3}" stroke="{c.shoes_d}" stroke-width="1.4" fill="none"/>'
def pelvis_front(c):
    hw = 38 * c.hip if c.sex == 'f' else 29
    if c.bottom == 'pants':
        d = f'M{CX-hw} 168 C{CX-hw-3} 184 {CX-hw+2} 196 {CX-hw+8} 204 L{CX-2} 206 L{CX} 196 L{CX+2} 206 L{CX+hw-8} 204 C{CX+hw-2} 196 {CX+hw+3} 184 {CX+hw} 168Z'
        return f'<path d="{d}" fill="{c.bot}"/><path d="M{CX+4} 170 C{CX+hw} 172 {CX+hw+3} 190 {CX+hw-8} 204 L{CX+2} 206Z" fill="{c.bot_d}" opacity="0.8"/><path d="M{CX} 170 V196" stroke="{c.bot_d}" stroke-width="1.4"/>'
    if c.bottom == 'skirt':
        d = f'M{CX-hw+2} 162 C{CX-hw-4} 180 {CX-hw-4} 200 {CX-hw-12} 248 Q{CX} 256 {CX+hw+12} 248 C{CX+hw+4} 200 {CX+hw+4} 180 {CX+hw-2} 162Z'
        return (f'<path d="{d}" fill="{c.bot}"/><path d="M{CX+10} 164 L{CX+hw-2} 162 C{CX+hw+4} 180 {CX+hw+4} 200 {CX+hw+12} 248 Q{CX+30} 254 {CX+22} 253Z" fill="{c.bot_d}"/>'
                f'<path d="M{CX-16} 176 Q{CX-22} 214 {CX-28} 250 M{CX-2} 178 Q{CX-2} 214 {CX-4} 254 M{CX+14} 176 Q{CX+18} 214 {CX+24} 251" stroke="{c.bot_d}" stroke-width="1.5" fill="none" opacity="0.55"/>')
    return ''
def belt(c, y):
    hw = (37 * c.hip if c.sex == 'f' else 29)
    return f'<path d="M{CX-hw} {y} L{CX+hw} {y} L{CX+hw} {y+7} L{CX-hw} {y+7}Z" fill="#2B1F17"/><rect x="{CX-5}" y="{y+0.5}" width="10" height="6" rx="1" fill="#C9A23A"/>'

GEST = {  # (left arm up, left low, left hand, right arm up, right low, right hand, mouth, shoulder lift)
 'idle': (8, 6, 'rest', 8, 6, 'rest', 'smile', 0),
 'talk': (8, 6, 'rest', 22, -70, 'palmup', 'open', 0),
 'wave': (8, 6, 'rest', 150, 25, 'open', 'smile', 0),
 'point': (8, 6, 'rest', 82, 4, 'point', 'closed', 0),
 'hips': (40, -105, 'fist', 40, -105, 'fist', 'smile', 0),
 'think': (8, 6, 'rest', 18, -158, 'fist', 'closed', 0),
 'shrug': (30, -95, 'palmup', 30, -95, 'palmup', 'closed', 5),
 'thumbs': (8, 6, 'rest', 22, -100, 'thumb', 'smile', 0),
}
def front(c, g='idle'):
    la, ll, lh, ra, rl, rh, mouth, lift = GEST[g]
    prof = torso_front(c, lift)
    o = [f'<ellipse cx="{CX}" cy="355" rx="44" ry="6" fill="#000" opacity="0.13"/>']
    o.append(f'<g id="legs" inkscape:label="legs">{legs_front(c)}</g>')
    hips_first = pelvis_front(c)
    o.append(f'<g id="pelvis" inkscape:label="pelvis">{hips_first}</g>')
    o.append(f'<g id="arm_back" inkscape:label="arm_left">{arm_front(c, -1, la, ll, lh, lift)}</g>')
    hem = 172 if c.bottom == 'pants' else 168
    o.append(f'<g id="torso" inkscape:label="torso">{shirt_front(c, prof, hem)}{belt(c, hem - 4) if c.bottom == "pants" else ""}</g>')
    o.append(f'<g id="head" inkscape:label="head">{head_front(c, mouth, hy=-lift * 0.4 + 0)}</g>')
    o.append(f'<g id="arm_front" inkscape:label="arm_right">{arm_front(c, 1, ra, rl, rh, lift)}</g>')
    return ''.join(o)

# ---------------- SIDE VIEW (facing right) ----------------
SX = 100
def head_side(c, hy, mouth=False):
    y = hy; x = SX + 2; o = []
    o.append(limb((x - 2, y + 52), (x - 4, y + 72), 8, 9, c.skin, c.skin_d, 0.45))
    if c.hairstyle == 'bun': o.append(f'<circle cx="{x-12}" cy="{y+2}" r="14" fill="{c.hair}"/>')
    if c.hairstyle == 'puffs': o.append(f'<circle cx="{x-16}" cy="{y+8}" r="15" fill="{c.hair}"/>')
    face = (f'M{x-18} {y+30} C{x-20} {y+10} {x-6} {y+4} {x+4} {y+5} C{x+16} {y+6} {x+20} {y+18} {x+20} {y+28} L{x+21} {y+33} '
            f'C{x+22} {y+36} {x+26} {y+40} {x+27} {y+43} C{x+27} {y+45} {x+24} {y+46} {x+22} {y+46} L{x+22} {y+50} C{x+23} {y+52} {x+22} {y+54} {x+20} {y+55} '
            f'C{x+21} {y+58} {x+19} {y+62} {x+12} {y+63} C{x+4} {y+64} {x-4} {y+58} {x-8} {y+54} C{x-14} {y+50} {x-18} {y+42} {x-18} {y+30}Z')
    cid = uid(); o.append(f'<clipPath id="{cid}"><path d="{face}"/></clipPath><path d="{face}" fill="{c.skin}"/>')
    o.append(f'<path d="M{x-20} {y+20} C{x-10} {y+30} {x-8} {y+50} {x+2} {y+66} L{x-30} {y+66}Z" fill="{c.skin_d}" opacity="0.45" clip-path="url(#{cid})"/>')
    o.append(f'<ellipse cx="{x-3}" cy="{y+38}" rx="4" ry="6.5" fill="{c.skin}"/><path d="M{x-4} {y+34} q3 4 0 8" stroke="{c.skin_d}" stroke-width="1.2" fill="none"/>')
    o.append(f'<path d="M{x+9} {y+35} Q{x+13} {y+32.5} {x+17} {y+35} Q{x+13} {y+37} {x+9} {y+35}Z" fill="#FBF6EE"/><circle cx="{x+14.5}" cy="{y+35}" r="2" fill="#2A170C"/><path d="M{x+8.5} {y+34.5} Q{x+13} {y+31.5} {x+17.5} {y+34.3}" stroke="#1A0F08" stroke-width="1.5" fill="none"/>')
    o.append(f'<path d="M{x+8} {y+28} Q{x+13} {y+26} {x+19} {y+28}" stroke="{c.hair}" stroke-width="{2 if c.sex == "f" else 2.8}" fill="none" stroke-linecap="round"/>')
    o.append(f'<path d="M{x+23} {y+45.5} Q{x+21} {y+44} {x+20} {y+45}" stroke="{c.skin_d}" stroke-width="1.2" fill="none"/>')
    if mouth: o.append(f'<path d="M{x+19} {y+51} q2 3 3 0" fill="#4A1A12"/>')
    o.append(f'<path d="M{x+18} {y+50} Q{x+21} {y+49} {x+22.5} {y+50} M{x+18.5} {y+53.5} Q{x+21} {y+55} {x+21.5} {y+53.5}" stroke="{c.lip}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    if c.glasses: o.append(f'<rect x="{x+8}" y="{y+30}" width="12" height="9" rx="3.5" fill="#fff" fill-opacity="0.2" stroke="{c.glasses}" stroke-width="1.8"/><path d="M{x+8} {y+33} h-12" stroke="{c.glasses}" stroke-width="1.6"/>')
    if c.hairstyle in ('bun', 'puffs'):
        o.append(f'<path d="M{x-19} {y+38} C{x-24} {y+12} {x-8} {y+2} {x+4} {y+3} C{x+14} {y+4} {x+20} {y+12} {x+20} {y+22} C{x+12} {y+14} {x+2} {y+14} {x-6} {y+20} C{x-10} {y+26} {x-10} {y+32} {x-9} {y+40}Z" fill="{c.hair}"/>')
    elif c.hairstyle == 'short':
        o.append(f'<path d="M{x-18.5} {y+34} C{x-21} {y+10} {x-6} {y+3} {x+4} {y+4} C{x+14} {y+5} {x+19} {y+12} {x+19.5} {y+21} C{x+12} {y+14} {x+2} {y+15} {x-4} {y+22} L{x-8} {y+36}Z" fill="{c.hair}"/>')
    if c.earrings and c.sex == 'f': o.append(f'<circle cx="{x-3}" cy="{y+50}" r="4" fill="none" stroke="#E8B62C" stroke-width="1.6"/>')
    return ''.join(o)
def torso_side(c, bob):
    y = bob; b = c.bust if c.sex == 'f' else 0; h = c.hip if c.sex == 'f' else 0; bel = c.belly
    front = [(SX + 4, y + 68), (SX + 14, y + 84), (SX + 16 + 8 * b, y + 106), (SX + 12 + 2 * b, y + 124), (SX + 10 + 6 * bel, y + 142), (SX + 12 + 8 * bel, y + 160), (SX + 13, y + 180)]
    back = [(SX - 6 - 12 * h, y + 198), (SX - 14 - 20 * h, y + 180), (SX - 10 - 8 * h, y + 154), (SX - 14, y + 132), (SX - 18, y + 100), (SX - 14, y + 78), (SX - 6, y + 68)]
    return front + back
def leg_side(c, hip, th, kn, ft, far=False):
    k = fk(hip, 86 * c.height, th); a = fk(k, 80 * c.height, th - kn)
    dk = lambda col: col if not far else _dark(col)
    if c.bottom == 'pants':
        o = limb(hip, k, 16, 11, dk(c.bot), dk(c.bot_d)) + limb(k, a, 11, 8, dk(c.bot), dk(c.bot_d))
    else:
        mid = (k[0] * 0.6 + a[0] * 0.4, k[1] * 0.6 + a[1] * 0.4); mc = (mid[0] - 2.5, mid[1])
        o = limb(hip, k, 14.5, 8.8, dk(c.skin), dk(c.skin_d)) + limb(k, mc, 8.8, 10, dk(c.skin), dk(c.skin_d)) + limb(mc, a, 10, 5.4, dk(c.skin), dk(c.skin_d))
    toe = fk(a, 1, 0)
    fang = 90 + ft  # foot points forward (screen right)
    tip = fk(a, 26, fang - 180 + 180) if False else (a[0] + 24 * cos(radians(-ft)), a[1] + 24 * sin(radians(-ft)) + 6)
    heel = (a[0] - 6, a[1] + 8)
    sc, scd = dk(c.shoes), dk(c.shoes_d)
    o += f'<path d="M{heel[0]:.1f} {heel[1]-12:.1f} L{a[0]+5:.1f} {a[1]-4:.1f} Q{tip[0]:.1f} {tip[1]-8:.1f} {tip[0]:.1f} {tip[1]:.1f} L{heel[0]:.1f} {heel[1]:.1f}Z" fill="{sc}"/>'
    o += f'<path d="M{heel[0]:.1f} {heel[1]:.1f} L{tip[0]:.1f} {tip[1]:.1f}" stroke="{"#F4F1EA" if c.shoe == "sneaker" else scd}" stroke-width="{3 if c.shoe == "sneaker" else 2}" stroke-linecap="round"/>'
    return o, a
def arm_side(c, sh, a1, bend, far=False):
    e = fk(sh, 54 * c.height, a1); w = fk(e, 48 * c.height, a1 + bend)
    dk = lambda col: col if not far else _dark(col)
    o = limb(sh, e, 9.5, 7.2, dk(c.skin), dk(c.skin_d)) + limb(e, w, 7, 5.2, dk(c.skin), dk(c.skin_d))
    if c.sleeve == 'short': o += limb(fk(sh, 3, a1), fk(sh, 24, a1), 10, 9, dk(c.top), dk(c.top_d))
    elif c.sleeve == 'long': o += limb(sh, e, 11, 8.8, dk(c.top), dk(c.top_d)) + limb(e, fk(e, 42, a1 + bend), 8.6, 7.2, dk(c.top), dk(c.top_d))
    hx, hy = fk(w, 8, a1 + bend)
    o += f'<g transform="translate({hx:.1f} {hy:.1f}) rotate({-(a1+bend):.1f})"><path d="M-6 -6 Q-7 6 -3 10 Q0 12 3 10 Q7 6 6 -6Z" fill="{dk(c.skin)}"/></g>'
    return o
def _dark(col):
    col = col.lstrip('#'); r, g, b = [int(col[i:i + 2], 16) for i in (0, 2, 4)]
    return '#%02X%02X%02X' % (int(r * 0.78), int(g * 0.78), int(b * 0.78))
# walk keyframes for the near leg (thigh deg forward, knee bend, foot angle); far leg = +4 frames
WALK = [(24, 4, 12), (14, 22, 0), (-2, 8, 0), (-16, 4, -10), (-24, 10, -30), (-10, 42, -20), (8, 58, 0), (20, 26, 8)]
BOB = [0, 4, -1, -3, 0, 4, -1, -3]
def side(c, f):
    th, kn, ft = WALK[f]; th2, kn2, ft2 = WALK[(f + 4) % 8]; bob = BOB[f]
    hip = (SX, 182 + bob)
    o = [f'<ellipse cx="{SX+4}" cy="355" rx="40" ry="5.5" fill="#000" opacity="0.13"/>']
    far_arm = arm_side(c, (SX - 2, 82 + bob), th * 0.8, -8 - max(0, th) * 0.6, far=True)
    o.append(f'<g id="arm_far" inkscape:label="arm_far">{far_arm}</g>')
    legf, _ = leg_side(c, hip, th2, kn2, ft2, far=True); o.append(f'<g id="leg_far" inkscape:label="leg_far">{legf}</g>')
    legn, _ = leg_side(c, hip, th, kn, ft); o.append(f'<g id="leg_near" inkscape:label="leg_near">{legn}</g>')
    tpts = torso_side(c, bob); hem = 176 + bob
    td = cr_path(tpts); cid = uid()
    body = f'<clipPath id="{cid}"><path d="{td}"/></clipPath>'
    if c.bottom == 'skirt':
        swing = th * 0.25
        body += f'<path d="M{SX-22-16*c.hip} {170+bob} C{SX-32-18*c.hip} {196+bob} {SX-24-14*c.hip+swing} {236+bob} {SX-22+swing} {252+bob} L{SX+30+swing} {252+bob} C{SX+26} {226+bob} {SX+20} {196+bob} {SX+14} {170+bob}Z" fill="{c.bot}"/>'
        body += f'<path d="M{SX-4} {176+bob} L{SX-2+swing} {250+bob}" stroke="{c.bot_d}" stroke-width="1.6"/>'
    body += f'<path d="{td}" fill="{c.top if c.bottom != "pants" else c.top}"/>'
    if c.bottom == 'pants':
        body += f'<path d="M{SX-30} {hem} L{SX+30} {hem} L{SX+30} {210+bob} L{SX-30} {210+bob}Z" fill="{c.bot}" clip-path="url(#{cid})"/><rect x="{SX-30}" y="{hem-6}" width="60" height="7" fill="#2B1F17" clip-path="url(#{cid})"/>'
    body += f'<path d="M{SX-30} {60+bob} C{SX-14} {100+bob} {SX-12} {150+bob} {SX-20} {210+bob} L{SX-40} {210+bob}Z" fill="{c.top_d}" opacity="0.7" clip-path="url(#{cid})"/>'
    if c.sex == 'f' and c.bust > 0.3: body += f'<path d="M{SX+4} {118+bob} Q{SX+14} {124+bob} {SX+20} {116+bob}" stroke="{c.top_d}" stroke-width="1.8" fill="none" clip-path="url(#{cid})"/>'
    o.append(f'<g id="torso" inkscape:label="torso">{body}</g>')
    o.append(f'<g id="head" inkscape:label="head">{head_side(c, bob - 2)}</g>')
    near_arm = arm_side(c, (SX - 2, 82 + bob), -th * 0.8, -10 - max(0, -th) * 0.7)
    o.append(f'<g id="arm_near" inkscape:label="arm_near">{near_arm}</g>')
    return ''.join(o)
