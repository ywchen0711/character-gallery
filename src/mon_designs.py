"""Monster designs drawn with mondraw: one function per base design, returning a finished Canvas.

Slot letters (each foe / beast maps them to NES colours, see nes_foes_art.py and nes_beasts_art.py):
  a b d   main material: light, mid, dark
  e f g   second material: light, mid, dark
  h i j   third material: light, mid, dark
  w       white / pale accent        r y   sprite-layer accents (eyes, glints)
  k       black (outline, mouths, pupils)
"""
from mondraw import Canvas, Mat, flat

BODY = Mat('a', 'b', 'd')
BODY2 = Mat('e', 'f', 'g')
BODY3 = Mat('h', 'i', 'j')
DARKB = Mat('b', 'd', 'd')          # the far limbs: in shadow
DARK2 = Mat('f', 'g', 'g')

DESIGNS = {}


def design(name, w, h, mirrored=False, open_slots=''):
    def deco(fn):
        DESIGNS[name] = dict(fn=fn, w=w, h=h, mirrored=mirrored, open_slots=open_slots)
        return fn
    return deco


def build(name):
    d = DESIGNS[name]
    c = Canvas(d['w'], d['h'])
    d['fn'](c)
    return c


WHITE = flat('w')

import mon_h  # noqa: E402,F401  (registers the designs)
import mon_h2  # noqa: E402,F401
import mon_a1  # noqa: E402,F401
import mon_a2  # noqa: E402,F401
import mon_a3  # noqa: E402,F401
import mon_b  # noqa: E402,F401
import mon_var  # noqa: E402,F401  (stronger-kin variants of the bases)
