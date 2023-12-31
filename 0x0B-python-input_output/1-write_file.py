#!/usr/bin/python3
"""a module to write a file and return the number of characters
that have been copied
"""


def write_file(filename="", text=""):
    """
    writes text to fileme.
    if the file does not exist, its created and if it exists
    its contents are overwritten

    Args

    file_name - the name of the file
    txt - the context to write to filename
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        size = file.write(text)

    return (size)
