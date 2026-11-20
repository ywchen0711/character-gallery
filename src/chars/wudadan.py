"""武大膽 Wu Dadan - Caravan escort. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='wudadan',
    name={'zh': '武大膽', 'en': 'Wu Dadan'},
    style_name={'zh': '膽小鏢頭', 'en': 'The Timid Escort'},
    title={'zh': '鏢師', 'en': 'Caravan escort'},
    bio={'zh': '名叫「大膽」，身高八尺、滿臉鬍子，卻是全江湖最膽小的鏢師。一害怕就躲進酒罈，可真到了要緊關頭，總會擋在同伴前面。', 'en': 'His name means "Great Courage", he is eight feet tall and bearded, and he is the most timid escort in the jianghu. Frightened, he hides in a wine jar; yet when it matters most he always stands in front of his friends.'},
    weapon={'zh': '鐵頭哨棒', 'en': 'Iron-shod staff'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('wudadan')]
