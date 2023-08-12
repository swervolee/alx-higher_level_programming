#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Len = len(my_list)

    List = my_list[:]

    if (idx >= 0) and (idx < Len):
        List[idx] = element
    return (List)
