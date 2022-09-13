"""
    Class 08A
"""

from math import sqrt
from random import randint

num = int(input("Enter a number: "))
rand = randint(1, 10)
square = sqrt(num)
print(f"the square root of {num} is {square}")
print(f"Your random number is {rand}")
