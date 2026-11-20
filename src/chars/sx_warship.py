"""樓船 Tower Ship - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_warship',
    name={'zh': '樓船', 'en': 'Tower Ship'},
    style_name={'zh': '水上城樓', 'en': 'A Fortress on the Water'},
    title={'zh': '樓船將軍', 'en': 'The tower-ship captain'},
    bio={'zh': '兩層樓高的戰船，紅柱黑船身，桅頂飄著金旗。肖像是戴鐵盔的船將。', 'en': 'A warship two storeys tall, red pillars on a dark hull, a gold banner at the masthead. The portrait is its captain in an iron helmet.'},
    weapon={'zh': '金旗', 'en': 'Gold banner'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_warship')]
