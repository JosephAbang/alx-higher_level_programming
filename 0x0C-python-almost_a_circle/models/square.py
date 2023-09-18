#!/usr/bin/python3
"""Module contains class named square"""
from rectangle import Rectangle


class Square(Rectangle):
    """class Swuare inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = val

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
