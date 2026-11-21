"""毒師 Poisoner - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_poison',
    name={'zh': '毒師', 'en': 'Poisoner'},
    style_name={'zh': '斷腸', 'en': 'Heartbreak'},
    title={'zh': '用毒的人', 'en': 'A master of poisons'},
    bio={'zh': '紫色兜帽下一雙細眼，腰間的綠葫蘆裡裝的不是藥。懂醫，也懂毒。', 'en': 'Narrow eyes under a purple hood; the green gourd at the waist holds no medicine. Knows healing, and its shadow.'},
    weapon={'zh': '毒葫蘆', 'en': 'Poison gourd'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_poison')]
