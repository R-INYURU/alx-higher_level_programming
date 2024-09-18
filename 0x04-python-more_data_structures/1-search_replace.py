#!/usr/bin/python3
def search_replace(my_list, search, replace):
    this_lst = []
    for i in my_list:
        if i == search:
            this_lst.append(replace)
        else:
            this_lst.append(i)
    return (this_lst)
