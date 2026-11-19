"""A small drawing helper for clean 8-bit monster art (used by nes_foes_art.py and nes_beasts_art.py).

A Canvas holds, per pixel, a part id (or -1 for empty) and a tone slot letter. Shapes are rasterised on pixel
centres, so a shape centred on the canvas middle comes out exactly symmetric; every shape is shaded by one light
from the top-left (sphere shading for ellipses and limbs, edge shading for polygons) into three tones per material:
light, mid and dark slots. finish() then
  * draws a 1-px separation line where a front part covers a part behind it (part.sep),
  * removes lone shading pixels (no same-tone neighbour) so the clusters stay clean,
  * traces a 1-px black outline ('k') around the whole silhouette using 4-neighbours (no doubled corners).
rows() returns the picture as rows of slot letters ('.' empty), the format nes.Pic takes.

Every tie (the most common neighbour tone, the order of colour groups) is broken by sorting, so a picture comes out
the same on every run whatever Python's string-hash seed is.

Designs that face the viewer are drawn on the left half (or across the middle) and mirrored with mirror();
deliberate asymmetric details (a weapon, a tilted tail) are drawn after the mirror.
"""
import math

L = (-0.48, -0.58, 0.66)
_n = math.sqrt(sum(v * v for v in L))
L = tuple(v / _n for v in L)


class Mat:
    """A material: its light, mid and dark slot letters (any may repeat), and the sphere-shading thresholds."""

    def __init__(self, light, mid, dark, hi=0.93, lo=0.34):
        self.light, self.mid, self.dark, self.hi, self.lo = light, mid, dark, hi, lo

    def tone(self, i):
        return self.light if i > self.hi else self.dark if i < self.lo else self.mid


def flat(slot):
    return Mat(slot, slot, slot)


class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.part = [[-1] * w for _ in range(h)]
        self.tone = [['.'] * w for _ in range(h)]
        self.parts = []        # per part id: dict(sep=..., z=...)
        self.locked = set()    # pixels painted by hand (shading cleanup leaves them alone)
        self.lines = set()     # separation-line pixels (thin() may give them back to the fill)

    # ---------------------------------------------------------------- parts and pixels
    def new_part(self, sep=True, sepslot='k'):
        self.parts.append(dict(sep=sep, sepslot=sepslot))
        return len(self.parts) - 1

    def _put(self, x, y, part, slot):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.part[y][x] = part
            self.tone[y][x] = slot

    def inside(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h and self.part[y][x] >= 0

    # ---------------------------------------------------------------- shapes
    def ellipse(self, cx, cy, rx, ry, mat, part=None, clip=None, light=None):
        """Ellipse centred on (cx, cy) in pixel-edge coordinates (cx=w/2 is the exact middle)."""
        part = self.new_part() if part is None else part
        for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
            for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
                nx, ny = (x + 0.5 - cx) / rx, (y + 0.5 - cy) / ry
                d = nx * nx + ny * ny
                if d <= 1.0 and (clip is None or clip(x, y)):
                    nz = math.sqrt(max(0.0, 1 - d))
                    i = nx * L[0] + ny * L[1] + nz * L[2]
                    self._put(x, y, part, mat.tone(i if light is None else light))
        return part

    def capsule(self, x0, y0, x1, y1, r, mat, part=None, r1=None):
        """A limb: every pixel within r of the segment (r tapers to r1 at the far end)."""
        part = self.new_part() if part is None else part
        r1 = r if r1 is None else r1
        dx, dy = x1 - x0, y1 - y0
        ll = dx * dx + dy * dy or 1e-9
        m = max(r, r1) + 1
        for y in range(int(min(y0, y1) - m), int(max(y0, y1) + m) + 1):
            for x in range(int(min(x0, x1) - m), int(max(x0, x1) + m) + 1):
                px, py = x + 0.5, y + 0.5
                t = max(0.0, min(1.0, ((px - x0) * dx + (py - y0) * dy) / ll))
                rr = r + (r1 - r) * t
                qx, qy = px - (x0 + dx * t), py - (y0 + dy * t)
                d = math.hypot(qx, qy)
                if d <= rr:
                    nx, ny = qx / rr, qy / rr
                    nz = math.sqrt(max(0.0, 1 - nx * nx - ny * ny))
                    self._put(x, y, part, mat.tone(nx * L[0] + ny * L[1] + nz * L[2]))
        return part

    def poly(self, pts, mat, part=None, shade='edge', dw=1, lw=1):
        """A filled polygon (pixel-edge coordinates), edge-shaded: dark band down-right, light band up-left."""
        part = self.new_part() if part is None else part
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        cells = set()
        for y in range(int(min(ys)) - 1, int(max(ys)) + 2):
            for x in range(int(min(xs)) - 1, int(max(xs)) + 2):
                if _in_poly(x + 0.5, y + 0.5, pts):
                    cells.add((x, y))
        self._edge_shade(cells, part, mat, dw, lw, shade)
        return part

    def rect(self, x0, y0, x1, y1, mat, part=None, shade='edge', dw=1, lw=1):
        """Inclusive pixel rectangle."""
        part = self.new_part() if part is None else part
        cells = {(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)}
        self._edge_shade(cells, part, mat, dw, lw, shade)
        return part

    def _edge_shade(self, cells, part, mat, dw, lw, shade):
        for (x, y) in cells:
            if shade == 'flat':
                s = mat.mid
            else:
                dark = any((x + k, y + k) not in cells or (x + k, y) not in cells or (x, y + k) not in cells
                           for k in range(1, dw + 1))
                light = any((x - k, y - k) not in cells or (x - k, y) not in cells or (x, y - k) not in cells
                            for k in range(1, lw + 1))
                s = mat.dark if dark else mat.light if light else mat.mid
            self._put(x, y, part, s)

    def reshade(self, part, cx, cy, rx, ry, mat, dw=2, hi=None):
        """Shade every pixel of a part (built from several shapes) as one form: a dark band dw pixels wide along
        the bottom / right edges of the part, a highlight where the ellipsoid (cx, cy, rx, ry) faces the light."""
        hi = mat.hi if hi is None else hi
        cells = {(x, y) for y in range(self.h) for x in range(self.w) if self.part[y][x] == part}
        for (x, y) in cells:
            if (x, y) in self.locked:
                continue
            dark = any((x + k, y + k) not in cells or (x, y + k) not in cells or (x + k, y) not in cells and k == 1
                       for k in range(1, dw + 1))
            nx, ny = (x + 0.5 - cx) / rx, (y + 0.5 - cy) / ry
            d = nx * nx + ny * ny
            i = nx * L[0] + ny * L[1] + math.sqrt(max(0.0, 1 - d)) * L[2] if d < 1 else -1
            self.tone[y][x] = mat.dark if dark else mat.light if i > hi else mat.mid

    def paint(self, x, y, slot, part=None, lock=True):
        """Set one pixel's tone (and part, if given; otherwise it must already be filled or a part is made)."""
        if not (0 <= x < self.w and 0 <= y < self.h):
            return
        if part is None:
            part = self.part[y][x] if self.part[y][x] >= 0 else self.new_part(sep=False)
        self.part[y][x] = part
        self.tone[y][x] = slot
        if lock:
            self.locked.add((x, y))

    def stamp(self, x0, y0, text, part=None, mirror=False):
        """Hand-typed pixels: rows of slot letters, '.' keeps what is there, ' ' too, '_' clears to empty."""
        rows = [r for r in text.strip('\n').split('\n')]
        rows = [r.strip() if r.strip() else r for r in rows]
        for dy, r in enumerate(rows):
            for dx, c in enumerate(r):
                for x in ([x0 + dx, self.w - 1 - (x0 + dx)] if mirror else [x0 + dx]):
                    y = y0 + dy
                    if c in '. ':
                        continue
                    if c == '_':
                        if 0 <= x < self.w and 0 <= y < self.h:
                            self.part[y][x] = -1
                            self.tone[y][x] = '.'
                        continue
                    self.paint(x, y, c, part)

    def cut(self, pts, m=False):
        """Clear every pixel inside a polygon (notches, gaps between fingers); m=True also cuts the mirror."""
        for P in ([pts, [(self.w - x, y) for x, y in pts]] if m else [pts]):
            xs = [p[0] for p in P]
            ys = [p[1] for p in P]
            for y in range(int(min(ys)) - 1, int(max(ys)) + 2):
                for x in range(int(min(xs)) - 1, int(max(xs)) + 2):
                    if _in_poly(x + 0.5, y + 0.5, P):
                        self.clear(x, y)

    def clear(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.part[y][x] = -1
            self.tone[y][x] = '.'

    # ---------------------------------------------------------------- mirrored pairs (exact: pixel centres mirror)
    def ellipse2(self, cx, cy, rx, ry, mat, part=None, **kw):
        part = self.ellipse(cx, cy, rx, ry, mat, part, **kw)
        self.ellipse(self.w - cx, cy, rx, ry, mat, part, **kw)
        return part

    def capsule2(self, x0, y0, x1, y1, r, mat, part=None, **kw):
        part = self.capsule(x0, y0, x1, y1, r, mat, part, **kw)
        self.capsule(self.w - x0, y0, self.w - x1, y1, r, mat, part, **kw)
        return part

    def poly2(self, pts, mat, part=None, **kw):
        part = self.poly(pts, mat, part, **kw)
        self.poly([(self.w - x, y) for x, y in pts], mat, part, **kw)
        return part

    def paint2(self, x, y, slot, part=None):
        self.paint(x, y, slot, part)
        self.paint(self.w - 1 - x, y, slot, part)

    # ---------------------------------------------------------------- symmetry
    def mirror(self, left=True):
        """Copy the left half onto the right half (or the right onto the left)."""
        w = self.w
        for y in range(self.h):
            for x in range(w // 2):
                sx, dx = (x, w - 1 - x) if left else (w - 1 - x, x)
                self.part[y][dx] = self.part[y][sx]
                self.tone[y][dx] = self.tone[y][sx]
                if (sx, y) in self.locked:
                    self.locked.add((dx, y))
        return self

    # ---------------------------------------------------------------- finishing
    def finish(self, outline='k', clean=True, sep=True, mirror_tones=None):
        w, h = self.w, self.h
        # separation lines: a pixel of an earlier (behind) part next to a later (front) part becomes the line
        if sep:
            marks = []
            for y in range(h):
                for x in range(w):
                    p = self.part[y][x]
                    if p < 0:
                        continue
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        q = self.part[y + dy][x + dx] if 0 <= x + dx < w and 0 <= y + dy < h else -1
                        if q > p and self.parts[q]['sep'] and self.tone[y][x] != 'k':
                            marks.append((x, y, self.parts[q]['sepslot']))
                            break
            for x, y, s in marks:
                if (x, y) not in self.locked:
                    self.tone[y][x] = s
                    self.lines.add((x, y))
        if clean:
            self.clean_tones()
        if outline:
            ring = []
            for y in range(h):
                for x in range(w):
                    if self.part[y][x] >= 0:
                        continue
                    if any(self.inside(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                        ring.append((x, y))
            for x, y in ring:
                self.part[y][x] = 10 ** 6
                self.tone[y][x] = outline
            self.close_gaps(outline)
            self.thin()
        return self

    def close_gaps(self, outline='k'):
        """A 2-pixel gap between two parts would get a 2x2 block of outline; fill one pixel of it instead."""
        w, h, O = self.w, self.h, 10 ** 6
        for _ in range(20):
            fixed = False
            for y in range(h - 1):
                for x in range(w - 1):
                    blk = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
                    if not all(self.part[b][a] == O for a, b in blk):
                        continue
                    best = None
                    for a, b in blk:
                        nb = [(a + dx, b + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                              if 0 <= a + dx < w and 0 <= b + dy < h and 0 <= self.part[b + dy][a + dx] < O]
                        if nb and (best is None or len(nb) > len(best[1])):
                            best = ((a, b), nb)
                    if not best:
                        continue
                    (a, b), nb = best
                    p, q = nb[0]
                    self.part[b][a] = self.part[q][p]
                    self.tone[b][a] = self.tone[q][p] if self.tone[q][p] != 'k' else 'k'
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        u, v = a + dx, b + dy
                        if 0 <= u < w and 0 <= v < h and self.part[v][u] < 0:
                            self.part[v][u] = O
                            self.tone[v][u] = outline
                    fixed = True
            if not fixed:
                break

    def thin(self):
        """Where black pixels form a 2x2 block (an outline meeting a separation line), give the inner ones back
        to the fill so every line stays one pixel wide."""
        w, h = self.w, self.h
        for _ in range(3):
            changed = False
            for y in range(h - 1):
                for x in range(w - 1):
                    blk = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
                    if not all(self.tone[b][a] == 'k' for a, b in blk):
                        continue
                    for a, b in blk:
                        if (a, b) in self.locked or (a, b) not in self.lines:
                            continue
                        n4 = [(a + dx, b + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                        if any(not (0 <= p < w and 0 <= q < h) or self.part[q][p] < 0 for p, q in n4):
                            continue
                        fills = [self.tone[q][p] for p, q in n4 if self.tone[q][p] not in '.k']
                        if fills:
                            self.tone[b][a] = max(sorted(set(fills)), key=fills.count)
                            src = next((p, q) for p, q in n4 if self.tone[q][p] == self.tone[b][a])
                            self.part[b][a] = self.part[src[1]][src[0]]
                            changed = True
                            break
            if not changed:
                break

    def tube(self, pts, r, mat, part=None, r1=None):
        """A smooth tube along a polyline (coils, tails), shaded from the nearest point of the whole centre line,
        its radius tapering from r to r1."""
        part = self.new_part() if part is None else part
        r1 = r if r1 is None else r1
        n = len(pts) - 1
        lens = [math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(n)]
        tot = sum(lens) or 1
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        m = max(r, r1) + 1
        for y in range(int(min(ys) - m), int(max(ys) + m) + 1):
            for x in range(int(min(xs) - m), int(max(xs) + m) + 1):
                px, py = x + 0.5, y + 0.5
                best = None
                acc = 0
                for i in range(n):
                    (x0, y0), (x1, y1) = pts[i], pts[i + 1]
                    dx, dy = x1 - x0, y1 - y0
                    ll = dx * dx + dy * dy or 1e-9
                    t = max(0.0, min(1.0, ((px - x0) * dx + (py - y0) * dy) / ll))
                    qx, qy = px - (x0 + dx * t), py - (y0 + dy * t)
                    d = math.hypot(qx, qy)
                    if best is None or d < best[0]:
                        best = (d, qx, qy, (acc + lens[i] * t) / tot)
                    acc += lens[i]
                d, qx, qy, s = best
                rr = r + (r1 - r) * s
                if d <= rr:
                    nx, ny = qx / rr, qy / rr
                    nz = math.sqrt(max(0.0, 1 - nx * nx - ny * ny))
                    self._put(x, y, part, mat.tone(nx * L[0] + ny * L[1] + nz * L[2]))
        return part

    def clean_tones(self, passes=2):
        """Lone shading pixels (no 4-neighbour of the same tone) take the most common neighbouring tone."""
        w, h = self.w, self.h
        for _ in range(passes):
            changes = []
            for y in range(h):
                for x in range(w):
                    t = self.tone[y][x]
                    if t in '.k' or (x, y) in self.locked:
                        continue
                    nb = [self.tone[y + dy][x + dx] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                          if 0 <= x + dx < w and 0 <= y + dy < h and self.part[y + dy][x + dx] == self.part[y][x]]
                    if not nb or t in nb:
                        continue
                    best = max(sorted(set(nb)), key=nb.count)
                    changes.append((x, y, best))
            for x, y, b in changes:
                self.tone[y][x] = b

    def line_mask(self):
        """Pixels that are outline or separation lines (not black areas drawn on purpose)."""
        ring = {(x, y) for y in range(self.h) for x in range(self.w) if self.part[y][x] == 10 ** 6}
        return ring | {p for p in self.lines if self.tone[p[1]][p[0]] == 'k'}

    # ---------------------------------------------------------------- finishing details (after finish())
    def cells(self, part):
        return [(x, y) for y in range(self.h) for x in range(self.w) if self.part[y][x] == part]

    def rim(self, part, slot, only=None, side='ul'):
        """Rim light: pixels of a part that touch the outline on the lit side (up / left) take `slot`.
        only: the tones that may be replaced (default: any but black)."""
        O = 10 ** 6
        dirs = {'ul': ((0, -1), (-1, 0)), 'u': ((0, -1),), 'l': ((-1, 0),), 'dr': ((0, 1), (1, 0))}[side]
        for (x, y) in self.cells(part):
            t = self.tone[y][x]
            if t == 'k' or (x, y) in self.locked or (only and t not in only):
                continue
            if any(0 <= x + dx < self.w and 0 <= y + dy < self.h and self.part[y + dy][x + dx] == O
                   for dx, dy in dirs):
                self.tone[y][x] = slot

    def pattern(self, part, tile, ox=0, oy=0, only=None, margin=1):
        """Tile a small hand-typed pattern over a part ('.' keeps the pixel). Pixels within `margin` of the
        part's edge and black pixels are left alone, so the texture sits in clean clusters inside the form."""
        rows = [r for r in tile.strip('\n').split('\n')]
        th, tw = len(rows), len(rows[0])
        mine = set(self.cells(part))
        for (x, y) in mine:
            t = self.tone[y][x]
            if t == 'k' or (x, y) in self.locked or (only and t not in only):
                continue
            if margin and any((x + dx, y + dy) not in mine for dx in range(-margin, margin + 1)
                              for dy in range(-margin, margin + 1)):
                continue
            c = rows[(y - oy) % th][(x - ox) % tw]
            if c != '.':
                self.tone[y][x] = c

    def put(self, pts, slot, part=None):
        """Paint a list of pixels (only where something is drawn, unless part is given)."""
        for (x, y) in pts:
            if part is not None or (0 <= x < self.w and 0 <= y < self.h and 0 <= self.part[y][x] < 10 ** 6):
                self.paint(x, y, slot, part)

    def put2(self, pts, slot, part=None):
        self.put(pts, slot, part)
        self.put([(self.w - 1 - x, y) for x, y in pts], slot, part)

    def rows(self):
        return [''.join(r) for r in self.tone]


def _in_poly(x, y, pts):
    inside = False
    n = len(pts)
    j = n - 1
    for i in range(n):
        xi, yi = pts[i]
        xj, yj = pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside


# ---------------------------------------------------------------- Famicom fitting
def fit(rows, groups, sprite_slots=(), near=None):
    """Split slot rows into background rows + sprite-overlay rows that obey the Famicom attribute rule.

    groups: up to 4 tuples of slot letters (the background sub-palettes, in slots). sprite_slots: slots that
    always go to the sprite layer (eyes, a glint). near: slot -> replacement slot used when an attribute area
    cannot hold a slot (the fit then reports it). Returns (bg_rows, sprite_rows, problems)."""
    near = near or {}
    h, w = len(rows), len(rows[0])
    bg = [list(r) for r in rows]
    sp = [['.'] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if bg[y][x] in sprite_slots:
                sp[y][x] = bg[y][x]
                bg[y][x] = 'k'          # under a sprite pixel the background is just black
    problems = []
    for ay in range(0, h, 16):
        for ax in range(0, w, 16):
            cnt = {}
            for y in range(ay, min(ay + 16, h)):
                for x in range(ax, min(ax + 16, w)):
                    c = bg[y][x]
                    if c not in '.k':
                        cnt[c] = cnt.get(c, 0) + 1
            if not cnt:
                continue
            best = max(groups, key=lambda g: (sum(n for c, n in cnt.items() if c in g), -len(g)))
            bad = {c: n for c, n in cnt.items() if c not in best}
            if bad:
                for y in range(ay, min(ay + 16, h)):
                    for x in range(ax, min(ax + 16, w)):
                        c = bg[y][x]
                        if c in bad:
                            r = near.get(c, {})
                            r = r if isinstance(r, str) else ''
                            rep = next((s for s in r if s in best), None)
                            bg[y][x] = rep or 'k'
                problems.append('area %d,%d: %s not in %s' % (ax, ay, ' '.join('%s%d' % kv for kv in bad.items()),
                                                               ''.join(best)))
    return [''.join(r) for r in bg], [''.join(r) for r in sp], problems


def cover(sets, maxg=4, size=3):
    """The fewest groups of at most `size` slots (at most maxg groups) such that every set is inside one group.
    Returns a list of tuples, or None when it cannot be done."""
    sets = [frozenset(s) for s in sets if s]
    sets = sorted({s for s in sets if not any(s < t for t in sets)}, key=lambda s: (-len(s), sorted(s)))
    if any(len(s) > size for s in sets):
        return None
    universe = sorted(set().union(*sets)) if sets else []
    from itertools import combinations

    def cands(s):
        extra = [u for u in universe if u not in s]
        out = []
        for k in range(size - len(s), -1, -1):
            for ex in combinations(extra, k):
                out.append(frozenset(s) | frozenset(ex))
        return out

    def solve(groups, n):
        left = [s for s in sets if not any(s <= g for g in groups)]
        if not left:
            return groups
        if n == 0:
            return None
        for g in cands(left[0]):
            r = solve(groups + [g], n - 1)
            if r is not None:
                return r
        return None

    for n in range(1, maxg + 1):
        r = solve([], n)
        if r is not None:
            return [tuple(sorted(g)) for g in r]
    return None


def famicom(rows, spr=''):
    """Split slot rows into a background layer and a sprite overlay (the slots in `spr`) and find the
    sub-palettes (in slots) that make every 16x16 background area and every 8x8 sprite tile legal.
    Returns (bg_rows, sprite_rows, bg_groups, sprite_groups); raises ValueError if it cannot be done."""
    h, w = len(rows), len(rows[0])
    bg = [list(r) for r in rows]
    sp = [['.'] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if bg[y][x] in spr:
                sp[y][x] = bg[y][x]
                bg[y][x] = 'k'
    # where an attribute area still holds more than three colours, lift the least-used ones (in that area only)
    # onto the sprite layer, the way Famicom artists overlaid sprites on busy spots
    for ay in range(0, h, 16):
        for ax in range(0, w, 16):
            for _ in range(4):
                cnt = {}
                for y in range(ay, min(ay + 16, h)):
                    for x in range(ax, min(ax + 16, w)):
                        if bg[y][x] not in '.k':
                            cnt[bg[y][x]] = cnt.get(bg[y][x], 0) + 1
                if len(cnt) <= 3:
                    break
                low = min(cnt, key=lambda s: (cnt[s], s))
                for y in range(ay, min(ay + 16, h)):
                    for x in range(ax, min(ax + 16, w)):
                        if bg[y][x] == low:
                            sp[y][x] = low
                            bg[y][x] = 'k'
    areas, tiles = [], []
    for ay in range(0, h, 16):
        for ax in range(0, w, 16):
            areas.append({bg[y][x] for y in range(ay, min(ay + 16, h)) for x in range(ax, min(ax + 16, w))} - set('.k'))
    lines = {}
    for ty in range(0, h, 8):
        for tx in range(0, w, 8):
            t = {sp[y][x] for y in range(ty, min(ty + 8, h)) for x in range(tx, min(tx + 8, w))} - {'.'}
            if t:
                tiles.append(t)
                lines[ty] = lines.get(ty, 0) + 1
    g = cover(areas)
    if g is None:
        bad = [''.join(sorted(a)) for a in areas if len(a) > 3]
        raise ValueError('background areas need too many colours: %s (areas %s)' % (
            bad, [(i % ((w + 15) // 16) * 16, i // ((w + 15) // 16) * 16) for i, a in enumerate(areas) if len(a) > 3]))
    sg = cover(tiles) if tiles else []
    if sg is None:
        raise ValueError('sprite tiles need too many colours: %s' % [''.join(sorted(t)) for t in tiles if len(t) > 3])
    if lines and max(lines.values()) > 8:
        raise ValueError('%d sprite tiles on one row of tiles (max 8)' % max(lines.values()))
    return [''.join(r) for r in bg], [''.join(r) for r in sp], g, sg


class Scaled:
    """Draw old-size geometry on a bigger canvas: every shape call is scaled by s about the canvas centre
    (horizontally) and anchored to the bottom, so mirrored pairs stay exact. Finishing stamps go on the canvas
    itself, in the new coordinates."""

    def __init__(self, c, s, oldw, oldh):
        self.c, self.s = c, s
        self.ox = (c.w - oldw * s) / 2
        self.oy = c.h - oldh * s

    def X(self, x):
        return x * self.s + self.ox

    def Y(self, y):
        return y * self.s + self.oy

    def P(self, pts):
        return [(self.X(x), self.Y(y)) for x, y in pts]

    def _clip(self, kw):
        if kw.get('clip'):
            f = kw['clip']
            kw['clip'] = lambda x, y: f((x - self.ox) / self.s, (y - self.oy) / self.s)
        if 'r1' in kw and kw['r1'] is not None:
            kw['r1'] = kw['r1'] * self.s
        return kw

    def new_part(self, *a, **k):
        return self.c.new_part(*a, **k)

    def ellipse(self, cx, cy, rx, ry, mat, part=None, **kw):
        return self.c.ellipse(self.X(cx), self.Y(cy), rx * self.s, ry * self.s, mat, part, **self._clip(kw))

    def ellipse2(self, cx, cy, rx, ry, mat, part=None, **kw):
        return self.c.ellipse2(self.X(cx), self.Y(cy), rx * self.s, ry * self.s, mat, part, **self._clip(kw))

    def capsule(self, x0, y0, x1, y1, r, mat, part=None, **kw):
        return self.c.capsule(self.X(x0), self.Y(y0), self.X(x1), self.Y(y1), r * self.s, mat, part,
                              **self._clip(kw))

    def capsule2(self, x0, y0, x1, y1, r, mat, part=None, **kw):
        return self.c.capsule2(self.X(x0), self.Y(y0), self.X(x1), self.Y(y1), r * self.s, mat, part,
                               **self._clip(kw))

    def poly(self, pts, mat, part=None, **kw):
        return self.c.poly(self.P(pts), mat, part, **kw)

    def poly2(self, pts, mat, part=None, **kw):
        return self.c.poly2(self.P(pts), mat, part, **kw)

    def rect(self, x0, y0, x1, y1, mat, part=None, **kw):
        return self.c.rect(round(self.X(x0)), round(self.Y(y0)), round(self.X(x1 + 1)) - 1,
                           round(self.Y(y1 + 1)) - 1, mat, part, **kw)

    def tube(self, pts, r, mat, part=None, r1=None):
        return self.c.tube(self.P(pts), r * self.s, mat, part, r1=None if r1 is None else r1 * self.s)

    def cut(self, pts, m=False):
        return self.c.cut(self.P(pts), m)

    def reshade(self, part, cx, cy, rx, ry, mat, **kw):
        return self.c.reshade(part, self.X(cx), self.Y(cy), rx * self.s, ry * self.s, mat, **kw)
