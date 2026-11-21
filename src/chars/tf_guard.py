"""衙役 Guard - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_guard',
    name={'zh': '衙役', 'en': 'Guard'},
    style_name={'zh': '守衛', 'en': 'Guard'},
    title={'zh': '守衛', 'en': 'Guard'},
    bio={'zh': '紅盔紅甲、手持長槍的衙役，守著城門與官道。', 'en': 'A guard in a red helmet and red armour with a spear, watching the gate and the high road.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_guard')]
