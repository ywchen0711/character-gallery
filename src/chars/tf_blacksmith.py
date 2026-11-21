"""鐵匠 Blacksmith - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_blacksmith',
    name={'zh': '鐵匠', 'en': 'Blacksmith'},
    style_name={'zh': '打鐵的', 'en': 'Smith'},
    title={'zh': '打鐵的', 'en': 'Smith'},
    bio={'zh': '赤膊繫皮圍裙、掄著鐵鎚的鐵匠，鎮上的刀都出自他手。', 'en': 'A bare-armed smith in a leather apron swinging his hammer; every blade in town came from his forge.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_blacksmith')]
