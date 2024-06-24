#!/usr/bin/python3
"""Class Square with a
private instance attribute: size
public instance method: returns square area
public instance method: prints in stdout
with square character #
"""


class Square:
    """Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be => 0')
        self.__size = size

    """Size getter"""
    @property
    def size(self):
        return self.__size

    """Size setter"""
    def size(size, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be => 0')
        self.__size = value

    """Returns area"""
    def area(self):
        return self.__size * self__size

    """Prints stdout the square with character #"""
    def my_print(self):
        if self.size != 0:
            for ch in range(self.__size):
                print('#' * self.__size)

            else:
                print()
