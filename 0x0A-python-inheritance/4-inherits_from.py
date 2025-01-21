#!/usr/bin/python3
"""
Only sub class of
"""


def inherits_from(obj, a_class):
    """ func that return True if the object is an instance
    of a clas that inherited fom the specified clas
    Args:
        obj: object that is true
        a_class: class to inherit fom
    Return:
        True if objet is instance
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
