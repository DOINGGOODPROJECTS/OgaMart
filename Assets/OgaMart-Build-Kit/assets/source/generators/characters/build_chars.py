import sys, os, json, subprocess; sys.path.insert(0, '/home/claude/rig2')
import rig2, side, cast2, extras
from concurrent.futures import ThreadPoolExecutor
NS = 'xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"'
VB = '-60 -100 320 460'
OUT = '/home/claude/pack2/OgaMart-GDevelop-Assets/characters'
SRC = '/home/claude/pack2/OgaMart-GDevelop-Assets/source/characters'
TMP = '/home/claude/tmp_svg'
for d in (OUT, SRC, TMP): os.makedirs(d, exist_ok=True)
def svg(body, vb=VB, w=640, h=920): return f'<svg {NS} viewBox="{vb}" width="{w}" height="{h}">{body}</svg>'
GROUPS = [('recurring', cast2.C), ('daniel_career', extras.CAREER), ('employees', extras.EMP), ('customers', extras.CUST), ('pedestrians', extras.PED)]
EMPW = ['scan_1', 'scan_2', 'restock_1', 'restock_2', 'carry_1', 'check_1']
CUSTW = ['pick_item_1', 'pick_item_2', 'pay_1', 'impatient_1', 'impatient_2']
PORTRAIT = ['smile', 'talk', 'happy', 'laugh', 'angry', 'surprised', 'sad', 'neutral']
STD_ORDER = list(rig2.STD)
jobs = []; manifest = {}
for grp, d in GROUPS:
    for n, c in d.items():
        folder = f'{OUT}/{grp}/{n}'; os.makedirs(folder, exist_ok=True)
        poses = dict(rig2.STD)
        if grp == 'recurring': poses.update(cast2.SIG.get(n, {}))
        if grp in ('employees', 'daniel_career'): poses.update({k: extras.WORK[k] for k in EMPW})
        if grp in ('customers', 'pedestrians'): poses.update({k: extras.WORK[k] for k in CUSTW})
        if n == 'Daniel': poses.update({k: extras.WORK[k] for k in CUSTW})
        anims = {}
        for k, p in poses.items():
            b = rig2.front(c, p); fn = f'{n}_{k}'
            jobs.append((svg(b), f'{folder}/{fn}.png', 600)); anims.setdefault(k.rsplit('_', 1)[0], []).append(fn + '.png')
        style = cast2.WALKSTYLE.get(n, 'normal')
        if n.startswith('Daniel_'): style = {'Daniel_Cashier': 'normal', 'Daniel_Supervisor': 'confident', 'Daniel_Manager': 'confident'}[n]
        if grp == 'employees' and n == 'Emp_Delivery': style = 'brisk'
        for f in range(8):
            b = side.side(c, f, style); fn = f'{n}_walk_{f+1}'
            jobs.append((svg(b), f'{folder}/{fn}.png', 600)); anims.setdefault('walk', []).append(fn + '.png')
        if n in ('SpeedySam', 'Daniel', 'Emp_Delivery'):
            for f in range(8):
                b = side.side(c, f, 'run'); fn = f'{n}_run_{f+1}'; jobs.append((svg(b), f'{folder}/{fn}.png', 600)); anims.setdefault('run', []).append(fn + '.png')
        # portraits for dialogue
        top = 352 - 352 * c.height - 36; s = 140 * max(1, c.height) * (1.3 if c.age == 'child' else 1)
        if c.age == 'child': top = 352 - 352 * c.height - 10
        for e in PORTRAIT:
            b = rig2.front(c, rig2.P(la=rig2.rel(-1, 8, 6), ra=rig2.rel(1, 8, 6), expr=e))
            fn = f'{n}_portrait_{e}'; jobs.append((svg(b, f'{100-s/2:.1f} {top:.1f} {s:.1f} {s:.1f}', 512, 512), f'{folder}/{fn}.png', 512)); anims.setdefault('portrait', []).append(fn + '.png')
        # editable Inkscape sources: idle front + walk side + full pose sheet
        open(f'{SRC}/{n}_front.svg', 'w').write(svg(rig2.front(c, rig2.STD['idle_1'])))
        open(f'{SRC}/{n}_side.svg', 'w').write(svg(side.side(c, 0, style)))
        manifest[n] = dict(group=grp, walk_style=style, animations={k: len(v) for k, v in anims.items()})
def run(j):
    s, out, h = j; t = f'{TMP}/{abs(hash(out))}.svg'; open(t, 'w').write(s)
    subprocess.run(['rsvg-convert', '-h', str(h), t, '-o', out], check=True); os.remove(t)
with ThreadPoolExecutor(16) as ex: list(ex.map(run, jobs))
json.dump(manifest, open('/home/claude/pack2/char_manifest.json', 'w'), indent=1)
print(len(jobs), 'pngs')
