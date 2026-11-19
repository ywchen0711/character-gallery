"""冷笑天 Leng Xiaotian - the Tyrant Dragon: silver hair, gold horns, black-and-gold robe, crimson cape. Drawn in the 8-bit `nes` style only (src/nes_longmen.py)."""

FACTION = 'longmen'
META = dict(
    id='xiaotian',
    name={'zh': '冷笑天', 'en': 'Leng Xiaotian'},
    style_name={'zh': '暴龍', 'en': 'Tyrant Dragon'},
    title={'zh': '暴龍崖之主', 'en': 'Master of Tyrant Dragon Cliff'},
    bio={'zh': '江湖人稱「暴龍」。銀髮金角，黑金龍鱗袍外披猩紅披風，嘴角總掛著一絲冷笑。不用兵器，只用一雙手掌；出手之前，總要先冷笑三聲。', 'en': 'Known on the rivers and lakes as the Tyrant Dragon. Silver hair and golden horns, a black robe worked with gold scales under a crimson cape, and a sneer at one corner of his mouth. He carries no weapon but his palms, and before he strikes he always laughs three cold laughs.'},
    weapon={'zh': '雙掌', 'en': 'Bare palms'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('xiaotian')]
