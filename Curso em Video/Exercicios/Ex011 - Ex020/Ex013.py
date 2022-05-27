# Make an algorithm that reads an employee's salary and displays their new salary, with a 15% increase.

salary = float(input("Enter the employers salary to be readjusted: "))
readjust = 15
salary_readjust = salary * (1+(readjust/100))
print(f"the salary is {salary}, with the readjust will be {salary_readjust:.4}")
