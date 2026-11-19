"""Paper Effigy papereffigy - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='papereffigy',
    name={'zh': '紙人', 'en': 'Paper Effigy'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '出殯用的紙紮人，畫上眼睛以後自己站了起來。', 'en': 'A paper funeral effigy that stood up by itself once its eyes were painted on.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='paperghost',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('papereffigy')]
