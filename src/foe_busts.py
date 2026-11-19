"""The common foes (小怪) as 霸王之路-style busts: 48x56 pictures on the black NES panel, like the generals.

People and the undead are head-and-shoulders busts (the generals' chest and robe shapes, hand-typed heads and
faces, iconic gear); animals, bugs and spirits are head-and-forequarters close-ups in the same clean shape
language. Everything is drawn with the mondraw helper (shapes on pixel centres, mirrored fronts, one light from
the top-left, a traced 1-px outline), heads and details are stamped by hand afterwards.

Slot letters (each foe maps them to NES colours in nes_foes_art.COLOURS, so palette swaps keep every detail):
  a b d   main material light / mid / dark        e f g   second material        h   third (paper hair)
  S s     skin and skin shadow                    w       white accents (fangs, glints, bowstrings)
  n o     props on the sprite layer (clubs, staves, bows, hilts)
  r y     small accents (eyes, beads, talismans)  k       black: outline, brows, mouths
nes_foes_art.py splits each picture into the background layer and a sprite overlay (mondraw.famicom) after
autofit() has made every 16x16 area fit the Famicom palette rule at slot level, the same for every swap.
The drawing is deterministic (no randomness, ties broken by sorting), so re-exports are stable.

    BUSTS[name] = dict(fn, mirrored, open_slots)      build(name) -> a finished mondraw Canvas
"""
import mondraw
from mondraw import Canvas, Mat, flat

W, H = 48, 56
BUSTS = {}


def bust(name, mirrored=True, open_slots=''):
    def deco(fn):
        BUSTS[name] = dict(fn=fn, mirrored=mirrored, open_slots=open_slots)
        return fn
    return deco


def build(name):
    c = Canvas(W, H)
    BUSTS[name]['fn'](c)
    return c


def T(text):
    return [ln.strip() for ln in text.strip('\n').split('\n') if ln.strip()]


def put(c, text, x0, y0, mirror=False, part=None, half=False):
    """Hand pixels (after finish()): '.' keeps, '_' clears, letters paint. mirror=True also paints the mirror pixel.
    half=True checks the rows are 24 wide (a left half)."""
    rows_ = T(text) if isinstance(text, str) else text
    if half:
        for i, r in enumerate(rows_):
            if len(r) != 24:
                raise ValueError('half row %d is %d wide: %s' % (i, len(r), r))
    for dy, r in enumerate(rows_):
        for dx, ch in enumerate(r):
            if ch == '.':
                continue
            for x in ([x0 + dx, c.w - 1 - (x0 + dx)] if mirror else [x0 + dx]):
                y = y0 + dy
                if not (0 <= x < c.w and 0 <= y < c.h):
                    continue
                if ch == '_':
                    c.clear(x, y)
                    continue
                p = c.part[y][x]
                if p < 0 or p == 10 ** 6:
                    p = part if part is not None else 999
                c.part[y][x] = p
                c.tone[y][x] = ch
                c.locked.add((x, y))


def head(c, text, y0=0):
    """A hand-typed left half (24 wide), mirrored."""
    put(c, text, 0, y0, mirror=True, half=True)


def shade_rows(c, mapping, band=3, x0=24, y0=0, y1=None, stops='.k'):
    """Right-side contour shading on the canvas tones: a tone in mapping becomes its shadow when one of the next
    `band` pixels to the right is backdrop or outline."""
    y1 = c.h if y1 is None else y1
    rows_ = c.rows()
    for y in range(y0, y1):
        r = rows_[y]
        for x in range(x0, c.w):
            ch = r[x]
            if ch in mapping and any(x + d >= c.w or r[x + d] in stops for d in range(1, band + 1)):
                c.tone[y][x] = mapping[ch]


def body(c, plate, pauld, scarf=None, cape=None, dots='d', neck_slot='s', wide=0, dy=0, neck=(19, 28),
         finish=True, robe=False):
    """The generals' shared chest: cape behind, torso plate (or a robe), round two-layer pauldrons, scarf at the neck."""
    P = {}
    Y = lambda v: v + dy
    if cape:
        P['cape'] = c.new_part()
        c.poly2([(24, Y(37)), (12, Y(37)), (0, Y(42)), (0, 56), (24, 56)], cape, P['cape'])
    P['torso'] = c.new_part()
    if robe:
        c.poly2([(24, Y(38)), (16, Y(38)), (7, Y(41)), (2, Y(45)), (0, Y(50)), (0, 56), (24, 56)], plate, P['torso'])
        c.reshade(P['torso'], 14, Y(44), 16, 14, plate, dw=2, hi=0.9)
        P['pa1'] = P['pa2'] = -5
    else:
        c.poly2([(24, Y(39)), (16, Y(39)), (8 - wide, Y(42)), (4 - wide, Y(47)), (3 - wide, 56), (24, 56)], plate, P['torso'])
        c.reshade(P['torso'], 16, Y(44), 14, 14, plate, dw=1, hi=0.9)
        P['pa2'] = c.new_part()
        c.ellipse2(7.5 - wide, Y(50.5), 7.5, 5.5, pauld, P['pa2'])
        P['pa1'] = c.new_part()
        c.ellipse2(8.5 - wide, Y(46.5), 8, 5.5, pauld, P['pa1'])
    P['neck'] = c.new_part()
    c.rect(neck[0], 28, neck[1], Y(40), flat(neck_slot), P['neck'], shade='flat')
    if scarf:
        P['scarf'] = c.new_part()
        c.ellipse(24, Y(40.5), 9, 2.6, scarf, P['scarf'])
    if finish:
        c.finish()
    if dots:
        c.pattern(P['torso'], """
......
.%s....
......
....%s.
""" % (dots, dots), ox=0, oy=0, margin=1)
    return P


FAMILY = ['abd', 'efg', 'hij', 'SsH', 'mno', 'w', 'r', 'y']


def autofit(rows_, spr, near=None, maxiter=40):
    """Slot-level fitting (the same for every palette swap): while some 16x16 area holds more than 3 background
    slots, or all areas cannot share 4 three-slot palettes, recolour the rarest slot of the busiest area to a
    slot of its family (near: extra slot -> preferred replacements). Returns (rows, notes)."""
    near = near or {}
    rows_ = [list(r) for r in rows_]
    h, w = len(rows_), len(rows_[0])
    notes = []
    for _ in range(maxiter):
        areas = []
        for ay in range(0, h, 16):
            for ax in range(0, w, 16):
                cnt = {}
                for y in range(ay, min(ay + 16, h)):
                    for x in range(ax, ax + 16):
                        ch = rows_[y][x]
                        if ch not in '.k' and ch not in spr:
                            cnt[ch] = cnt.get(ch, 0) + 1
                areas.append(((ax, ay), cnt))
        if all(len(c) <= 3 for _, c in areas) and mondraw.cover([set(c) for _, c in areas]) is not None:
            break
        busy = sorted(areas, key=lambda a: (-len(a[1]), a[0][1], a[0][0]))
        (ax, ay), cnt = busy[0]
        if len(cnt) <= 3:
            # palettes do not cover: merge in the area whose set is shared least
            sets = [frozenset(c) for _, c in areas if c]
            (ax, ay), cnt = min((a for a in areas if len(a[1]) >= 2), key=lambda a: (sum(1 for s in sets if s >= frozenset(a[1])), sum(a[1].values()), a[0][1], a[0][0]))
        rare = sorted(cnt, key=lambda s: (cnt[s], s))
        done = False
        for s in rare:
            fam = next((f for f in FAMILY if s in f), s)
            cands = [t for t in near.get(s, '') if t in cnt] + [t for t in fam if t != s and t in cnt]
            if cands:
                t = cands[0]
                for y in range(ay, min(ay + 16, h)):
                    for x in range(ax, ax + 16):
                        if rows_[y][x] == s:
                            rows_[y][x] = t
                notes.append('%d,%d %s->%s x%d' % (ax, ay, s, t, cnt[s]))
                done = True
                break
        if not done:
            notes.append('stuck at %d,%d %s' % (ax, ay, cnt))
            break
    return [''.join(r) for r in rows_], notes


def centre_fix(c, light_map=None, x0=16, x1=32, y0=32, y1=48, sx0=10, sx1=38):
    """The chest attribute area under the chin holds skin shadow + two body tones only: chin / neck skin in shadow,
    body light tones pushed to mid (as the generals do)."""
    light_map = {'a': 'b'} if light_map is None else light_map
    for y in range(y0, y1):
        for x in range(sx0, sx1):
            t = c.tone[y][x]
            if t == 'S':
                c.tone[y][x] = 's'
            elif t in light_map and x0 <= x < x1:
                c.tone[y][x] = light_map[t]


import foe_busts_people  # noqa: E402,F401  (registers the designs)
import foe_busts_animals  # noqa: E402,F401
