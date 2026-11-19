"""呂布 Lü Bu - an enemy general of 三國志 霸王之路 (stage: 虎牢關). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='lubu',
    name={'zh': '呂布', 'en': 'Lü Bu'},
    style_name={'zh': '飛將', 'en': 'The Flying General'},
    title={'zh': '虎牢關・飛將', 'en': 'Hulao Pass - The Flying General'},
    bio={'zh': '天下無雙的飛將：紫金冠插兩根雉雞翎、金甲紅袍，手持方天畫戟。霸王之路的最後一關，等在虎牢關上。', 'en': 'The peerless Flying General: a gold crown with two pheasant feathers, gold armour, a red robe and the Sky Piercer halberd. The last battle of the road, waiting on Hulao Pass.'},
    weapon={'zh': '方天畫戟', 'en': 'Sky Piercer halberd'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('lubu')]
