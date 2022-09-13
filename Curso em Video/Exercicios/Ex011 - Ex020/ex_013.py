# Make an algorithm that reads an employee's salary and displays their new salary, with a 15% increase.

salary = float(input("Enter the employers salary to be readjusted: "))  # Salary of the employer
readjust = 15   # How much will be to readjust
salary_readjust = salary * (1+(readjust/100))   # Calculates to readjust
print(f"the salary is {salary}, with the readjust will be {salary_readjust:.4}")
