"""紀靈 Ji Ling - an enemy general of 三國志 霸王之路 (stage: 壽春討伐). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='jiling',
    name={'zh': '紀靈', 'en': 'Ji Ling'},
    style_name={'zh': '袁術大將', 'en': "Yuan Shu's general"},
    title={'zh': '壽春討伐・袁術大將', 'en': "The Shouchun Campaign - Yuan Shu's general"},
    bio={'zh': '袁術手下第一大將，紫纓鐵盔、面色冷峻，使一把三尖兩刃刀。守著壽春，一步也不退。', 'en': "Yuan Shu's foremost general: a purple-plumed iron helmet, a stern clean face and a three-pointed double-edged blade. He holds Shouchun and will not give a step."},
    weapon={'zh': '三尖兩刃刀', 'en': 'Three-pointed blade'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('jiling')]
