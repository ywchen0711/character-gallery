"""江船 River Boat - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_boat',
    name={'zh': '江船', 'en': 'River Boat'},
    style_name={'zh': '一葦渡江', 'en': 'Crossing on a Reed'},
    title={'zh': '船家', 'en': 'The boatman'},
    bio={'zh': '竹篷布帆的小船，在江上穿來穿去。肖像是戴斗笠、扶著槳的船家。', 'en': 'A little boat with a matting sail that darts about the river. The portrait is the boatman in a straw hat, oar in hand.'},
    weapon={'zh': '船槳', 'en': 'Oar'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_boat')]
