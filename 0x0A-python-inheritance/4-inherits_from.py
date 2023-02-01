#!/usr/bin/python3
"""subclass"""


def inherits_from(obj, a_class):
    """is subclass"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
