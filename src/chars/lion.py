"""鎮宅石獅 the Stone Guardian Lion. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='lion',
    name={'zh': '鎮宅石獅', 'en': 'Stone Guardian Lion'},
    style_name={'zh': '石怪', 'en': 'Living stone'},
    title={'zh': '古宅門前的守護', 'en': 'Guardian at the Old Gate'},
    bio={'zh': '荒廢古宅門口的石獅子，捲毛鬃、銅鈴眼，口含石珠，座上長滿青苔。白天一動也不動；夜裡有人擅闖，眼睛就亮起紅光。', 'en': 'The stone lion at the gate of a ruined mansion: curled mane, bulging eyes, a stone ball in its mouth, moss on its plinth. By day it never moves; when someone trespasses at night, its eyes glow red.'},
    habitat={'zh': '荒廢古宅與廟門', 'en': 'Ruined mansions and temple gates'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('lion')]
