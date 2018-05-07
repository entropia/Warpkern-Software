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
        bytedata = data.tobytes()

        while(len(bytedata) > 4000):    # Write in chuncks of 1000
            wiringpi.wiringPiSPIDataRW(0, bytedata[0:4000])
            bytedata = bytedata[4000:]
        wiringpi.wiringPiSPIDataRW(0, bytedata)  # write the last chunk
