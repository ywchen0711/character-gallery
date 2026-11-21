"""舞孃 Dancer - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_dancer',
    name={'zh': '舞孃', 'en': 'Dancer'},
    style_name={'zh': '戲班子', 'en': 'Troupe dancer'},
    title={'zh': '戲班子', 'en': 'Troupe dancer'},
    bio={'zh': '雙髻粉紅衣的舞孃，戲班子到哪裡，她就跳到哪裡。', 'en': 'A dancer with two buns and a pink gown who dances wherever the troupe stops.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_dancer')]
