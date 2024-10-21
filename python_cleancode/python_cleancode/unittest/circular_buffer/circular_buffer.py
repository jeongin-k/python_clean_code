import printer

class CircularBuffer:
    CAPACITY = 5

    def __init__(self, capacity=CAPACITY):
        self.index = 0
        self.outdex = 0
        self.capacity = capacity
        self.buffer = [0] * self.capacity
        self.empty = True
        self.full = False

    def is_empty(self):
        return self.empty

    def is_full(self):
        return self.full

    def put(self, i):
        self.empty = False
        self.buffer[self.index] = i
        self.index = self.next(self.index)
        if self.full:
            self.outdex = self.next(self.outdex)
        elif self.index == self.outdex:
            self.full = True

    def get(self):
        result = -1
        self.full = False

        if not self.empty:
            result = self.buffer[self.outdex]
            self.outdex = self.next(self.outdex)
            if self.outdex == self.index:
                self.empty = True

        return result

    def get_capacity(self):
        return self.capacity

    def next(self, i):
        if i + 1 >= self.capacity:
            return 0
        return i + 1

    def print(self, printer):
        printer.print("Circular buffer content:\n<")

        print_index = self.outdex
        count = self.index - self.outdex

        if not self.empty and (self.index <= self.outdex):
            count = self.capacity - (self.outdex - self.index)

        for i in range(count):
            printer.print(self.buffer[print_index])
            print_index = self.next(print_index)
            if i + 1 != count:
                printer.print(", ")

        printer.print(">\n")

