import os, sys, glob
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, '/home/claude/label'); from names import CHAR, nice, anim_label
R = '/home/claude/pack2/OgaMart-GDevelop-Assets'
FB = '/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf'; FR = '/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf'
if not os.path.exists(FR): FR = FB
f_title = ImageFont.truetype(FB, 44); f_name = ImageFont.truetype(FB, 20); f_file = ImageFont.truetype(FR, 13); f_sub = ImageFont.truetype(FR, 22)
PW, COLS, CW, CH = 1700, 6, 270, 330
BG = (239, 233, 223); CARD = (255, 253, 248); GREEN = (36, 80, 59); GREY = (120, 112, 100)
def wrap(d, text, font, w):
    words = text.split(); lines = ['']
    for wd in words:
        t = (lines[-1] + ' ' + wd).strip()
        if d.textlength(t, font=font) <= w: lines[-1] = t
        else: lines.append(wd)
    return lines[:2]
def pages(title, subtitle, items):
    """items: list of (png_path, label). returns list of PIL pages"""
    out = []; per = COLS * 6; 
    for p0 in range(0, max(1, len(items)), per):
        chunk = items[p0:p0 + per]; rows = (len(chunk) + COLS - 1) // COLS
        H = 150 + rows * (CH + 14) + 40
        pg = Image.new('RGB', (PW, H), BG); d = ImageDraw.Draw(pg)
        d.rectangle([0, 0, PW, 110], fill=GREEN); d.text((40, 22), title + (f'  ({p0//per+1})' if len(items) > per else ''), font=f_title, fill=(232, 182, 44))
        d.text((40, 118), subtitle, font=f_sub, fill=GREY)
        for i, (path, label) in enumerate(chunk):
            x = 40 + (i % COLS) * (CW + 6); y = 160 + (i // COLS) * (CH + 14)
            d.rounded_rectangle([x, y, x + CW - 8, y + CH], 14, fill=CARD, outline=(217, 210, 197), width=2)
            im = Image.open(path).convert('RGBA'); im.thumbnail((CW - 30, CH - 92))
            pg.paste(im, (x + (CW - 8 - im.width) // 2, y + 12 + (CH - 104 - im.height) // 2), im)
            for j, ln in enumerate(wrap(d, label, f_name, CW - 24)): d.text((x + 12, y + CH - 78 + j * 24), ln, font=f_name, fill=GREEN)
            fn = os.path.basename(path); fn = fn if len(fn) < 36 else fn[:33] + '…'
            d.text((x + 12, y + CH - 26), fn, font=f_file, fill=GREY)
        out.append(pg)
    return out
def objs(folder_glob):
    return [(p, nice(os.path.splitext(os.path.basename(p))[0])) for p in sorted(glob.glob(f'{R}/{folder_glob}'))]
SECTIONS = []
# characters overview
groups = [('recurring', 'Recurring characters (doc 6.3)'), ('daniel_career', "Daniel's career looks (doc 6.8)"), ('employees', 'Store staff (doc 4.7)'), ('customers', 'Customer types (doc 4.3)'), ('pedestrians', 'Pedestrians')]
for g, t in groups:
    its = [(f'{R}/characters/{g}/{n}/{n}_idle_1.png', CHAR[n]) for n in sorted(os.listdir(f'{R}/characters/{g}'))]
    SECTIONS.append((f'Characters – {t}', 'Name shown under each character. Folder: characters/' + g, its))
SECTIONS.append(('Name tags', 'ui/name_tags – show above a character\'s head in game', objs('ui/name_tags/*.png')))
for title, sub, gl in [
 ('Products (doc 4.2)', 'products/', 'products/*.png'),
 ('Store – Shelves, full stock (doc 4.2/4.6)', 'store/shelves/<category>/ – each also has stock 1-4', 'store/shelves/*/*_stock_5.png'),
 ('Store – Stock levels example (Drinks, metal)', 'Use the 5 images as frames of one Sprite', 'store/shelves/drinks/*_metal_*.png'),
 ('Store – Fridges, freezer, stands', 'store/equipment/', 'store/equipment/*.png'),
 ('Store – Checkout (doc 4.4)', 'store/checkout/', 'store/checkout/*.png'),
 ('Store – Storage, displays, carts', 'store/storage, displays, carts', 'store/[sdc][ti]*/*.png'),
 ('Store – Entrance, lighting, signage, decor', 'store/entrance, lighting, signage, decor', 'store/[eld][niie]*/*.png'),
 ('Store – Floors & walls (themes, doc 8.5)', 'store/floors_walls – Tiled Sprite', 'store/floors_walls/*.png'),
 ('Neighborhood – OgaMart exteriors (doc 8.5)', 'neighborhood/ogamart_exterior/', 'neighborhood/ogamart_exterior/*.png'),
 ('Neighborhood – Buildings (doc 5.2)', 'neighborhood/buildings/<type>/ – basic, established, premium', 'neighborhood/buildings/*/*.png'),
 ('Neighborhood – Construction & plots', 'neighborhood/construction/', 'neighborhood/construction/*.png'),
 ('Neighborhood – Nature & street', 'neighborhood/nature, street', 'neighborhood/[ns][at]*/*.png'),
 ('Neighborhood – Vehicles', 'neighborhood/vehicles/', 'neighborhood/vehicles/*.png'),
 ('Neighborhood – Ground tiles & sky', 'neighborhood/ground, sky', 'neighborhood/[gs][rk]*/*.png'),
 ('Neighborhood – Events & festivals', 'neighborhood/events/', 'neighborhood/events/*.png'),
 ('UI – Icons', 'ui/icons/<group>/', 'ui/icons/[!g]*/*.png'),
 ('UI – Buttons & panels', 'ui/buttons, ui/panels', 'ui/[bp]*/*.png'),
 ('UI – Effects', 'ui/effects/', 'ui/effects/*.png'),
 ('UI – Emotion bubbles & relationship badges', 'ui/emotion_bubbles, ui/relationship', 'ui/[er][me]*/*.png')]:
    SECTIONS.append((title, sub, objs(gl)))
# per-character animation pages
CHARPAGES = []
for g, t in groups:
    for n in sorted(os.listdir(f'{R}/characters/{g}')):
        files = sorted(glob.glob(f'{R}/characters/{g}/{n}/*.png'), key=lambda p: (('portrait' in p), p))
        CHARPAGES.append((f'{CHAR[n]} – all animations', f'characters/{g}/{n}/  ·  {len(files)} frames', [(p, anim_label(os.path.splitext(os.path.basename(p))[0], n)) for p in files]))
