"""白猿 the White Ape - guardian of the red fruit on the broken cliff. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='ape',
    name={'zh': '白猿', 'en': 'White Ape'},
    style_name={'zh': '靈獸', 'en': 'Spirit beast'},
    title={'zh': '斷崖守果靈猿', 'en': 'Guardian of the Cliff Fruit'},
    bio={'zh': '斷崖深谷裡的白猿，一身白毛，灰黑的皮臉，雙臂長過膝蓋。守著崖上的朱果，誰伸手就一掌拍下去；認可的人，牠會親手把果子遞過去。', 'en': 'A white ape of the gorge under the broken cliff: white fur, a dark leathery face, arms longer than its legs. It guards the red fruit on the cliff and swats any hand that reaches for it; to someone it accepts, it hands the fruit over itself.'},
    habitat={'zh': '斷崖下的深谷與瀑布', 'en': 'The gorge and falls under the broken cliff'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('ape')]
