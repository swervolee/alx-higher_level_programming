#!/usr/bin/python3

def list_division(list_1, list_2, length):

    new = []
    for i in range(length):
        try:
            x = list_1[i] / list_2[i]
            new.append(x)
        except IndexError:
            print("out of range")
            new.append(0)
        except ZeroDivisionError:
            print("diviision by 0")
            new.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            new.append(0)
    return (new)
