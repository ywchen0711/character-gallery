"""投石車 Catapult - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_catapult',
    name={'zh': '投石車', 'en': 'Catapult'},
    style_name={'zh': '石落如雨', 'en': 'Stones Fall like Rain'},
    title={'zh': '投石車的匠師', 'en': 'The catapult engineer'},
    bio={'zh': '木架、拋臂和一塊大石頭。肖像是戴圓帽的匠師，手裡掂著下一顆石彈。', 'en': 'A timber frame, a throwing arm and a big stone. The portrait is the engineer in a round cap, weighing the next shot.'},
    weapon={'zh': '石彈', 'en': 'Stone shot'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_catapult')]
