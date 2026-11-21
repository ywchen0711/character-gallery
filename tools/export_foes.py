"""Re-export only the common foes (faction `foe`) and merge them into chars/index.json, leaving every other
character's files untouched (used after a change to the foe busts, e.g. the 2026-11-20 soft-nose fix).

    python -P tools/export_foes.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))

import export as EX  # noqa: E402


def main():
    path = os.path.join(ROOT, 'chars', 'index.json')
    data = json.load(open(path, encoding='utf-8'))
    out = []
    for c in data['characters']:
        if c['faction'] == 'foe':
            extra = [v for v in c['variants'] if v['style'] != 'nes']
            c = EX.export(c['id'])
            c['variants'] += extra
        out.append(c)
    data['characters'] = out
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    # the foe group pictures
    from pixlib import scale
    from nes_foes import group
    for gid, name, cols in (('foes', 'group-nes', 10), ('foes', 'group-nes-5col', 5),
                            ('longmen2Foes', 'group-nes-l2', 8), ('longmen2Foes', 'group-nes-l2-4col', 4)):
        im = group(data['groups'][gid]['members'], cols=cols)
        im.save(os.path.join(ROOT, 'chars', 'foes', name + '.png'))
        scale(im, 4).save(os.path.join(ROOT, 'chars', 'foes', name + '@4x.png'))


if __name__ == '__main__':
    main()
