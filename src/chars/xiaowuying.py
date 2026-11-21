"""蕭無影 Xiao Wuying - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'tactics'
META = dict(
    id='xiaowuying',
    name={'zh': '蕭無影', 'en': 'Xiao Wuying'},
    style_name={'zh': '掌旗使', 'en': 'The Banner Steward'},
    title={'zh': '武林盟掌旗使', 'en': 'Banner Steward of the Wulin Alliance'},
    bio={'zh': '替武林盟管了十年戰旗的掌旗使。烏紗帽、深紫官服，袖裡藏著飛鏢。每一面旗的針腳他都數過，卻從來不是舉旗的那個人；到了夜裡，他戴上一張白色的鬼面。', 'en': "For ten years he kept the Wulin Alliance's banners: a black gauze cap, a deep violet official's robe, darts up his sleeve. He has counted every stitch of every banner yet was never the one to raise them; by night he wears a white ghost mask."},
    weapon={'zh': '袖鏢', 'en': 'Sleeve darts'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('xiaowuying')]
