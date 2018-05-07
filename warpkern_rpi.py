from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

from time import time

from threading import Thread

import numpy as np

def writeData(data):
    wiringpi.wiringPiSPIDataRW(0, data)  # write the last chunk

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 4800000)

        self.thread = None

    def pushData(self, data: np.array):
        wiringpi._wiringpi.wiringPiSPIDataRW(0, data.ctypes.data, len(data))

        """
        if self.thread is not None:
            while(self.thread.is_alive()):
                pass
            self.thread = None

        self.thread = Thread(target=writeData, args=(data.tobytes(), ))
        self.thread.start()"""



