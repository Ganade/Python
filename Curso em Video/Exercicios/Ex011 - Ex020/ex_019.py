"""
Exercise 019 - Sorting an item from the list
A teacher wants to draw one of his four students to erase the board. Make a program that helps him
reading the name of the students and writing the name of the chosen one on the screen.
"""

from random import choice

# students to be called
STD_1 = str(input("First Student name: "))
STD_2 = str(input("Second Student name: "))
STD_3 = str(input("Third Student name: "))
STD_4 = str(input("Fourth Student name: "))
# Create students list
students = [STD_1, STD_2, STD_3, STD_4]
# Draw a Student from the list
chosen = choice(students)
# Show the chosen student
print(f"The chosen student was {chosen}")
