#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    leny = len(sys.argv)
    if (leny == 2):
        print("{} argument:".format(leny - 1))
    elif (leny == 1):
        print("{} arguments.".format(leny - 1))
    else:
        print("{} arguments:".format(leny - 1))

    if ((leny - 1) >= 1):
        i = 0
        for a in sys.argv:
            if (i != 0):
                print("{}: {}".format(i, a))
            i += 1
