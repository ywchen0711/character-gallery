"""山賊 Bandit - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_bandit',
    name={'zh': '山賊', 'en': 'Bandit'},
    style_name={'zh': '綠林', 'en': 'Bandit'},
    title={'zh': '綠林', 'en': 'Bandit'},
    bio={'zh': '灰頭巾、灰面巾，只露出一雙兇眼的山賊。', 'en': 'A bandit in a grey kerchief and grey face cloth, only his fierce eyes showing.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_bandit')]
