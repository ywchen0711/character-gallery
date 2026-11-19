"""鐵無私 Tie Wusi - deputy of the Martial Alliance and Master of the Law Hall. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='tiewusi',
    name={'zh': '鐵無私', 'en': 'Tie Wusi'},
    style_name={'zh': '執法堂主', 'en': 'Law Master'},
    title={'zh': '武林盟副盟主・執法堂主', 'en': 'Deputy of the Martial Alliance, Master of the Law Hall'},
    bio={'zh': '武林盟的副盟主，執掌執法堂。頭戴烏紗、兩撇濃黑八字鬍，一張臉像鐵鑄的，從來不笑；只認證據，不認交情。腰間一條鐵鍊，「鐵鎖連環」一出，沒幾個人走得掉。', 'en': 'Deputy of the Martial Alliance and master of its Law Hall. A black official cap, a heavy black moustache and a face like cast iron that never smiles; he trusts proof, never friendship. Few get away once his Iron Lock Chain comes out.'},
    weapon={'zh': '鐵鍊', 'en': 'Iron chain'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tiewusi')]
