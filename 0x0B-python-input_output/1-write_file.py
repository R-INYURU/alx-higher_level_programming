#!/usr/bin/python3
""" Function to write text in text file """


def write_file(filename="", text=""):
    """ Write text in a file
    Args:
        filename: filename to write into
        text: text to write in file
    Returns:
        number of written chars
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
