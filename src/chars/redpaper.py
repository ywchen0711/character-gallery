"""Red Paper Effigy redpaper - a common foe of Longmen Quest II (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='redpaper',
    name={'zh': '紅紙人', 'en': 'Red Paper Effigy'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '冥婚喜宴上燒剩的紅紙人，咧著嘴笑，跟著鈴聲跳舞。', 'en': 'A red paper figure left over from a ghost wedding, grinning and dancing to the bell.'},
    habitat={'zh': '蘇家舊宅', 'en': 'The old Su mansion'},
    tier=3,
    base='paperghost',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('redpaper')]
