"""連弩手 Repeater Crossbows - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_crossbow',
    name={'zh': '連弩手', 'en': 'Repeater Crossbows'},
    style_name={'zh': '一弩十箭', 'en': 'Ten Bolts a Breath'},
    title={'zh': '連弩手', 'en': 'A repeater crossbowman'},
    bio={'zh': '青綠甲衣，端著連弩。機括一響，十箭連發。', 'en': 'In teal armour with a repeating crossbow levelled: one click and ten bolts fly.'},
    weapon={'zh': '連弩', 'en': 'Repeating crossbow'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_crossbow')]
