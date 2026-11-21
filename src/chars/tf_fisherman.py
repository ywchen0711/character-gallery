"""漁夫 Fisherman - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_fisherman',
    name={'zh': '漁夫', 'en': 'Fisherman'},
    style_name={'zh': '打魚的', 'en': 'Fisherman'},
    title={'zh': '打魚的', 'en': 'Fisherman'},
    bio={'zh': '青頭巾、青衣，扛著釣竿的漁夫，最懂河裡的動靜。', 'en': 'A fisherman in a teal headband and teal clothes with a rod on his shoulder; he knows every stir of the river.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_fisherman')]
