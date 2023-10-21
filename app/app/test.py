"""
sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
        """Test subtract function"""
        res = calc.subtract(6, 4)

        self.assertEquals(res, 2)

    def test_multiply_numbers(self):
        """Multiply two function"""
        res = calc.multiply(6, 5)

        self.assertEquals(res, 36)
