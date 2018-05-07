from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

from time import time

import numpy as np

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 4800000)

    def pushData(self, data: np.array):
        wiringpi.wiringPiSPIDataRW(0, data.tobytes())  # write the last chunk
