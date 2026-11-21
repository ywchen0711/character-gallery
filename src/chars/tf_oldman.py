"""老翁 Old man - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_oldman',
    name={'zh': '老翁', 'en': 'Old man'},
    style_name={'zh': '長者', 'en': 'Elder'},
    title={'zh': '長者', 'en': 'Elder'},
    bio={'zh': '白髮白鬚、拄著木杖的老人家，龍門鎮的舊事都記在他心裡。', 'en': 'A white-haired, white-bearded old man with a walking stick who remembers every old story of Longmen.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_oldman')]
