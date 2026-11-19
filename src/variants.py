"""A variant = one character drawn in one style. Every variant gives:
  portrait()  -> PIL image
  frames()    -> dict animation name -> list of PIL images (all the same size)
  fps         -> dict animation name -> frames per second
  anchor      -> (x, y) of the feet inside a frame
  notes       -> optional dict animation name -> note
"""
import chibi
import portrait as koei_portrait


class Variant:
    style = None
    fps = {}
    loop = {}
    anchor = (0, 0)
    notes = {}
    primary = False

    def portrait(self):
        raise NotImplementedError

    def frames(self):
        raise NotImplementedError


class KoeiVariant(Variant):
    """霸王の大陸-style portrait + pixel-baseball chibi, built from a character namespace
    with PAL/FACE/FRONT... (portrait) and CPAL/CHIBI (chibi)."""
    style = 'koei'
    fps = {'idle': 3, 'walk': 8, 'walk_side': 8, 'action': 8}
    loop = {'action': False}
    anchor = (28, 62)
    notes = {'walk_side': 'faces right; mirror horizontally for left'}

    def __init__(self, ns, full=True, primary=False):
        self.ns, self.full, self.primary = ns, full, primary

    def portrait(self):
        return koei_portrait.render(self.ns)

    def frames(self):
        if self.full:
            fr = chibi.frames(self.ns)
        else:
            fr = {'idle': [chibi.front(self.ns, 0, 0), chibi.front(self.ns, 0, 1)]}
        return {k: [f.image(self.ns.CPAL) for f in v] for k, v in fr.items()}
