from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 4800000)

    def pushData(self, data: List[float]):
        bytedata = [0, 0, 0, 0]     # Startframe

        for i in range(len(data)//3):
            bytedata += [255,
                        floatToByte(data[i*3+2]),
                        floatToByte(data[i*3+1]),
                        floatToByte(data[i*3])]

        for i in range(int(math.ceil(len(bytedata)/8))):
            bytedata.append(1)  # Add padding at end

        while(len(bytedata) > 4000):    # Write in chuncks of 1000
            dataout = bytedata[0:4000]
            wiringpi.wiringPiSPIDataRW(0, bytes(dataout))
            bytedata = bytedata[4000:]
        wiringpi.wiringPiSPIDataRW(0, bytes(bytedata))  # write the last chunk