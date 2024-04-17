#!/usr/bin/python3
"""
Module for preparing objects for JSON ops
"""


class Student:
    """
    A class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Object initializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert an object to a serializable form
        """
        if attrs and type(attrs) is list:
            varsed = dict()
            for item in attrs:
                varsed[item] = self.__dict__[item]
            return (varsed)
        else:
            return (vars(self))
