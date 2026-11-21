"""鎮上的男子 Townsman - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_man',
    name={'zh': '鎮上的男子', 'en': 'Townsman'},
    style_name={'zh': '布衣百姓', 'en': 'Commoner'},
    title={'zh': '布衣百姓', 'en': 'Commoner'},
    bio={'zh': '戴髮髻、穿土黃布衣的鎮上男子，見了誰都先笑三分。', 'en': 'A townsman with a topknot and a khaki cotton robe who smiles at everyone first.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_man')]
