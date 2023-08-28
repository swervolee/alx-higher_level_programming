#!/usr/bin/python3

def list_division(list_1, list_2, length):

    new = []
    for i in range(length):
        try:
            x = list_1[i] / list_2[i]
        except IndexError:
            print("out of range")
            x = 0
        except ZeroDivisionError:
            print("diviision by 0")
            x = 0
        except (TypeError, ValueError):
            print("wrong type")
            x = 0
        finally:
            new.append(x)
    return (new)
