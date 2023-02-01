#!/usr/bin/python3
"""json"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return (vars(self))

        dicto = {}
        for i in attrs:
            try:
                dicto[i] = vars(self)[i]
            except:
                Exception

        return (dicto)
