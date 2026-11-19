"""吊睛白額虎 the White-Browed Mountain Tiger. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='tiger',
    name={'zh': '吊睛白額虎', 'en': 'White-Browed Tiger'},
    style_name={'zh': '猛獸', 'en': 'Beast'},
    title={'zh': '山中虎王', 'en': 'King of the Mountain'},
    bio={'zh': '額頭一個「王」字、雙眼吊梢的大老虎。白天伏在山崗上曬太陽，黃昏才下山找吃的；一聲吼，整片林子的鳥都飛走了。', 'en': 'A great tiger with the character for “king” on its brow and slanting eyes. It suns itself on the ridge by day and comes down at dusk to hunt; one roar and every bird in the forest takes flight.'},
    habitat={'zh': '山崗與松林', 'en': 'Mountain ridges and pine woods'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('tiger')]
