#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    argv = sys.argv
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2][0]

    if (c == '+'):
        print("{} + {} = {}".format(a, b, calc.add(a, b)))
    elif (c == '-'):
        print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    elif (c == '*'):
        print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    elif (c == '/'):
        print("{} / {} = {}".format(a, b, calc.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
