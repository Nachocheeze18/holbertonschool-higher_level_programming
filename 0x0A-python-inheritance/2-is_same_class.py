#!/usr/bin/python3
"""is same class file"""


def is_same_class(obj, a_class):
    """function test"""
    if (a_class is type(obj)):
        return True
    else:
        return False
