n = input("Digite um valor: ")
print(f"O valor digitado é numérico? {n.isnumeric()}")
print(f"O valor digitado é  somente letras? {n.isalpha()}")
print(f"O valor digitado é  somente letras maiúsculas? {n.isupper()}")
print(f"O valor digitado é  somente letras minusculas? {n.islower()}")
print(f"O valor digitado é  Alfanumerico? {n.isalnum()}")