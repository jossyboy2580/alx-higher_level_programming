#!/usr/bin/python3
"""
A module that contains the definition of a MyInt
class
"""


class MyInt(int):
    """
    A MyInt class that inherits from
    the int type
    """

    def __eq__(self, other):
        if self.real == other.real:
            return (False)
        else:
            return (True)

    def __ne__(self, other):
        if self.real != other.real:
            return (False)
        else:
            return (True)
