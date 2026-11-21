"""小孩 Child - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_child',
    name={'zh': '小孩', 'en': 'Child'},
    style_name={'zh': '鎮上的孩子', 'en': 'Town child'},
    title={'zh': '鎮上的孩子', 'en': 'Town child'},
    bio={'zh': '綁著小髻、臉頰紅紅的孩子，到處跟著俠客跑。', 'en': 'A rosy-cheeked child with a little topknot who follows every hero around town.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_child')]
