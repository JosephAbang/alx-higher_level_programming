#!/usr/bin/python3
"""Module contains a class: rectangle"""
from models.base import Base


class Rectangle(Base):
    """Derived class rectangle from base class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes of instance"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        elif type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        elif type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter for width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        elif val < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = val

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter for height"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        elif val < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = val

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter for x"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter for y"""
        if type(val) != int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        high = self.__height
        wide = self.__width
        x = self.__x
        y = self.__y

        for k in range(y):
            print()
        for i in range(high):
            for m in range(x):
                print(' ', end='')
            for j in range(wide):
                print("#", end='')
            print()

    def __str__(self):
        """implement str() function"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update instance attr of a rectangle"""
        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

    def to_dictionary(self):
        """convert json to dictionary"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
