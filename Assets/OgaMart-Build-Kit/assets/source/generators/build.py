import sys, os; sys.path.insert(0, '/home/claude/label')
from sheets import *
R2 = R + '/preview'
for f in glob.glob(R2 + '/*.png'): os.remove(f)
allpages = []
for i, (t, s, its) in enumerate(SECTIONS):
    ps = pages(t, s, its); allpages += ps
    for j, p in enumerate(ps): p.save(f'{R2}/{i+1:02d}_{t.split("(")[0].strip().replace(" – ", "_").replace(" ", "_").replace("&", "and").replace(",", "").replace("/", "_")}{"_"+str(j+1) if len(ps) > 1 else ""}.png', optimize=True)
os.makedirs(R2 + '/characters', exist_ok=True); charpages = []
for t, s, its in CHARPAGES:
    ps = pages(t, s, its); charpages += ps
    nm = t.split(' – ')[0].replace('.', '').replace(' ', '_').replace('(', '').replace(')', '')
    for j, p in enumerate(ps): p.save(f'{R2}/characters/{nm}{"_"+str(j+1) if len(ps) > 1 else ""}.png', optimize=True)
def pdf(pgs, path):
    A = [p.convert('RGB') for p in pgs]; A[0].save(path, save_all=True, append_images=A[1:], resolution=150)
pdf(allpages, '/mnt/user-data/outputs/OgaMart-Asset-Catalog-Labeled.pdf')
pdf(charpages, '/mnt/user-data/outputs/OgaMart-Character-Animations-Labeled.pdf')
print(len(allpages), len(charpages))
