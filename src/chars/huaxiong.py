"""華雄 Hua Xiong - an enemy general of 三國志 霸王之路 (stage: 汜水關). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='huaxiong',
    name={'zh': '華雄', 'en': 'Hua Xiong'},
    style_name={'zh': '董卓麾下猛將', 'en': "Dong Zhuo's champion"},
    title={'zh': '汜水關・董卓麾下猛將', 'en': "Sishui Pass - Dong Zhuo's champion"},
    bio={'zh': '董卓帳下的猛將，滿臉濃鬍、紅纓鐵盔、一把大刀。守在汜水關前，連斬聯軍數將。', 'en': "Dong Zhuo's fierce champion: a bushy beard, an iron helmet with a red plume and a broad dao. He holds Sishui Pass and has cut down several allied officers."},
    weapon={'zh': '大刀', 'en': 'Broad dao'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('huaxiong')]
