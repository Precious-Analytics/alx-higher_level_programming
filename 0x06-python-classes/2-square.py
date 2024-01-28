#!/bin/usr/python3

"""Define a class called Square."""

class Square:
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square (default is 0).
                         Must be a non-negative integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        """Use double underscore to make 'size' a private attribute."""
        self.__size = size

        """Check if 'size' is an integer."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """Check if 'size' is non-negative."""
        elif size < 0:
            raise ValueError("size must be >= 0")
