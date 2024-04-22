#!/usr/bin/python3
"""
This is a test module for the rectangle class
"""
import sys
import os
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_path)
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This test class contains a series of tests for all
    the cases in our Rectangle class
    """

    def test_rectangle_id(self):
        """
        Test if the correct id is being assigned
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 3)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 4)
        r3 = Rectangle(10, 2, 0, 0,12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_validation(self):
        """
        This Test case checks for validation of inputs
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle('223', 'we')
        with self.assertRaises(ValueError):
            r2 = Rectangle(-4, 9)



if __name__ == "__main__":
    unittest.main()
