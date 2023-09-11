#!/usr/bin/python3
"""
Module contains an inherited class
"""


class MyList(list):
    """MyList inherits from list"""

    def __init__(self):
        """Instatiation of attributes and classes"""
        list.__init__(self)

    def print_sorted(self):
        print(sorted(self))
