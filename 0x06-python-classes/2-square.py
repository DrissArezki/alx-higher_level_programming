#!/usr/bin/python3
"""Defining a class named Square."""


class Square:
    """This is a square."""

    def __init__(self, size):
        """Init a new square.


        Arguments are:
            size (int): is the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
