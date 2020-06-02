from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    """Test that two num are addedd together"""
    def test_add_two_num(self):
        self.assertEqual(add(3,8),11)

    def test_subtract_numbers(self):
        """Test that two num are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)
