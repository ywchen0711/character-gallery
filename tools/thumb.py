"""960x540 lobby thumbnail: the family group scene at 7x, framed.
python tools/thumb.py"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = Image.open(os.path.join(ROOT, 'chars', 'family', 'group-scene.png')).convert('RGB')
T = Image.new('RGB', (960, 540), (24, 26, 32))
big = g.resize((g.width * 7, g.height * 7), Image.NEAREST)
T.paste(big, ((960 - big.width) // 2, (540 - big.height) // 2))
T.save(os.path.join(ROOT, 'thumb.jpg'), quality=92)
