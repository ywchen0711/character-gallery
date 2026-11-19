"""Side-by-side look at the four family portraits: python tools/famlook.py out.png [zoom]"""
import os
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from PIL import Image
import family_portraits as fp

z = int(sys.argv[2]) if len(sys.argv) > 2 else 4
ims = [f() for f in (fp.jeff, fp.erin, fp.josh, fp.jasper)]
S = Image.new('RGBA', (4 * (72 * z + 8), 80 * z), (40, 40, 40, 255))
for i, im in enumerate(ims):
    S.paste(im.resize((72 * z, 80 * z), 0), (i * (72 * z + 8), 0))
S.save(sys.argv[1])
