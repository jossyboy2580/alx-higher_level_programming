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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to json string
        """
        if not isinstance(list_dictionaries, list):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the json representation yo a file
        """
        list_to_save = []
        if list_objs is not None:
            for obj in list_objs:
                list_to_save.append(obj.to_dictionary())
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as fp:
            fp.write(cls.to_json_string(list_to_save))
            fp.close()
