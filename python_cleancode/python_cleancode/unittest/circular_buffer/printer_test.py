import unittest
from printer import MockPrinter

class PrinterTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_printer = MockPrinter()

    def tearDown(self):
        pass

    def test_print_string(self):
        self.mock_printer.print("hello")
        self.mock_printer.print("hello\n")
        expected = "hellohello\n"
        assert expected == self.mock_printer.get_output()

    def test_print_int(self):
        self.mock_printer.print(1234)
        expected = str(1234)
        assert expected == self.mock_printer.get_output()


if __name__ == "__main__":
  unittest.main() # run all tests
