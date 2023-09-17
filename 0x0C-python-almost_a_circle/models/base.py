#!/usr/bin/python3
"""
a module to create a class called base
"""
import json
import csv


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
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance from a dictionary
        """
        if cls.__name__ == "Square":
            crt = cls(1)
        else:
            crt = cls(1, 1)
        crt.update(**dictionary)
        return (crt)

    @classmethod
    def   load_from_file(cls):
        """
        Return a list of classes from a file of json strings
        """
        File = cls.__name__ + ".json"
        try:
            with open(File, "r") as file:
                dc = Base.from_json_string(file.read())
                return [cls.create(**a) for a in dc]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serialrizes a list of objects to csv
        """
        lb = list_objs
        File = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        with open(File, "w", newline="") as file:
            if lb is None or len(lb) == 0:
                file.write("[]")
            else:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for a in lb:
                    writer.writerow(a.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        creates instances of  classes from a csv file
        """
        File = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]
        try:
            with open(File, "r", newline="") as file:
                reader = csv.DictReader(file, fieldnames=fieldnames)
                ls = [dict([k, int(v)] for k, v in a.items()) for a in reader]
                return [cls.create(**a) for a in list(ls)]
        except IOError:
            return []
