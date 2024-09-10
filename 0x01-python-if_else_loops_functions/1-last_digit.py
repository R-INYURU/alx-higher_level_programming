#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mod = (number * -1) % 10
    print(f"Last digit of {number} is {-mod} and is less than 6 and not 0")
elif number > 0:
    mod = number % 10
    if mod > 5:
        print(f"Last digit of {number} is {mod} and is greater than 5")
    elif mod == 0:
        print(f"Last digit of {number} is {mod} and is 0")
    elif mod < 6:
        print(f"Last digit of {number} is {mod} and is less than 6 and not 0")
elif number == 0:
    print(f"Last of digit of {number} is 0 and is 0")
