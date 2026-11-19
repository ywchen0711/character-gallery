"""Look at family sprites: python tools/famspr.py out.png zoom name [name ...]
Each member: one row per animation."""
import os
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from PIL import Image
import family_members as fm
import family_sprites as fs

out, z, names = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
rows = []
for n in names:
    m = getattr(fm, n)()
    an = fs.animations(m, getattr(fm, n + '_action'))
    for k, v in an.items():
        rows.append(v)
W = max(len(r) for r in rows) * (fs.FW * z + 4)
S = Image.new('RGBA', (W, len(rows) * (fs.FH * z + 4)), (110, 120, 112, 255))
for y, r in enumerate(rows):
    for x, im in enumerate(r):
        S.alpha_composite(im.resize((fs.FW * z, fs.FH * z), 0), (x * (fs.FW * z + 4), y * (fs.FH * z + 4)))
S.save(out)
