import sys
import math
import struct
import getch
from functools import reduce
__author__ = 'Zodiac Working Group'


def binfromfloat(value):
    return struct.unpack('Q', struct.pack('d', value))[0]


def bintofloat(bits):
    return struct.unpack('d', struct.pack('Q', bits))[0]


class Programme:
    def __init__(self, prog):
        self.i = 0
        self.raw = prog
        self.instructions = []
        self.parse()

    def parse(self):
        j = 0
        while j < len(self.raw):
            args = []

            ins = self.raw[j:j+2]
            j += 2

            arglen = ord(self.raw[j])
            j += 1

            for k in range(arglen-1):
                args.append(self.raw[j:j+8])
                j += 8

            self.instructions.append((ins, args))

    def __getitem__(self, item):
        return self.instructions[item]

    def __len__(self):
        return len(self.instructions)


class RegMap:
    def __init__(self):
        self.map = {}

    def __getitem__(self, item):
        if item in self.map:
            return self.map[item]
        else:
            return 0

    def __setitem__(self, item, value):
        self.map[item] = value

    def __delitem__(self, item):
        del self.map[item]

    def __str__(self):
        return 'regarray: '+str(self.map)


def tonum(s, rtype=int):
    def tobin(t):
        return bin(t)[2:].zfill(8)

    r = ''
    for x in s:
        r += tobin(ord(x))

    r = int(r, 2)

    if rtype == float:
        r = bintofloat(r)

    return r


def main(prog):
    prog = Programme(prog.split('\x00', 0)[0])
    regs = RegMap()

    i = 0
    while i < len(prog):
        coma = prog[i][0][0]
        if coma == '\x00':
            comb = prog[i][0][1]
            args = prog[i][1]
            if comb == '\x00':
                regnum = tonum(args[0])
                k = 0
                while k < len(args[1:]):
                    regs[regnum+k] = tonum(args[1:][k])
                    k += 1

            elif comb == '\x01':
                startregnum = tonum(args[0])
                otherregnums = [tonum(x) for x in args[1:]]
                for x in otherregnums:
                    regs[x] = regs[startregnum]

            elif comb == '\x02':
                startregnum = tonum(args[0])
                otherregnums = [tonum(x) for x in args[1:]]
                for x in otherregnums:
                    regs[x] = regs[regs[startregnum]]

            elif comb == '\x03':
                regs[tonum(args[0])] = reduce(lambda y, z: y + z, [regs[y] for y in args[1:]], 1)

            elif comb == '\x04':
                regs[tonum(args[0])] = reduce(lambda y, z: y - z, [regs[y] for y in args[1:]], 1)

            elif comb == '\x05':
                regs[tonum(args[0])] = reduce(lambda y, z: y * z, [regs[y] for y in args[1:]], 1)

            elif comb == '\x06':
                regs[tonum(args[0])] = reduce(lambda y, z: y // z, [regs[y] for y in args[1:]], 1)

            elif comb == '\x07':
                regs[tonum(args[0])] = reduce(lambda y, z: y ** z, [regs[y] for y in args[1:]], 1)

            elif comb == '\x08':
                regs[tonum(args[0])] = binfromfloat(reduce(lambda y, z: y + z, [bintofloat(y) for y in [regs[y] for y in args[1:]]], 1))

            elif comb == '\x09':
                regs[tonum(args[0])] = binfromfloat(reduce(lambda y, z: y - z, [bintofloat(y) for y in [regs[y] for y in args[1:]]], 1))

            elif comb == '\x0A':
                regs[tonum(args[0])] = binfromfloat(reduce(lambda y, z: y * z, [bintofloat(y) for y in [regs[y] for y in args[1:]]], 1))

            elif comb == '\x0B':
                regs[tonum(args[0])] = binfromfloat(reduce(lambda y, z: y / z, [bintofloat(y) for y in [regs[y] for y in args[1:]]], 1))

            elif comb == '\x0C':
                regs[tonum(args[0])] = binfromfloat(reduce(lambda y, z: y ** z, [bintofloat(y) for y in [regs[y] for y in args[1:]]],1))

            elif comb == '\x0D':
                regs[tonum(args[0])] = binfromfloat(math.sqrt(regs[args[1]]))

            elif comb == '\x0E':
                regs[tonum(args[0])] = binfromfloat(math.sin(regs[args[1]]))

            elif comb == '\x0F':
                regs[tonum(args[0])] = binfromfloat(math.cos(regs[args[1]]))

            elif comb == '\x10':
                regs[tonum(args[0])] = binfromfloat(math.tan(regs[args[1]]))

            elif comb == '\x11':
                regs[tonum(args[0])] = binfromfloat(math.asin(regs[args[1]]))

            elif comb == '\x12':
                regs[tonum(args[0])] = binfromfloat(math.acos(regs[args[1]]))

            elif comb == '\x13':
                regs[tonum(args[0])] = binfromfloat(math.atan(regs[args[1]]))

            elif comb == '\x14':
                regs[tonum(args[0])] = binfromfloat(math.sinh(regs[args[1]]))

            elif comb == '\x15':
                regs[tonum(args[0])] = binfromfloat(math.cosh(regs[args[1]]))

            elif comb == '\x16':
                regs[tonum(args[0])] = binfromfloat(math.tanh(regs[args[1]]))

            elif comb == '\x17':
                regs[tonum(args[0])] = binfromfloat(math.asinh(regs[args[1]]))

            elif comb == '\x18':
                regs[tonum(args[0])] = binfromfloat(math.acosh(regs[args[1]]))

            elif comb == '\x19':
                regs[tonum(args[0])] = binfromfloat(math.atanh(regs[args[1]]))

            elif comb == '\x1A':
                regs[tonum(args[0])] = bintofloat(regs[args[1]])

            elif comb == '\x1B':
                regs[tonum(args[0])] = round(bintofloat(regs[args[1]]))

            elif comb == '\x1C':
                for x in args:
                    regs[x] = getch.getch()

            elif comb == '\x1D':
                print(*[regs[x] for x in args], end='')

            elif comb == '\x1E':
                print(*[regs[x] for x in args], end='', file=sys.stderr)

            elif comb == '\x1F':
                sys.stdout.flush()

            elif comb == '\x20':
                sys.stderr.flush()

            elif comb == '\x21':
                for x in args:
                    j = args[x]
                    s = ''
                    while regs[j] != ' ':
                        s += chr(regs[j])
                        j += 1
                    print(s, end='')

            elif comb == '\x22':
                pass

            elif comb == '\x23':
                pass

            elif comb == '\x24':
                pass

            elif comb == '\x25':
                if all([x == 0 for x in [regs[y] for y in args[1:]]]):
                    i = regs[args[0]]-1

            elif comb == '\x26':
                if all([x != 0 for x in [regs[y] for y in args[1:]]]):
                    i = regs[args[0]]-1

            elif comb == '\x27':
                if all([x < 0 for x in [regs[y] for y in args[1:]]]):
                    i = regs[args[0]]-1

            elif comb == '\x28':
                if all([x > 0 for x in [regs[y] for y in args[1:]]]):
                    i = regs[args[0]]-1

            elif comb == '\x29':
                if all([x <= 0 for x in [regs[y] for y in args[1:]]]):
                    i = regs[args[0]]-1

            elif comb == '\x2A':
                if all([x >= 0 for x in [regs[y] for y in args[1:]]]):
                    i = regs[args[0]]-1

        i += 1

    return regs

if __name__ == '__main__':
    print(main(open('SETinstructionexamplecompiled.tau').read()))
    input()
