# OgaMart realistic 2D character rig v2 (front + side), svg strings
import sys; sys.path.insert(0, '/home/claude/rig2')
from math import sin, cos, radians, degrees, atan2, acos, hypot
from base import capsule_d, cr_path, sym, fk, _dark, uid
def limb(a, b, r1, r2, col, shade, k=0.5):
    d = capsule_d(a[0], a[1], b[0], b[1], r1, r2); cid = uid()
    dx, dy = b[0] - a[0], b[1] - a[1]; L = hypot(dx, dy) or 1; nx, ny = -dy / L, dx / L
    if nx < 0: nx, ny = -nx, -ny
    off = 1 - k
    sd = capsule_d(a[0] + nx * r1 * (1 + off), a[1] + ny * r1 * (1 + off), b[0] + nx * r2 * (1 + off), b[1] + ny * r2 * (1 + off), r1, r2)
    return f'<clipPath id="{cid}"><path d="{d}"/></clipPath><path d="{d}" fill="{col}"/><path d="{sd}" fill="{shade}" clip-path="url(#{cid})"/>'
def shade_of(c, key): return getattr(c, key + '_d', _dark(getattr(c, key)))
CX = 100; GROUND = 352
class Char:
    def __init__(self, **k):
        d = dict(name='char', sex='f', skin='#9A5E36', skin_d='#7A4526', skin_h='#B57548', lip='#7E3B2E', hair='#1B110B', hair_h='#3A2618',
                 hairstyle='short', headwear=None, head_col='#7B3AA8', eyewear=None, eye_col='#2B2118', facial=None, facial_col='#1B110B',
                 top='#6FA8DC', top_d=None, top_h=None, top_kind='tshirt', sleeve='short', pattern=None,
                 outfit=None, outfit_col='#5B2A86', outfit_d=None, trim='#E8B62C',
                 bottom='pants', bot='#3D5A80', bot_d=None, shoes='#2B2118', shoes_d=None, shoe='flat',
                 bust=0.0, hip=1.0, rear=0.0, belly=0.0, girth=1.0, height=1.0, shoulder=1.0,
                 earrings=None, chain=False, watch=False, tie=None, apron=None, nametag=None, vest=None, jacket=None,
                 handbag=None, backpack=None, stick=False, prop=None, age='adult')
        d.update(k); self.__dict__.update(d)
        for key, src in (('top', 'top'), ('bot', 'bot'), ('shoes', 'shoes'), ('outfit', 'outfit_col')):
            if getattr(self, key + '_d') is None: setattr(self, key + '_d', _dark(getattr(self, src)))
        if self.top_h is None: self.top_h = _light(self.top)
def _light(col, f=0.25):
    col = col.lstrip('#'); r, g, b = [int(col[i:i + 2], 16) for i in (0, 2, 4)]
    return '#%02X%02X%02X' % (int(r + (255 - r) * f), int(g + (255 - g) * f), int(b + (255 - b) * f))
def pattern_def(c, pid):
    if c.pattern == 'ankara':
        return (f'<pattern id="{pid}" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="scale(1.6)"><rect width="16" height="16" fill="{c.outfit_col if c.outfit else c.top}"/>'
                f'<circle cx="8" cy="8" r="4.6" fill="none" stroke="#1E6B45" stroke-width="2.2"/><circle cx="8" cy="8" r="1.6" fill="#C8412E"/><path d="M0 0l3 3M16 0l-3 3M0 16l3-3M16 16l-3-3" stroke="#7B3AA8" stroke-width="1.6"/></pattern>')
    if c.pattern == 'kente':
        return (f'<pattern id="{pid}" width="20" height="20" patternUnits="userSpaceOnUse"><rect width="20" height="20" fill="#E8B62C"/><rect width="20" height="5" fill="#1E6B45"/><rect y="10" width="20" height="3" fill="#C8412E"/><rect x="8" width="4" height="20" fill="#2B2118" opacity="0.7"/></pattern>')
    return ''
def fill_of(c, base, pid): return f'url(#{pid})' if c.pattern and pid else base

# ---------------- expressions ----------------
EXPR = {'smile': ('open', 'smile', 'normal'), 'talk': ('open', 'talk', 'normal'), 'grin': ('open', 'grin', 'normal'), 'laugh': ('happy', 'laugh', 'raised'),
        'angry': ('angry', 'frown', 'angry'), 'surprised': ('wide', 'o', 'raised'), 'sad': ('open', 'frown', 'sad'), 'neutral': ('open', 'line', 'normal'),
        'happy': ('happy', 'grin', 'raised'), 'blink': ('closed', 'smile', 'normal'), 'proud': ('half', 'smile', 'normal'), 'confused': ('open', 'side', 'confused')}

def eyes_front(c, x0, y0, kind, brow):
    o = []
    for s in (-1, 1):
        ex = x0 + s * 8.5; ey = y0 + 36
        if kind in ('happy', 'closed'):
            o.append(f'<path d="M{ex-5} {ey+0.5} Q{ex} {ey-4 if kind == "happy" else ey+2} {ex+5} {ey+0.5}" stroke="#1A0F08" stroke-width="1.8" fill="none" stroke-linecap="round"/>')
        else:
            sc = 1.25 if kind == 'wide' else 1.0
            top_lid = {'angry': 1.2, 'half': 1.6}.get(kind, 0)
            o.append(f'<path d="M{ex-5.5*sc} {ey} Q{ex} {ey-4.4*sc} {ex+5.5*sc} {ey} Q{ex} {ey+3.4*sc} {ex-5.5*sc} {ey}Z" fill="#FBF6EE"/>')
            o.append(f'<circle cx="{ex+0.3}" cy="{ey-0.2}" r="{2.9 if kind != "wide" else 2.6}" fill="#3B2314"/><circle cx="{ex+0.3}" cy="{ey-0.2}" r="1.4" fill="#120A06"/><circle cx="{ex+1.3}" cy="{ey-1.2}" r="0.8" fill="#fff"/>')
            if top_lid: o.append(f'<path d="M{ex-6} {ey-4.6} L{ex+6} {ey-4.6} L{ex+6} {ey-4.6+top_lid*2.2} Q{ex} {ey-3.4+top_lid*2.6} {ex-6} {ey-4.6+top_lid*2.2}Z" fill="{c.skin}"/>')
            o.append(f'<path d="M{ex-5.8*sc} {ey} Q{ex} {ey-5*sc} {ex+5.8*sc} {ey-0.4}" stroke="#1A0F08" stroke-width="{1.6 if c.sex == "f" else 1.2}" fill="none" stroke-linecap="round"/>')
            if c.sex == 'f': o.append(f'<path d="M{ex+s*5.6} {ey-0.6} l{s*1.8} -1.4" stroke="#1A0F08" stroke-width="1.2" stroke-linecap="round"/>')
            if c.age == 'old': o.append(f'<path d="M{ex+s*6} {ey+1} l{s*2.5} 1.5 M{ex+s*6} {ey+3} l{s*2} 2" stroke="{c.skin_d}" stroke-width="0.9"/>')
        # brows
        bc = '#E8E3D8' if c.age == 'old' and c.hair.upper() in ('#DADADA', '#E8E3D8', '#C9C9CE', '#F4F1EA') else c.hair
        lift = {'raised': -2.5, 'angry': 1.5, 'sad': -1, 'confused': -2 if s < 0 else 0.5}.get(brow, 0)
        inner = {'angry': 3, 'sad': -2.5}.get(brow, 0)
        bw = 2.1 if c.sex == 'f' else 2.9
        o.append(f'<path d="M{ex-s*6} {ey-7+lift+(inner if s < 0 else 0)*-0 + (inner if True else 0)*0} Q{ex} {ey-10.5+lift} {ex+s*6} {ey-7.5+lift+inner}" stroke="{bc}" stroke-width="{bw}" fill="none" stroke-linecap="round"/>'.replace(f'M{ex-s*6} {ey-7+lift}', f'M{ex+s*-6} {ey-7+lift}'))
    return ''.join(o)
def mouth_front(c, x0, y0, kind):
    my = y0 + 54.5; L = c.lip; o = ''
    if kind == 'smile':
        o = (f'<path d="M{x0-6.5} {my-0.5} Q{x0-3} {my-2.6} {x0} {my-1.4} Q{x0+3} {my-2.6} {x0+6.5} {my-0.5} Q{x0} {my+1.2} {x0-6.5} {my-0.5}Z" fill="{L}"/>'
             f'<path d="M{x0-6.5} {my-0.5} Q{x0} {my+5} {x0+6.5} {my-0.5} Q{x0} {my+1.4} {x0-6.5} {my-0.5}Z" fill="{L}" opacity="0.85"/><path d="M{x0-6.5} {my-0.4} Q{x0} {my+2.4} {x0+6.5} {my-0.4}" stroke="#3B140C" stroke-width="0.9" fill="none"/>')
    elif kind == 'talk':
        o = (f'<path d="M{x0-6} {my} Q{x0} {my-2} {x0+6} {my} Q{x0} {my+7} {x0-6} {my}Z" fill="#4A1A12"/><path d="M{x0-4.5} {my+0.4} Q{x0} {my-0.8} {x0+4.5} {my+0.4} L{x0+4} {my+1.6} L{x0-4} {my+1.6}Z" fill="#fff"/>'
             f'<path d="M{x0-6.5} {my} Q{x0-3} {my-3} {x0} {my-1.6} Q{x0+3} {my-3} {x0+6.5} {my}" stroke="{L}" stroke-width="1.8" fill="none"/>')
    elif kind in ('grin', 'laugh'):
        h = 6 if kind == 'grin' else 9
        o = (f'<path d="M{x0-8} {my-1.5} Q{x0} {my+0.5} {x0+8} {my-1.5} Q{x0} {my+h+3} {x0-8} {my-1.5}Z" fill="#4A1A12"/>'
             f'<path d="M{x0-7} {my-1} Q{x0} {my+0.8} {x0+7} {my-1} L{x0+6} {my+2} Q{x0} {my+3.4} {x0-6} {my+2}Z" fill="#fff"/>'
             + (f'<ellipse cx="{x0}" cy="{my+h-1}" rx="4" ry="2" fill="#C9534A"/>' if kind == 'laugh' else '') +
             f'<path d="M{x0-8.5} {my-1.8} Q{x0} {my+0.2} {x0+8.5} {my-1.8}" stroke="{L}" stroke-width="2" fill="none" stroke-linecap="round"/>')
    elif kind == 'frown':
        o = f'<path d="M{x0-6} {my+1.5} Q{x0} {my-3} {x0+6} {my+1.5}" stroke="{L}" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    elif kind == 'o':
        o = f'<ellipse cx="{x0}" cy="{my+1}" rx="4" ry="5" fill="#4A1A12" stroke="{L}" stroke-width="2"/>'
    elif kind == 'side':
        o = f'<path d="M{x0-5} {my+1} Q{x0+1} {my} {x0+6} {my-2}" stroke="{L}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    else:
        o = f'<path d="M{x0-5.5} {my} Q{x0} {my-1} {x0+5.5} {my}" stroke="{L}" stroke-width="2.3" fill="none" stroke-linecap="round"/>'
    return o

def hair_back_front(c, x, y):
    h, hh = c.hair, c.hair_h
    return {'bun': f'<circle cx="{x}" cy="{y-4}" r="15" fill="{h}"/><circle cx="{x-4}" cy="{y-8}" r="6" fill="{hh}" opacity="0.5"/>',
            'silver_bun': f'<circle cx="{x}" cy="{y+2}" r="12" fill="{h}"/><circle cx="{x-3}" cy="{y-1}" r="5" fill="#fff" opacity="0.35"/>',
            'puffs': f'<circle cx="{x-25}" cy="{y+6}" r="14" fill="{h}"/><circle cx="{x+25}" cy="{y+6}" r="14" fill="{h}"/><circle cx="{x-28}" cy="{y+2}" r="5" fill="{hh}" opacity="0.5"/>',
            'afro': f'<ellipse cx="{x}" cy="{y+20}" rx="32" ry="30" fill="{h}"/>',
            'bouffant': f'<ellipse cx="{x}" cy="{y+16}" rx="34" ry="28" fill="{h}"/><circle cx="{x-30}" cy="{y+30}" r="10" fill="{h}"/><circle cx="{x+30}" cy="{y+30}" r="10" fill="{h}"/>',
            'updo': f'<path d="M{x-14} {y+10} C{x-20} {y-40} {x+20} {y-40} {x+14} {y+10}Z" fill="{h}"/>' + ''.join(f'<path d="M{x-12+i*1.5} {y-4-i*9} h{24-i*3}" stroke="#E8B62C" stroke-width="2"/>' for i in range(4)),
            'long_braids': f'<path d="M{x-22} {y+20} C{x-28} {y+60} {x-26} {y+90} {x-20} {y+104} L{x+20} {y+104} C{x+26} {y+90} {x+28} {y+60} {x+22} {y+20}Z" fill="{h}"/>' + ''.join(f'<path d="M{x+dx} {y+40} v60" stroke="{hh}" stroke-width="1.4"/>' for dx in (-18, -12, 12, 18)),
            }.get(c.hairstyle, '')
def hair_front_front(c, x, y):
    h, hh = c.hair, c.hair_h
    cap = (f'<path d="M{x-20} {y+30} C{x-24} {y+8} {x-8} {y+2} {x} {y+3} C{x+10} {y+2} {x+24} {y+8} {x+20} {y+30} C{x+16} {y+18} {x+8} {y+14} {x} {y+15} C{x-8} {y+14} {x-16} {y+18} {x-20} {y+30}Z" fill="{h}"/>'
           f'<path d="M{x-14} {y+12} q10 -6 22 -3" stroke="{hh}" stroke-width="1.5" fill="none" opacity="0.8"/>')
    short = (f'<path d="M{x-20.5} {y+30} C{x-22} {y+6} {x-8} {y+2} {x} {y+2} C{x+10} {y+2} {x+22} {y+6} {x+20.5} {y+30} L{x+19} {y+24} C{x+14} {y+15} {x+6} {y+13} {x} {y+13.5} C{x-6} {y+13} {x-14} {y+15} {x-19} {y+24}Z" fill="{h}"/>'
             + ''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="0.9" fill="{hh}"/>' for dx, dy in [(-12, 9), (-6, 6), (2, 5), (9, 7), (14, 11), (-15, 15), (-3, 9), (6, 10)]))
    return {'bun': cap, 'puffs': cap, 'updo': cap, 'long_braids': cap, 'silver_bun': cap.replace(f'stroke="{hh}"', 'stroke="#FFFFFF"'),
            'afro': f'<path d="M{x-22} {y+30} C{x-26} {y+4} {x-10} {y-2} {x} {y-2} C{x+10} {y-2} {x+26} {y+4} {x+22} {y+30} C{x+18} {y+20} {x+8} {y+14} {x} {y+14} C{x-8} {y+14} {x-18} {y+20} {x-22} {y+30}Z" fill="{h}"/>',
            'bouffant': f'<path d="M{x-22} {y+30} C{x-28} {y+0} {x-10} {y-6} {x} {y-6} C{x+10} {y-6} {x+28} {y+0} {x+22} {y+30} C{x+18} {y+16} {x+6} {y+12} {x-6} {y+14} C{x-14} {y+16} {x-20} {y+22} {x-22} {y+30}Z" fill="{h}"/><path d="M{x-16} {y+4} q14 -8 30 2" stroke="{hh}" stroke-width="2" fill="none" opacity="0.7"/>',
            'short': short, 'fade': short,
            'messy': f'<path d="M{x-21} {y+30} L{x-25} {y+12} L{x-15} {y+14} L{x-16} {y+0} L{x-6} {y+8} L{x-2} {y-4} L{x+5} {y+7} L{x+13} {y-1} L{x+14} {y+10} L{x+24} {y+8} L{x+21} {y+30} C{x+16} {y+18} {x+8} {y+14} {x} {y+15} C{x-8} {y+14} {x-16} {y+18} {x-21} {y+30}Z" fill="{h}"/>',
            'bald': f'<path d="M{x-21} {y+34} C{x-22} {y+26} {x-21} {y+22} {x-19} {y+20} L{x-17} {y+30}Z M{x+21} {y+34} C{x+22} {y+26} {x+21} {y+22} {x+19} {y+20} L{x+17} {y+30}Z" fill="{h}"/><ellipse cx="{x-6}" cy="{y+10}" rx="7" ry="3" fill="#fff" opacity="0.18"/>',
            }.get(c.hairstyle, short)
def headwear_front(c, x, y, pid=None):
    hw = c.headwear; col = c.head_col; cd = _dark(col)
    if hw == 'gele':
        f = f'url(#{pid})' if pid else col
        return (f'<path d="M{x-24} {y+22} C{x-34} {y-14} {x-6} {y-30} {x+2} {y-20} C{x+14} {y-34} {x+42} {y-16} {x+26} {y+22} C{x+12} {y+12} {x-10} {y+12} {x-24} {y+22}Z" fill="{f}"/>'
                f'<path d="M{x+20} {y-14} C{x+44} {y-34} {x+56} {y-14} {x+44} {y+2} C{x+38} {y-6} {x+30} {y-10} {x+20} {y-14}Z" fill="{col}"/><path d="M{x-20} {y+6} C{x-6} {y-6} {x+12} {y-6} {x+24} {y+6}" stroke="{cd}" stroke-width="3" fill="none"/><path d="M{x-14} {y-8} C{x-2} {y-16} {x+12} {y-16} {x+20} {y-6}" stroke="{cd}" stroke-width="2" fill="none"/>')
    if hw == 'straw_hat':
        return (f'<ellipse cx="{x}" cy="{y+14}" rx="42" ry="9" fill="#D9B26A"/><path d="M{x-22} {y+14} C{x-22} {y-14} {x+22} {y-14} {x+22} {y+14}Z" fill="#C9A055"/><rect x="{x-22}" y="{y+6}" width="44" height="6" fill="#8C4B32"/>'
                + ''.join(f'<path d="M{x-40+i*8} {y+12} l4 4" stroke="#B8914A" stroke-width="1"/>' for i in range(11)) + f'<ellipse cx="{x}" cy="{y+16}" rx="42" ry="3" fill="#000" opacity="0.1"/>')
    if hw == 'kufi':
        return f'<path d="M{x-21} {y+16} C{x-21} {y-6} {x+21} {y-6} {x+21} {y+16}Z" fill="{col}"/>' + ''.join(f'<circle cx="{x-14+i*7}" cy="{y+8}" r="1.6" fill="#E8B62C"/>' for i in range(5)) + f'<path d="M{x-21} {y+14} H{x+21}" stroke="#E8B62C" stroke-width="1.5"/>'
    if hw == 'cap':
        return f'<path d="M{x-21} {y+20} C{x-22} {y-2} {x+22} {y-2} {x+21} {y+20}Z" fill="{col}"/><path d="M{x-24} {y+20} Q{x} {y+15} {x+24} {y+20} Q{x} {y+27} {x-24} {y+20}Z" fill="{cd}"/><circle cx="{x}" cy="{y+2}" r="2" fill="{cd}"/>'
    if hw == 'helmet':
        return (f'<path d="M{x-24} {y+30} C{x-26} {y-6} {x+26} {y-6} {x+24} {y+30}Z" fill="#E2435E"/><path d="M{x-18} {y+8} C{x-8} {y-2} {x+8} {y-2} {x+18} {y+8}" stroke="#F5C542" stroke-width="5" fill="none"/>'
                f'<path d="M{x-22} {y+18} C{x-10} {y+10} {x+10} {y+10} {x+22} {y+18}" stroke="#3B7DD8" stroke-width="5" fill="none"/><rect x="{x-24}" y="{y+26}" width="48" height="5" rx="2" fill="#2B2118"/>')
    if hw == 'fila':
        return f'<path d="M{x-21} {y+18} C{x-20} {y-6} {x+24} {y-8} {x+24} {y+14} L{x+30} {y+6} C{x+20} {y-2} {x+4} {y-4} {x-21} {y+18}Z" fill="{col}"/><path d="M{x-21} {y+16} H{x+22}" stroke="#E8B62C" stroke-width="2.4"/>'
    if hw == 'headband':
        return f'<path d="M{x-20} {y+14} Q{x} {y+4} {x+20} {y+14}" stroke="{col}" stroke-width="5" fill="none"/>'
    return ''
def eyewear_front(c, x, y):
    e = c.eyewear; col = c.eye_col; ey = y + 36
    if e == 'oversized': return f'<g fill="#fff" fill-opacity="0.22" stroke="{col}" stroke-width="2.6"><circle cx="{x-9}" cy="{ey}" r="8.5"/><circle cx="{x+9}" cy="{ey}" r="8.5"/></g><path d="M{x-1} {ey-1} h2 M{x-17.5} {ey-2} l-4 -1 M{x+17.5} {ey-2} l4 -1" stroke="{col}" stroke-width="2.4"/>'
    if e == 'round': return f'<g fill="#fff" fill-opacity="0.18" stroke="{col}" stroke-width="1.6"><circle cx="{x-8.5}" cy="{ey}" r="6.5"/><circle cx="{x+8.5}" cy="{ey}" r="6.5"/></g><path d="M{x-2} {ey-1} h4" stroke="{col}" stroke-width="1.4"/>'
    if e in ('stylish', 'colorful'):
        w = 2.6 if e == 'colorful' else 1.8
        return f'<g fill="#fff" fill-opacity="0.18" stroke="{col}" stroke-width="{w}"><path d="M{x-16} {ey-5} h13 v6 q0 5 -6 5 q-7 0 -7 -6z"/><path d="M{x+16} {ey-5} h-13 v6 q0 5 6 5 q7 0 7 -6z"/></g><path d="M{x-3} {ey-3} h6" stroke="{col}" stroke-width="1.6"/>'
    if e == 'sunglasses': return f'<path d="M{x-17} {ey-5} h14 v5 q0 6 -7 6 q-7 0 -7 -6z M{x+17} {ey-5} h-14 v5 q0 6 7 6 q7 0 7 -6z" fill="#151515"/><path d="M{x-3} {ey-3} h6" stroke="#151515" stroke-width="2"/><path d="M{x-14} {ey-3} l5 0" stroke="#fff" stroke-width="1.2" opacity="0.6"/>'
    return ''
def facial_front(c, x, y):
    f = c.facial; col = c.facial_col
    if f == 'mustache': return f'<path d="M{x-12} {y+52} C{x-8} {y+45} {x-2} {y+46} {x} {y+49} C{x+2} {y+46} {x+8} {y+45} {x+12} {y+52} C{x+6} {y+51} {x+2} {y+50} {x} {y+51} C{x-2} {y+50} {x-6} {y+51} {x-12} {y+52}Z" fill="{col}"/>'
    if f in ('beard_thick', 'beard_long'):
        L = 90 if f == 'beard_long' else 70
        return (f'<path d="M{x-20} {y+38} C{x-21} {y+54} {x-14} {y+L-6} {x} {y+L} C{x+14} {y+L-6} {x+21} {y+54} {x+20} {y+38} C{x+16} {y+50} {x+10} {y+48} {x+6} {y+50} C{x+2} {y+47} {x-2} {y+47} {x-6} {y+50} C{x-10} {y+48} {x-16} {y+50} {x-20} {y+38}Z" fill="{col}"/>'
                f'<path d="M{x-5} {y+55} Q{x} {y+57} {x+5} {y+55}" stroke="{c.lip}" stroke-width="2" fill="none"/>' + ''.join(f'<path d="M{x+dx} {y+60} q1 8 0 {L-66}" stroke="#fff" stroke-width="0.8" opacity="0.35" fill="none"/>' for dx in (-8, -3, 3, 8)))
    if f == 'stubble': return f'<path d="M{x-18} {y+44} C{x-14} {y+62} {x+14} {y+62} {x+18} {y+44}" stroke="{col}" stroke-width="5" fill="none" opacity="0.25"/>'
    return ''

def head_front(c, expr='smile', dx=0, dy=0, tilt=0, pid=None):
    x, y = CX + dx, dy; ek, mk, bk = EXPR[expr]; o = []
    o.append(hair_back_front(c, x, y))
    o.append(limb((x, y + 52), (CX, 72), 8 * min(1.15, c.girth), 9 * min(1.2, c.girth), c.skin, c.skin_d, 0.45))
    o.append(f'<path d="M{x-8} {y+58} Q{x} {y+66} {x+8} {y+58} L{x+8} {y+54} L{x-8} {y+54}Z" fill="{c.skin_d}" opacity="0.7"/>')
    for s in (-1, 1): o.append(f'<ellipse cx="{x+s*20.5}" cy="{y+38}" rx="3.6" ry="6.5" fill="{c.skin}"/><path d="M{x+s*20.5} {y+34} q{s*2} 4 0 8" stroke="{c.skin_d}" stroke-width="1.2" fill="none"/>')
    jaw = 16.5 + (c.girth - 1) * 10
    prof = [(y + 8, 0.1), (y + 12, 13), (y + 22, 19.5), (y + 36, 20.5 + (c.girth - 1) * 4), (y + 48, jaw), (y + 57, 10 + (c.girth - 1) * 8), (y + 62, 4)]
    face = cr_path(sym(x, prof)); cid = uid()
    o.append(f'<clipPath id="{cid}"><path d="{face}"/></clipPath><path d="{face}" fill="{c.skin}"/>')
    o.append(f'<path d="M{x+10} {y+8} C{x+30} {y+20} {x+24} {y+52} {x+6} {y+64} L{x+34} {y+64} L{x+34} {y+8}Z" fill="{c.skin_d}" opacity="0.45" clip-path="url(#{cid})"/>')
    o.append(f'<ellipse cx="{x-11}" cy="{y+45}" rx="5" ry="3" fill="#E07A5F" opacity="0.18"/><ellipse cx="{x+11}" cy="{y+45}" rx="5" ry="3" fill="#E07A5F" opacity="0.14"/>')
    if c.age == 'old': o.append(f'<path d="M{x-14} {y+48} q2 5 6 7 M{x+14} {y+48} q-2 5 -6 7 M{x-8} {y+20} h16" stroke="{c.skin_d}" stroke-width="1" fill="none" opacity="0.8"/>')
    o.append(eyes_front(c, x, y, ek, bk))
    o.append(f'<path d="M{x-1} {y+38} Q{x-2} {y+45} {x-4.5} {y+47} Q{x-3} {y+50} {x} {y+49.5} Q{x+3} {y+50} {x+4.5} {y+47}" stroke="{c.skin_d}" stroke-width="1.4" fill="none" stroke-linecap="round"/><ellipse cx="{x-0.5}" cy="{y+46.5}" rx="2.4" ry="1.6" fill="{c.skin_h}" opacity="0.6"/>')
    o.append(facial_front(c, x, y) if c.facial in ('beard_thick', 'beard_long', 'stubble') else '')
    o.append(mouth_front(c, x, y, mk))
    if c.facial == 'mustache': o.append(facial_front(c, x, y))
    o.append(eyewear_front(c, x, y))
    if c.headwear not in ('gele', 'helmet', 'straw_hat'): o.append(hair_front_front(c, x, y))
    o.append(headwear_front(c, x, y, pid))
    if c.earrings:
        r = {'small': 2.5, 'hoop': 4, 'big': 6.5}[c.earrings]
        for s in (-1, 1): o.append(f'<circle cx="{x+s*21}" cy="{y+46+r}" r="{r}" fill="none" stroke="#E8B62C" stroke-width="{1.6 if r < 5 else 2.4}"/>')
    g = ''.join(o)
    return f'<g transform="rotate({tilt} {x} {y+60})">{g}</g>' if tilt else g

# ---------------- body (front) ----------------
def torso_prof(c, lift=0):
    g = c.girth; w = 1.0; b = c.bust; h = c.hip; bel = c.belly; sw = c.shoulder
    if c.sex == 'f':
        return [(68 - lift, 9 * g), (74 - lift, 26 * sw * g), (80 - lift, 32 * sw * g), (96, (32 + 3 * b) * g), (110, (31 + 4 * b) * g), (124, (25 + 6 * bel) * g), (138, (24 + 8 * bel) * g), (156, (30 * h + 4 * bel) * g), (172, 37 * h * g), (186, 38 * h * g)]
    return [(68 - lift, 10 * g), (74 - lift, 30 * sw * g), (80 - lift, 36 * sw * g), (100, 34 * g), (120, (30 + 8 * bel) * g), (140, (28 + 12 * bel) * g), (160, (28 + 9 * bel) * g), (176, 29 * g), (186, 29 * g)]
def hw_at(prof, y):
    pts = sorted(prof)
    for (y1, w1), (y2, w2) in zip(pts, pts[1:]):
        if y1 <= y <= y2: return w1 + (w2 - w1) * (y - y1) / ((y2 - y1) or 1)
    return pts[-1][1] if y > pts[-1][0] else pts[0][1]
def shirt(c, prof, hem, pid=None, fill=None, shade=None):
    fill = fill or (f'url(#{pid})' if c.pattern and not c.outfit and pid else c.top); shade = shade or c.top_d
    pts = [p for p in prof if p[0] < hem] + [(hem, hw_at(prof, hem) + 1.5)]
    d = cr_path(sym(CX, pts)); cid = uid()
    o = f'<clipPath id="{cid}"><path d="{d}"/></clipPath><path d="{d}" fill="{fill}"/>'
    o += f'<path d="M{CX+14} 60 C{CX+46} 90 {CX+46} 150 {CX+32} {hem+6} L{CX+70} {hem+6} L{CX+70} 60Z" fill="#000" opacity="0.14" clip-path="url(#{cid})"/>'
    o += f'<path d="M{CX-26} 84 Q{CX-30} 100 {CX-26} 118" stroke="#fff" stroke-width="5" fill="none" opacity="0.18" clip-path="url(#{cid})" stroke-linecap="round"/>'
    if c.sex == 'f' and c.bust > 0.3: o += f'<path d="M{CX-28} 114 Q{CX-15} 125 {CX-2} 116 M{CX+2} 116 Q{CX+15} 125 {CX+28} 114" stroke="#000" stroke-opacity="0.2" stroke-width="1.8" fill="none" clip-path="url(#{cid})" stroke-linecap="round"/>'
    if c.belly > 0.3: o += f'<path d="M{CX-24} 150 Q{CX} 166 {CX+24} 150" stroke="#000" stroke-opacity="0.18" stroke-width="2" fill="none" clip-path="url(#{cid})"/>'
    return o, cid
def collar(c):
    k = c.top_kind
    if k in ('shirt', 'polo', 'oversized', 'blouse'):
        return f'<path d="M{CX-9} 66 L{CX} 82 L{CX+9} 66" stroke="{c.top_d}" stroke-width="2" fill="{c.skin}"/><path d="M{CX-10} 65 L{CX-4} 86 L{CX} 82 M{CX+10} 65 L{CX+4} 86 L{CX} 82" stroke="{c.top_d}" stroke-width="1.3" fill="{c.top}"/>' + (''.join(f'<circle cx="{CX}" cy="{y}" r="1.4" fill="{c.top_d}"/>' for y in (92, 108, 124, 140)) if k == 'shirt' else '')
    if k == 'tshirt': return f'<path d="M{CX-10} 66 Q{CX} 76 {CX+10} 66" stroke="{c.top_d}" stroke-width="2.4" fill="{c.skin}"/>'
    if k == 'suit':
        return (f'<path d="M{CX-10} 66 L{CX} 106 L{CX+10} 66Z" fill="#F4F4F4"/><path d="M{CX-10} 66 L{CX} 106 L{CX-18} 92 L{CX-14} 70Z M{CX+10} 66 L{CX} 106 L{CX+18} 92 L{CX+14} 70Z" fill="{_dark(c.top, 0.85) if False else c.top_d}"/>'
                f'<circle cx="{CX}" cy="{126}" r="2" fill="#C9A23A"/><circle cx="{CX}" cy="{142}" r="2" fill="#C9A23A"/><rect x="{CX+16}" y="90" width="9" height="5" rx="1" fill="#fff"/>')
    if k == 'delivery': return f'<path d="M{CX-10} 66 Q{CX} 76 {CX+10} 66" stroke="{c.top_d}" stroke-width="2.4" fill="{c.skin}"/><path d="M{CX} 70 V160" stroke="{c.top_d}" stroke-width="2"/><rect x="{CX-30}" y="120" width="60" height="5" fill="#F5E9C8" opacity="0.9"/>'
    return ''
def legs_front(c, lift_l=0, lift_r=0, spread=0, bend_l=0, bend_r=0):
    o = []; g = c.girth; hipw = (13 if c.sex == 'm' else 14 * c.hip) * min(g, 1.3)
    for s, lift, bend in ((-1, lift_l, bend_l), (1, lift_r, bend_r)):
        hp = (CX + s * hipw, 182); k = (CX + s * (12 + spread + bend * 0.3) * min(g, 1.25), 266 - lift * 0.6); an = (CX + s * (11 + spread) * min(g, 1.25), 342 - lift)
        if (c.bottom in ('pants',) and c.outfit not in ('dress', 'robe')) or c.outfit == 'agbada':
            o.append(limb(hp, k, 17 * (c.hip if c.sex == 'f' else 1) * g, 11 * g, c.bot, c.bot_d) + limb(k, an, 11 * g, 8 * min(g, 1.2), c.bot, c.bot_d))
        else:
            mid = (k[0] * 0.6 + an[0] * 0.4, k[1] * 0.6 + an[1] * 0.4)
            o.append(limb(hp, k, 15.5 * c.hip * g, 8.8 * g, c.skin, c.skin_d) + limb(k, mid, 8.8 * g, 10.2 * g, c.skin, c.skin_d) + limb(mid, an, 10.2 * g, 5.4 * min(g, 1.2), c.skin, c.skin_d))
        o.append(shoe_front(c, an))
    return ''.join(o)
def shoe_front(c, an):
    x, y = an; sc, sd = c.shoes, c.shoes_d
    if c.shoe == 'sneaker': return f'<path d="M{x-9} {y-2} Q{x-10} {y+12} {x} {y+13} Q{x+10} {y+12} {x+9} {y-2}Z" fill="{sc}"/><path d="M{x-10} {y+10} Q{x} {y+15} {x+10} {y+10}" stroke="#F4F1EA" stroke-width="3" fill="none"/><path d="M{x-4} {y+2} h8 M{x-4} {y+5} h8" stroke="{sd}" stroke-width="1"/>'
    if c.shoe == 'boot': return f'<path d="M{x-10} {y-14} h20 v20 q0 8 -10 8 q-10 0 -10 -8z" fill="{sc}"/><path d="M{x-10} {y+10} h20" stroke="{sd}" stroke-width="3"/><circle cx="{x-4}" cy="{y}" r="2.5" fill="#8B6A4A"/><circle cx="{x+5}" cy="{y-6}" r="2" fill="#8B6A4A"/>'
    if c.shoe == 'heel': return f'<path d="M{x-6} {y-2} Q{x-7} {y+10} {x} {y+11} Q{x+7} {y+10} {x+6} {y-2}Z" fill="{sc}"/><rect x="{x-1.5}" y="{y+8}" width="3" height="6" fill="{sd}"/>'
    if c.shoe == 'dress_shoe': return f'<path d="M{x-8} {y-1} Q{x-10} {y+11} {x} {y+12} Q{x+10} {y+11} {x+8} {y-1}Z" fill="{sc}"/><ellipse cx="{x-3}" cy="{y+5}" rx="2.5" ry="1.4" fill="#fff" opacity="0.7"/>'
    if c.shoe == 'sandal': return f'<ellipse cx="{x}" cy="{y+9}" rx="9" ry="4" fill="{sc}"/><path d="M{x-6} {y+4} q6 -4 12 0" stroke="{sd}" stroke-width="2.4" fill="none"/>'
    return f'<path d="M{x-7} {y-1} Q{x-9} {y+11} {x} {y+12} Q{x+9} {y+11} {x+7} {y-1}Z" fill="{sc}"/><path d="M{x-6} {y+3} Q{x} {y+6} {x+6} {y+3}" stroke="{sd}" stroke-width="1.4" fill="none"/>'
def lower_front(c, pid, sway=0):
    g = c.girth; hw = (38 * c.hip if c.sex == 'f' else 29) * g; out = c.outfit
    if out in ('dress', 'robe'):
        f = f'url(#{pid})' if c.pattern and pid else c.outfit_col; hem = 336 if out == 'robe' else 322
        prof = torso_prof(c); w0 = hw_at(prof, 140) - 1
        hipmax = max(w0 + 4, (hw if c.sex == 'f' else hw) * (1 + 0.12 * c.rear)); hemw = max(w0 + 6, hipmax * (0.86 if c.sex == 'f' else 1.05))
        d = (f'M{CX-w0} 140 C{CX-hipmax-2} 162 {CX-hipmax-2} 196 {CX-hipmax+sway} 214 C{CX-hipmax+2+sway} 250 {CX-hemw+sway} 290 {CX-hemw+sway} {hem} '
             f'Q{CX+sway} {hem+6} {CX+hemw+sway} {hem} C{CX+hemw+sway} 290 {CX+hipmax-2+sway} 250 {CX+hipmax+sway} 214 C{CX+hipmax+2} 196 {CX+hipmax+2} 162 {CX+w0} 140Z')
        cid = uid()
        return (f'<clipPath id="{cid}"><path d="{d}"/></clipPath><path d="{d}" fill="{f}"/><path d="M{CX+14} 140 C{CX+hipmax} 180 {CX+hipmax-10} 260 {CX+hemw-14} {hem+8} L{CX+120} {hem+8} L{CX+120} 140Z" fill="#000" opacity="0.16" clip-path="url(#{cid})"/>'
                f'<path d="M{CX-hipmax+10} 186 Q{CX-hipmax+20} 176 {CX-hipmax+32} 180" stroke="#fff" stroke-opacity="0.25" stroke-width="5" fill="none" stroke-linecap="round" clip-path="url(#{cid})"/>'
                f'<path d="M{CX-hemw-4+sway} {hem-12} Q{CX+sway} {hem-6} {CX+hemw+4+sway} {hem-12}" stroke="{c.trim}" stroke-width="5" fill="none" clip-path="url(#{cid})"/>'
                f'<path d="M{CX-14} 220 Q{CX-16+sway} 270 {CX-18+sway} {hem} M{CX+10} 220 Q{CX+12+sway} 270 {CX+14+sway} {hem}" stroke="#000" stroke-opacity="0.12" stroke-width="2" fill="none" clip-path="url(#{cid})"/>')
    if c.bottom == 'pants':
        hw = ((13 if c.sex == 'm' else 14 * c.hip) + 17 * (c.hip if c.sex == 'f' else 1)) * min(g, 1.3) - 3
        d = f'M{CX-hw} 168 C{CX-hw-3} 184 {CX-hw+2} 196 {CX-hw+8} 204 L{CX-2} 206 L{CX} 196 L{CX+2} 206 L{CX+hw-8} 204 C{CX+hw-2} 196 {CX+hw+3} 184 {CX+hw} 168Z'
        return f'<path d="{d}" fill="{c.bot}"/><path d="M{CX+4} 170 C{CX+hw} 172 {CX+hw+3} 190 {CX+hw-8} 204 L{CX+2} 206Z" fill="{c.bot_d}" opacity="0.8"/><path d="M{CX} 170 V196" stroke="{c.bot_d}" stroke-width="1.4"/>'
    if c.bottom in ('skirt', 'long_skirt'):
        hem = 248 if c.bottom == 'skirt' else 300
        d = f'M{CX-hw+2} 162 C{CX-hw-4} 180 {CX-hw-4+sway} 200 {CX-hw-12+sway} {hem} Q{CX+sway} {hem+8} {CX+hw+12+sway} {hem} C{CX+hw+4+sway} 200 {CX+hw+4} 180 {CX+hw-2} 162Z'
        return (f'<path d="{d}" fill="{c.bot}"/><path d="M{CX+10} 164 L{CX+hw-2} 162 C{CX+hw+4} 180 {CX+hw+4+sway} 200 {CX+hw+12+sway} {hem} Q{CX+30+sway} {hem+6} {CX+22+sway} {hem+5}Z" fill="{c.bot_d}"/>'
                f'<path d="M{CX-16} 176 Q{CX-22+sway} 214 {CX-28+sway} {hem} M{CX-2} 178 Q{CX-2+sway} 214 {CX-4+sway} {hem+6}" stroke="{c.bot_d}" stroke-width="1.5" fill="none" opacity="0.5"/>')
    return ''

# ---------------- arms + hands ----------------
ARM1, ARM2 = 54, 48
def shoulder_pt(c, side, lift=0): return (CX + side * (31 if c.sex == 'f' else 34) * c.shoulder * c.girth ** 0.7, 80 - lift)
def ik(c, side, target, lift=0):
    S = shoulder_pt(c, side, lift); L1, L2 = ARM1 * c.height, ARM2 * c.height
    dx, dy = target[0] - S[0], target[1] - S[1]; d = max(8, min(hypot(dx, dy), L1 + L2 - 0.5))
    base = degrees(atan2(dx, dy)); A = degrees(acos(max(-1, min(1, (L1 * L1 + d * d - L2 * L2) / (2 * L1 * d)))))
    best = None
    for sgn in (1, -1):
        a1 = base + sgn * A; E = fk(S, L1, a1)
        score = (E[0] - S[0]) * side
        if best is None or score > best[0]: best = (score, a1, E)
    _, a1, E = best
    a2 = degrees(atan2(target[0] - E[0], target[1] - E[1]))
    return a1, a2
def hand(c, w, ang, side, kind, col=None):
    col = col or c.skin; cd = c.skin_d
    hx, hy = fk(w, 8, ang); rot = -ang
    if kind == 'open':
        g = (f'<ellipse cx="0" cy="0" rx="7" ry="8.5" fill="{col}"/>' + ''.join(f'<rect x="{x-1.9}" y="-18" width="3.8" height="{h}" rx="1.9" fill="{col}"/>' for x, h in [(-4.8, 12), (-1.6, 14), (1.6, 13.5), (4.8, 11)]) +
             f'<rect x="{-side*8-2}" y="-6" width="4" height="10" rx="2" fill="{col}" transform="rotate({side*40} {-side*7} -2)"/><path d="M-4 3 q4 2 8 0" stroke="{cd}" stroke-width="1" fill="none"/>')
        rot = 180 - ang if abs(ang) > 90 else -ang + 180
    elif kind == 'point': g = f'<ellipse cx="0" cy="0" rx="6.5" ry="7.5" fill="{col}"/><rect x="-1.9" y="2" width="3.8" height="15" rx="1.9" fill="{col}"/><path d="M-5 -2 q5 3 10 0" stroke="{cd}" stroke-width="1.1" fill="none"/>'
    elif kind == 'thumb': g = f'<rect x="-6.5" y="-6" width="13" height="12" rx="5" fill="{col}"/><rect x="-1.8" y="-16" width="4.2" height="12" rx="2.1" fill="{col}"/><path d="M-6 0 h12 M-6 3 h12" stroke="{cd}" stroke-width="0.9"/>'; rot = 180 - ang
    elif kind == 'palmup': g = f'<ellipse cx="0" cy="0" rx="8" ry="6" fill="{col}"/><path d="M-7 -2 q7 -4 14 0" stroke="{cd}" stroke-width="1" fill="none"/><rect x="{4*side}" y="-5" width="9" height="4" rx="2" fill="{col}"/>'; rot = 0
    elif kind in ('fist', 'grip'): g = f'<rect x="-6.5" y="-6" width="13" height="12" rx="5" fill="{col}"/><path d="M-6 0 h12" stroke="{cd}" stroke-width="0.9"/>'
    else: g = f'<path d="M-6 -6 Q-7 6 -3 10 Q0 12 3 10 Q7 6 6 -6Z" fill="{col}"/><path d="M-2 0 v8 M1.5 0 v8" stroke="{cd}" stroke-width="0.9"/>'
    return f'<g transform="translate({hx:.1f} {hy:.1f}) rotate({rot:.1f})">{g}</g>', (hx, hy)
def sleeve_cols(c):
    if c.outfit in ('agbada', 'dress', 'robe'): return c.outfit_col, c.outfit_d
    if c.jacket: return c.jacket, _dark(c.jacket)
    return c.top, c.top_d
def arm(c, side, a1, a2, hk='rest', lift=0, pid=None):
    S = shoulder_pt(c, side, lift); E = fk(S, ARM1 * c.height, a1); W = fk(E, ARM2 * c.height, a2); g = min(c.girth, 1.4)
    o = limb(S, E, 9.5 * g, 7.2 * g, c.skin, c.skin_d) + limb(E, W, 7 * g, 5.2 * g, c.skin, c.skin_d)
    sc, sd = sleeve_cols(c); sf = f'url(#{pid})' if c.pattern and pid and (c.outfit or True) else sc
    sl = 'wide' if c.outfit in ('agbada', 'robe') else c.sleeve
    if sl == 'short': o += limb(fk(S, 3, a1), fk(S, 24, a1), 10.5 * g, 9.5 * g, sf, sd)
    elif sl == 'long': o += limb(S, E, 11 * g, 9 * g, sf, sd) + limb(E, fk(E, 42, a2), 9 * g, 7.4 * g, sf, sd)
    elif sl == 'wide': o += limb(S, E, 12 * g, 13 * g, sf, sd) + limb(E, fk(E, 30, a2), 13 * g, 16 * g, sf, sd)
    elif sl == 'puff': o += limb(fk(S, 2, a1), fk(S, 20, a1), 13 * g, 11 * g, sf, sd)
    h, hp = hand(c, W, a2, side, hk)
    if c.watch and side == 1: o += limb(fk(E, 40, a2), fk(E, 45, a2), 6.5, 6, '#E8B62C', '#B98A12')
    return o + h, hp, a2
# ---------------- props ----------------
def handbag(c, hp, mode='hang', ang=0):
    col = c.handbag or '#D63A2A'; cd = _dark(col); x, y = hp
    if mode == 'wave':
        return f'<g transform="rotate({ang} {x} {y})"><path d="M{x-10} {y} C{x-10} {y-14} {x+10} {y-14} {x+10} {y}" stroke="#2B2118" stroke-width="3" fill="none"/><rect x="{x-17}" y="{y}" width="34" height="28" rx="6" fill="{col}"/><rect x="{x-17}" y="{y}" width="34" height="8" rx="4" fill="{cd}"/><rect x="{x-5}" y="{y+5}" width="10" height="6" rx="2" fill="#E8B62C"/></g>'
    return f'<path d="M{x-8} {y+2} C{x-10} {y+18} {x+14} {y+18} {x+12} {y+2}" stroke="#2B2118" stroke-width="3" fill="none"/><rect x="{x-14}" y="{y+14}" width="32" height="26" rx="6" fill="{col}"/><rect x="{x-14}" y="{y+14}" width="32" height="8" rx="4" fill="{cd}"/><rect x="{x-2}" y="{y+19}" width="10" height="6" rx="2" fill="#E8B62C"/>'
def prop_svg(name, x, y):
    if name == 'basket':
        return f'<path d="M{x-22} {y} h44 l-5 24 h-34z" fill="#A47648"/><path d="M{x-21} {y+8} h42 M{x-20} {y+16} h40" stroke="#7F5833" stroke-width="1.4"/>' + ''.join(f'<circle cx="{x-14+i*9}" cy="{y-3}" r="6" fill="{c}"/>' for i, c in enumerate(['#D63A2A', '#E2452F', '#D63A2A', '#7BB343'])) + f'<path d="M{x-4} {y-9} v-3" stroke="#3E7D4A" stroke-width="2"/>'
    if name == 'tablet': return f'<rect x="{x-11}" y="{y-15}" width="22" height="30" rx="3" fill="#2B2118"/><rect x="{x-9}" y="{y-12}" width="18" height="24" rx="1.5" fill="#5FBF8E"/><rect x="{x-6}" y="{y-8}" width="12" height="3" rx="1" fill="#fff" opacity="0.8"/>'
    if name == 'snackbox': return f'<rect x="{x-16}" y="{y-10}" width="32" height="24" rx="3" fill="#F28C28"/><rect x="{x-16}" y="{y-10}" width="32" height="7" fill="#D9731A"/><text x="{x}" y="{y+8}" font-family="Poppins, sans-serif" font-size="6" font-weight="700" fill="#fff" text-anchor="middle">SOFIA\'S</text>'
    if name == 'pot': return f'<ellipse cx="{x}" cy="{y-6}" rx="16" ry="4" fill="#3A3F44"/><path d="M{x-16} {y-6} h32 v16 a6 6 0 0 1 -6 6 h-20 a6 6 0 0 1 -6 -6z" fill="#4A5056"/><path d="M{x-5} {y-12} q-3 -6 0 -10 M{x+4} {y-12} q3 -6 0 -10" stroke="#C9C1B4" stroke-width="1.6" fill="none"/><path d="M{x-20} {y} l-6 -2 q-3 4 2 6z" fill="#D63A2A"/>'
    if name == 'clutch': return f'<rect x="{x-12}" y="{y-6}" width="24" height="14" rx="4" fill="#E2435E"/><path d="M{x-8} {y-6} q8 -7 16 0" stroke="#B8324A" stroke-width="2" fill="none"/>'
    if name == 'clipboard': return f'<rect x="{x-11}" y="{y-14}" width="22" height="28" rx="2" fill="#8B6A4A"/><rect x="{x-8}" y="{y-10}" width="16" height="22" fill="#fff"/><path d="M{x-5} {y-5} h10 M{x-5} {y} h10 M{x-5} {y+5} h7" stroke="#8E8476" stroke-width="1.4"/><rect x="{x-4}" y="{y-16}" width="8" height="4" rx="1" fill="#C9C1B4"/>'
    if name == 'box': return f'<rect x="{x-16}" y="{y-12}" width="32" height="24" fill="#C9A06A"/><path d="M{x-16} {y-4} h32 M{x} {y-12} v8" stroke="#A47648" stroke-width="2"/>'
    if name == 'phone': return f'<rect x="{x-5}" y="{y-9}" width="10" height="18" rx="2" fill="#2B2118"/><rect x="{x-4}" y="{y-7}" width="8" height="13" fill="#6FA8DC"/>'
    if name == 'shopping_bag': return f'<path d="M{x-12} {y} h24 l-2 26 h-20z" fill="#F4E9D8"/><path d="M{x-6} {y} q6 -10 12 0" stroke="#8B6A4A" stroke-width="2" fill="none"/><rect x="{x-10}" y="{y+8}" width="20" height="6" fill="#24503B"/>'
    if name == 'camera': return f'<rect x="{x-12}" y="{y-8}" width="24" height="16" rx="3" fill="#2B2118"/><circle cx="{x}" cy="{y}" r="5" fill="#6FA8DC" stroke="#888" stroke-width="2"/>'
    if name == 'child_hand': return ''
    return ''
def backpack_front(c):
    col = c.backpack; cd = _dark(col)
    return f'<rect x="{CX-40}" y="64" width="80" height="96" rx="10" fill="{col}"/><rect x="{CX-40}" y="64" width="80" height="18" rx="9" fill="{cd}"/>'
def stick_svg(top, bottom): return f'<path d="M{top[0]:.1f} {top[1]:.1f} L{bottom[0]:.1f} {bottom[1]:.1f}" stroke="#6B4A32" stroke-width="4" stroke-linecap="round"/><path d="M{top[0]:.1f} {top[1]:.1f} q0 -10 -9 -10" stroke="#6B4A32" stroke-width="4" fill="none" stroke-linecap="round"/>'

# ---------------- poses ----------------
# pose: dict(la=(a1,a2) absolute OR ('ik', (x,y))), ra=..., lh, rh, expr, tilt, jump, lift_l, lift_r, sway, head_tilt, shoulder_lift, extra
def P(**k): return k
def rel(side, up, low): return (side * up, side * (up + low))
HEAD = lambda dx, dy: (CX + dx, dy)
def resolve(c, side, spec, lift):
    if spec[0] == 'ik': return ik(c, side, spec[1], lift)
    return spec
STD = {
 'idle_1': P(la=rel(-1, 8, 6), ra=rel(1, 8, 6), expr='smile'),
 'idle_2': P(la=rel(-1, 9, 8), ra=rel(1, 9, 8), expr='blink', breathe=True),
 'talk_1': P(la=rel(-1, 8, 6), ra=rel(1, 24, -72), rh='palmup', expr='talk'),
 'talk_2': P(la=rel(-1, 8, 6), ra=rel(1, 30, -60), rh='palmup', expr='smile'),
 'happy_1': P(la=rel(-1, 30, -95), lh='fist', ra=rel(1, 30, -95), rh='fist', expr='happy'),
 'happy_2': P(la=rel(-1, 140, 20), lh='open', ra=rel(1, 140, 20), rh='open', expr='laugh', jump=8),
 'angry_1': P(la=rel(-1, 40, -105), lh='fist', ra=rel(1, 40, -105), rh='fist', expr='angry'),
 'angry_2': P(la=rel(-1, 40, -105), lh='fist', ra=rel(1, 70, -20), rh='point', expr='angry', head_tilt=-4),
 'surprised_1': P(la=('ik', HEAD(-14, 48)), lh='open', ra=('ik', HEAD(14, 48)), rh='open', expr='surprised', jump=4),
 'sad_1': P(la=rel(-1, 4, 2), ra=rel(1, 4, 2), expr='sad', head_tilt=6, slump=True),
 'wave_1': P(la=rel(-1, 8, 6), ra=rel(1, 150, 25), rh='open', expr='smile'),
 'wave_2': P(la=rel(-1, 8, 6), ra=rel(1, 138, 48), rh='open', expr='grin'),
 'point_1': P(la=rel(-1, 8, 6), ra=rel(1, 82, 4), rh='point', expr='neutral'),
 'think_1': P(la=rel(-1, 30, -100), lh='fist', ra=('ik', HEAD(4, 62)), rh='fist', expr='confused'),
 'shrug_1': P(la=rel(-1, 30, -95), lh='palmup', ra=rel(1, 30, -95), rh='palmup', expr='neutral', shoulder_lift=5),
 'thumbs_1': P(la=rel(-1, 8, 6), ra=rel(1, 22, -100), rh='thumb', expr='grin'),
 'celebrate_1': P(la=rel(-1, 150, 15), lh='fist', ra=rel(1, 150, 15), rh='fist', expr='laugh', jump=14),
 'celebrate_2': P(la=rel(-1, 120, 40), lh='fist', ra=rel(1, 120, 40), rh='fist', expr='happy', jump=4),
 'celebrate_3': P(la=rel(-1, 150, 15), lh='fist', ra=rel(1, 150, 15), rh='fist', expr='laugh', jump=14),
 'celebrate_4': P(la=rel(-1, 60, -40), lh='fist', ra=rel(1, 60, -40), rh='fist', expr='grin'),
}
def front(c, pose):
    pid = uid('pat') if c.pattern else None
    la = resolve(c, -1, pose.get('la', rel(-1, 8, 6)), pose.get('shoulder_lift', 0)); ra = resolve(c, 1, pose.get('ra', rel(1, 8, 6)), pose.get('shoulder_lift', 0))
    lift = pose.get('shoulder_lift', 0); sway = pose.get('sway', 0)
    prof = torso_prof(c, lift)
    o = [f'<defs>{pattern_def(c, pid)}</defs>' if pid else '']
    if c.backpack: o.append(backpack_front(c))
    o.append(f'<g id="legs" inkscape:label="legs">{legs_front(c, pose.get("lift_l", 0), pose.get("lift_r", 0), pose.get("spread", 0))}</g>')
    o.append(f'<g id="lower" inkscape:label="lower_body">{lower_front(c, pid, sway)}</g>')
    larm, lhp, la2 = arm(c, -1, la[0], la[1], pose.get('lh', 'rest'), lift, pid)
    hem = 172 if c.bottom == 'pants' and not c.outfit else (160 if c.outfit in ('dress', 'robe') else 168)
    if c.outfit == 'agbada':
        g = c.girth; wide = 70 * g
        o.append(f'<g id="agbada" inkscape:label="agbada"><path d="M{CX-30*g} 70 C{CX-wide} 110 {CX-wide-6} 220 {CX-wide+4} 290 L{CX+wide-4} 290 C{CX+wide+6} 220 {CX+wide} 110 {CX+30*g} 70Z" fill="{c.outfit_col}"/>'
                 f'<path d="M{CX+10} 70 C{CX+wide} 110 {CX+wide+6} 220 {CX+wide-4} 290 L{CX+30} 290 C{CX+30} 220 {CX+24} 120 {CX+10} 70Z" fill="#000" opacity="0.15"/>'
                 + ''.join(f'<circle cx="{CX+dx}" cy="{dy}" r="2" fill="{c.trim}"/>' for dx, dy in [(-40, 160), (36, 180), (-50, 240), (52, 250), (-10, 220), (20, 270)]) + '</g>')
    o.append(f'<g id="arm_back" inkscape:label="arm_left">{larm}</g>')
    tfill = None
    if c.outfit in ('dress', 'robe'): tfill = f'url(#{pid})' if c.pattern and pid else c.outfit_col
    sh, scid = shirt(c, prof, hem, pid, tfill, c.outfit_d if c.outfit else None)
    extra = collar(c) if not c.outfit else (f'<path d="M{CX-10} 66 Q{CX} 80 {CX+10} 66" stroke="{c.trim}" stroke-width="3" fill="none"/>' if c.outfit != 'agbada' else '')
    if c.outfit == 'agbada': extra += f'<path d="M{CX-12} 66 Q{CX} 120 {CX+12} 66" stroke="{c.trim}" stroke-width="4" fill="none"/><path d="M{CX-8} 90 Q{CX} 130 {CX+8} 90" stroke="{c.trim}" stroke-width="2.4" fill="none"/>'
    if c.top_kind == 'overalls' or c.vest == 'overalls':
        extra += f'<path d="M{CX-16} 112 H{CX+16} V172 H{CX-16}Z" fill="{c.bot}"/><path d="M{CX-22} 74 L{CX-14} 114 M{CX+22} 74 L{CX+14} 114" stroke="{c.bot}" stroke-width="6"/><rect x="{CX-8}" y="120" width="16" height="10" rx="1" fill="{c.bot_d}"/><circle cx="{CX-14}" cy="114" r="2.4" fill="#C9A23A"/><circle cx="{CX+14}" cy="114" r="2.4" fill="#C9A23A"/>'
    if c.vest and c.vest != 'overalls':
        extra += f'<path d="M{CX-30} 82 C{CX-34} 120 {CX-30} 150 {CX-26} 170 L{CX-6} 170 L{CX-4} 90 Z M{CX+30} 82 C{CX+34} 120 {CX+30} 150 {CX+26} 170 L{CX+6} 170 L{CX+4} 90Z" fill="{c.vest}"/>'
    if c.apron: extra += f'<path d="M{CX-24} 104 H{CX+24} L{CX+28} 214 H{CX-28}Z" fill="{c.apron}"/><path d="M{CX-18} 104 L{CX-14} 70 M{CX+18} 104 L{CX+14} 70" stroke="{c.apron}" stroke-width="4"/><rect x="{CX-12}" y="150" width="24" height="16" rx="2" fill="{_dark(c.apron)}"/>'
    if c.tie: extra += f'<path d="M{CX-3} 72 h6 l3 34 l-6 8 l-6 -8z" fill="{c.tie}"/>'
    if c.nametag: extra += f'<rect x="{CX+12}" y="96" width="18" height="10" rx="1.5" fill="#fff"/><path d="M{CX+15} 101 h12" stroke="{c.nametag}" stroke-width="1.6"/>'
    if c.chain: extra += f'<path d="M{CX-16} 70 Q{CX} 104 {CX+16} 70" stroke="#E8B62C" stroke-width="2.4" fill="none"/><path d="M{CX-12} 72 Q{CX} 96 {CX+12} 72" stroke="#E8B62C" stroke-width="1.6" fill="none"/><circle cx="{CX}" cy="102" r="4" fill="#E8B62C"/>'
    belt = f'<path d="M{CX-hw_at(prof,168)} 168 h{2*hw_at(prof,168)} v7 h-{2*hw_at(prof,168)}z" fill="#2B1F17"/><rect x="{CX-5}" y="168.5" width="10" height="6" rx="1" fill="#C9A23A"/>' if c.bottom == 'pants' and not c.outfit and c.top_kind not in ('oversized', 'overalls') else ''
    o.append(f'<g id="torso" inkscape:label="torso">{sh}{extra}{belt}</g>')
    hs = f' transform="translate({CX} 66) scale(1.4) translate({-CX} -66)"' if c.age == 'child' else ''
    o.append(f'<g id="head" inkscape:label="head"{hs}>{head_front(c, pose.get("expr", "smile"), 0, -lift * 0.4, pose.get("head_tilt", 0), pid)}</g>')
    rarm, rhp, ra2 = arm(c, 1, ra[0], ra[1], pose.get('rh', 'rest'), lift, pid)
    o.append(f'<g id="arm_front" inkscape:label="arm_right">{rarm}</g>')
    # held items
    items = ''
    if c.handbag and pose.get('bag', 'hang') != 'none':
        if pose.get('bag') == 'wave': items += handbag(c, rhp, 'wave', pose.get('bag_ang', 0))
        else: items += handbag(c, lhp)
    if c.stick: items += stick_svg((rhp[0], rhp[1] - 4), (rhp[0] + 6, GROUND))
    pr = pose.get('prop', c.prop)
    if pr: items += prop_svg(pr, *(pose.get('prop_at') or (lhp[0], lhp[1] + 6)))
    if pose.get('confetti'): items += confetti()
    o.append(f'<g id="props" inkscape:label="props">{items}</g>')
    body = ''.join(o)
    # whole-body transforms
    tf = []
    j = pose.get('jump', 0)
    if j: tf.append(f'translate(0 {-j})')
    if pose.get('tilt'): tf.append(f'rotate({pose["tilt"]} {CX} {GROUND})')
    if pose.get('breathe'): tf.append(f'translate(0 {GROUND}) scale(1 0.988) translate(0 {-GROUND})')
    if pose.get('slump'): tf.append(f'translate(0 {GROUND}) scale(1 0.98) translate(0 {-GROUND})')
    if c.height != 1: tf.insert(0, f'translate({CX} {GROUND}) scale({c.height}) translate({-CX} {-GROUND})')
    shadow = f'<ellipse cx="{CX}" cy="{GROUND+3}" rx="{44*c.girth*c.height}" ry="6" fill="#000" opacity="0.13"/>'
    return shadow + (f'<g transform="{" ".join(tf)}">{body}</g>' if tf else body)
def confetti():
    import random; r = random.Random(7); cols = ['#E8B62C', '#E2435E', '#4CC38A', '#3D6FA8', '#F28C28']
    return ''.join(f'<rect x="{r.uniform(20,180):.0f}" y="{r.uniform(-40,60):.0f}" width="7" height="4" rx="1" fill="{r.choice(cols)}" transform="rotate({r.uniform(0,180):.0f} 100 40)"/>' for _ in range(26))
