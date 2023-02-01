#!/usr/bin/python3
"""MyList class file"""


class MyList(list):
    """function in class to print sorted list"""
    def print_sorted(self):
        print(sorted(self))
