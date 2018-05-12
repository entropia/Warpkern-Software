import sys
import base64
from PIL import Image
from urllib.parse import urlparse
import json
import io
from itertools import chain, cycle
import numpy as np
from warpkern import PrerenderedAnim

def load_image_from_datauri(datauri: str):
    path = urlparse(datauri).path
    data = base64.b64decode(path.split(",")[-1])
    im = Image.open(io.BytesIO(data))
    if im.size != (191, 12):
        raise RuntimeError("invalid dimensions: " + str(im.size))
    return im.convert("RGBA")

def load_anim(f):
    data = json.load(f)

    images = (load_image_from_datauri(i) for i in data["preview"])

    for i in images:

        yield np.array(list(chain((0, 0, 0, 0), chain.from_iterable((0xFF, b, g, r) for r, g, b, a in i.getdata()))), np.uint8)


class ShaderAnim(PrerenderedAnim):
    def __init__(self, filename):
        with open(filename) as f:
            arrays = list(load_anim(f))

        self.looper = cycle(arrays)

    def tick(self, time, dt):
        return next(self.looper)

def generate_animations(filenames):
    return [ShaderAnim(shaderfile)
            for shaderfile in filenames]
