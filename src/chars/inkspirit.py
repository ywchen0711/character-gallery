"""Ink Spirit inkspirit - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='inkspirit',
    name={'zh': '墨靈', 'en': 'Ink Spirit'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '書齋裡打翻的一灘墨，吸了書生的怨氣，到處亂爬。', 'en': "A spilt pool of ink in a study that soaked up a scholar's grudge and now crawls about."},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='inkblot',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('inkspirit')]
