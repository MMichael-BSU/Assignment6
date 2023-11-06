import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(3, 5), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(10, 7), 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(4, 6), 24)

    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertIsNone(self.calculator.divide(5, 0))

    def test_division_float(self):
        self.assertAlmostEqual(self.calculator.divide(5,2), 2.5)


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return None
        return x / y



if __name__ == '__main__':
    unittest.main()



TestCalculator()