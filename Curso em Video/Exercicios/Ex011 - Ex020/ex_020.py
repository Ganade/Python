"""
Exercise 020 - Sorting a order from the list
The same teacher from challenge 19 wants to draw the order of presentation of students' work. Make a
program that reads the names of the four students and shows the order drawn.
"""

from random import shuffle

# students to be called
STD_1 = str(input("First Student name: "))
STD_2 = str(input("Second Student name: "))
STD_3 = str(input("Third Student name: "))
STD_4 = str(input("Fourth Student name: "))
# Create students list
students = [STD_1, STD_2, STD_3, STD_4]
# Suffle the students list
shuffle(students)
# Show the order of presentation
print(f"The order of presentation is {students}")
