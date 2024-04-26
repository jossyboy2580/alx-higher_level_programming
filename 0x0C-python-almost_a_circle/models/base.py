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

    @staticmethod
    def from_json_string(json_string):
        """
        This static method takes a supposedly
        json string and returns a list of dictionary
        from it
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object from this dictionary
        """
        if cls.__name__ == 'Square':
            dummy = cls(4)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(4, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        This class method returns a list of
        instances from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="utf-8") as fp:
                list_objs_read = fp.read()
        except FileNotFoundError:
            list_objs_read = "[]"
        finally:
            list_objs = from_json_string(list_objs_read)
            objs_array = cls.create(list_objs)
            return objs_array
