"""Tiny palette-indexed pixel library.

Every picture is authored as text grids: one character = one pixel, '.' or ' ' =
transparent. Grids are stamped onto a Layer (a 2-D array of characters) at an
offset, then the finished Layer is turned into an image through a palette that
maps each character to a colour. Characters are semantic slots (skin, hair,
robe ...), so one drawing can be re-coloured per character.
"""
from PIL import Image

CLEAR = '.'


def G(text):
    """Parse a text grid. Leading/trailing blank lines are dropped; a line may
    start with '|' to protect leading spaces (the '|' is removed)."""
    rows = []
    for ln in text.split('\n'):
        s = ln.rstrip()
        if not s.strip():
            continue
        s = s.strip()
        if s.startswith('|'):
            s = s[1:]
        rows.append(s.replace(' ', CLEAR))
    return rows


def hex2rgba(h):
    h = h.lstrip('#')
    if len(h) == 6:
        h += 'ff'
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4, 6))


class Layer:
    def __init__(self, w, h, fill=CLEAR):
        self.w, self.h = w, h
        self.px = [[fill] * w for _ in range(h)]

    def copy(self):
        L = Layer(self.w, self.h)
        L.px = [r[:] for r in self.px]
        return L

    def get(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            return self.px[y][x]
        return CLEAR

    def set(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[y][x] = c

    def stamp(self, rows, ox=0, oy=0, flip=False, only=None, under=False, remap=None):
        """Stamp a grid. flip mirrors it horizontally. only=set of target chars it may
        overwrite. under=True paints only where the target is clear. remap maps chars."""
        for y, r in enumerate(rows):
            n = len(r)
            for x, c in enumerate(r):
                if c == CLEAR or c == ' ':
                    continue
                if remap and c in remap:
                    c = remap[c]
                tx = ox + (n - 1 - x if flip else x)
                ty = oy + y
                if not (0 <= tx < self.w and 0 <= ty < self.h):
                    continue
                cur = self.px[ty][tx]
                if under and cur != CLEAR:
                    continue
                if only is not None and cur not in only:
                    continue
                self.px[ty][tx] = c
        return self

    def outline(self, c='k', diag=False, skip=()):
        """Draw an outline of char c on clear pixels touching the silhouette."""
        add = []
        for y in range(self.h):
            for x in range(self.w):
                if self.px[y][x] != CLEAR:
                    continue
                nb = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                if diag:
                    nb += [(1, 1), (-1, 1), (1, -1), (-1, -1)]
                for dx, dy in nb:
                    v = self.get(x + dx, y + dy)
                    if v != CLEAR and v != c and v not in skip:
                        add.append((x, y))
                        break
        for x, y in add:
            self.px[y][x] = c
        return self

    def shift(self, dx, dy):
        L = Layer(self.w, self.h)
        for y in range(self.h):
            for x in range(self.w):
                c = self.px[y][x]
                if c != CLEAR:
                    L.set(x + dx, y + dy, c)
        return L

    def rows(self):
        return [''.join(r) for r in self.px]

    def image(self, pal, bg=None):
        im = Image.new('RGBA', (self.w, self.h), (0, 0, 0, 0))
        P = im.load()
        cache = {k: hex2rgba(v) for k, v in pal.items()}
        for y in range(self.h):
            for x in range(self.w):
                c = self.px[y][x]
                if c == CLEAR:
                    if bg is not None:
                        P[x, y] = bg(x, y)
                    continue
                if c not in cache:
                    raise KeyError('no colour for %r at %d,%d' % (c, x, y))
                P[x, y] = cache[c]
        return im


def scale(im, k):
    return im.resize((im.width * k, im.height * k), Image.NEAREST)


def count_colours(im):
    return len({p for p in im.getdata() if p[3] > 0})


def strands(rows, base='x', hi='X', period=4, drift=0.5, phase=0, keep_hi=True):
    """Give hair/beard flowing strands: re-tone the base char so highlight lines run
    diagonally (drift = columns per row). Hand-placed outline/dark chars are kept."""
    out = []
    for y, r in enumerate(rows):
        s = list(r)
        for x, c in enumerate(s):
            if c == base or (c == hi and not keep_hi):
                k = int(x + y * drift + phase) % period
                s[x] = hi if k == 0 else base
        out.append(''.join(s))
    return out


def retone(rows, mapping):
    return [''.join(mapping.get(c, c) for c in r) for r in rows]


def bezier_pts(p0, p1, p2, n=200):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y, t))
    return pts


def stroke(L, p0, p1, p2=None, width=lambda t: 1, tone=lambda t, side: 'x', outline='k'):
    """Paint a (curved) stroke: for props like feathers, bow limbs and shafts.
    width(t) is the half-width in pixels; tone(t, side) picks the char where side
    is -1..1 across the stroke (left edge to right edge)."""
    if p2 is None:
        p2 = p1
        p1 = ((p0[0] + p2[0]) / 2, (p0[1] + p2[1]) / 2)
    pts = bezier_pts(p0, p1, p2)
    painted = {}
    for i, (x, y, t) in enumerate(pts):
        j = min(i + 1, len(pts) - 1)
        dx, dy = pts[j][0] - pts[max(0, i - 1)][0], pts[j][1] - pts[max(0, i - 1)][1]
        ln = (dx * dx + dy * dy) ** 0.5 or 1
        nx, ny = -dy / ln, dx / ln
        w = width(t)
        steps = max(1, int(w * 4))
        for k in range(-steps, steps + 1):
            o = k / steps * w
            px, py = round(x + nx * o), round(y + ny * o)
            side = o / w if w else 0
            if (px, py) not in painted or abs(side) < abs(painted[(px, py)][1]):
                painted[(px, py)] = (t, side)
    for (px, py), (t, side) in painted.items():
        L.set(px, py, tone(t, side))
    if outline:
        add = []
        for (px, py) in painted:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (px + dx, py + dy)
                if q not in painted and L.get(*q) == CLEAR:
                    add.append(q)
        for q in add:
            L.set(q[0], q[1], outline)
    return L


def rot90(rows, cw=True):
    """Rotate a grid by 90 degrees (lossless)."""
    h, w = len(rows), max(len(r) for r in rows)
    rows = [r.ljust(w, CLEAR) for r in rows]
    if cw:
        return [''.join(rows[h - 1 - r][c] for r in range(h)) for c in range(w)]
    return [''.join(rows[r][w - 1 - c] for r in range(h)) for c in range(w)]


def flipv(rows):
    return list(reversed(rows))


def fliph(rows):
    w = max(len(r) for r in rows)
    return [r.ljust(w, CLEAR)[::-1] for r in rows]


def RLE(text, width=None):
    """Run-length rows: each line is tokens like '4. 2k 3S' (count + char); a token
    without a number counts 1. Checks every row against width when given."""
    rows = []
    for ln in text.strip().split('\n'):
        ln = ln.strip()
        if not ln:
            continue
        out = ''
        for tok in ln.split():
            n = ''.join(ch for ch in tok[:-1] if ch.isdigit())
            out += tok[-1] * (int(n) if n else 1)
        if width is not None and len(out) != width:
            raise ValueError('RLE row %d is %d wide, want %d: %s' % (len(rows), len(out), width, ln))
        rows.append(out)
    return rows
