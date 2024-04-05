#!/usr/bin/python3
"""Defining an int add func."""

def add_integer(a, b=98):
    """add of a and b.

    Float args switched to ints before addition.

    Exception:
        TypeError if a or b are non int and non float.
        """

        if ((not_isinstance(a, int) and not isinstance(a, float))):
            raise TypeError("a must be an integer")
        if ((not_isinstance(b, int) and not isinstance(b, float))):
            raise TypeError("b must be an integer")
        retutn (int(a) + int(b))
