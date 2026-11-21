"""商人 Merchant - Longmen townsfolk (the unnamed people of the Longmen Quest towns), drawn with the nes2 kit
(src/nes2_cast_town.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmenTown'
META = dict(
    id='tf_merchant',
    name={'zh': '商人', 'en': 'Merchant'},
    style_name={'zh': '掌櫃', 'en': 'Merchant'},
    title={'zh': '掌櫃', 'en': 'Merchant'},
    bio={'zh': '頭戴紅瓜皮帽、一身金黃的胖商人，算盤打得比誰都響。', 'en': 'A round merchant in a red melon cap and golden robe whose abacus clicks loudest of all.'},
    weapon={'zh': '', 'en': ''},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tf_merchant')]
