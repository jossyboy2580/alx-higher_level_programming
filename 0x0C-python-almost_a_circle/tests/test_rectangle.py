#!/usr/bin/python3
"""
This is a test module for the rectangle class
"""
from models.rectangle import Rectangle
import unittest


class Test_Rectangle(unittest.TestCase):
    """
    This test class contains a series of tests for all
    the cases in our Rectangle class
    """

    def setup(self):
        r1 = Rectangle(
