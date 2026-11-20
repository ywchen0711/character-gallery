"""Lava Wolf lavawolf - a common foe of Longmen Quest II (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='lavawolf',
    name={'zh': '熔岩狼', 'en': 'Lava Wolf'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '毛色像冷掉的熔岩，一張嘴就吐出熱氣。', 'en': 'Its coat looks like cooled lava; it breathes out hot air.'},
    habitat={'zh': '赤焰窟', 'en': 'The Red Flame Caves'},
    tier=4,
    base='wolf_scar',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('lavawolf')]
