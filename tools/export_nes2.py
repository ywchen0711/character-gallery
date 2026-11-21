"""Export the round-1 `nes2` redraws of the Longmen heroes (src/nes2_longmen.py portraits, src/nes2_longmen_sprites.py
field sprites) to chars/<id>/nes2/ and merge them into chars/index.json as an extra variant. The old `nes` art and
every other character are left untouched, so the games keep pulling the `nes` files until nes2 is approved.

    python -P tools/export_nes2.py

Also writes chars/longmen/compare-nes2.png (old vs new, 4x) used by compare-longmen.html.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

from PIL import Image  # noqa: E402
from pixlib import count_colours, scale  # noqa: E402
import nes2_longmen as P  # noqa: E402
import nes2_longmen_sprites as SP  # noqa: E402
from styles import STYLES  # noqa: E402

IDS = ['yirui', 'yishuo', 'liuhanyan', 'baixian', 'kuchan', 'xiaotian']
FPS = {'idle': 2, 'walk': 4, 'walk_side': 4, 'walk_up': 4}
NOTES = {'walk': 'front; frame 2 has the same body as frame 1, only the legs step (the bottom rows)',
         'walk_side': 'faces right (stride, then legs together; same body); mirror horizontally for left',
         'walk_up': 'back view; frame 2 has the same body, only the legs step'}


def export(cid):
    out = os.path.join(ROOT, 'chars', cid, 'nes2')
    os.makedirs(out, exist_ok=True)
    por = P.portrait(cid).image()
    por.save(os.path.join(out, 'portrait.png'))
    scale(por, 4).save(os.path.join(out, 'portrait@4x.png'))
    fr = SP.frames(cid)
    names = list(fr)
    body = fr['idle'][0]
    body.save(os.path.join(out, 'body.png'))
    scale(body, 4).save(os.path.join(out, 'body@4x.png'))
    sheet = Image.new('RGBA', (32, 24 * len(names)), (0, 0, 0, 0))
    anims = {}
    for row, n in enumerate(names):
        for i, f in enumerate(fr[n]):
            sheet.alpha_composite(f, (i * 16, row * 24))
        anims[n] = {'row': row, 'frames': len(fr[n]), 'fps': FPS[n], 'loop': True}
        if n in NOTES:
            anims[n]['note'] = NOTES[n]
    sheet.save(os.path.join(out, 'sheet.png'))
    scale(sheet, 4).save(os.path.join(out, 'sheet@4x.png'))
    meta = {'image': 'sheet.png', 'frameWidth': 16, 'frameHeight': 24,
            'anchor': {'x': 8, 'y': 23, 'note': 'feet centre in each cell'}, 'animations': anims}
    json.dump(meta, open(os.path.join(out, 'sheet.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    base = 'chars/%s/nes2/' % cid
    files = {k: base + n for k, n in {'portrait': 'portrait.png', 'portrait4x': 'portrait@4x.png', 'body': 'body.png',
                                     'body4x': 'body@4x.png', 'sheet': 'sheet.png', 'sheet4x': 'sheet@4x.png',
                                     'sheetJson': 'sheet.json'}.items()}
    print('  %s/nes2: portrait %dc, sheet %dc, %s' % (cid, count_colours(por), count_colours(sheet), ', '.join(names)))
    return {'style': 'nes2', 'styleName': STYLES['nes2']['name'], 'primary': False, 'files': files,
            'sizes': {'portrait': [48, 56], 'frame': [16, 24]},
            'colours': {'portrait': count_colours(por), 'sheet': count_colours(sheet)}, 'animations': names}


def main():
    path = os.path.join(ROOT, 'chars', 'index.json')
    data = json.load(open(path, encoding='utf-8'))
    data['styles']['nes2'] = {'name': STYLES['nes2']['name'], 'blurb': STYLES['nes2']['blurb']}
    by = {c['id']: c for c in data['characters']}
    for cid in IDS:
        v = export(cid)
        c = by[cid]
        c['variants'] = [x for x in c['variants'] if x['style'] != 'nes2'] + [v]
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('index.json updated:', len(IDS), 'nes2 variants')


if __name__ == '__main__':
    main()
