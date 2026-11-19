"""Second walk frames for the 16x24 `nes` field sprites.

The old sheets made front walk frame 2 by mirroring the whole figure, so every asymmetric part (a saber, headband
ties, a staff, the outline) jumped to the other side each step. Here frame 2 keeps the body pixel-identical to
frame 1 and only the legs change:

  front: the bottom `n` rows (the legs and hem) are reflected inside their own span [x0, x1], so the forward foot
         swaps sides while nothing above the knees moves. Props that reach into those rows (a staff, a ball) are
         kept out of the span.
  side:  frame 1 is the stride; frame 2 is frame 1 with its bottom `n` rows replaced by legs-together rows
         (the passing pose), taken from the character's `side2` drawing or given as `side_legs`.

Games that composite frame 1's body with frame 2's bottom five rows (Longmen Quest) keep working, because
nothing above the bottom five rows ever differs.
"""


def _span(rows):
    xs = [x for r in rows for x, c in enumerate(r) if c != '.']
    return (min(xs), max(xs)) if xs else (0, len(rows[0]) - 1)


def front2(front, n=3, span=None):
    """front frame 2: the bottom n rows reflected inside [x0, x1] (default: their own bounding span)."""
    body, legs = front[:-n], front[-n:]
    x0, x1 = span or _span(legs)
    out = []
    for r in legs:
        seg = r[x0:x1 + 1]
        out.append(r[:x0] + seg[::-1] + r[x1 + 1:])
    return body + out


def side2(side, legs):
    """side frame 2: the stride frame with its bottom rows swapped for legs-together rows."""
    n = len(legs)
    return side[:-n] + list(legs)


def check_same_body(a, b, keep=5):
    """True if a and b differ only in their bottom `keep` rows."""
    return a[:-keep] == b[:-keep]


# Hand-set leg rows for frame 2 where the automatic reflection is not right (props in the leg rows, robes to the
# floor, figures that stand above the bottom row). 'front' / 'side' replace that many bottom rows of frame 1.
LEGS = {
    'erin': dict(front=['....kk...kkk....'],
                 side=['...kccccccck....', '...kcccccccck...', '...kcccccccck...', '...kkkkkkkkkk...', '.....kkkkkk.....']),
    'josh': dict(front=['....kcckcccck...', '....kkk.kkkkk...', '...kkk...kkkk...'],
                 side=['....kccccck.....', '.....kkkkkk.....', '.....kkkkk......']),
    'jasper': dict(front=['....kkk.kkkk....', '...kkk...kkk....'],
                   side=['....kkkkkk......', '....kkkkk.......']),
    'guanyu': dict(front=['..kkkkk.kkkkkkk.', '...kkk....kkkk..']),
    'yishuo': dict(front=['....kcckcccck...', '....kkk.kkkkk.kk', '...kkkk...kkkkSk', '...kkk........kk'],
                   side=['....kccccck.....', '....kkkkkk...kk.', '....kkkkk...kSSk', '.............kkk']),
    'baixian': dict(front=['..kccccckcccccck', '..kkkkkkkkkkkkk.'],
                    side=['...kccccccck....', '...kcccccccck...', '...kcccccccck...', '...kkkkkkkkkk...', '....kkkkkkk.....']),
    'liuhanyan': dict(front=['....kk...kkk....'],
                      side=['...kccccccck....', '...kkkkkkkkk....', '.....kkkkk......']),
    'kuchan': dict(front=['..k...kkk..kkkk.', '..k........kkkk.'],
                   side=['..k.kccccccck...', '..k.kccccccck...', '..k.kkkkkkkkk...', '..k..kkkkkkk....', '..k.............']),
    'heixiong': dict(front=['.....kkkkk.kkkk.', '....kkkkkk......']),
    'shouhou': dict(front=['....kkkk.kkkk...', '....kkk...kkk...', '...kkk..........'],
                    side=['....kcckccck....', '.....kkkkkk.....', '.....kkkkk......', '................', '................']),
    'tuqianqiu': dict(front=['...kkkkk...kkk..'],
                      side=['...kccccccck....', '...kkkkkkkkk....', '.....kkkkk......', '................', '................']),
}


def legs_for(cid, d):
    """(front frame 2 rows, side frame 2 rows) for a sprite dict d (see nes_sprites.SPRITES)."""
    fa, sd = d['front'], d['side']
    L = dict(LEGS.get(cid, {}))
    L.update(d.get('legs', {}))
    f2 = fa[:-len(L['front'])] + L['front'] if 'front' in L else front2(fa)
    s2 = side2(sd, L['side']) if 'side' in L else side2(sd, d['side2'][-5:])
    return f2, s2
