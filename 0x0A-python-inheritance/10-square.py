#!/usr/bin/python3

"""a class that inherits from the rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """innitializes the square"""
        super().__init__(size, size)
