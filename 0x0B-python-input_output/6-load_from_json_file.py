#!/usr/bin/python3

"""
a module thats reads an object from a json file
"""


def load_from_json_file(filename):
    """
    a function that creates an object from a json file

    Args:
    filename - the file to read the object from

    return - an object
    """

    import json

    with open(filename, mode="r", encoding="utf-8") as file:
        ob = json.load(file)

    return (ob)
