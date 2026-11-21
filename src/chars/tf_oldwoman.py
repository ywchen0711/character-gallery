"""老婆婆 Old woman - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_oldwoman',
    name={'zh': '老婆婆', 'en': 'Old woman'},
    style_name={'zh': '長者', 'en': 'Elder'},
    title={'zh': '長者', 'en': 'Elder'},
    bio={'zh': '灰髻黑衣、拄杖慢慢走的老婆婆，最會說天快要下雨。', 'en': 'A grey-haired grandmother in black with a cane, always the first to say rain is coming.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_oldwoman')]
