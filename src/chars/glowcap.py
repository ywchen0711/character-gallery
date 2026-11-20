"""Glowcap glowcap - a common foe of Longmen Quest II (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='glowcap',
    name={'zh': '熒光菇', 'en': 'Glowcap'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '在洞穴深處發光的菇妖，孢子讓人昏昏欲睡。', 'en': 'A mushroom imp that glows deep in caves; its spores make you drowsy.'},
    habitat={'zh': '碧波洞與南疆的濕地', 'en': 'Green Wave Cave and the southern wetlands'},
    tier=3,
    base='mushroom',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('glowcap')]
