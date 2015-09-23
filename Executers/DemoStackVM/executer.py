import sys
import math
from stack import stack
from getch import getch


def parse(prog):
    du = [0x00, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x18, 0x19, 0x1A, 0x1B]
    argcounts = {
        tuple(du): 0,
        tuple([x for x in range(0x1F) if x not in du]): 1
    }

    r = []
    i = 0

    while i < len(prog):
        argc = 0
        ins = [prog[i]]
        for x in argcounts:
            if prog[i] in x:
                argc = argcounts[x]
                break
        j = 0
        while j < argc:
            ins.append(prog[i+j+1])
            i += 1
            j += 1

        r.append(tuple([ord(x) for x in ins]))
        i += 1

    return r


class Code:
    def __init__(self, prog):
        self.prog = parse(prog)
        self.i = 0

    def getins(self):
        if self.i < len(self.prog):
            return self.prog[self.i]
        else:
            return None

    def next(self):
        self.i += 1

    def goto(self, i):
        self.i = i-1


def evalscript(script):
    code = Code(script)
    st = stack()

    while code.getins():
        ins = code.getins()
        com = ins[0]

        if com == 0x00:  # PUSH
            st.push(ins[1])

        elif com == 0x01:  # DROP
            st.pop()

        elif com == 0x02:  # DUP
            a = st.pop()
            st.push(a)
            st.push(a)

        elif com == 0x03:  # SWAP
            a = st.pop()
            b = st.pop()
            st.push(a)
            st.push(b)

        elif com == 0x04:  # OVER
            a = st.pop()
            b = st.pop()
            st.push(b)
            st.push(a)
            st.push(b)

        elif com == 0x05:  # CROT
            a = st.pop()
            b = st.pop()
            c = st.pop()
            st.push(b)
            st.push(a)
            st.push(c)

        elif com == 0x06:  # CCROT
            a = st.pop()
            b = st.pop()
            c = st.pop()
            st.push(a)
            st.push(c)
            st.push(b)

        elif com == 0x07:  # ADD
            a = st.pop()
            b = st.pop()
            st.push(b+a)

        elif com == 0x08:  # SUB
            a = st.pop()
            b = st.pop()
            st.push(b-a)

        elif com == 0x09:  # PRO
            a = st.pop()
            b = st.pop()
            st.push(b*a)

        elif com == 0x0A:  # QUO
            a = st.pop()
            b = st.pop()
            st.push(b//a)

        elif com == 0x0B:  # MOD
            a = st.pop()
            b = st.pop()
            st.push(b%a)

        elif com == 0x0C:  # ADDI
            a = st.pop()
            b = ins[1]
            st.push(b+a)

        elif com == 0x0D:  # SUBI
            a = st.pop()
            b = ins[1]
            st.push(b-a)

        elif com == 0x0E:  # SUBI2
            a = ins[1]
            b = st.pop()
            st.push(b-a)

        elif com == 0x0F:  # PROI
            a = st.pop()
            b = ins[1]
            st.push(b*a)

        elif com == 0x10:  # QUOI
            a = st.pop()
            b = ins[1]
            st.push(b//a)

        elif com == 0x11:  # MODI
            a = st.pop()
            b = ins[1]
            st.push(b%a)

        elif com == 0x12:  # QUOI2
            a = ins[1]
            b = st.pop()
            st.push(b//a)

        elif com == 0x13:  # MODI2
            a = ins[1]
            b = st.pop()
            st.push(b%a)

        elif com == 0x14:  # SQRT
            st.push(math.sqrt(st.pop()))

        elif com == 0x15:  # SIN
            st.push(math.sin(st.pop()))

        elif com == 0x16:  # COS
            st.push(math.cos(st.pop()))

        elif com == 0x17:  # TAN
            st.push(math.tan(st.pop()))

        elif com == 0x18:  # BRNCH
            code.goto(ins[1])

        elif com == 0x19:  # BTOS
            code.goto(st.pop())

        elif com == 0x1A:  # BIZ
            a = st.pop()
            if a == 0:
                code.goto(ins[1])

        elif com == 0x1B:  # BINZ
            a = st.pop()
            if a != 0:
                code.goto(ins[1])

        elif com == 0x1C:  # PUTCH
            print(chr(st.pop()), end='')
            sys.stdout.flush()

        elif com == 0x1D:  # GETCH
            st.push(ord(getch()))

        elif com == 0x1E:  # PRINTS
            popped = None
            while popped != 0:
                popped = st.pop()
                if not popped == 0:
                    print(chr(popped), end='')
                    sys.stdout.flush()


if __name__ == '__main__':
    evalscript(open(sys.argv[1]).read())
