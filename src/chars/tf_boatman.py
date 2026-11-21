"""船夫 Boatman - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_boatman',
    name={'zh': '船夫', 'en': 'Boatman'},
    style_name={'zh': '渡口船家', 'en': 'Boatman'},
    title={'zh': '渡口船家', 'en': 'Boatman'},
    bio={'zh': '斗笠、曬黑的手臂和格紋背心，渡口上最快的船就是他的。', 'en': 'A straw hat, sun-browned arms and a checked vest: the fastest boat at the ferry is his.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_boatman')]
