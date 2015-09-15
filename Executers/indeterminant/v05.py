import getch
from functools import reduce
__author__ = 'Zodiac Working Group'


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


class regmap():
    def __init__(self):
        self.map = {}

    def __getitem__(self, item):
        if item in self.map:
            return self.map[item]
        else:
            return 0

    def __setitem__(self, item, value):
        self.map[item] = value

    def __delitem__(self, item, value):
        del self.map[item]

    def __str__(self):
        return 'regarray: '+str(self.map)


def tonum(s):
    def tobin(t):
        return bin(t)[2:].zfill(8)

    r = ''
    for x in s:
        r += tobin(ord(x))

    return int(r, 2)


def main(prog):
    prog = Programme(prog.split('\x00', 0)[0])
    regs = regmap()

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
                regs[tonum(args[0])] = reduce(lambda x, y: x + y, regs[1:], 1)

            elif comb == '\x04':
                regs[tonum(args[0])] = reduce(lambda x, y: x - y, regs[1:], 1)

            elif comb == '\x05':
                regs[tonum(args[0])] = reduce(lambda x, y: x * y, regs[1:], 1)

            elif comb == '\x06':
                regs[tonum(args[0])] = reduce(lambda x, y: x // y, regs[1:], 1)

            elif comb == '\x07':
                regs[tonum(args[0])] = reduce(lambda x, y: x ** y, regs[1:], 1)



        i+=1
        
    return regs

if __name__ == '__main__':
    print(main(open('SETinstructionexamplecompiled.tau').read()))
