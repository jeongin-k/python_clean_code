
class Printer:
    def __init__(self):
        pass

    def print(self, value):
        print(value, end='')


class MockPrinter(Printer):
    def __init__(self):
        super().__init__()
        self.saved_output = ""

    def print(self, value):
        if isinstance(value, int):
            self.saved_output += str(value)
        elif isinstance(value, str):
            self.saved_output += value
        else:
            raise TypeError("Unsupported value type for printing")

    def get_output(self):
        return self.saved_output

