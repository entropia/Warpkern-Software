from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

from time import time

from threading import Thread

import numpy as np

from cffi import FFI

def writeData(data):
    wiringpi.wiringPiSPIDataRW(0, data)  # write the last chunk

def floatToByte(val: float) -> int:
    return max(0, min(int(val*255), 255)) # Convert float to byte + temporal dithering

class PiPhy(WarpkernPhy):
    def __init__(self):
        #wiringpi.wiringPiSetup()

        #wiringpi.wiringPiSPISetup(0, 4800000)

        self.thread = None

        self.ffi = FFI()
        self.ffi.cdef("""
int wiringPiSetup (void) ;
int wiringPiSPIGetFd     (int channel) ;
int wiringPiSPIDataRW    (int channel, unsigned char *data, int len) ;
int wiringPiSPISetupMode (int channel, int speed, int mode) ;
int wiringPiSPISetup     (int channel, int speed) ;
""")
        self._wiringpi = self.ffi.dlopen("/usr/lib/libwiringPi.so")

        self._wiringpi.wiringPiSetup()
        self._wiringpi.wiringPiSPISetip(self.ffi.cast("int", 0), self.ffi.cast("int", 4500000))

    def pushData(self, data: np.array):
        #wiringpi._wiringpi.wiringPiSPIDataRW(0, data.ctypes.data)

        chan = self.ffi.cast("int", 0)
        dataptr = self.ffi.cast("char*", data.ctypes.data)
        dlen = self.ffi.cast("int", len(data))
        self._wiringpi.wiringPiSPIDataRW(chan, dataptr, dlen)

        """
        if self.thread is not None:
            while(self.thread.is_alive()):
                pass
            self.thread = None

        self.thread = Thread(target=writeData, args=(data.tobytes(), ))
        self.thread.start()"""



