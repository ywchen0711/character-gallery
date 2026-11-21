"""Promote the approved `nes2` art to the main `nes` style for the whole Longmen cast (run once, at rollout).

For every character that has an nes2 variant:
  chars/<id>/nes/   -> chars/<id>/nes_old/   (the previous art, kept for reference)
  chars/<id>/nes2/  -> chars/<id>/nes/       (the games' existing tools read chars/<id>/nes/, so they pick it up)
and chars/index.json: the `nes` variant points at the new files (with walk_up in its animations), a `nes_old`
variant points at the old ones, and the `nes2` entry is dropped (its folder stays as the source copy).

After promoting, src/nes_variant.NESVariant must draw these ids from the nes2 sources, or a later full
`python tools/export.py` would write the old art back into nes/ (see PROMOTED in src/nes_variant.py).

    python -P tools/promote_nes2.py [--root DIR] [--dry]
"""
import json
import os
import shutil
import sys


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    dry = '--dry' in sys.argv
    path = os.path.join(root, 'chars', 'index.json')
    data = json.load(open(path, encoding='utf-8'))
    data['styles'].setdefault('nes_old', {
        'name': {'zh': '8-bit 紅白機（舊版）', 'en': '8-bit Famicom (previous art)'},
        'blurb': {'zh': '換成新版之前的龍門人物圖，留作參考。', 'en': 'The Longmen art before the redraw, kept for reference.'}})
    moved = []
    for c in data['characters']:
        new = next((v for v in c['variants'] if v['style'] == 'nes2'), None)
        old = next((v for v in c['variants'] if v['style'] == 'nes'), None)
        if not new or not old:
            continue
        d = os.path.join(root, 'chars', c['id'])
        if not dry:
            if os.path.isdir(os.path.join(d, 'nes_old')):
                shutil.rmtree(os.path.join(d, 'nes_old'))
            shutil.copytree(os.path.join(d, 'nes'), os.path.join(d, 'nes_old'))
            shutil.rmtree(os.path.join(d, 'nes'))
            shutil.copytree(os.path.join(d, 'nes2'), os.path.join(d, 'nes'))
        keep = dict(old)
        keep['style'] = 'nes_old'
        keep['primary'] = False
        keep['styleName'] = data['styles']['nes_old']['name']
        keep['files'] = {k: v.replace('/nes/', '/nes_old/') for k, v in old['files'].items()}
        promoted = dict(new)
        promoted['style'] = 'nes'
        promoted['primary'] = True
        promoted['styleName'] = data['styles']['nes']['name']
        promoted['files'] = {k: v.replace('/nes2/', '/nes/') for k, v in new['files'].items()}
        c['variants'] = [promoted if v is old else v for v in c['variants'] if v is not new] + [keep]
        moved.append(c['id'])
    if not dry:
        json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%s %d characters: %s' % ('would promote' if dry else 'promoted', len(moved), ' '.join(moved)))


if __name__ == '__main__':
    main()
