"""女冠 Daoist nun - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_nun',
    name={'zh': '女冠', 'en': 'Daoist nun'},
    style_name={'zh': '出家人', 'en': 'Nun'},
    title={'zh': '出家人', 'en': 'Nun'},
    bio={'zh': '長髮淡藍袍的女冠，在路邊替人解籤。', 'en': 'A long-haired Daoist nun in pale blue who reads fortune sticks by the road.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_nun')]
