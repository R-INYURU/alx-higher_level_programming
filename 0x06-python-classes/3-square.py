#!/usr/bin/python3
""" Square Class init size and def square area """


class Square:
    """ Sqaure Class init size and def square area """

    def __init__(self, size=0):
        """initialize square
        Args:
        size (init); size of the sqaure
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """retuns the area
        Returns:
        area
        """
        return self.__size**2
