"""Lava Scorpion lavascorpion - a common foe of Longmen Quest II (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='lavascorpion',
    name={'zh': '火蠍', 'en': 'Lava Scorpion'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '赤焰窟裡的紅蠍，尾針燒得發亮。', 'en': 'A red scorpion of the Red Flame Caves; its sting glows.'},
    habitat={'zh': '赤焰窟', 'en': 'The Red Flame Caves'},
    tier=4,
    base='scorpion',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('lavascorpion')]
