#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    else:
        for i in range(len(my_list)):
            if idx == i:
                my_list[i] = element
            else:
                my_list[i] = my_list[i]
        return (my_list)
