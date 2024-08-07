#!/usr/bin/python3

"""Defining a class named Square."""


class Square:
    """This is a square."""

    def __init__(self, size=0):
        """Init a new square.


        Arguments are:
            size (int): is the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Current area of the square."""
        return (self.__size * self.__size)
