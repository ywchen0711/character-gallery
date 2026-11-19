"""Re-export every character in src/roster.py to chars/<id>/ and chars/index.json.

    python tools/export.py

Per character:
  portrait.png      56x64 bust portrait
  portrait@4x.png   224x256
  body.png          56x64 chibi, front idle frame
  body@4x.png       224x256
  sheet.png         all animation frames, one animation per row (56x64 cells)
  sheet@4x.png      the same at 4x
  sheet.json        frame size, rows, frame counts, fps
"""
import importlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))

from PIL import Image  # noqa: E402
import chibi  # noqa: E402
import portrait  # noqa: E402
from pixlib import count_colours, scale  # noqa: E402
from roster import ROSTER  # noqa: E402

FPS = {'idle': 3, 'walk': 8, 'walk_side': 8, 'action': 8}
LOOP = {'idle': True, 'walk': True, 'walk_side': True, 'action': False}
FACTION_COLOUR = {'wu': '#c8402e', 'shu': '#3f8f4e', 'wei': '#3b5ba8', 'qun': '#b08a3a'}
FACTION_NAME = {'wu': {'zh': '吳', 'en': 'Wu'}, 'shu': {'zh': '蜀', 'en': 'Shu'},
                'wei': {'zh': '魏', 'en': 'Wei'}, 'qun': {'zh': '群', 'en': 'Other'}}


def export(cid):
    ch = importlib.import_module(cid)
    out = os.path.join(ROOT, 'chars', cid)
    os.makedirs(out, exist_ok=True)
    por = portrait.render(ch)
    por.save(os.path.join(out, 'portrait.png'))
    scale(por, 4).save(os.path.join(out, 'portrait@4x.png'))

    fr = chibi.frames(ch)
    body = fr['idle'][0].image(ch.CPAL)
    body.save(os.path.join(out, 'body.png'))
    scale(body, 4).save(os.path.join(out, 'body@4x.png'))

    names = list(fr)
    cols = max(len(fr[n]) for n in names)
    sheet = Image.new('RGBA', (cols * chibi.FW, len(names) * chibi.FH), (0, 0, 0, 0))
    anims = {}
    for row, n in enumerate(names):
        for i, f in enumerate(fr[n]):
            sheet.alpha_composite(f.image(ch.CPAL), (i * chibi.FW, row * chibi.FH))
        anims[n] = {'row': row, 'frames': len(fr[n]), 'fps': FPS.get(n, 8), 'loop': LOOP.get(n, True)}
    anims['walk_side']['note'] = 'faces right; mirror horizontally for left' if 'walk_side' in anims else None
    sheet.save(os.path.join(out, 'sheet.png'))
    scale(sheet, 4).save(os.path.join(out, 'sheet@4x.png'))
    meta = {'image': 'sheet.png', 'frameWidth': chibi.FW, 'frameHeight': chibi.FH,
            'anchor': {'x': 28, 'y': 62, 'note': 'feet centre in each cell'},
            'animations': anims}
    with open(os.path.join(out, 'sheet.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    M = ch.META
    files = {k: f'chars/{cid}/{v}' for k, v in {
        'portrait': 'portrait.png', 'portrait4x': 'portrait@4x.png', 'body': 'body.png',
        'body4x': 'body@4x.png', 'sheet': 'sheet.png', 'sheet4x': 'sheet@4x.png', 'sheetJson': 'sheet.json'}.items()}
    entry = dict(M, faction=ch.FACTION, factionName=FACTION_NAME[ch.FACTION],
                 colour=FACTION_COLOUR[ch.FACTION], files=files,
                 sizes={'portrait': list(por.size), 'body': [chibi.FW, chibi.FH]},
                 colours={'portrait': count_colours(por), 'body': count_colours(sheet)})
    summary = ', '.join('%sx%d' % (n, anims[n]['frames']) for n in names)
    print(f'{cid}: portrait {por.size} {count_colours(por)} colours, sheet {sheet.size} '
          f'{count_colours(sheet)} colours, animations {summary}')
    return entry


def main():
    entries = [export(c) for c in ROSTER]
    with open(os.path.join(ROOT, 'chars', 'index.json'), 'w', encoding='utf-8') as f:
        json.dump({'version': 1, 'characters': entries}, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
