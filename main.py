import argparse

from warpkern import Warpkern, WarpkernPhy

from anims import *

import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Warpkern")
    parser.add_argument("-r", "--ringcount", type=int, required=True, help="Amount of rings in the Warpkern")
    parser.add_argument("-l", "--ledcount", type=int, required=True, help="LEDs per ring")
    parser.add_argument("-v", "--verbose", action="store_true", help="Generate some debug output")
    parser.add_argument("-d", "--debug", action="store_true", help="Quickly cycles through some debug animations")

    args = parser.parse_args()

    if args.debug:
        wk = Warpkern(args.ringcount, args.ledcount, [TestAnim1, WarpCore], WarpkernPhy() , args.verbose, args.debug)
    else:
        wk = Warpkern(args.ringcount, args.ledcount, [WarpCore], WarpkernPhy(), args.verbose, False)

    while(True):
        #print("\nFrame start")
        a = time.time()
        wk.tick()
        time.sleep(0)
        #print("Tick: %s" % (time.time() - a))