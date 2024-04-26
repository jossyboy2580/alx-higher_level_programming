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
        to json string
        """
        if not list_dictionaries or not isinstance(list_dictionaries, list):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
