"""Contact sheet of portraits: python tools/sheet.py out.png scale id1 id2 ..."""
import sys, importlib
sys.path.insert(0, 'src'); sys.path.insert(0, 'src/chars')
from PIL import Image
import portrait
out, k, ids = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
ims = [portrait.render(importlib.import_module(i)) for i in ids]
cols = min(5, len(ims)); rows = (len(ims) + cols - 1) // cols
S = Image.new('RGBA', (cols * (56 * k + 8) + 8, rows * (64 * k + 8) + 8), (24, 24, 28, 255))
for n, im in enumerate(ims):
    S.alpha_composite(im.resize((56 * k, 64 * k), 0), (8 + (n % cols) * (56 * k + 8), 8 + (n // cols) * (64 * k + 8)))
S.save(out)
