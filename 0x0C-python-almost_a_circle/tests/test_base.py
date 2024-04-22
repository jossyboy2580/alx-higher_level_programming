#!/usr/bin/python3
"""
This is a test module for the rectangle class
"""
import sys
import os
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)
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
        """
        Test if the correct attribute is being assigned
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)


if __name__ == "__main__":
    unittest.main()
