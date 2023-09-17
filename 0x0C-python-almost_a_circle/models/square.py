#!/usr/bin/python3
"""
a class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class square that is a subclass of the class Rectangle

    Args

    size - (int) the size of the square
    x/y - (int) the cordinates
    id - (int) the class id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructot
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the values of the object

        Args:
        args is a nonekeyworded input eg a number 5
        kwargs is keyworded and is of type dictionary
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
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        returns a dictionary representation
        """
        dc = {
            "id" : self.id,
            "size": self.size,
            "x" : self.x,
            "y" : self.y
            }
        return (dc)
