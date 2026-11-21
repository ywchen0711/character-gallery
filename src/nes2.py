"""Helpers for the `nes2` style: the Longmen cast redrawn to the 霸王之路 (src/nes_sango.py) quality bar.

A portrait is 48x56 on the black NES panel. It is drawn on a mondraw Canvas in slot letters:
  body, robe, cape and props with mondraw shapes (clean stepped outlines, one light from the top-left, three
  tones per material), the head stamped by hand as a 24-wide left half that is mirrored, then the hair, the face
  (tiny dark eyes, no whites) and every asymmetric detail stamped on top, then right-side contour shading.
fit() maps the slots to NES colours, merges slots that share a colour, splits the picture into the background layer
and a sprite overlay with mondraw.famicom() and returns an nes.Pic that check() proves legal.

Slot letters used by every nes2 drawing (each character maps them to NES colours):
  k black line / '.' panel     S s t  skin light / shadow / deep        h i j  hair light / mid / dark
  a b d  main cloth             e f g  second cloth (collar, sash)       m n o  third (cape, trim)
  p q    props (wood, metal)    v w    silver / white                    y r    gold / red accents
  z Z    the panel backdrop motif (drawn after linting, behind the figure)
"""
import mondraw
import nes
from mondraw import Canvas, Mat, flat  # noqa: F401

W, H = 48, 56


def T(text):
    return [ln.strip() for ln in text.strip('\n').split('\n') if ln.strip()]


def put(c, text, x0, y0, mirror=False, half=False):
    """Hand pixels: '.' keeps, '_' clears, letters paint (locked). mirror=True also paints the mirror pixel."""
    rows = T(text) if isinstance(text, str) else text
    for dy, r in enumerate(rows):
        if half and len(r) != 24:
            raise ValueError('half row %d is %d wide: %s' % (dy, len(r), r))
        for dx, ch in enumerate(r):
            if ch == '.':
                continue
            xs = [x0 + dx, c.w - 1 - (x0 + dx)] if mirror else [x0 + dx]
            for x in xs:
                y = y0 + dy
                if not (0 <= x < c.w and 0 <= y < c.h):
                    continue
                if ch == '_':
                    c.clear(x, y)
                    continue
                p = c.part[y][x]
                if p < 0 or p == 10 ** 6:
                    p = 999
                c.part[y][x] = p
                c.tone[y][x] = ch
                c.locked.add((x, y))


def half(c, text, y0=0):
    """A hand-typed left half (rows of 24), mirrored onto the right."""
    put(c, text, 0, y0, mirror=True, half=True)


def shade_right(c, mapping, band=3, x0=24, y0=0, y1=None, stops='.k'):
    """Contour shading on the shadow side: a tone in mapping becomes its shadow when one of the next `band`
    pixels to the right is panel or line."""
    y1 = c.h if y1 is None else y1
    rows = c.rows()
    for y in range(y0, y1):
        r = rows[y]
        for x in range(x0, c.w):
            ch = r[x]
            if ch in mapping and any(x + d >= c.w or r[x + d] in stops for d in range(1, band + 1)):
                c.tone[y][x] = mapping[ch]


def shade_under(c, mapping, band=1, x0=0, x1=None, y0=0, y1=None, stops='k'):
    """Shadow under a form: a tone becomes its shadow when one of the next `band` pixels below is a line."""
    x1 = c.w if x1 is None else x1
    y1 = c.h if y1 is None else y1
    rows = c.rows()
    for y in range(y0, y1):
        for x in range(x0, x1):
            ch = rows[y][x]
            if ch in mapping and any(y + d < c.h and rows[y + d][x] in stops for d in range(1, band + 1)):
                c.tone[y][x] = mapping[ch]


def recolour(c, mapping, x0=0, y0=0, x1=None, y1=None, cond=None):
    x1 = c.w if x1 is None else x1
    y1 = c.h if y1 is None else y1
    for y in range(y0, y1):
        for x in range(x0, x1):
            t = c.tone[y][x]
            if t in mapping and (cond is None or cond(x, y)):
                c.tone[y][x] = mapping[t]


def _areas(rows, size):
    h, w = len(rows), len(rows[0])
    for ay in range(0, h, size):
        for ax in range(0, w, size):
            yield ax, ay, [(x, y) for y in range(ay, min(ay + size, h)) for x in range(ax, min(ax + size, w))]


def _best_groups(counts, maxg=4):
    """counts: list of {slot: pixels} per area. Choose up to maxg 3-slot groups that leave the fewest pixels
    uncovered (each area uses its best group). Greedy pick, then swap-improve."""
    from itertools import combinations
    slots = sorted({s for c in counts for s in c})
    cands = set()
    for cnt in counts:
        top = sorted(cnt, key=lambda s: (-cnt[s], s))[:5]
        for k in (3, 2, 1):
            for comb in combinations(top, min(k, len(top))):
                base = frozenset(comb)
                if len(base) == 3:
                    cands.add(base)
                else:
                    for extra in combinations([s for s in slots if s not in base], 3 - len(base)):
                        cands.add(base | frozenset(extra))
    if not cands:
        return [], 0
    cands = sorted(cands, key=lambda g: sorted(g))

    def cost(groups):
        tot = 0
        for cnt in counts:
            n = sum(cnt.values())
            tot += min(n - sum(v for s, v in cnt.items() if s in g) for g in groups) if groups else n
        return tot

    groups = []
    for _ in range(maxg):
        best = min(cands, key=lambda g: (cost(groups + [g]), sorted(g)))
        groups.append(best)
        if cost(groups) == 0:
            break
    improved = True
    while improved:
        improved = False
        for i in range(len(groups)):
            cur = cost(groups)
            for g in cands:
                trial = groups[:i] + [g] + groups[i + 1:]
                if cost(trial) < cur:
                    groups, cur, improved = trial, cost(trial), True
    return groups, cost(groups)


def split(rows, spr, near, name='nes2'):
    """Background layer + sprite overlay for slot rows: the slots in `spr` always go to sprites; every 16x16 area
    takes its best background group (at most 4 groups of 3); pixels the group lacks go to the sprite layer, or,
    when a sprite tile would need a 4th colour or a scanline more than 8 tiles, become their `near` slot."""
    h, w = len(rows), len(rows[0])
    bg = [list(r) for r in rows]
    sp = [['.'] * w for _ in range(h)]
    sp_back = {}
    for y in range(h):
        for x in range(w):
            if bg[y][x] in spr:
                sp[y][x], bg[y][x] = bg[y][x], 'k'
    areas = list(_areas(rows, 16))
    counts = []
    for ax, ay, px in areas:
        cnt = {}
        for x, y in px:
            if bg[y][x] not in '.k':
                cnt[bg[y][x]] = cnt.get(bg[y][x], 0) + 1
        counts.append(cnt)
    groups, _ = _best_groups(counts)
    for (ax, ay, px), cnt in zip(areas, counts):
        if not cnt:
            continue
        g = max(groups, key=lambda g: (sum(v for s, v in cnt.items() if s in g), sorted(g)))
        for x, y in px:
            s = bg[y][x]
            if s not in '.k' and s not in g:
                sp[y][x], bg[y][x] = s, 'k'
                # remember the area group so an evicted pixel can fall back to a near slot it holds
                sp_back[(x, y)] = g
    # sprite tiles: at most 3 colours each, 4 sprite groups, 8 tiles per row of tiles
    for _ in range(60):
        tiles = []
        for tx, ty, px in _areas(rows, 8):
            cnt = {}
            for x, y in px:
                if sp[y][x] != '.':
                    cnt[sp[y][x]] = cnt.get(sp[y][x], 0) + 1
            tiles.append((tx, ty, px, cnt))
        per_row = {}
        for tx, ty, px, cnt in tiles:
            if cnt:
                per_row[ty] = per_row.get(ty, 0) + 1
        sg = mondraw.cover([set(t[3]) for t in tiles if t[3]]) if all(len(t[3]) <= 3 for t in tiles) else None
        if sg is not None and (not per_row or max(per_row.values()) <= 8):
            break
        # fix the worst tile: drop its rarest evicted slot back to a near background slot
        bad = [t for t in tiles if len(t[3]) > 3]
        if not bad and per_row and max(per_row.values()) > 8:
            ty = max(per_row, key=lambda k: per_row[k])
            bad = sorted([t for t in tiles if t[1] == ty and t[3]], key=lambda t: sum(t[3].values()))
        if not bad:
            bad = sorted([t for t in tiles if t[3]], key=lambda t: (-len(t[3]), sum(t[3].values())))
        tx, ty, px, cnt = bad[0]
        cand = sorted([s for s in cnt if s not in spr], key=lambda s: (cnt[s], s))
        if not cand:
            raise ValueError('%s: sprite tile %d,%d cannot be simplified: %s' % (name, tx, ty, cnt))
        s = cand[0]
        for x, y in px:
            if sp[y][x] == s:
                g = sp_back.get((x, y), ())
                rep = next((r for r in near.get(s, '') if r in g), None)
                if rep is None:
                    nb = [bg[y + dy][x + dx] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                          if 0 <= x + dx < w and 0 <= y + dy < h and bg[y + dy][x + dx] in g]
                    rep = max(sorted(set(nb)), key=nb.count) if nb else None
                sp[y][x] = '.'
                bg[y][x] = rep or 'k'
                NOTES.append('%s: %s at %d,%d -> %s' % (name, s, x, y, rep or 'k'))
    else:
        raise ValueError('%s: could not fit the sprite layer' % name)
    return [''.join(r) for r in bg], [''.join(r) for r in sp], [tuple(sorted(g)) for g in groups], sg


NOTES = []


def raw_image(rows, colours):
    from PIL import Image
    im = Image.new('RGBA', (len(rows[0]), len(rows)), nes.rgba(0x0F))
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch not in '.k':
                im.putpixel((x, y), nes.rgba(colours[ch]))
    return im


def fit(rows, colours, spr='', name='nes2', backdrop_rows=None, near=None):
    """Slot rows -> a legal nes.Pic. colours: slot -> NES index. spr: slots that always go on the sprite layer.
    backdrop_rows: optional panel motif rows (slots z/Z, '.' elsewhere) laid under the figure's empty pixels."""
    if backdrop_rows:
        rows = [''.join(b if a == '.' else a for a, b in zip(r, br)) for r, br in zip(rows, backdrop_rows)]
    # one slot per NES colour (two letters with the same colour would waste palette room)
    canon = {}
    keep_spr = set(spr)
    for s, v in sorted(colours.items()):
        if s not in keep_spr:
            canon.setdefault(v, s)
    m = {s: canon.get(v, s) for s, v in colours.items()}
    rows2 = []
    for r in rows:
        out = []
        for ch in r:
            if ch in '.k':
                out.append(ch)
            elif ch in keep_spr:
                out.append(ch)
            else:
                if ch not in m:
                    raise ValueError('%s: no colour for slot %r' % (name, ch))
                out.append(m[ch] if colours[ch] != 0x0F else 'k')
        rows2.append(''.join(out))
    near2 = {m.get(a, a): ''.join(m.get(b, b) for b in v) for a, v in (near or {}).items()}
    bg, sp, g, sg = split(rows2, spr, near2, name)
    slots = {s: colours[s] for s in set(''.join(bg)) - set('.k')}
    sslots = {s: colours[s] for s in set(''.join(sp)) - set('.')}
    pal = [tuple(colours[s] for s in grp) for grp in g]
    spal = [tuple(colours[s] for s in grp) for grp in sg]
    pic = nes.Pic(bg, slots, pal, sp, sslots, spal, name=name)
    pic.check()
    return pic


def sprite(rows, pal, pal2):
    return nes.sprite_image(rows, pal, pal2)


def G(text, h=24):
    rows = [ln.strip() for ln in text.strip('\n').split('\n') if ln.strip()]
    rows = ['.' * 16] * (h - len(rows)) + rows
    for r in rows:
        if len(r) != 16:
            raise ValueError('sprite row is %d wide: %s' % (len(r), r))
    if len(rows) != h:
        raise ValueError('sprite has %d rows' % len(rows))
    return rows


def mirror_rows(rows):
    """A left-facing frame from a right-facing one (or back)."""
    return [r[::-1] for r in rows]
