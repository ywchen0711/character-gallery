"""鐵騎 Iron Cavalry - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_ironcav',
    name={'zh': '鐵騎', 'en': 'Iron Cavalry'},
    style_name={'zh': '鐵甲雷蹄', 'en': 'Iron Hooves like Thunder'},
    title={'zh': '重甲騎兵', 'en': 'Heavy cavalry'},
    bio={'zh': '人和馬都披著鐵甲，衝鋒時地面跟著震動。', 'en': 'Rider and horse both clad in iron; the ground shakes when they charge.'},
    weapon={'zh': '長槍與鐵甲', 'en': 'Lance and barding'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_ironcav')]
