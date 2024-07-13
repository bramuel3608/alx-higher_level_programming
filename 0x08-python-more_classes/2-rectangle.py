#!/usr/bin/python3
"""Class Rectangle
private instance attribute: width
private instance attribute: height
public instance method: def area()
returns area
public insatnce method: def perimeter(self)
returns perimeter
"""


class Rectangle:
    """class constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must >= 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError('height must be an int')

        if value < 0:
            raise ValueError('height must >= 0')
        self.__height = value

    def area(self):
        """Returns Rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns Rectangle perimeter"""
        perimeter = (self.__width + self.__height) * 2
        if self.__width == 0 | self.__height == 0:
            perimeter = 0

        return (perimeter)
