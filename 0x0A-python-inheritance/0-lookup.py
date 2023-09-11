#!/usr/bin/python3
"""
a module to print the  attributes of a python clas
"""


def lookup(obj):
    """
    a function to list a classes attributes

    args:

    @obj:
    the object input

    @return:
    a list of the objects attributes
    """
    return (dir(obj))
