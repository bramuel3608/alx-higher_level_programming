#!/usr/bin/python3
"""class Square that defines asquare
Private instance attribute:size
Property def size(self) to retreive it
Prperty setter def size(self, value)
Private instance attribute position
Property def position(self):to retreive it
Property setter def psition(self, value): to set it
Public instance method def area(self): returs area
Public instance variable def my_print(self):prints the stdout
the asquare with character #
"""


class Square:
    """class constractor"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """Property getter"""
    @property
    def size(self):
        return self.__size

    """Property setter"""
    def size(size, value):
        self.__size = value
        if not instance(value, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must >= 0')

    """Property getter"""
    def position(self):
        return self.__position

    """Property setter"""
    def position(self, value):
        if not (instance(size, tuple) or
                len(value) != 2 or
                not all(instance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """Returns area"""
    def area(self):
        return self.__size * self.__size

    """Prints stdout the square with  # character"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
