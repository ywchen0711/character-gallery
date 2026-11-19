"""Bamboo Viper bambooviper - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='bambooviper',
    name={'zh': '竹葉青', 'en': 'Bamboo Viper'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '藏在竹林裡的小青蛇，綠得跟竹葉分不出來。', 'en': 'A small green snake that hides in bamboo, the same colour as the leaves.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='snake',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bambooviper')]
