#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    d = (number % -10)
else:
    d = number % 10
if (d > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, d))
elif (d == 0):
    print("Last digit of {} is {} and is 0".format(number, d))
else:
    print("Last digit of {} is {} ".format(number, d), end="")
    print("and is less than 6 and not 0")
