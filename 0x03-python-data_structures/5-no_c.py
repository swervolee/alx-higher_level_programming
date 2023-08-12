#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    length = len(my_string)

    for i in range(length):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]
    return new_string
