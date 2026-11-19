"""960x540 lobby thumbnail: every character's main-style portrait with its sprite, side by side.
python tools/thumb.py"""
import json
import os
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(ROOT, 'chars', 'index.json'), encoding='utf-8'))
T = Image.new('RGB', (960, 540))
d = ImageDraw.Draw(T)
for y in range(540):
    d.line([(0, y), (960, y)], fill=(20 + y // 30, 26 + y // 28, 30 + y // 24))
items = []
for c in data['characters']:
    v = next((x for x in c['variants'] if x['primary']), c['variants'][0])
    items.append(v)
slot = 960 // len(items)
for i, v in enumerate(items):
    por = Image.open(os.path.join(ROOT, v['files']['portrait'])).convert('RGBA')
    body = Image.open(os.path.join(ROOT, v['files']['body'])).convert('RGBA')
    k = max(1, min(4, 300 // por.height, (slot - 12) // por.width))
    p = por.resize((por.width * k, por.height * k), 0)
    T.paste(p, (i * slot + (slot - p.width) // 2, 310 - p.height), p)
    kb = max(1, min(8, 200 // body.height, (slot - 12) // body.width))
    b = body.resize((body.width * kb, body.height * kb), 0)
    T.paste(b, (i * slot + (slot - b.width) // 2, 530 - b.height), b)
T.save(os.path.join(ROOT, 'thumb.jpg'), quality=92)
