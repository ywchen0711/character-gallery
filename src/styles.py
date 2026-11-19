"""Art styles in the gallery. Every variant of a character names one of these."""

STYLES = {
    'sango': {
        'name': {'zh': '8-bit 紅白機・霸王之路主將', 'en': '8-bit Famicom, Path of the Hegemon general'},
        'blurb': {'zh': '《三國志 霸王之路》裡的主將造型：同一張 8-bit 臉，換上漢代將軍的冠、明光鎧與披風。',
                  'en': 'The main-general look from Three Kingdoms: Path of the Hegemon: the same 8-bit face in a Han general\'s cap, mirror armour and cape.'},
    },
    'nes': {
        'name': {'zh': '8-bit 紅白機（三國志 霸王の大陸風）', 'en': '8-bit Famicom (霸王の大陸-like)'},
        'blurb': {'zh': '主畫風。仿紅白機《三國志 霸王の大陸》的 8-bit 頭像：48×56、粗黑線、平塗兩三階陰影，'
                        '只用紅白機標準色盤，每 16×16 格一組三色（全圖最多四組），眼白、唇色等小細節用精靈疊上；'
                        '配 16×24 的紅白機小人，正面與側面兩格步行，孩子明顯比大人矮。',
                  'en': 'The main style. 8-bit Famicom portraits in the manner of 三國志 霸王の大陸: 48×56, bold black lines, '
                        'flat two- or three-step shading, only colours from the NES palette with one 3-colour set per 16×16 '
                        'area (at most four sets), and small sprite overlays for eye whites and lips; plus 16×24 NES field '
                        'sprites with a two-frame front and side walk, the children clearly shorter than their parents.'},
    },
    'family': {
        'name': {'zh': 'HD-2D 可愛版（八方旅人風）', 'en': 'HD-2D, cuter (Octopath-like)'},
        'blurb': {'zh': '前一版主畫風。柔和溫暖的 HD-2D 大頭像，加上圓臉小黑眼、四方向行走的 Q 版角色；一家人同一畫布、同一條地平線，身高一看就懂。',
                  'en': 'The previous main style. Warm, soft HD-2D portraits and round-faced sprites with small dark eyes that walk in four directions; the whole family shares one canvas and baseline, so heights read at a glance.'},
    },
    'koei': {
        'name': {'zh': '霸王の大陸 × 像素棒球', 'en': '16-bit Three Kingdoms × pixel baseball'},
        'blurb': {'zh': '16-bit 三國策略遊戲式的寫實側光半身頭像，配像素棒球遊戲式的 Q 版全身。',
                  'en': 'Side-lit 16-bit Three Kingdoms strategy bust portraits with pixel-baseball chibis.'},
    },
    'hd2d': {
        'name': {'zh': 'HD-2D（八方旅人風）', 'en': 'HD-2D (Octopath-like)'},
        'blurb': {'zh': '細緻柔和的大頭像，加上約三頭身、柔和陰影、小黑眼的角色點陣。',
                  'en': 'A detailed painterly portrait and a soft-shaded sprite about three heads tall with tiny dark eyes.'},
    },
    'snes': {
        'name': {'zh': 'SNES JRPG（FF6 風）', 'en': 'SNES JRPG (FF6-like)'},
        'blurb': {'zh': '柔和漸層的 48×48 選單頭像，加上 16×24 四方向行走的地圖角色。',
                  'en': 'A soft-shaded 48×48 menu portrait and a 16×24 field sprite walking in four directions.'},
    },
    'gba': {
        'name': {'zh': 'GBA 戰棋（聖火降魔錄風）', 'en': 'GBA tactics (Fire Emblem-like)'},
        'blurb': {'zh': '明亮賽璐璐上色、銳利輪廓的 16 色頭像，加上厚實的戰鬥角色。',
                  'en': 'A bright cel-shaded 16-colour portrait with crisp outlines and a chunky battle sprite.'},
    },
    'dq': {
        'name': {'zh': '8-bit 紅白機（勇者鬥惡龍風）', 'en': '8-bit NES (Dragon Quest-like)'},
        'blurb': {'zh': '每個角色 3 色加透明的 16×16 小人與兩格步行，配簡單的頭像視窗。',
                  'en': '16×16 sprites in 3 colours plus transparency with a two-frame walk, and a simple portrait window.'},
    },
}
