"""Contact sheet of every exported variant at 4x: portrait, then each animation's frames.
python tools/contact.py out.png"""
import json, os, sys
from PIL import Image, ImageDraw
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = json.load(open(os.path.join(ROOT, 'chars', 'index.json'), encoding='utf-8'))
K, GAP = 4, 8
rows = []
for c in data['characters']:
    for v in c['variants']:
        por = Image.open(os.path.join(ROOT, v['files']['portrait'])).convert('RGBA')
        sheet = Image.open(os.path.join(ROOT, v['files']['sheet'])).convert('RGBA')
        meta = json.load(open(os.path.join(ROOT, v['files']['sheetJson']), encoding='utf-8'))
        fw, fh = meta['frameWidth'], meta['frameHeight']
        frames = []
        for n, a in meta['animations'].items():
            for i in range(a['frames']):
                frames.append(sheet.crop((i * fw, a['row'] * fh, (i + 1) * fw, (a['row'] + 1) * fh)))
            if len(frames) >= 12:
                break
        rows.append((f"{c['id']} / {v['style']}", por, frames[:12]))
W = max(r[1].width * K + sum(f.width * K + GAP for f in r[2]) + 3 * GAP for r in rows)
H = sum(max(r[1].height, max(f.height for f in r[2])) * K + 3 * GAP + 14 for r in rows)
S = Image.new('RGBA', (W, H), (84, 92, 88, 255))
d = ImageDraw.Draw(S)
y = GAP
for name, por, frames in rows:
    d.text((GAP, y), name, fill=(240, 240, 230, 255)); y += 14
    S.alpha_composite(por.resize((por.width * K, por.height * K), 0), (GAP, y))
    x = GAP * 3 + por.width * K
    for f in frames:
        S.alpha_composite(f.resize((f.width * K, f.height * K), 0), (x, y)); x += f.width * K + GAP
    y += max(por.height, max(f.height for f in frames)) * K + 2 * GAP
S.save(sys.argv[1])
print(S.size)
