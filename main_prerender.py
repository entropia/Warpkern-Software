import argparse

from warpkern import PrerenderedWarpkern, WarpkernPhy
from warpkern_rpi import PiPhy
from read_wkshader import generate_animations
import glob

import time

class TestPhy:
    def pushData(a, array):
        print(array, len(array))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Warpkern")
    parser.add_argument("-d", "--dir", type=str, required=True, help="animation.json folder")

    args = parser.parse_args()

    objects = glob.glob(args.dir + "/*.json")

    if not objects:
        raise IOError("no .json files found in anim dir")

    animations = generate_animations(objects)

    wk = PrerenderedWarpkern(animations, TestPhy())

    while(True):
        wk.tick()
        time.sleep(0.0)
