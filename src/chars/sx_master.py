"""絕頂高手 Peerless Master - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_master',
    name={'zh': '絕頂高手', 'en': 'Peerless Master'},
    style_name={'zh': '白髮青鋒', 'en': 'White Hair, Blue Steel'},
    title={'zh': '武功絕頂的高手', 'en': 'A master at the summit'},
    bio={'zh': '一頭白髮、灰黑長袍滾金邊，劍負在背上很少出鞘。據說他出鞘的那一劍，沒有人看清楚過。', 'en': 'White hair and a dark robe edged in gold; the sword on his back rarely leaves its sheath. They say no one has ever seen the one stroke he draws it for.'},
    weapon={'zh': '背上的長劍', 'en': 'The sword on his back'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_master')]
