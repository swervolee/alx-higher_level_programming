#!/usr/bin/python3
"""
a module to transform a python object to json string
"""

import json


def to_json_string(my_obj):
    """
    transforms a python object to json string

    Args:
    my_obj - the python object

    Return:
    JSON string representation of my_obj
    """
    return (json.dumps(my_obj))
