#!/usr/bin/python3


"""a class that defines a square"""


class Square:
    """adds exception to the class square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not (isinstance(value[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 > value[1]):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for a in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
