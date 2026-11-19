"""Drowned Ghost drowned - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='drowned',
    name={'zh': '水鬼', 'en': 'Drowned Ghost'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '長髮蓋臉、渾身滴水的水鬼，在渡口抓人的腳。', 'en': 'A dripping ghost with long hair over its face that grabs ankles at the ferry landing.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='drowned',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('drowned')]
