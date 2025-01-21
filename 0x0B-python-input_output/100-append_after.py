#!/usr/bin/python3
""" append text after certain string """


def append_after(filename="", search_string="", new_string=""):
    """ Insert text after each line with search string
    Args:
        filename: filename
        search_string: string to search for
        new_string: string to append
    """

    res_line = []
    with open(filename) as f:
        for line in f:
            res_line += [line]
            if line.find(seach_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("".join(res_line)
