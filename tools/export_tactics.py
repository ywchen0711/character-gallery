"""Export only the 龍門戰記 (Longmen Tactics) characters and merge them into chars/index.json, leaving every other
character's files untouched (a full tools/export.py run also works and gives the same result for these).

    python tools/export_tactics.py
"""
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
import nes_tactics  # noqa: E402

GROUPS = {
    'tactics': (nes_tactics.STORY, {'zh': '龍門戰記・登場人物', 'en': 'Longmen Tactics: people of the story'}, 'longmen'),
    'tacticsJobs': (nes_tactics.JOBS, {'zh': '龍門戰記・江湖百業', 'en': 'Longmen Tactics: the jobs of the jianghu'}, 'sects'),
}


def main():
    path = os.path.join(ROOT, 'chars', 'index.json')
    data = json.load(open(path, encoding='utf-8'))
    ids = nes_tactics.STORY + nes_tactics.JOBS
    entries = {c['id']: c for c in data['characters']}
    order = [c['id'] for c in data['characters']]
    for cid in ids:
        print(cid)
        entries[cid] = EX.export(cid)
        if cid not in order:
            order.append(cid)
    data['characters'] = [entries[c] for c in order]
    gd = os.path.join(ROOT, 'chars', 'tactics')
    os.makedirs(gd, exist_ok=True)
    for gid, (members, name, faction) in GROUPS.items():
        files = {}
        for key, nm, c in (('nes', 'group-nes-' + gid, min(6, len(members))), ('nesTall', 'group-nes-' + gid + '-tall', min(4, len(members)))):
            im = nes_group(members, cols=c)
            im.save(os.path.join(gd, nm + '.png'))
            scale(im, 4).save(os.path.join(gd, nm + '@4x.png'))
            files[key] = 'chars/tactics/' + nm + '.png'
            files[key + '4x'] = 'chars/tactics/' + nm + '@4x.png'
        data['groups'][gid] = {'name': name, 'faction': faction, 'members': members, 'style': 'nes', 'files': files}
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print('index.json:', len(data['characters']), 'characters')


if __name__ == '__main__':
    main()
