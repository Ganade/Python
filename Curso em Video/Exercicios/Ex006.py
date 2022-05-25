# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math

n = float(input("Digite um valor para os calculos de dobro, triplo e de raiz quadrada: "))
dobro = n * 2
triplo = n * 3
raiz_multiplicando = n ** 0.5
raiz_sqrt = math.sqrt(n)
raiz_pow = math.pow(n, 1/2)
print(f"Para o valor {n:.2f} o dobro é {dobro:.2f}, o triplo é {triplo:.2f} e a raiz quadrada é "
      # f"{raiz_multiplicando:.2f}      
      # f"{raiz_sqrt:.2f} "
      f"{raiz_pow:.2f} ")
