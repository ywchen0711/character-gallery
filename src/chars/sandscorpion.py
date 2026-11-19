"""Sand Scorpion sandscorpion - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='sandscorpion',
    name={'zh': '沙蠍', 'en': 'Sand Scorpion'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '躲在沙裡只露出尾鉤的蠍子。', 'en': 'A scorpion that hides in the sand with only its stinger showing.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='scorpion',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('sandscorpion')]
