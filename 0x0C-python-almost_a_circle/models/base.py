#!/usr/bin/python3
"""
A package for models
"""


class Base:
    """
    A base Model
    """

    __no_objects = 0

    def __init__(self, id=None):
        """ Class object initializer """
        if id is not None:
            self.id = id
        else:
            Base.__no_objects += 1
            self.id = Base.__no_objects
