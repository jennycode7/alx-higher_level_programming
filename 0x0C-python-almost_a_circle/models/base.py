#!/usr/bin/python3
"""
A module
"""
import json


class Base:
    """
    A class Base
    foundation for other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize self
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a JSON string representation of the object
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the list of objects in a file
        The filename must be: <Class name>.json
        """
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs]))
