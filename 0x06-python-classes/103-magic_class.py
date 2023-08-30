#!/usr/bin/python3
"""and instance of a circle"""


import math


class MagicClass:
    """defines models on the circle eg area and circumfrence"""

    def __init__(self, radius):
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError("Radius must be int or float")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * (math.pi))

    def circumfrence(self):
        return (2 * math.pi * self.__radius)