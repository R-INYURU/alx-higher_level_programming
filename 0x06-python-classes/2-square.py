#!/usr/bin/python3
""" Square Class raising error if size is -ve or not a num """


class Square:
    """ Square Class raising error if size is -ve or not a num """

    def __init__(self, size=0):
        """initialise square
        Args:
        size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
