"""Two-frame field animation for monsters from one hand-typed frame (see nes_foes_fields.py).

field_frames(rows, mode) -> (frame 1 rows, frame 2 rows)
  squash  the body drops one pixel over the feet: a blank row goes on top and one leg row is taken out
          (the row in the lower half that best matches the one below it, so the legs just look bent)
  hop     the whole sprite one pixel higher
  float   the whole sprite one pixel lower (fliers bob down between wing beats)
"""


def _blank(r):
    return set(r) <= {'.'}


def field_frames(rows, mode):
    rows = list(rows)
    h, w = len(rows), len(rows[0])
    if mode == 'hop' and not _blank(rows[0]) and _blank(rows[-1]):
        mode = 'float'
    if mode == 'float' and not _blank(rows[-1]) and _blank(rows[0]):
        mode = 'hop'
    if mode == 'hop':
        if not _blank(rows[0]):
            raise ValueError('hop needs an empty top row')
        return rows, rows[1:] + ['.' * w]
    if mode == 'float':
        if not _blank(rows[-1]):
            raise ValueError('float needs an empty bottom row')
        return rows, ['.' * w] + rows[:-1]
    if mode == 'squash':
        filled = [i for i, r in enumerate(rows) if not _blank(r)]
        bottom = filled[-1]
        lo = bottom - 4
        best = None
        for i in range(lo, bottom - 1):
            a, b = rows[i], rows[i + 1]
            diff = sum(1 for x, y in zip(a, b) if x != y)
            if best is None or diff < best[0] or (diff == best[0] and i > best[1]):
                best = (diff, i)
        cut = best[1]
        return rows, ['.' * w] + rows[:cut] + rows[cut + 1:]
    raise ValueError(mode)
