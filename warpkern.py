from typing import List, Type

from time import time
import random

class WarpkernPhy():
    def pushData(self, data: List[List[float]]):
        print(data)

class Anim():
    def tick(self, time: float, dt: float):
        pass

    def getPix(self, ringindex: int, ledindex: int, time: float, dt: float) -> List[float]:
        """Fetch single pixel from animation

        :param ringindex: Index of ring (0 is at bottom)
        :param ledindex: Index of LED along ring
        :param time: time since start
        :param dt: time since last frame
        :return:
        """
        pass

class Warpkern():
    def __init__(self, ringcount: int, ledcount: int, anims: List[Type], phy: WarpkernPhy, verbose: bool=False, debug: bool=False):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.animclasses = anims
        self.phy = phy
        self.verbose = verbose
        self.debug = debug

        self.anims = [x(self.ringcount, self.ledcount) for x in self.animclasses]

        self.currentAnim = random.choice(self.anims)    # type: Anim
        self.nextAnim = self.currentAnim                # type: Anim

        self.time = time()

        self.transitionStart = 0     # Starttime of transition
        self.transitionEnd = 0       # Endtime of transition
        self.nextTransitionAt = 0    # When next transition shall begin

        self.currdata = [] * (self.ringcount * self.ledcount * 3)
        self.nextdata = [] * (self.ringcount * self.ledcount * 3)
        self.mixdata = [] * (self.ringcount * self.ledcount * 3)

    def startTransition(self):
        self.transitionStart = self.time
        self.transitionEnd = self.time + 10 # 10 Seconds transition time
        if self.debug:
            self.transitionEnd = self.time + 2
        self.nextAnim = random.choice(self.anims)  # TODO: prevent same animation being called twice
        if self.verbose:
            print("TRANSITION START:")
            print("  Start: %s" % self.transitionStart)
            print("  End: %s" % self.transitionEnd)
            print("  CurrentAnim: %s" % self.currentAnim)
            print("  NextAnim: %s" % self.nextAnim)

    def tick(self):
        self.dt = time() - self.time
        self.time = time()

        # Anim tracking
        ## End transition
        if self.time > self.transitionEnd and self.nextAnim is not None:
            self.currentAnim = self.nextAnim
            self.nextAnim = None
            self.nextTransitionAt = self.time + (360 + random.random() * 180)     # Every 10-15 minutes
            if self.debug:
                self.nextTransitionAt = self.time + (360 + random.random() * 180)*0.01  # More quickly for debugging reasons
            if self.verbose:
                print("TRANSITION END:")
                print("  Next: %s (in %s)" % (self.nextTransitionAt, self.nextTransitionAt - self.time))

        ## Start transition
        if self.time >= self.nextTransitionAt and self.time > self.transitionEnd:
            self.startTransition()

        # Generate Pixeldata
        self.currentAnim.tick(self.time, self.dt)
        for r in range(self.ringcount):
            for l in range(self.ledcount):
                indx = (r * self.ledcount + l) * 3
                self.currdata[indx:indx+3] = self.currentAnim.getPix(r, l, self.time, self.dt)

        ## We're in transition
        """if self.transitionStart <= self.time < self.transitionEnd and self.nextAnim is not None:
            # Generate pixeldata for next anim
            self.nextAnim.tick(self.time, self.dt)
            for r in range(self.ringcount):
                for l in range(self.ledcount):
                    self.nextdata.append(self.nextAnim.getPix(r, l, self.time, self.dt))

            # Linearly mix currdata and nextdata into mixdata
            alpha = (self.time - self.transitionStart)/(self.transitionEnd - self.transitionStart)
            mixdata = []
            def lerp3(a, b, x):
                return [a[0] * (1 - x) + b[0] * x,
                        a[1] * (1 - x) + b[1] * x,
                        a[2] * (1 - x) + b[2] * x]
            for i in range(len(currdata)):
                mixdata.append(lerp3(currdata[i], nextdata[i], alpha))

            self.phy.pushData(mixdata)
        else:   # Not in transition"""
        self.phy.pushData(self.currdata)
