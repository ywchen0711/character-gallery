"""胡半仙 Hu Banxian - Fortune-teller. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='hubanxian',
    name={'zh': '胡半仙', 'en': 'Hu Banxian'},
    style_name={'zh': '鐵口直斷', 'en': 'The Infallible'},
    title={'zh': '算命先生', 'en': 'Fortune-teller'},
    bio={'zh': '擺攤算命的胡半仙，招牌寫著「鐵口直斷，不準不要錢」。他說的話，從來沒有一句準過——所以從來沒收過錢。', 'en': 'Hu Banxian tells fortunes under a banner reading "An iron mouth, a sure word, no charge if I\'m wrong". Not one of his prophecies has ever come true, so he has never been paid.'},
    weapon={'zh': '算命幡', 'en': 'Fortune banner'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('hubanxian')]
