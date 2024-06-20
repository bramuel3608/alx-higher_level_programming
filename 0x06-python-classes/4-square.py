#!/usr/bin/python3
"""class Square that defines a square
Private instance attribute: size
Property def (size): to retreive it
Proerty setter def size(self, value): to set it
instantiation size:def __init__(self, size)
"""
class Square:
	"""class constuctor"""
	def __init__(self, size=0):
		if type(size) != int:
			raise TypeError("size must be an integer")
		if size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size

	"""Size getter"""
	@property
	def size(self):
		return self.__size

	"""Size setter"""
	@size.setter
	def size(self, value):
		if type(value) != int:
			raise TypeError("size must be an integer")
		if value < 0:
			raise ValueError("size must be >= 0")
		self.__size = value

	"""returns the current square area"""
	def area(self):
		return self.__size * self.__size
