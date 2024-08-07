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
        student_dict = dict()

        if attrs and type(attrs) is list:
            for key in attrs:
                try:
                    student_dict[key] = self.__dict__[key]
                except KeyError:
                    pass
        else:
            student_dict = vars(self)
        return student_dict
