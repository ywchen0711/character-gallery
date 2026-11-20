"""Lava Crab lavacrab - a common foe of Longmen Quest II (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='lavacrab',
    name={'zh': '火蟹', 'en': 'Lava Crab'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '在熔岩裡爬的螃蟹，殼燒得通紅，會往人身上噴火。', 'en': 'A crab that crawls in lava, its shell red-hot; it spits fire.'},
    habitat={'zh': '赤焰窟', 'en': 'The Red Flame Caves'},
    tier=4,
    base='crab',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('lavacrab')]
