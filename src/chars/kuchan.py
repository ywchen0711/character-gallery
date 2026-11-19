"""苦禪 Master Kuchan - abbot of the Thousand Buddhas Temple. Drawn in the 8-bit `nes` style only (src/nes_longmen.py)."""

FACTION = 'longmen'
META = dict(
    id='kuchan',
    name={'zh': '苦禪', 'en': 'Kuchan'},
    style_name={'zh': '大師', 'en': 'Master'},
    title={'zh': '千佛寺住持', 'en': 'Abbot of the Thousand Buddhas'},
    bio={'zh': '千佛寺的住持，白眉長鬚，杏黃僧袍外披紅色袈裟，手持禪杖。總是笑瞇瞇的，說起話來慢條斯理；記性卻好得驚人。', 'en': 'Abbot of the Thousand Buddhas Temple: white brows and a long white beard, a saffron robe under a red kasaya, a monk’s staff in hand. Always smiling and slow of speech, with a remarkably long memory.'},
    weapon={'zh': '禪杖', 'en': 'Monk’s staff'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('kuchan')]
