"""女醫 Woman Physician - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_physician_f',
    name={'zh': '女醫', 'en': 'Woman Physician'},
    style_name={'zh': '杏林春暖', 'en': 'Spring in the Apricot Grove'},
    title={'zh': '女郎中', 'en': 'A woman physician'},
    bio={'zh': '青衣高髻的女大夫，藥葫蘆不離身。說話溫和，下針卻又快又準。', 'en': 'A woman doctor in teal with her hair in a high bun, never without her medicine gourd. Gentle words, and needles quick and sure.'},
    weapon={'zh': '藥葫蘆與金針', 'en': 'Medicine gourd and golden needles'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_physician_f')]
