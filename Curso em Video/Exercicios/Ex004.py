# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

n = input("Digite algo: ")
print(f"O tipo primitivo de {n} é {type(n)}")
print(f"O valor digitado é numérico? {n.isnumeric()}")  # Verifica se oque foi digitado é numérico
print(f"O valor digitado é somente letras? {n.isalpha()}")  # Verifica se oque foi digitado é letras
print(f"O valor digitado é somente letras maiúsculas? {n.isupper()}")  # Verifica se oque foi digitado está em maiúsculas
print(f"O valor digitado é somente letras minusculas? {n.islower()}")  # Verifica se oque foi digitado está em minusculas
print(f"O valor digitado é alfanumerico? {n.isalnum()}") # Verifica se oque foi digitado é alphanumerico
print(f"O valor digitado é somente espaços? {n.isspace()}")  # Verifica se oque foi digitado é somente espaços
