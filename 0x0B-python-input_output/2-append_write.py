#!/usr/bin/python3

"""
a module that appends to a file the given context
"""


def append_write(filename="", text=""):
    """
    this module appends some text  to a file

    arg:

    filename - the file to append to
    text - the text to append to the file

    Return - the number of characters that have been appendee
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        size = file.write(text)
    return (size)
