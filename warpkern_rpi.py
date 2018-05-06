from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

from time import time

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 4800000)

    def pushData(self, data: List[float]):
        t = time()
        bytedata = [0, 0, 0, 0] + data    # Startframe

        bytedata = list(map(floatToByte, bytedata))

        print("Convert data: %s" % (time() - t))
        t = time()

        for i in range(int(math.ceil(len(bytedata)/8))):
            bytedata.append(1)  # Add padding at end

        print("Padding: %s" % (time() - t))
        t = time()

        while(len(bytedata) > 4000):    # Write in chuncks of 1000
            dataout = bytedata[0:4000]
            wiringpi.wiringPiSPIDataRW(0, bytes(dataout))
            bytedata = bytedata[4000:]
        wiringpi.wiringPiSPIDataRW(0, bytes(bytedata))  # write the last chunk

        print("Write: %s" % (time() - t))
        t = time()

        print("push over")