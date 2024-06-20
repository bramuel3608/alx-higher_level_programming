#!/usr/bin/python3
"""square class defines a square by
  Private instance attribute size:size
  Instantiation with size (no type/value verification)
"""


class Square:
	"""class constructor"""
	def __init__(self, size):
		self.__size = size
