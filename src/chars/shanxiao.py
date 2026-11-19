"""山魈 the Shanxiao, a one-footed mountain imp. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='shanxiao',
    name={'zh': '山魈', 'en': 'Shanxiao'},
    style_name={'zh': '山精', 'en': 'Mountain imp'},
    title={'zh': '一足山精', 'en': 'One-Footed Imp'},
    bio={'zh': '深山裡的山精：一圈金色鬃毛，紅鼻樑、藍色的皺紋臉頰，只有一隻大腳，跳起來卻比人跑得還快。愛偷旅人的鹽和火種，被叫出名字就會逃走。', 'en': "An imp of the deep mountains: a ring of golden mane, a red nose ridge and blue ribbed cheeks, and only one big foot, yet it hops faster than a man can run. It steals travellers' salt and tinder, and flees when called by its name."},
    habitat={'zh': '深山密林', 'en': 'Deep mountain forest'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('shanxiao')]
