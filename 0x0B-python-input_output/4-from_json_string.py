#!/usr/bin/python3
"""
a string to convert a json to a string
"""


def from_json_string(my_str):
    """
    a function to deserialize a json string

    Args:
    my_str - the json input

    return:
    deserialized string
    """
    import json
    return (json.loads(my_str))
