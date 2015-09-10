__author__ = 'Zodiac Working Group'


class Programme:
    def __init__(self, prog):
        self.i = 0
        self.raw = prog

    def read(self, n):
        r = tuple(self.raw[i:i+n])
        self.i += n
        return r

    def setloc

def main(prog):
    prog = Programme(prog)
    while prog.finished == False:
        pass
