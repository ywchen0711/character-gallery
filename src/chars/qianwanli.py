"""錢萬里 Qian Wanli - treasurer of the Martial Alliance. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='qianwanli',
    name={'zh': '錢萬里', 'en': 'Qian Wanli'},
    style_name={'zh': '金算盤', 'en': 'Golden Abacus'},
    title={'zh': '武林盟司庫', 'en': 'Treasurer of the Martial Alliance'},
    bio={'zh': '武林盟的司庫，人稱「金算盤」。圓臉肚子大，瓜皮帽頂一顆紅珠，金珠算盤從不離手，一文一釐都算得清清楚楚。笑起來和氣，談起帳來寸步不讓。', 'en': 'Treasurer of the Martial Alliance, known as the Golden Abacus. Round of face and belly, a red bead on top of his melon-skin cap, the gold-beaded abacus always in hand; he accounts for every last copper. Genial when he smiles, immovable when it comes to the books.'},
    weapon={'zh': '金珠算盤', 'en': 'Gold-beaded abacus'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('qianwanli')]
