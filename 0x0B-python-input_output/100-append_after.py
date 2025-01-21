#!/usr/bin/python3
""" append text after certain string """


def append_after(filename="", search_string="", new_string=""):
    """ Insert text after each line with search string
    Args:
        filename: filename
        search_string: string to search for
        new_string: string to append
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
