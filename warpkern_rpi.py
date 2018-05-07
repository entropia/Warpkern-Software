from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

from time import time

from threading import Thread

import numpy as np

import os

def writeData(data):
    wiringpi.wiringPiSPIDataRW(0, data)  # write the last chunk

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        wiringpi.wiringPiSetup()

        wiringpi.wiringPiSPISetup(0, 4800000)

        self.thread = None

        self.spifd = wiringpi._wiringpi.wiringPiSPIGetFd(0)


    def pushData(self, data: np.array):
        os.write(self.spidf, data.tobytes())

        """
        if self.thread is not None:
            while(self.thread.is_alive()):
                pass
            self.thread = None

        self.thread = Thread(target=writeData, args=(data.tobytes(), ))
        self.thread.start()"""



