"""
Exercise 16 - breaking a number
"""
# make a program that reads any real number from the keyboard and displays its entire portion on the
# screen.

from math import floor

numb = float(input("Enter a real number please: "))
entire_number = floor(numb)
print(f"you typed the number {numb} and its integer part is {entire_number}")
