#!/usr/bin/python3
"""Module contains class named square"""
from rectangle import Rectangle


class Square(Rectangle):
    """class Swuare inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
