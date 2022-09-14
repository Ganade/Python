"""
Exercise 017
"""
# Write a program that reads the length of the opposite and adjacent sides of a right triangle.
# Calculate and display the length of the hypotenuse.

from math import hypot

# Get the length of the opposite side of the triangle
oppo = float(input("Enter the length of the opposite side of the triangle: "))
# Get the length of the adjacent side of the triangle
adja = float(input("Enter the length of the adjacent side of the triangle: "))
# calculates the length of the hypotenuse
hyp = hypot(oppo, adja)
print(f"The hypotenuse from the triangle entered is {hyp:.2f}")
