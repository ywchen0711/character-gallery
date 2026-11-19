"""Ink Scorpion inkscorpion - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='inkscorpion',
    name={'zh': '墨蠍', 'en': 'Ink Scorpion'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '漆黑發藍的蠍子，毒一進血就變成墨色。', 'en': 'A blue-black scorpion; its venom turns the blood the colour of ink.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='scorpion',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('inkscorpion')]
