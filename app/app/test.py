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

