#!/usr/bin/python3
"""Class square that defines a square
   Private instance: size
   size must an integer
"""
class Square:
	"""class constuctor"""
	def __init__(self, size=0):
		self.__size = size
		if type(size) != int:
		  raise TypeError("size must be an integer")
		if size < 0:
		  raise ValueError("size must be <= 0")
