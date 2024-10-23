import unittest

from src.calculator import divide, subtract, suma


class TestCalculator(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(14, 90), 104)

    def test_subtract(self):
        self.assertEqual(subtract(14, 90), -76)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
