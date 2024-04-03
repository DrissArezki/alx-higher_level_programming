#!/usr/bin/python3

"""Defining a Magic Class exactly as the bytecode by Holberton."""

import math


class MagicClass:
    """This is a circle."""

    def __init__(self, radius=0):
        """init a MagicClass.

        args:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

        def area(self):
            """Area of the MagicClass."""
            return (self.__radius ** 2 * math.pi)

        def circumference(self):
            """Circumfeence of the MagicClass."""
            return (2 * math.pi * self.__radius)
