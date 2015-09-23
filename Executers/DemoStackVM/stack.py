class Stack:
    def __init__(self):
        self._l = []
        self.size = 0

    def pop(self):
        r = self._l[-1]
        del self._l[-1]
        self.size -= 1
        return r

    def push(self, val):
        self._l.append(val % 256)
        self.size += 1
