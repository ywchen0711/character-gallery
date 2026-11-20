"""賈八方 Jia Bafang - Peddler. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='jiabafang',
    name={'zh': '賈八方', 'en': 'Jia Bafang'},
    style_name={'zh': '八方通', 'en': 'Jia of the Eight Directions'},
    title={'zh': '行商', 'en': 'Peddler'},
    bio={'zh': '天底下沒有他不賣的東西，連自己的鞋、帽子和外衣都賣了。每次見面，他身上的東西就少一件。', 'en': "There is nothing under heaven he won't sell, his own shoes, hat and coat included. Each time you meet him he is wearing a little less."},
    weapon={'zh': '貨箱', 'en': 'His pack'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('jiabafang')]
