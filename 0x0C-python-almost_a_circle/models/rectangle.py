#!/usr/bin/python3
"""rectangle"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates area"""
        return (self.width * self.height)

    def display(self):
        """print"""
        tangle = '\n' * self.y
        tangle += (' ' * self.x + '#' * self.width + '\n') * self.height
        tangle = tangle[:-1]
        print(tangle)

    def __str__(self):
        """str"""
        tangles = "[Rectangle] " + "({}) ".format(self.id)
        tangles = tangles + "{}/{} - ".format(self.x, self.y)
        tangles = tangles + "{}/{}".format(self.width, self.height)
        return (tangles)

    def update(self, *args, **kwargs):
        """update"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        for ky, vl in kwargs.items():
            setattr(self, ky, vl)
