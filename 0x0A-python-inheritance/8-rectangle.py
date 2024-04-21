#!/usr/bin/python3
"""
Rectangle object representation in
classes defined below
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle object that inherits basegeometry
    """

    def __init__(self, width, height):
        """ class obj initializer """
        try:
            self.integer_validator("width", width)
        except Exception:
            raise
        else:
            self.__width = width
        try:
            self.integer_validator("height", height)
        except Exception:
            raise
        else:
            self.__height = height
