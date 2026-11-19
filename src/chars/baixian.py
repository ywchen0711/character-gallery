"""白先生 Mr Bai - the storyteller of the Listening-to-Rain teahouse. Drawn in the 8-bit `nes` style only (src/nes_longmen.py)."""

FACTION = 'longmen'
META = dict(
    id='baixian',
    name={'zh': '白先生', 'en': 'Mr Bai'},
    style_name={'zh': '說書人', 'en': 'Storyteller'},
    title={'zh': '聽雨樓說書人', 'en': 'Storyteller of the Listening-to-Rain'},
    bio={'zh': '十字路口聽雨樓的說書先生。方巾長袖，山羊鬍，醒木一拍，古今江湖的大小消息就從他嘴裡說出來——沒有他不知道的事。', 'en': 'The storyteller of the Listening-to-Rain teahouse at the crossroads. Square cap, long sleeves, a little goatee: one clap of his wooden block and every tale of the rivers and lakes, old and new, comes out of his mouth. There is no news he has not heard.'},
    weapon={'zh': '醒木', 'en': 'Clapper block'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('baixian')]
