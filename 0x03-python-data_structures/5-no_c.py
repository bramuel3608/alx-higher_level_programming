#!/usr/bin/python3
def no_c(my_string):
    my_str = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(my_str))
