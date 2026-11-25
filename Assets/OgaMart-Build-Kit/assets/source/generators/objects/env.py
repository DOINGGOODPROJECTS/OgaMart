from common import *
import math, random
def tree(kind='mango', seed=1):
    r = random.Random(seed); o = shadow(100, 300, 70, 10)
    if kind == 'palm':
        o += '<path d="M100 300 C104 220 92 150 112 70" stroke="#8B6A4A" stroke-width="16" fill="none"/>' + ''.join(f'<path d="M{100+i*0.9} {300-i*23} q6 -4 12 0" stroke="#6E5236" stroke-width="2" fill="none"/>' for i in range(10))
        for a in range(-80, 260, 40):
            ex = 112 + 90 * math.cos(math.radians(a)); ey = 70 + 50 * math.sin(math.radians(a)) + 20
            o += f'<path d="M112 70 Q{(112+ex)/2} {min(ey,70)-30} {ex} {ey}" stroke="#3E7D4A" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M112 70 Q{(112+ex)/2} {min(ey,70)-30} {ex} {ey}" stroke="#5DAE5C" stroke-width="4" fill="none"/>'
        o += '<circle cx="106" cy="80" r="8" fill="#6E5236"/><circle cx="118" cy="82" r="8" fill="#6E5236"/>'
        return o, '0 0 220 320'
    if kind == 'coconut': return tree('palm', seed)
    o += '<path d="M90 300 C92 250 88 220 94 180 L106 180 C112 220 108 250 112 300Z" fill="#6E4A32"/><path d="M98 200 L70 160 M102 210 L136 168" stroke="#6E4A32" stroke-width="10" stroke-linecap="round"/>'
    cols = {'mango': ('#2F6B3A', '#3E7D4A', '#4E9A4F'), 'round': ('#4A8A3C', '#5DAE5C', '#7BC46A'), 'flame': ('#2F6B3A', '#3E7D4A', '#4E9A4F'), 'bush': ('#3E7D4A', '#4E9A4F', '#5DAE5C')}[kind]
    if kind == 'bush':
        return shadow(60, 96, 56, 6) + ''.join(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{c}"/>' for x, y, rr, c in [(30, 70, 28, cols[0]), (90, 70, 28, cols[0]), (60, 56, 34, cols[1]), (40, 50, 18, cols[2]), (80, 52, 16, cols[2])]), '0 0 120 100'
    blobs = [(100, 120, 80), (50, 150, 50), (150, 150, 52), (70, 90, 48), (130, 86, 50), (100, 60, 46)]
    for i, c in enumerate(cols):
        for (x, y, rr) in blobs: o += f'<circle cx="{x + (i-1)*-6}" cy="{y + (i-1)*-8}" r="{rr*(1-i*0.22)}" fill="{c}"/>'
    if kind == 'mango': o += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="6" ry="8" fill="#F2B233"/><ellipse cx="{x-2}" cy="{y-3}" rx="2" ry="3" fill="#FCE08A"/>' for x, y in [(70, 150), (128, 140), (100, 170), (150, 110), (60, 110)])
    if kind == 'flame': o += ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#E2452F"/>' for x, y in [(60, 80), (100, 50), (140, 90), (80, 130), (130, 140), (100, 110)])
    return o, '0 0 220 320'
def flowerbed():
    o = '<rect x="0" y="60" width="120" height="30" rx="6" fill="#8B5A3C"/><rect x="4" y="54" width="112" height="12" rx="5" fill="#6E4630"/>'
    for i in range(7): o += f'<path d="M{12+i*16} 56 v-20" stroke="#3E7D4A" stroke-width="3"/><circle cx="{12+i*16}" cy="34" r="8" fill="{["#E2435E","#F5C542","#7B3AA8","#F28C28"][i%4]}"/><circle cx="{12+i*16}" cy="34" r="3" fill="#FFF2B8"/>'
    return o, '-4 20 128 74'
def hedge(): return '<rect x="0" y="20" width="200" height="70" rx="20" fill="#3E7D4A"/>' + ''.join(f'<circle cx="{10+i*20}" cy="26" r="16" fill="#4E9A4F"/>' for i in range(10)) + shadow(100, 92, 100, 5), '-10 0 220 100'
def bench():
    o = shadow(100, 102, 96, 6) + ''.join(f'<rect x="10" y="{20+i*16}" width="180" height="11" rx="3" fill="#A8754E"/>' for i in range(2)) + '<rect x="4" y="58" width="192" height="12" rx="3" fill="#8B5A3C"/>'
    return o + '<path d="M20 70 v30 M180 70 v30 M20 20 v50 M180 20 v50" stroke="#2B2B2B" stroke-width="6"/>', '-6 0 212 110'
def streetlight(on=True):
    g = '<defs><radialGradient id="sg"><stop offset="0" stop-color="#FFF0B0" stop-opacity="0.85"/><stop offset="1" stop-color="#FFF0B0" stop-opacity="0"/></radialGradient></defs><circle cx="96" cy="40" r="70" fill="url(#sg)"/>' if on else ''
    return g + shadow(40, 352, 24, 5) + '<rect x="34" y="40" width="10" height="310" fill="#3A3F44"/><path d="M39 44 Q40 20 90 24" stroke="#3A3F44" stroke-width="8" fill="none"/><path d="M76 24 h34 l-6 14 h-22z" fill="#2B2B2B"/>' + f'<ellipse cx="93" cy="40" rx="11" ry="4" fill="{"#FFF4C2" if on else "#9AA3A8"}"/><rect x="26" y="340" width="26" height="12" rx="3" fill="#2B2B2B"/>', '0 -30 170 390'
def fountain():
    return shadow(80, 132, 80, 8) + '<ellipse cx="80" cy="110" rx="80" ry="22" fill="#B4BBC2"/><ellipse cx="80" cy="106" rx="70" ry="16" fill="#6FB3D9"/><rect x="72" y="50" width="16" height="56" fill="#C9CED4"/><ellipse cx="80" cy="50" rx="30" ry="8" fill="#B4BBC2"/><path d="M80 50 Q60 10 40 100 M80 50 Q100 10 120 100 M80 46 v-36" stroke="#BFE3F2" stroke-width="4" fill="none"/>', '-4 0 168 140'
def trashbin(): return shadow(30, 92, 26, 4) + '<path d="M8 20 h44 l-4 70 h-36z" fill="#24503B"/><rect x="4" y="12" width="52" height="10" rx="3" fill="#1A3A2B"/><path d="M20 30 v50 M30 30 v50 M40 30 v50" stroke="#1A3A2B" stroke-width="2"/>', '0 0 60 100'
def road(kind):
    o = '<rect width="256" height="256" fill="#4A4F55"/>'
    if kind == 'h': o += '<rect y="0" width="256" height="20" fill="#B4ADA0"/><rect y="236" width="256" height="20" fill="#B4ADA0"/>' + ''.join(f'<rect x="{i*64+8}" y="124" width="40" height="8" fill="#F5E9C8"/>' for i in range(4))
    elif kind == 'v': o += '<rect x="0" width="20" height="256" fill="#B4ADA0"/><rect x="236" width="20" height="256" fill="#B4ADA0"/>' + ''.join(f'<rect y="{i*64+8}" x="124" height="40" width="8" fill="#F5E9C8"/>' for i in range(4))
    elif kind == 'cross': o += ''.join(f'<rect x="{c[0]}" y="{c[1]}" width="20" height="20" fill="#B4ADA0"/>' for c in [(0, 0), (236, 0), (0, 236), (236, 236)])
    elif kind == 'crosswalk': o += '<rect y="0" width="256" height="20" fill="#B4ADA0"/><rect y="236" width="256" height="20" fill="#B4ADA0"/>' + ''.join(f'<rect x="{20+i*30}" y="40" width="18" height="176" fill="#F4F1EA"/>' for i in range(8))
    elif kind == 'sidewalk': o = '<rect width="256" height="256" fill="#C9C1B4"/>' + ''.join(f'<path d="M{i*64} 0 V256 M0 {i*64} H256" stroke="#ADA596" stroke-width="2"/>' for i in range(5))
    elif kind == 'path': o = '<rect width="256" height="256" fill="#8DC26F"/>' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="26" ry="18" fill="#D9CDB4"/>' for x, y in [(40, 40), (110, 70), (190, 40), (60, 140), (150, 150), (220, 130), (40, 220), (120, 220), (210, 220)])
    elif kind == 'grass': o = '<rect width="256" height="256" fill="#8DC26F"/>' + ''.join(f'<path d="M{(i*37)%256} {(i*61)%256} l3 -8 l3 8" stroke="#6FA552" stroke-width="2" fill="none"/>' for i in range(60))
    elif kind == 'parking': o += '<rect y="236" width="256" height="20" fill="#B4ADA0"/>' + ''.join(f'<rect x="{i*64}" y="40" width="6" height="140" fill="#F4F1EA"/>' for i in range(5)) + '<text x="96" y="140" font-family="Arial" font-size="60" font-weight="800" fill="#F4F1EA" opacity="0.7">P</text>'
    elif kind == 'dirt': o = '<rect width="256" height="256" fill="#B5916A"/>' + ''.join(f'<circle cx="{(i*47)%256}" cy="{(i*83)%256}" r="{2+i%4}" fill="#9C7A55"/>' for i in range(50))
    return o, '0 0 256 256'
def vehicle(kind, col='#C8412E'):
    def wheels(xs, y, r=20): return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#1F1F1F"/><circle cx="{x}" cy="{y}" r="{r*0.45}" fill="#B4BBC2"/>' for x in xs)
    f, d = grad_fill(col, 'v', a=.3, b=.25)
    if kind == 'car':
        o = d + shadow(130, 132, 120, 8) + f'<path d="M10 100 Q8 70 40 66 L80 30 H170 L210 66 Q250 70 250 100 V112 H10Z" fill="{f}"/><path d="M88 38 H126 V66 H62Z M134 38 H166 L196 66 H134Z" fill="#9CC6DA"/><rect x="236" y="76" width="14" height="10" rx="3" fill="#FFF4C2"/><rect x="10" y="78" width="10" height="10" fill="#C8412E"/>'
        return o + wheels([62, 196], 112), '0 20 260 120'
    if kind == 'taxi':
        o, vb = vehicle('car', '#F5C542'); return o + '<rect x="110" y="18" width="40" height="14" rx="3" fill="#2B2B2B"/><text x="130" y="29" font-family="Arial" font-size="9" fill="#F5C542" text-anchor="middle" font-weight="700">TAXI</text>' + ''.join(f'<rect x="{30+i*20}" y="88" width="10" height="10" fill="#2B2B2B"/>' for i in range(10)), '0 10 260 130'
    if kind == 'danfo':
        o = shadow(160, 152, 150, 8) + '<path d="M10 130 V50 Q10 30 30 30 H270 Q300 30 304 70 L310 130Z" fill="#F5C542"/><path d="M10 96 H310 M10 104 H310" stroke="#2B2B2B" stroke-width="5"/>' + ''.join(f'<rect x="{26+i*52}" y="42" width="44" height="40" rx="4" fill="#9CC6DA"/>' for i in range(5)) + '<path d="M272 42 H292 L302 82 H272Z" fill="#9CC6DA"/>'
        return o + '<text x="140" y="124" font-family="Arial" font-size="12" font-weight="800" fill="#2B2B2B">NO TELL GOD</text>' + wheels([70, 250], 132, 22), '0 20 320 140'
    if kind == 'truck':
        o = shadow(170, 162, 160, 8) + f'<rect x="10" y="20" width="220" height="120" rx="4" fill="#F4F1EA"/><rect x="10" y="80" width="220" height="30" fill="#24503B"/><text x="120" y="102" font-family="Arial" font-size="18" font-weight="800" fill="#E8B62C" text-anchor="middle">OGAMART</text>'
        o += '<path d="M234 60 H290 L326 100 V140 H234Z" fill="#24503B"/><path d="M246 70 H286 L312 100 H246Z" fill="#9CC6DA"/><rect x="316" y="114" width="12" height="10" fill="#FFF4C2"/>'
        return o + wheels([70, 190, 290], 142, 20), '0 10 340 160'
    if kind == 'pickup':
        o = d + shadow(150, 142, 140, 8) + f'<path d="M10 120 V80 H170 V40 H230 L266 80 Q290 82 290 100 V120Z" fill="{f}"/><path d="M180 48 H226 L252 80 H180Z" fill="#9CC6DA"/>' + ''.join(f'<circle cx="{40+i*30}" cy="74" r="12" fill="{c}"/>' for i, c in enumerate(['#D63A2A', '#7BB343', '#F28C28', '#D63A2A']))
        return o + wheels([66, 236], 122), '0 20 300 130'
    if kind == 'tractor':
        o = shadow(130, 172, 120, 8) + '<rect x="60" y="80" width="150" height="50" rx="6" fill="#C8412E"/><path d="M120 80 V20 H190 V80" stroke="#2B2B2B" stroke-width="6" fill="#9CC6DA" fill-opacity="0.6"/><rect x="190" y="50" width="10" height="34" fill="#2B2B2B"/>'
        return o + '<circle cx="90" cy="134" r="38" fill="#1F1F1F"/><circle cx="90" cy="134" r="16" fill="#F5C542"/>' + wheels([210], 148, 24), '0 10 260 180'
    if kind == 'motorbike':
        o = shadow(90, 112, 80, 6) + '<path d="M40 90 L80 60 H120 L150 90" stroke="#E2435E" stroke-width="10" fill="none" stroke-linejoin="round"/><path d="M70 60 h50 l6 -10 h-62z" fill="#2B2B2B"/><path d="M130 60 l12 -24 h12" stroke="#3A3F44" stroke-width="5" fill="none"/><rect x="18" y="30" width="48" height="40" rx="6" fill="#3B7DD8"/>'
        return o + wheels([40, 150], 92, 20), '0 20 180 100'
    if kind == 'keke':
        o = shadow(110, 142, 100, 8) + '<path d="M20 130 V60 Q24 30 60 30 H160 Q196 34 200 80 V130Z" fill="#F5C542"/><path d="M20 70 H200" stroke="#1E6B45" stroke-width="12"/><path d="M60 40 h80 v24 h-80z" fill="#9CC6DA" opacity="0.7"/>'
        return o + wheels([50, 180], 130, 18), '0 20 220 130'
def sky(kind):
    stops = {'day': ('#7EC8F0', '#CFEFFF'), 'sunset': ('#F28C5A', '#FCD9A0'), 'night': ('#0F1A3A', '#2C3A6A'), 'dawn': ('#C9B6E4', '#FCE3C8')}[kind]
    o = f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{stops[0]}"/><stop offset="1" stop-color="{stops[1]}"/></linearGradient></defs><rect width="1920" height="1080" fill="url(#sk)"/>'
    if kind == 'night': o += ''.join(f'<circle cx="{(i*397)%1920}" cy="{(i*211)%600}" r="{1+i%3}" fill="#fff" opacity="0.8"/>' for i in range(80)) + '<circle cx="1600" cy="160" r="60" fill="#F4F1EA"/><circle cx="1625" cy="145" r="55" fill="#0F1A3A"/>'
    elif kind == 'sunset': o += '<circle cx="1400" cy="760" r="140" fill="#FFE08A" opacity="0.9"/>'
    else: o += '<circle cx="1600" cy="180" r="80" fill="#FFF4C2"/><circle cx="1600" cy="180" r="140" fill="#FFF4C2" opacity="0.25"/>'
    if kind != 'night': o += ''.join(cloud(x, y, s) for x, y, s in [(200, 160, 1.2), (800, 100, 0.9), (1200, 240, 1.4)])
    return o, '0 0 1920 1080'
def cloud(x=0, y=0, s=1):
    return f'<g transform="translate({x} {y}) scale({s})" fill="#fff" opacity="0.92"><ellipse cx="0" cy="40" rx="110" ry="34"/><circle cx="-40" cy="20" r="40"/><circle cx="20" cy="0" r="54"/><circle cx="70" cy="26" r="36"/></g>'
def overlay(kind):
    if kind == 'night_tint': return '<rect width="512" height="512" fill="#0B1640" opacity="0.45"/>', '0 0 512 512'
    if kind == 'sunset_tint': return '<rect width="512" height="512" fill="#F28C28" opacity="0.18"/>', '0 0 512 512'
    if kind == 'lamp_glow': return '<defs><radialGradient id="lg"><stop offset="0" stop-color="#FFE9A0" stop-opacity="0.8"/><stop offset="1" stop-color="#FFE9A0" stop-opacity="0"/></radialGradient></defs><circle cx="256" cy="256" r="256" fill="url(#lg)"/>', '0 0 512 512'
    if kind == 'rain': return ''.join(f'<path d="M{(i*53)%512} {(i*97)%512} l-8 24" stroke="#BFE3F2" stroke-width="2" opacity="0.7"/>' for i in range(90)), '0 0 512 512'
    if kind == 'cloud': return cloud(150, 60, 1), '0 0 300 140'
def market_stall(col='#C8412E', goods=('tomatoes', 'peppers', 'oranges', 'yam')):
    import products as P
    o = shadow(130, 232, 130, 8) + '<path d="M20 230 V60 M240 230 V60" stroke="#6E4630" stroke-width="8"/>'
    o += f'<path d="M0 30 H260 L250 70 H10Z" fill="{col}"/>' + ''.join(f'<path d="M{i*26} 30 L{10+i*24} 70 L{10+(i+1)*24} 70 L{(i+1)*26} 30Z" fill="#F4F1EA"/>' for i in range(0, 10, 2))
    o += '<rect x="10" y="150" width="240" height="20" fill="#8B5A3C"/><rect x="20" y="170" width="220" height="60" fill="#A8754E"/>' + ''.join(f'<g transform="translate({50+i*55} 150) scale(0.55) translate(-50 -92)">{P.CATALOG[g]()}</g>' for i, g in enumerate(goods))
    return o, '-10 20 280 220'
def festival_arch():
    o = '<path d="M20 300 V80 Q200 -20 380 80 V300" stroke="#C8412E" stroke-width="22" fill="none"/>' + ''.join(f'<circle cx="{200+180*math.cos(math.radians(a))}" cy="{100-80*math.sin(math.radians(a))}" r="12" fill="{["#E8B62C","#4CC38A","#3B7DD8","#E2435E"][i%4]}"/>' for i, a in enumerate(range(10, 180, 20)))
    return o + '<rect x="100" y="60" width="200" height="50" rx="8" fill="#24503B"/>' + txt(200, 94, 'FESTIVAL', 24, '#E8B62C'), '0 -10 400 320'
def ribbon():
    return '<path d="M0 60 H400" stroke="#C8412E" stroke-width="16"/><path d="M200 60 l-40 -30 v60z M200 60 l40 -30 v60z" fill="#E2452F"/><circle cx="200" cy="60" r="14" fill="#B8324A"/><path d="M196 70 l-20 50 M204 70 l20 50" stroke="#C8412E" stroke-width="10"/>' + '<rect x="-10" y="40" width="12" height="160" fill="#C9A23A"/><rect x="398" y="40" width="12" height="160" fill="#C9A23A"/>', '-20 0 440 210'
def flag_bunting():
    cols = ['#E2435E', '#E8B62C', '#4CC38A', '#3B7DD8', '#F28C28']
    return '<path d="M0 10 Q200 50 400 10" stroke="#555" stroke-width="2" fill="none"/>' + ''.join(f'<path d="M{i*25} {10+40*(i/16)*(1-i/16)*4*0.5} l12 30 l12 -30z" fill="{cols[i%5]}"/>' for i in range(16)), '-4 0 408 60'
def xmas_tree():
    return shadow(80, 236, 60, 6) + '<rect x="70" y="200" width="20" height="34" fill="#6E4630"/>' + ''.join(f'<path d="M{80-w} {y} L80 {y-70} L{80+w} {y}Z" fill="#2F6B3A"/>' for y, w in [(210, 70), (160, 56), (110, 42)]) + ''.join(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/>' for x, y, c in [(60, 190, '#C8412E'), (100, 180, '#E8B62C'), (80, 140, '#3B7DD8'), (66, 120, '#E8B62C'), (96, 100, '#C8412E')]) + '<path d="M80 30 l6 14 h14 l-11 9 l4 14 l-13 -8 l-13 8 l4 -14 l-11 -9 h14z" fill="#F5C542"/>', '0 20 160 230'
def lantern(col='#C8412E'): return f'<path d="M30 0 v14" stroke="#555" stroke-width="2"/><ellipse cx="30" cy="40" rx="24" ry="28" fill="{col}"/><path d="M14 20 v40 M30 12 v56 M46 20 v40" stroke="{dk(col,.25)}" stroke-width="2"/><rect x="20" y="10" width="20" height="6" fill="#E8B62C"/><rect x="20" y="66" width="20" height="6" fill="#E8B62C"/>', '0 -4 60 84'
