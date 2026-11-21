"""Re-export only the given characters and merge them into chars/index.json (other characters untouched; variants a
character's variants() does not produce, e.g. ones written by another tool, are kept).

    python -P tools/export_ids.py jasper yishuo ...
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))

import export as EX  # noqa: E402


def main(ids):
    path = os.path.join(ROOT, 'chars', 'index.json')
    data = json.load(open(path, encoding='utf-8'))
    out = []
    for c in data['characters']:
        if c['id'] in ids:
            keep = {v['style']: v for v in c['variants']}
            n = EX.export(c['id'])
            made = {v['style'] for v in n['variants']}
            n['variants'] += [v for s, v in keep.items() if s not in made]
            c = n
        out.append(c)
    data['characters'] = out
    json.dump(data, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('re-exported', ' '.join(ids))


if __name__ == '__main__':
    main(sys.argv[1:])
