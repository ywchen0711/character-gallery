"""和尚 Monk - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_monk',
    name={'zh': '和尚', 'en': 'Monk'},
    style_name={'zh': '出家人', 'en': 'Monk'},
    title={'zh': '出家人', 'en': 'Monk'},
    bio={'zh': '光頭、橘色僧衣的小和尚，下山化緣，總是笑瞇瞇的。', 'en': 'A shaven monk in an orange robe, down from the mountain for alms and always smiling.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_monk')]
