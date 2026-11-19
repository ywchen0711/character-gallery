"""Zoomed preview with a pixel grid, for checking hand-authored grids.
python tools/preview.py in.png out.png [zoom]"""
import sys
from PIL import Image, ImageDraw

src, out = sys.argv[1], sys.argv[2]
z = int(sys.argv[3]) if len(sys.argv) > 3 else 10
im = Image.open(src).convert('RGBA')
W, H = im.width * z, im.height * z
bg = Image.new('RGBA', (W + 30, H + 30), (40, 40, 48, 255))
big = im.resize((W, H), Image.NEAREST)
bg.alpha_composite(big, (30, 30))
d = ImageDraw.Draw(bg)
for x in range(im.width + 1):
    c = (255, 255, 0, 120) if x % 8 == 0 else (90, 90, 100, 90)
    d.line([(30 + x * z, 30), (30 + x * z, 30 + H)], fill=c)
    if x % 4 == 0 and x < im.width:
        d.text((30 + x * z + 1, 2), str(x), fill=(220, 220, 220, 255))
for y in range(im.height + 1):
    c = (255, 255, 0, 120) if y % 8 == 0 else (90, 90, 100, 90)
    d.line([(30, 30 + y * z), (30 + W, 30 + y * z)], fill=c)
    if y % 4 == 0 and y < im.height:
        d.text((2, 30 + y * z + 1), str(y), fill=(220, 220, 220, 255))
bg.save(out)
