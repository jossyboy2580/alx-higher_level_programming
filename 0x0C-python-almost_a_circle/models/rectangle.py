#!/usr/bin/python3
"""
A module for a Rectangle
"""
import base


class Rectangle(base.Base):
    """
    A class definition for a rectangle object
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(self)
        self.width(width)

    @property
    def width():
        return (self.__width)

    
    @setter.width
    def width(self, value):
        self.__width = value
