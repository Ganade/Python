# Develop a program that reads a student's two grades, calculates and displays their average.

grade_1 = float(input("Enter the first grade: "))   # Reads the first grade.
grade_2 = float(input("Enter the second grade: "))  # Reads the second grade.
average = (grade_1 + grade_2) / 2   # Calculates the average between the first and second grade
print(f"the student school average is {average:.3}")    # show the student's average
