"""Vajra Guardian vajraguardian - a common foe (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='vajraguardian',
    name={'zh': '金剛銅人', 'en': 'Vajra Guardian'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '鍍金的銅人，一拳能把石碑打斷。', 'en': 'A gilded bronze man whose fist can break a stone tablet.'},
    habitat={'zh': '幽冥殿與雪峰', 'en': 'The Netherworld Hall and the snow peaks'},
    tier=5,
    base='bronze',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('vajraguardian')]
