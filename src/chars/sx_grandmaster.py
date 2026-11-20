"""宗師 Grandmaster - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsPeople'
META = dict(
    id='sx_grandmaster',
    name={'zh': '宗師', 'en': 'Grandmaster'},
    style_name={'zh': '白眉宗師', 'en': 'The White-browed Grandmaster'},
    title={'zh': '一代宗師', 'en': 'A grandmaster of his age'},
    bio={'zh': '白髮白眉、長鬚過胸，藍袍、金頂禪杖。他教過的弟子，後來都開了自己的門派。', 'en': 'White hair and brows, a beard past his chest, a blue robe and a gold-topped staff. Every pupil he taught went on to found a sect.'},
    weapon={'zh': '金頂杖', 'en': 'Gold-topped staff'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_grandmaster')]
