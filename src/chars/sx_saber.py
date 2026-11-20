"""刀客 Saber - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_saber',
    name={'zh': '刀客', 'en': 'Saber'},
    style_name={'zh': '大刀在手', 'en': 'Broadsword in Hand'},
    title={'zh': '江湖刀客', 'en': 'A saber of the jianghu'},
    bio={'zh': '棕色短打，一把厚背大刀扛在肩上。刀法不花俏，只求一刀見效。', 'en': 'A brown jacket and a thick-backed broadsword on the shoulder. No flourishes: one cut, one result.'},
    weapon={'zh': '厚背刀', 'en': 'Thick-backed saber'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_saber')]
