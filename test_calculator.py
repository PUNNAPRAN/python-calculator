import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(2,5),7)
        self.assertEqual(self.calc.add(2,2),4)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,3),7)
        self.assertEqual(self.calc.subtract(1,3),-2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,5),10)
        self.assertEqual(self.calc.multiply(10,10),100)

    def test_divine(self):
        self.assertEqual(self.calc.divide(100,4),25)
        self.assertEqual(self.calc.divide(3,3),1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,2),0)
        self.assertEqual(self.calc.modulo(10,3),1)

if __name__ == '__main__':
    unittest.main()