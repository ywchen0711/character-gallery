"""鏢隊 Escort Caravan - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_caravan',
    name={'zh': '鏢隊', 'en': 'Escort Caravan'},
    style_name={'zh': '鏢旗所到', 'en': 'Where the Escort Flag Goes'},
    title={'zh': '走鏢的鏢頭', 'en': 'The escort master'},
    bio={'zh': '一輛蓋著布的鏢車，車上插著紅色鏢旗。肖像是領隊的鏢頭，手裡握著鏢旗。', 'en': 'A covered cart flying the red escort banner. The portrait is the escort master who leads it, banner in hand.'},
    weapon={'zh': '鏢旗', 'en': 'Escort banner'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_caravan')]
