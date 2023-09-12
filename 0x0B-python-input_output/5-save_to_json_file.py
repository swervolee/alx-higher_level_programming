#!/usr/bin/python3
"""
a module to write an object to a file
"""


def save_to_json_file(my_obj, filename):
    """
    a function to write an object to a file

    Args:
    my_obj - the input object
    filename - the file where to write the object

    return - nothing
    """

    import json
    j_object = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(j_object, file)
