import unittest
from HW_Tailakov_Class_Number import Number

class NumberTests(unittest.TestCase):
    def setUp(self):
        self.number = Number(10)

    def test_set_value(self):
        self.number.set_value(20)
        self.assertEqual(self.number.get_value(), 20)

    def test_to_octal(self):
        self.assertEqual(self.number.to_octal(), '0o12')

    def test_to_hexadecimal(self):
        self.assertEqual(self.number.to_hexadecimal(), '0xa')

    def test_to_binary(self):
        self.assertEqual(self.number.to_binary(), '0b1010')


if __name__ == '__main__':
    unittest.main()