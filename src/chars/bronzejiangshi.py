"""Bronze-armoured Jiangshi bronzejiangshi - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='bronzejiangshi',
    name={'zh': '銅甲小殭屍', 'en': 'Bronze-armoured Jiangshi'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '穿著陪葬銅甲的小殭屍，刀槍都砍不進。', 'en': 'A little jiangshi in the bronze armour it was buried with; blades glance off.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='littlejiangshi',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bronzejiangshi')]
