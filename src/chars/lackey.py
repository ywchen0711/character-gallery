"""Black Wind Lackey lackey - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='lackey',
    name={'zh': '黑風嘍囉', 'en': 'Black Wind Lackey'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '黑風寨最底層的嘍囉，扛著木棍，嗓門比本事大。', 'en': 'The lowest of the Black Wind Fort: a cudgel on his shoulder and a voice bigger than his skill.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='lackey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('lackey')]
