#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square is rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def __str__(self):
        """str"""
        tangles = "[Square] " + "({}) ".format(self.id)
        tangles = tangles + "{}/{} - ".format(self.x, self.y)
        tangles = tangles + "{}".format(self.width)
        return (tangles)

    def update(self, *args, **kwargs):
        """update"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for ii in range(len(args)):
                setattr(self, attrs[ii], args[ii])
        else:
            for ky, vl in kwargs.items():
                setattr(self, ky, vl)
