from warpkern import Anim



class TestAnim1(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0

    def tick(self, time: float, dt: float):
        self.counter += 1
        if self.counter >= self. totalLeds:
            self.counter = 0

    def getPix(self, ringindex: int, ledindex: int, time: float, dt: float):
        if ringindex * self.ledcount + ledindex == self.counter:
            return [1, 1, 1]
        else:
            return [0, 0, 0]

class TestAnim2(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0
        self.ringindx = 0

    def tick(self, time: float, dt: float):
        self.counter += 1
        if self.counter >= 10:
            self.counter = 0
            self.ringindx += 1
        if self.ringindx > self.ringcount:
            self.ringindx = 0

    def getPix(self, ringindex: int, ledindex: int, time: float, dt: float):
        if ringindex == self.ringindx:
            return [1, 0, 0]
        else:
            return [0, 0, 0]

class TestAnim3(Anim):
    def __init__(self, ringcount: int, ledcount: int):
        self.ringcount = ringcount
        self.ledcount = ledcount
        self.totalLeds = ringcount * ledcount
        self.counter = 0
        self.ringindx = 0

    def tick(self, time: float, dt: float):
        self.counter += 1
        if self.counter >= self. totalLeds:
            self.counter = 0

    def getPix(self, ringindex: int, ledindex: int, time: float, dt: float):
        if ledindex == 0:
            return [1, 0, 0]
        else:
            return [0, 0, 0]