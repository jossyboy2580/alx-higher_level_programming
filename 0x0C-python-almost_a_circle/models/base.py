#!/usr/bin/python3
"""
A package for models
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        to_json_string is a method that returns the json
        string representation
        of list_dictionaries
        """
        if not list_dictionaries of len(list_dictionaries) < 1:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    def save_to_file(cls, list_objs):
        pass
