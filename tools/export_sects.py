"""Export only the 龍門江湖志 (Sects of Longmen) characters and merge them into chars/index.json, leaving every
other character's files untouched (a full tools/export.py run also works and gives the same result for these).

    python tools/export_sects.py
"""
import importlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))

import export as EX  # noqa: E402
from pixlib import scale  # noqa: E402
from nes_variant import group as nes_group  # noqa: E402
import nes_sects  # noqa: E402

GROUPS = {
    'sects': (nes_sects.TROOPS, {'zh': '龍門江湖志・江湖兵卒', 'en': 'Sects of Longmen: the troops'}, 7),
    'sectsUnique': (nes_sects.UNIQUE, {'zh': '龍門江湖志・各派獨門弟子', 'en': "Sects of Longmen: each sect's own fighters"}, 6),
    'sectsPeople': (nes_sects.PEOPLE, {'zh': '龍門江湖志・慈雲庵主與奇人', 'en': 'Sects of Longmen: the abbess and great people'}, 3),
}


def main():
    path = os.path.join(ROOT, 'chars', 'index.json')
    data = json.load(open(path, encoding='utf-8'))
    ids = nes_sects.PEOPLE + nes_sects.TROOPS + nes_sects.UNIQUE
    entries = {c['id']: c for c in data['characters']}
    order = [c['id'] for c in data['characters']]
    for cid in ids:
        print(cid)
        e = EX.export(cid)
        ch = importlib.import_module(cid)
        if getattr(ch, 'META', {}).get('alsoIn'):
            e['alsoIn'] = ch.META['alsoIn']
        entries[cid] = e
        if cid not in order:
            order.append(cid)
    data['characters'] = [entries[c] for c in order]
    gd = os.path.join(ROOT, 'chars', 'sects')
    os.makedirs(gd, exist_ok=True)
    for gid, (members, name, cols) in GROUPS.items():
        tall = max(2, (len(members) + 1) // 2) if len(members) > 4 else 2
        files = {}
        for key, nm, c in (('nes', 'group-nes-' + gid, cols), ('nesTall', 'group-nes-' + gid + '-tall', min(4, cols))):
            im = nes_group(members, cols=c)
            im.save(os.path.join(gd, nm + '.png'))
            scale(im, 4).save(os.path.join(gd, nm + '@4x.png'))
            files[key] = 'chars/sects/' + nm + '.png'
            files[key + '4x'] = 'chars/sects/' + nm + '@4x.png'
        data['groups'][gid] = {'name': name, 'faction': 'sects' if gid != 'sectsPeople' else 'sects', 'members': members, 'style': 'nes', 'files': files}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('index.json:', len(data['characters']), 'characters')


if __name__ == '__main__':
    main()
