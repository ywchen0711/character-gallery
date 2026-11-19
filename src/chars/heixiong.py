"""黑熊 Black Bear - chief of the Black Wind Fort bandits. Drawn in the 8-bit `nes` style only (src/nes_longmen2.py)."""

FACTION = 'longmen'
META = dict(
    id='heixiong',
    name={'zh': '黑熊', 'en': 'Black Bear'},
    style_name={'zh': '寨主', 'en': 'Bandit Chief'},
    title={'zh': '黑風寨寨主', 'en': 'Chief of the Black Wind Fort'},
    bio={'zh': '黑風寨的寨主，虎背熊腰，一臉濃密黑鬍，肩上披著自己獵來的熊皮，手提一根狼牙棒。嗓門大、脾氣粗，可別被他騙了：寨子能在官府眼皮底下撐這麼多年，靠的不只是蠻力。', 'en': "Chief of the Black Wind Fort: broad as a bear, a thick black beard, the hide of a bear he hunted himself over one shoulder and a spiked club in his fist. He is loud and rough, but do not be fooled: a fort does not hold out under the magistrate's nose for so many years on muscle alone."},
    weapon={'zh': '狼牙棒', 'en': 'Spiked club'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('heixiong')]
