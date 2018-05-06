from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255 + (random.random() - 0.5)*0.95), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 5000000)

    def pushData(self, data: List[List[float]]):
        bytedata = [0, 0, 0, 0]     # Startframe
        for pix in data:
            bytedata += [255,
                        floatToByte(pix[2]),
                        floatToByte(pix[1]),
                        floatToByte(pix[0])]

        for i in range(int(math.ceil(len(bytedata)/8))):
            bytedata.append(1)  # Add padding at end

        while(len(bytedata) > 1000):    # Write in chuncks of 1000
            dataout = bytedata[0:1000]
            wiringpi.wiringPiSPIDataRW(0, bytes(dataout))
            bytedata = bytedata[1000:]
        wiringpi.wiringPiSPIDataRW(0, bytes(bytedata))  # write the last chunk