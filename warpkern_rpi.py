from warpkern import WarpkernPhy

import wiringpi
from typing import List

import random
import math

from time import time

import numpy as np

import sys

if __name__ == "__main__":
    wiringpi.wiringPiSetup()
    wiringpi.wiringPiSPISetup(0, 4800000)
    while True:
        bytedata = sys.stdin.buffer.read(100)
        wiringpi.wiringPiSPIDataRW(0, bytedata)