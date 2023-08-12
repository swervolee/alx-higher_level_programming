#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if (length == 0):
        return(None)
    greatest = my_list[0]

    for i in range(length):
        if (my_list[i] > greatest):
            greatest = my_list[i]
    return (greatest)
