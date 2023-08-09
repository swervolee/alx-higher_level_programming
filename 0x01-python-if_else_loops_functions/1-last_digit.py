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
    print("Last digit of {} is {} and is zero".format(number, d))
else:
    print("Last digit of {} is {} and is less than 6 nd not 0".format(number, d))
