#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv)
    if (l == 2):
        print("{} arguement".format(l - 1))
    elif (l == 1):
        print("{} arguements.".format(l - 1))
    else:
        print("{} arguements:".format(l - 1))

    
