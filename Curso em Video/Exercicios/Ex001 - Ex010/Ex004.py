# Write a program that reads something on the keyboard and displays its primitive type and all possible information
# about it on the screen.

n = input("Type something: ")  # Read the n variable
print(f"The primitive type of {n} is {type(n)}")  # Shows the primitive type of the variable n
print(f"The value entered is numeric? {n.isnumeric()}")  # Check if what was typed is only numeric
print(f"The value entered is only letters? {n.isalpha()}")  # Check if what was typed is only letters
print(f"The value entered is capital letters only? {n.isupper()}")  # Check that what you type is in uppercase
print(f"The value entered is only lowercase letters? {n.islower()}")  # Check if what was typed is in lower case
print(f"The value entered is alphanumeric? {n.isalnum()}")  # Check if what was typed is alphanumeric
print(f"The value entered is only spaces? {n.isspace()}")  # Check if what was typed is only spaces
