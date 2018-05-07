from warpkern import Anim

import numpy as np

class TestAnim1(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0

    def tick(self, data: np.array, time: float, dt: float):
        self.data = data
        self.counter += 1
        if self.counter > self.totalLeds:
            self.counter = 0

        self.data = np.transpose(self.data)
        for r in range(self.ringcount):
            #ring = np.arange(self.ledcount)
            indxs = self.ledcount * r
            indxe = self.ledcount * (r + 1)

            self.data[1][indxs:indxe] = np.zeros(self.ledcount)
            self.data[2][indxs:indxe] = np.zeros(self.ledcount)
            self.data[3][indxs:indxe] = np.zeros(self.ledcount)

        self.data = np.transpose(self.data)
        self.data[self.counter] = np.array([1, 1, 1, 1])

class TestAnim2(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0
        self.ringindx = 0

    def tick(self, data: np.array, time: float, dt: float):
        self.data = data
        self.counter += 1
        if self.counter >= 10:
            self.counter = 0
            self.ringindx += 1
        if self.ringindx > self.ringcount:
            self.ringindx = 0

        self.data = np.transpose(self.data)
        for r in range(self.ringcount):
            ring = np.arange(self.ledcount)
            indxs = self.ledcount * r
            indxe = self.ledcount * (r + 1)

            self.data[1][indxs:indxe] = np.abs(np.sin(ring*np.pi*0.1))
            self.data[2][indxs:indxe] = np.ones(self.ledcount)
            self.data[3][indxs:indxe] = np.zeros(self.ledcount)

        self.data = np.transpose(self.data)


class WarpCore(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0
        self.ringindx = 0

    def tick(self, data: np.array, time: float, dt: float):
        self.data = data
        self.counter += 1
        if self.counter >= 10:
            self.counter = 0
            self.ringindx += 1
        if self.ringindx > self.ringcount:
            self.ringindx = 0

        self.data = np.transpose(self.data)
        pow = np.ones(self.ledcount) * 4
        for r in range(self.ringcount):
            speed = 1.
            anim = np.ones(self.ledcount) + ((time * 0.2) + (r * 0.1))
            indxs = self.ledcount * r
            indxe = self.ledcount * (r + 1)

            self.data[1][indxs:indxe] = np.power(np.sin(anim*np.pi), pow)
            self.data[2][indxs:indxe] = np.zeros(self.ledcount)
            self.data[3][indxs:indxe] = np.zeros(self.ledcount)

        self.data = np.transpose(self.data)

class BlauFoo(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0
        self.ringindx = 0

    def tick(self, data: np.array, time: float, dt: float):
        self.data = data
        self.counter += 1
        if self.counter >= 10:
            self.counter = 0
            self.ringindx += 1
        if self.ringindx > self.ringcount:
            self.ringindx = 0

        self.data = np.transpose(self.data)
        for r in range(self.ringcount):
            speed = 1.
            anim = np.arange(self.ledcount) - self.ledcount//2 + (time * 5)
            indxs = self.ledcount * r
            indxe = self.ledcount * (r + 1)

            self.data[1][indxs:indxe] = np.sin(anim*np.pi*0.1)
            self.data[2][indxs:indxe] = np.zeros(self.ledcount)
            self.data[3][indxs:indxe] = np.zeros(self.ledcount)

        self.data = np.transpose(self.data)