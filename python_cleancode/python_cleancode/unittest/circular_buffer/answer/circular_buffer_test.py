import unittest
from printer import MockPrinter
from circular_buffer_answer import CircularBuffer

class CircularBufferTestCase(unittest.TestCase):

    def fill_the_queue(self, seed, how_many):
        for i in range(how_many):
            self.buffer.put(seed + i)

    def remove_from_queue(self, how_many):
        for i in range(how_many):
            self.buffer.get()

    def setUp(self):
        self.mock_printer = MockPrinter()
        self.buffer = CircularBuffer()

    def tearDown(self):
        pass

    def test_empty_after_creation(self):
        self.assertTrue(self.buffer.is_empty())

    def test_not_empty(self):
        self.buffer.put(10046)
        self.assertFalse(self.buffer.is_empty())

    def test_not_empty_then_empty(self):
        self.buffer.put(4567)
        self.assertFalse(self.buffer.is_empty())
        self.buffer.get()
        self.assertTrue(self.buffer.is_empty())

    def test_get_put_one_value(self):
        self.buffer.put(4567)
        self.assertEqual(4567, self.buffer.get())

    def test_get_put_a_few(self):
        self.buffer.put(1)
        self.buffer.put(2)
        self.buffer.put(3)
        self.assertEqual(1, self.buffer.get())
        self.assertEqual(2, self.buffer.get())
        self.assertEqual(3, self.buffer.get())

    def test_capacity(self):
        buffer_two = CircularBuffer(2)
        self.assertEqual(2, buffer_two.get_capacity())

    def test_is_full(self):
        self.fill_the_queue(0, self.buffer.get_capacity())
        self.assertTrue(self.buffer.is_full())

    def test_empty_to_full_to_empty(self):
        self.fill_the_queue(100, self.buffer.get_capacity())
        self.assertTrue(self.buffer.is_full())
        self.remove_from_queue(self.buffer.get_capacity())
        self.assertTrue(self.buffer.is_empty())

    def test_wrap_around(self):
        self.fill_the_queue(100, self.buffer.get_capacity())
        self.assertTrue(self.buffer.is_full())
        self.assertEqual(100, self.buffer.get())
        self.assertFalse(self.buffer.is_full())
        self.buffer.put(1000)
        self.assertTrue(self.buffer.is_full())
        
        self.remove_from_queue(self.buffer.get_capacity() - 1)
        self.assertEqual(1000, self.buffer.get())
        self.assertTrue(self.buffer.is_empty())

    def test_put_to_full(self):
        current_capacity = self.buffer.get_capacity()
        self.fill_the_queue(900, current_capacity)
        self.buffer.put(9999)

        for i in range(current_capacity - 1):
            self.assertEqual(i + 900 + 1, self.buffer.get())

        self.assertEqual(9999, self.buffer.get())
        self.assertTrue(self.buffer.is_empty())

    def test_get_from_empty(self):
        self.assertEqual(-1, self.buffer.get())
        self.assertTrue(self.buffer.is_empty())
    
# using mock object
    def test_print_empty(self):
        my_printer = MockPrinter()
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<>\n",
            my_printer.get_output())

    def test_print_after_one_put(self):
        my_printer = MockPrinter()
        self.buffer.put(1)
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<1>\n",
            my_printer.get_output())

    def test_print_not_yet_wrapped_or_full(self):
        my_printer = MockPrinter()
        self.buffer.put(1)
        self.buffer.put(2)
        self.buffer.put(3)
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<1, 2, 3>\n",
            my_printer.get_output())

    def test_print_not_yet_wrapped_and_is_full(self):
        my_printer = MockPrinter()
        self.fill_the_queue(200, self.buffer.get_capacity())
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<200, 201, 202, 203, 204>\n",
            my_printer.get_output())

    def test_print_wrapped_and_is_full_oldest_to_newest(self):
        my_printer = MockPrinter()
        self.fill_the_queue(200, self.buffer.get_capacity())
        self.buffer.get()
        self.buffer.put(999)
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<201, 202, 203, 204, 999>\n",
            my_printer.get_output())

    def test_print_wrapped_and_full_overwrite_oldest(self):
        my_printer = MockPrinter()
        self.fill_the_queue(200, self.buffer.get_capacity())
        self.buffer.put(9999)
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<201, 202, 203, 204, 9999>\n",
            my_printer.get_output())

    def test_print_boundfary(self):
        my_printer = MockPrinter()
        self.fill_the_queue(200, self.buffer.get_capacity())
        self.remove_from_queue(self.buffer.get_capacity() - 2)
        self.buffer.put(888)
        self.fill_the_queue(300, self.buffer.get_capacity() - 1)
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<888, 300, 301, 302, 303>\n",
            my_printer.get_output())

    def test_fill_empty_then_print(self):
        my_printer = MockPrinter()
        self.fill_the_queue(200, self.buffer.get_capacity())
        self.remove_from_queue(self.buffer.get_capacity())
        self.buffer.print(my_printer)
        self.assertEqual("Circular buffer content:\n<>\n",
            my_printer.get_output())


    def test_remain_after_creation(self):
        self.assertEqual(self.buffer.remain(), self.buffer.get_capacity())

    def test_remain_after_full(self):
        self.fill_the_queue(0, self.buffer.get_capacity())
        self.assertEqual(self.buffer.remain(), 0)

    def test_remain_after_wrap_around_and_get_a_few(self):
        self.fill_the_queue(0, self.buffer.get_capacity())
        self.remove_from_queue(3)
        self.assertEqual(self.buffer.remain(), 3)

    def test_remain_after_wrap_around_and_get_a_few_and_put_one(self):
        self.fill_the_queue(0, self.buffer.get_capacity())
        self.remove_from_queue(3)
        self.buffer.put(10)
        self.assertEqual(self.buffer.remain(), 2)

    def test_remain_after_wrap_around_and_get_a_few_and_get_one(self):
        self.fill_the_queue(0, self.buffer.get_capacity())
        self.remove_from_queue(3)
        self.buffer.get()
        self.assertEqual(self.buffer.remain(), 4)

    def test_remain_after_full_and_empty(self):
        self.fill_the_queue(0, self.buffer.get_capacity())
        self.remove_from_queue(self.buffer.get_capacity())
        self.assertEqual(self.buffer.remain(), self.buffer.get_capacity())

    def test_remain_after_one_put(self):
        self.buffer.put(1)
        self.assertEqual(self.buffer.remain(), (self.buffer.get_capacity() - 1))

    def test_remain_after_put_a_few(self):
        self.buffer.put(1)
        self.buffer.put(2)
        self.buffer.put(3)
        self.assertEqual(self.buffer.remain(), (self.buffer.get_capacity() - 3))

    def test_remain_after_put_a_few_and_one_get(self):
        self.buffer.put(1)
        self.buffer.put(2)
        self.buffer.put(3)
        self.buffer.get()
        self.assertEqual(self.buffer.remain(), (self.buffer.get_capacity() - 2))

    def test_remain_after_put_a_few_and_get_a_few(self):
        self.buffer.put(1)
        self.buffer.put(2)
        self.buffer.put(3)
        self.buffer.get()
        self.buffer.get()
        self.buffer.get()
        self.assertEqual(self.buffer.remain(), self.buffer.get_capacity())

    def test_remain_after_put_a_few_and_one_get_and_put_a_few(self):
        self.buffer.put(1)
        self.buffer.put(2)
        self.buffer.put(3)
        self.buffer.get()
        self.buffer.put(4)
        self.buffer.put(5)
        self.buffer.put(6)
        self.buffer.put(7)
        self.assertEqual(self.buffer.remain(), 0)


if __name__ == "__main__":
  unittest.main() # run all tests
