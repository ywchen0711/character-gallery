"""Ghostface Hornet ghosthornet - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='ghosthornet',
    name={'zh': '鬼面蜂', 'en': 'Ghostface Hornet'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '背上花紋像一張鬼臉的毒蜂，養在古墓的蜂窩裡。', 'en': 'A poison hornet whose back is patterned like a ghost face; it nests in old tombs.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='hornet',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('ghosthornet')]
