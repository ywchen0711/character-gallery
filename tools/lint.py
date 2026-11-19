"""Pixel-art lint for the monster pictures (src/mon_designs.py): flags the things that make pixel art look crooked.

    python -P tools/lint.py            lint every design, one line per problem, exit 1 if any error
    python -P tools/lint.py wolf bat   only these

Errors (must be fixed): orphan pixels (an opaque pixel with no opaque neighbour), broken outline (a filled pixel
touching the transparent outside without a black edge), doubled outline (a 2x2 black block on the silhouette),
jaggies (a run in a stepped outline that breaks the 1-2-3 / 3-2-1 progression by 2 or more, e.g. 3-1-3 or 1-3-1).
Warnings: lone tone pixels (a shading pixel with no same-tone neighbour), asymmetry counts in mirrored designs.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))

ACCENT = set('rywkp')      # eyes, glints and black details may be single pixels
DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def _trace(mask, w, h):
    """Moore-neighbour trace of the outer boundary of the largest blob; returns the list of moves (0-7)."""
    start = None
    for y in range(h):
        for x in range(w):
            if mask[y][x]:
                start = (x, y)
                break
        if start:
            break
    if not start:
        return []
    moves = []
    pts = []
    cur, back = start, 4         # we came from the left (west)
    for _ in range(w * h * 4):
        found = False
        for k in range(1, 9):
            d = (back + k) % 8
            nx, ny = cur[0] + DIRS[d][0], cur[1] + DIRS[d][1]
            if 0 <= nx < w and 0 <= ny < h and mask[ny][nx]:
                moves.append(d)
                pts.append((nx, ny))
                cur = (nx, ny)
                back = (d + 4) % 8
                found = True
                break
        if not found or (cur == start and len(moves) > 2):
            break
    _trace.pts = pts
    return moves


def jaggies(moves):
    """Count jaggy spots: split the chain code into stretches made of two moves 45 degrees apart and look at the
    run lengths of the dominant move; a run that is a local peak or dip by 2 or more is a jaggy."""
    jaggies.where = []
    if not moves:
        return 0
    runs = []
    pts = getattr(_trace, 'pts', [])
    for i, m in enumerate(moves):
        if runs and runs[-1][0] == m:
            runs[-1][1] += 1
        else:
            runs.append([m, 1, pts[i] if i < len(pts) else None])
    bad = 0
    i = 0
    while i < len(runs):
        pair = {runs[i][0]}
        j = i
        while j < len(runs) and (runs[j][0] in pair or (len(pair) == 1 and (runs[j][0] - runs[i][0]) % 8 in (1, 7))):
            pair.add(runs[j][0])
            j += 1
        seg = runs[i:j]
        if len(pair) == 2 and len(seg) >= 5:
            a, b = list(pair)
            ca = sum(r[1] for r in seg if r[0] == a)
            cb = sum(r[1] for r in seg if r[0] == b)
            major = a if ca >= cb else b
            mr = [r for r in seg if r[0] == major][1:-1]       # first and last runs are partial
            rl = [r[1] for r in mr]
            for k in range(2, len(rl) - 2):            # runs next to a junction may legitimately jump
                d1, d2 = rl[k] - rl[k - 1], rl[k] - rl[k + 1]
                if d1 * d2 > 0 and max(abs(d1), abs(d2)) >= 2:
                    bad += 1
                    jaggies.where.append(mr[k][2])
        i = max(j - 1, i + 1)
    return bad


def check_rows(rows, mirrored=False, accent=ACCENT, lines=None, open_slots=''):
    h, w = len(rows), len(rows[0])
    op = [[c != '.' for c in r] for r in rows]
    msgs = []

    def at(x, y):
        return rows[y][x] if 0 <= x < w and 0 <= y < h else '.'

    orphans, broken, lone = [], [], []
    for y in range(h):
        for x in range(w):
            c = rows[y][x]
            if c == '.':
                continue
            n8 = [at(x + dx, y + dy) for dx, dy in DIRS]
            if all(n == '.' for n in n8):
                orphans.append((x, y))
            if c != 'k' and c not in open_slots and any(at(x + dx, y + dy) == '.' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                broken.append((x, y))
            if c not in accent and c not in n8:
                lone.append((x, y))
    doubled = []
    for y in range(h - 1):
        for x in range(w - 1):
            blk = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            if all(rows[b][a] == 'k' and (lines is None or (a, b) in lines) for a, b in blk):
                if any(at(a + dx, b + dy) == '.' for a, b in blk for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    doubled.append((x, y))
    jg = jaggies(_trace(op, w, h))
    if orphans:
        msgs.append('ERROR orphan pixels %s' % orphans[:6])
    if broken:
        msgs.append('ERROR broken outline %s' % broken[:6])
    if doubled:
        msgs.append('ERROR doubled outline at %s' % doubled[:6])
    if jg:
        msgs.append('ERROR %d jaggies in the silhouette near %s' % (jg, jaggies.where[:4]))
    if lone:
        msgs.append('warn %d lone tone pixels %s' % (len(lone), lone[:5]))
    if mirrored:
        diff = sum(1 for y in range(h) for x in range(w // 2) if op[y][x] != op[y][w - 1 - x])
        msgs.append('info %d silhouette pixels differ from the mirror' % diff)
    return msgs


def main(names):
    import mon_designs as M
    names = names or list(M.DESIGNS)
    errors = 0
    for n in names:
        c = M.build(n)
        for m in check_rows(c.rows(), M.DESIGNS[n]['mirrored'], lines=c.line_mask(), open_slots=M.DESIGNS[n]['open_slots']):
            print('%-14s %s' % (n, m))
            errors += m.startswith('ERROR')
    # the 16x16 field sprites: 1-px limbs may stay open at this size, so broken outlines are only warnings
    import nes_foes_art as FA
    import nes_beasts_art as BA
    fields = [(b, [t.strip('\n').split('\n') for t in v[2]]) for b, v in FA.BASES.items()]
    fields += [(c, d['move']) for c, d in BA.SPRITES.items() if c in BA.FIELD_MODE]
    for n, frames in fields:
        for i, rows in enumerate(frames):
            for m in check_rows(rows, accent=set('rywkpeS')):
                if 'lone' in m or 'info' in m:
                    continue
                if 'broken' in m:
                    m = m.replace('ERROR', 'warn')
                print('%-14s field %d %s' % (n, i + 1, m))
                errors += m.startswith('ERROR')
    print('%d designs, %d errors' % (len(names), errors))
    return errors


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:]) else 0)
