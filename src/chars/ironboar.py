"""Ironbristle Boar ironboar - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='ironboar',
    name={'zh': '鐵鬃豬', 'en': 'Ironbristle Boar'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '背上的鬃毛硬得像鐵釘，刀砍下去會冒火星。', 'en': 'Its back bristles are as hard as iron nails; a blade striking them throws sparks.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='boar',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('ironboar')]
