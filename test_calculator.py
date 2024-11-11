import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
        self.assertEqual(self.calc.divide(2, 3), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(2, 3), 2)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()