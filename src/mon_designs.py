"""Monster designs drawn with mondraw: the nine big beasts (mon_b.py), one function per design, returning a finished
Canvas. (The common foes are 霸王之路-style busts in foe_busts.py.)

Slot letters (each beast maps them to NES colours, see nes_beasts_art.py):
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

import mon_b  # noqa: E402,F401  (registers the designs; the common foes are busts now, see foe_busts.py)
