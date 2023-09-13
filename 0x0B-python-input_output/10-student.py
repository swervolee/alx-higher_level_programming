#!/usr/bin/python3
"""
a class student
"""


class Student:
    """
    a student class
    """
    def __init__(self, first_name, last_name, age):
        """
        innitializez names and age of the student

        Args:

        first_name - the first name of the student

        last_name - the last name of the student

        age - the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        if attrs is not none - returns a dictonary of the specified values
        returns a dictionary representation of self
        """
        if attrs:
            new = {}
            for x, y in self.__dict__.items():
                if x in attrs:
                    new[x] = y
            return (new)
        return self.__dict__.copy()
