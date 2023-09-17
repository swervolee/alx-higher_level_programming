#!/usr/bin/python3
"""
a module to create a class called base
"""
import json


class Base:
    """
    the class base setup
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor innitialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a JSON representation of list dictionary
        """
        dc = list_dictionaries

        if not dc or len(dc) == 0:
            return "[]"
        return (json.dumps(dc))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        takes a list of objects that inherit from base
        and gets a dictionary representation of those objects
        then changes those dictionary objects to a json representation
        and finally writes that data to a file
        """
        File = cls.__name__ + ".json"
        with open(File, mode="w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                dc = [a.to_dictionary() for a in list_objs]
                file.write(Base.to_json_string(dc))

    @staticmethod
    def from_json_string(json_string):
        """
        deserializes a json string
        """
        if json_string == "[]" or json_string is None:
            return "[]"
        else:
            return (json.loads(json_string))
