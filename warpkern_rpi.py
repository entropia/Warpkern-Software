from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random

def floatToByte(val: float) -> int:
    return max(0, min(int(float*255 + random.random() - 0.5), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 10000000)

    def pushData(self, data: List[List[float]]):
        bytedata = [0, 0, 0, 0]     # Startframe
        for pix in data:
            bytedata += [floatToByte(1),
                        floatToByte(pix[0]),
                        floatToByte(pix[1]),
                        floatToByte(pix[2])]

        wiringpi.wiringPiSPIDataRW(0, bytes(bytedata))