import unittest
from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.add(9, 13), 22)
        self.assertNotEqual(self.calc.add(45, 5), 56)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,2), 2)
        self.assertEqual(self.calc.subtract(18, 9), 9)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 30), 150)
    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(80, 8), 10)