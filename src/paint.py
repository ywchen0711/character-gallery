"""Soft 'painterly' shading for the HD-2D style.

Shapes are still hand-authored grids; each authored char maps to (material, tone).
soften() then blends tones only between neighbours of the same material, giving
smooth hue-shifted ramps without blurring edges between materials (skin vs hair).
"""
from PIL import Image
from pixlib import hex2rgba


class Soft:
    def __init__(self, w, h, ramps):
        self.w, self.h, self.ramps = w, h, ramps
        self.m = [[None] * w for _ in range(h)]   # material name or None
        self.t = [[0.0] * w for _ in range(h)]    # tone index (float)
        self.fixed = {}                           # (x, y) -> hex colour painted after softening

    def put(self, x, y, mat, tone):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.m[y][x] = mat
            self.t[y][x] = float(tone)

    def get(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            return self.m[y][x]
        return None

    def stamp(self, rows, ox, oy, key, scale=1):
        """key: char -> (material, tone) or None to skip; '.' always skips."""
        for y, r in enumerate(rows):
            for x, c in enumerate(r):
                if c == '.' or c not in key or key[c] is None:
                    continue
                mat, tone = key[c]
                for dy in range(scale):
                    for dx in range(scale):
                        self.put(ox + x * scale + dx, oy + y * scale + dy, mat, tone)

    def soften(self, passes=2, mats=None, weight=2.0):
        for _ in range(passes):
            nt = [row[:] for row in self.t]
            for y in range(self.h):
                for x in range(self.w):
                    m = self.m[y][x]
                    if m is None or (mats and m not in mats) or m == 'line':
                        continue
                    tot, n = self.t[y][x] * weight, weight
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        if self.get(x + dx, y + dy) == m:
                            tot += self.t[y + dy][x + dx]
                            n += 1
                    nt[y][x] = tot / n
            self.t = nt

    def paint(self, x, y, colour):
        self.fixed[(x, y)] = colour

    def image(self, bg=None):
        im = Image.new('RGBA', (self.w, self.h), (0, 0, 0, 0))
        P = im.load()
        cache = {k: [hex2rgba(c) for c in v] for k, v in self.ramps.items()}
        for y in range(self.h):
            for x in range(self.w):
                m = self.m[y][x]
                if m is None:
                    if bg:
                        P[x, y] = bg(x, y)
                    continue
                ramp = cache[m]
                i = max(0, min(len(ramp) - 1, int(round(self.t[y][x]))))
                P[x, y] = ramp[i]
        for (x, y), c in self.fixed.items():
            if 0 <= x < self.w and 0 <= y < self.h:
                P[x, y] = hex2rgba(c)
        return im
