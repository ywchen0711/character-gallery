"""960x540 lobby thumbnail: python tools/thumb.py"""
import os, sys, importlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src')); sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))
from PIL import Image, ImageDraw
import chibi, portrait
from roster import ROSTER

T = Image.new('RGB', (960, 540), (18, 22, 19))
d = ImageDraw.Draw(T)
for y in range(540):
    d.line([(0, y), (960, y)], fill=(18 + y // 40, 24 + y // 36, 20 + y // 40))
ch = importlib.import_module(ROSTER[0])
por = portrait.render(ch).resize((56 * 7, 64 * 7), 0)
T.paste(por, (60, 46), por)
fr = chibi.frames(ch)
picks = [fr['idle'][0], fr['walk_side'][0], fr['action'][1]]
for i, f in enumerate(picks):
    im = f.image(ch.CPAL).resize((56 * 4, 64 * 4), 0)
    x = 480 + (i % 2) * 230 - (0 if i < 2 else -115)
    y = 20 if i < 2 else 272
    T.paste(im, (x, y), im)
T.save(os.path.join(ROOT, 'thumb.jpg'), quality=92)
