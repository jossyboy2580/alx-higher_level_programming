#!/usr/bin/python3
"""
A module defining a class MyList that inherits
from list
"""


class MyList(List):
    """
    A class subclassed from the list object
    """

    def print_sorted(self):
        """ A method to print tbe sorted list """
        print(self.sort())
