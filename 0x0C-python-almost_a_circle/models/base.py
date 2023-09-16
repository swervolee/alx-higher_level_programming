#!/usr/bin/python3
"""
a module to create a class called base
"""


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
