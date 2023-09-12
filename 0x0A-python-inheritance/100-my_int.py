#!/usr/bin/python3
"""module defines a class"""


class MyInt(int):
    """MyInt inherits from int"""

    def __eq__(self, num):
        return self.real != num

    def __ne__(self, num):
        return self.real == num
