"""牛飽飽 Niu Baobao - Camp master. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='niubaobao',
    name={'zh': '牛飽飽', 'en': 'Niu Baobao'},
    style_name={'zh': '百獸山寨主', 'en': 'Master of the Hundred Beasts Camp'},
    title={'zh': '寨主', 'en': 'Camp master'},
    bio={'zh': '百獸山寨的寨主，收留被打醒的妖物。最愛吃肉包，送人四個肉包，到手只剩三個。他的表親在各地客棧當夥計。', 'en': 'Master of the Hundred Beasts Camp, where creatures come to their senses. He loves meat buns: he gives you four and you get three. His cousins work at inns everywhere.'},
    weapon={'zh': '肉包', 'en': 'Meat buns'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('niubaobao')]
