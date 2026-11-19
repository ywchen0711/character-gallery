"""The family style as a gallery variant, plus the group picture of all four."""
import math
from PIL import Image
from variants import Variant
import family_members as fm
import family_portraits as fp
import family_sprites as fs


class FamilyVariant(Variant):
    style = 'family'
    primary = True
    fps = {'idle': 3, 'walk_down': 7, 'walk_up': 7, 'walk_left': 7, 'walk_right': 7, 'action': 6}
    loop = {'action': False}
    anchor = (fs.CXS, fs.BASE)
    notes = {'idle': 'all four share the 40x60 cell and the y=57 baseline, so heights compare directly',
             'walk_right': 'mirror of walk_left', 'action': 'signature move'}

    def __init__(self, name):
        self.name = name

    def portrait(self):
        return getattr(fp, self.name)()

    def frames(self):
        m = getattr(fm, self.name)()
        return fs.animations(m, getattr(fm, self.name + '_action'))


def group(scene=False):
    """All four standing together, kids between their parents: 128x72."""
    W, H = 128, 72
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    if scene:
        P = im.load()
        for y in range(H):
            for x in range(W):
                t = y / H
                c = [46 + 70 * t, 52 + 50 * t, 66 + 8 * t]
                for (lx, ly, lr, col) in ((14, 12, 12, (250, 210, 140)), (110, 10, 10, (255, 236, 180)),
                                          (64, 4, 9, (240, 190, 120)), (100, 40, 12, (230, 150, 90))):
                    d = math.hypot(x - lx, y - ly)
                    if d < lr:
                        k = 0.45 * (1 - (d / lr) ** 2)
                        c = [c[i] + (col[i] - c[i]) * k for i in range(3)]
                if y >= 62:
                    c = [96 - (y - 62) * 3, 82 - (y - 62) * 3, 60 - (y - 62) * 2]
                P[x, y] = tuple(int(v) // 4 * 4 for v in c) + (255,)
    order = [('jeff', 8), ('josh', 34), ('jasper', 58), ('erin', 84)]
    for name, x in order:
        spr = fs.frame(getattr(fm, name)())
        im.alpha_composite(spr, (x, H - fs.FH - 3))
    return im
