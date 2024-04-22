#!/usr/bin/python3
"""
This is a test module for the rectangle class
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """
    This test class contains a series of tests for all
    the cases in our Rectangle class
    """

    def setup(self):
        """
        Setting up some dependencies for each of our testcases
        """
        b1 = Base()

    def test_base_id(self):
        unittest.assertEqual(b1.id, 1)


if __name__ == "__main__":
    unittest.main()
