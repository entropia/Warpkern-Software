from typing import List, Type

from time import time
import random

import numpy as np

import sys


def floatToByte(val: float) -> int:
    return max(0, min(int(val * 255), 255))  # Convert float to byte + temporal dithering


class WarpkernPhy():
    def pushData(self, data: List[List[float]]):
        sys.stdout.buffer.write(data.tobytes())

class Anim():
    def tick(self, data: np.array, time: float, dt: float):
        pass


class Warpkern():
    def __init__(self, ringcount: int, ledcount: int, anims: List[Type], phy: WarpkernPhy, verbose: bool=False, debug: bool=False):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.animclasses = anims
        self.phy = phy
        self.verbose = verbose
        self.debug = debug

        self.anims = [x(self.ringcount, self.ledcount) for x in self.animclasses]

        self.currentAnim = random.choice(self.anims)    # type: Anim

        self.time = time()

        self.nextAnimAt = self.time + 360

        self.totalLedCount = self.ringcount * self.ledcount
        self.totalByteCount = self.totalLedCount * 4 + 1 + self.totalLedCount//8
        self.pixdata = np.ones((self.totalLedCount, 4))
        self.outdata = np.ones((self.totalByteCount, 4))
        self.outdata[0][0] = 0
        self.outdata[0][1] = 0
        self.outdata[0][2] = 0
        self.outdata[0][3] = 0

    def tick(self):
        self.dt = time() - self.time
        self.time = time()

        if self.time > self.nextAnimAt:
            self.currentAnim = random.choice(self.anims)

        self.currentAnim.tick(self.pixdata, self.time, self.dt)

        self.outdata[1:self.totalLedCount+1] = self.pixdata

        self.phy.pushData(np.array(self.outdata.clip(0, 1) * 255, np.uint8).flatten())
