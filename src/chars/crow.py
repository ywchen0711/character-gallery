"""三足火鴉 the Three-Legged Fire Crow. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='crow',
    name={'zh': '三足火鴉', 'en': 'Fire Crow'},
    style_name={'zh': '火鳥', 'en': 'Fire bird'},
    title={'zh': '烈日下的凶鳥', 'en': 'Bird of the Blazing Sun'},
    bio={'zh': '三隻腳的大火鴉，暗紅羽毛的翅尖燒著火焰，眼睛像燒紅的炭。飛過的地方草木焦黃，乾旱的年頭最常見到牠。', 'en': 'A great three-legged crow with dark red plumage and flames at its wingtips, eyes like glowing coals. Grass browns where it flies, and it is seen most in years of drought.'},
    habitat={'zh': '火山口與旱地', 'en': 'Volcano rims and drought lands'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('crow')]
