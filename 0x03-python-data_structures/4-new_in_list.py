#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)

    if idx > (len(my_list) - 1):
        return (my_list)
    newlist = [i for i in my_list]
    newlist[idx] = element
    return (newlist)
