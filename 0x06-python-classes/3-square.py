#!/usr/bin/python3
"""Square class that defines a square
   private instance attribute: size
   public instance method that defines area
"""
class Square:
	"""class constructor"""
	def __init__(self, size=0):

	   if type(size) != int:
	     raise TypeError("size must be an integer")
	   if size < 0:
	     raise ValueError("size must >= 0")
	   self.__size = size

	"""returns the current square area"""
	def area(self):
	    return self.__size * self.__size
