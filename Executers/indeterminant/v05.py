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


def tonum(s):
    def tobin(t):
        return bin(t)[2:]

    r = ''
    for x in s:
        r += tobin(ord(x))
    return int(r, 2)


def main(prog):
    prog = Programme(prog.split('\0', 1)[1])
    regs = {}

    i = 0
    while i < len(prog):
        if prog[i][0] == '\x00\x00':
            regnum = tonum(prog[i][1][0])
            k = 0
            while k < len(prog[i][1][1:]):
                regs[regnum+k] = tonum(prog[i][1][1:][k])
                k += 1
        i+=1

    return regs

if __name__ == '__main__':
    print(main(open('SETinstructionexamplecompiled.tau').read()))
