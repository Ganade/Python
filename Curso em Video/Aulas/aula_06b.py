"""
Class 06B
"""

n = input("Digite um valor: ")
print(f"The value entered is numérico? {n.isnumeric()}")
print(f"The value entered is  somente letras? {n.isalpha()}")
print(f"The value entered is  somente letras maiúsculas? {n.isupper()}")
print(f"The value entered is  somente letras minusculas? {n.islower()}")
print(f"The value entered is  Alfanumerico? {n.isalnum()}")