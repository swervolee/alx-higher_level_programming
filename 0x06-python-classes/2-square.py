#!/usr/bin/python3

"""a class that defines a square"""


class Square:
    """adds exception to the class square"""

    def __init__(self, size=0):

        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
