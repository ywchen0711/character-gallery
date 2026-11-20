"""阿蠻 A-Man - Miao girl. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='aman',
    name={'zh': '阿蠻', 'en': 'A-Man'},
    style_name={'zh': '聽獸語的姑娘', 'en': 'The Girl Who Talks to Beasts'},
    title={'zh': '苗女', 'en': 'Miao girl'},
    bio={'zh': '青竹寨的苗家姑娘，從小跟狼一起長大，聽得懂妖物說話，卻不太會說人話。', 'en': 'A Miao girl of Green Bamboo village who grew up among wolves. She understands creatures, but hardly speaks the human tongue.'},
    weapon={'zh': '骨哨', 'en': 'Bone whistle'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('aman')]
