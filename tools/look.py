"""Quick look at one variant: python tools/look.py <id> <style> <out.png> [zoom]
Renders the portrait and every animation frame, zoomed, on a mid-grey board."""
import os, sys, importlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src')); sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))
from PIL import Image
cid, style, out = sys.argv[1:4]
z = int(sys.argv[4]) if len(sys.argv) > 4 else 4
ch = importlib.import_module(cid)
v = [x for x in ch.variants() if x.style == style][0]
por = v.portrait(); fr = v.frames()
rows = [[por]] + [fr[n] for n in fr]
W = max(sum(i.width * z + 6 for i in r) for r in rows) + 6
H = sum(max(i.height for i in r) * z + 6 for r in rows) + 6
S = Image.new('RGBA', (W, H), (96, 104, 100, 255)); y = 6
for r in rows:
    x = 6
    for i in r:
        S.alpha_composite(i.resize((i.width * z, i.height * z), 0), (x, y)); x += i.width * z + 6
    y += max(i.height for i in r) * z + 6
S.save(out)
