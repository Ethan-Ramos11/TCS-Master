import unittest
from calculator import calculate


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        """Test addition operation"""
        self.assertEqual(calculate(2, 3, '+'), 5)
        self.assertEqual(calculate(-1, 1, '+'), 0)
        self.assertEqual(calculate(0, 0, '+'), 0)

    def test_subtraction(self):
        """Test subtraction operation"""
        self.assertEqual(calculate(5, 3, '-'), 2)
        self.assertEqual(calculate(1, 1, '-'), 0)
        self.assertEqual(calculate(0, 5, '-'), -5)

    def test_multiplication(self):
        """Test multiplication operation"""
        self.assertEqual(calculate(2, 3, '*'), 6)
        self.assertEqual(calculate(-2, 3, '*'), -6)
        self.assertEqual(calculate(0, 5, '*'), 0)

    def test_division(self):
        """Test division operation"""
        self.assertEqual(calculate(6, 2, '/'), 3)
        self.assertEqual(calculate(5, 2, '/'), 2.5)
        self.assertEqual(calculate(0, 5, '/'), 0)

    def test_division_by_zero(self):
        """Test division by zero error"""
        with self.assertRaises(ZeroDivisionError):
            calculate(5, 0, '/')

    def test_invalid_operation(self):
        """Test invalid operation error"""
        with self.assertRaises(ValueError):
            calculate(5, 3, '%')


if __name__ == '__main__':
    unittest.main()
