"""乞丐 Beggar - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_beggar',
    name={'zh': '乞丐', 'en': 'Beggar'},
    style_name={'zh': '叫化子', 'en': 'Beggar'},
    title={'zh': '叫化子', 'en': 'Beggar'},
    bio={'zh': '亂髮、補丁衣、捧著破碗的乞丐，江湖消息他最靈通。', 'en': 'A beggar with wild hair, patched clothes and a cracked bowl, the best-informed man in the jianghu.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_beggar')]
