#!/usr/bin/python3
"""
a class rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The class constructor

        ARGS

        width - (int) the width of the rectangle
        height - (int) the height of the rectangle
        x/y - (int) cordinates
        id - super class inheritance

        RAISES AN EXCEPTION WHEN:
        width/height/x/y is not an integer
        width/height <= 0
        x/y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        calculates and returns the area of a rectangle
        """
        return (self.width * self.height)

    def display(self):
        """
        prints the rectangle using the hash symbol
        """
        w = self.width
        h = self.height

        for _ in range(self.y):
            print("")

        for _ in range(h):
            print(" " * self.x, end="")
            print("".join(["#" for _ in range(w)]))

    def __str__(self):
        """
        returns a string representation of the class
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y,
                 self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Used to set or update the values of the object
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        prints a dictionary representation of the class
        """
        dc = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
        return dc
