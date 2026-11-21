"""Lint the round-1 `nes2` Longmen art with the gallery's pixel rules (tools/lint.py check_rows):
portraits (the figure before the panel motif; busts are cut by the panel, so edge=True) must have no orphan pixels,
broken or doubled outlines or jaggies; the Famicom fit is proved by nes.Pic.check() inside nes2.fit().
Field sprites follow the rule tools/lint.py uses for 16x16 fields: 1-px props may stay open (broken outline is a
warning), and 2-row black shoes / black-filled cloth and hair are allowed to touch the outline (doubled = warning).

    python -P tools/lint_nes2.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import lint  # noqa: E402
import nes2  # noqa: E402
import nes2_longmen as P  # noqa: E402
import nes2_longmen_sprites as SP  # noqa: E402


def main():
    errors = 0
    for cid in P.BUSTS:
        c = P.build(cid)
        for m in lint.check_rows(c.rows(), lines=c.line_mask(), edge=True, accent=set('rywkpvSsz')):
            print('%-10s portrait %s' % (cid, m))
            errors += m.startswith('ERROR')
        P.portrait(cid)                       # raises if the Famicom rules fail
        lost = [n for n in nes2.NOTES if n.startswith(cid + '/')]
        print('%-10s portrait famicom ok, %d pixels recoloured to fit' % (cid, len(lost)))
        nes2.NOTES.clear()
    names = ['front', 'front2', 'side', 'side2', 'back', 'back2']
    for cid in SP.SPRITES:
        SP.frames(cid)                        # raises if a sprite layer has more than 3 colours
        for n, rows in zip(names, SP.views(cid)):
            for m in lint.check_rows(rows, accent=set('rywkpeSbhdgwqcH')):
                if 'lone' in m or 'info' in m:
                    continue
                if 'broken' in m or 'doubled' in m:
                    m = m.replace('ERROR', 'warn')
                print('%-10s %-6s %s' % (cid, n, m))
                errors += m.startswith('ERROR')
    print('%d errors' % errors)
    return errors


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
