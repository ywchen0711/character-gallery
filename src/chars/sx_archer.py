"""弓手 Archer - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_archer',
    name={'zh': '弓手', 'en': 'Archer'},
    style_name={'zh': '百步之外', 'en': 'A Hundred Paces Away'},
    title={'zh': '門派的弓手', 'en': "The sect's archer"},
    bio={'zh': '紅頭帶、綠衣，背一壺箭。說話不多，開弓之前會先數三下風。', 'en': 'Red headband, green robe and a full quiver. Says little; counts the wind three times before every draw.'},
    weapon={'zh': '長弓', 'en': 'Longbow'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_archer')]
