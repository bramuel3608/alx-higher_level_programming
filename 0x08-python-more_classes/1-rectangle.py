#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """class constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width property"""
        return self.__width

    @property
    def height(self):
        """getter height property"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter width property"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """setter height property"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be  >= 0')
        self.__height = value
