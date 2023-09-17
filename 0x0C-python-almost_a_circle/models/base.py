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
