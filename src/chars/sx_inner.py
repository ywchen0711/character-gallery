"""內家高手 Inner-art Adept - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_inner',
    name={'zh': '內家高手', 'en': 'Inner-art Adept'},
    style_name={'zh': '掌心生光', 'en': 'Light in the Palms'},
    title={'zh': '內功深厚的高手', 'en': 'An adept of the inner arts'},
    bio={'zh': '白衣長髮，不帶兵器。運起內功時，掌心泛著淡淡的光。', 'en': 'White robes, long hair, no weapon. When the inner strength rises, a faint light gathers in the palms.'},
    weapon={'zh': '雙掌', 'en': 'Bare palms'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_inner')]
