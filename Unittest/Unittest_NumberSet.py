import unittest
from HW_Tailakov_Class_Number import NumberSet

class NumberSetTests(unittest.TestCase):
    def setUp(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.number_set = NumberSet(self.numbers)

    def test_sum(self):
        self.assertEqual(self.number_set.sum(), sum(self.numbers))

    def test_average(self):
        self.assertEqual(self.number_set.average(), sum(self.numbers) / len(self.numbers))

    def test_maximum(self):
        self.assertEqual(self.number_set.maximum(), max(self.numbers))

    def test_minimum(self):
        self.assertEqual(self.number_set.minimum(), min(self.numbers))


if __name__ == '__main__':
    unittest.main()