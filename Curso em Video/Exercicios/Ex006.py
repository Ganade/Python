# Create an algorithm that reads a number and displays its double, triple, and square root.

import math

n = float(input("Enter a value for double, triple, and square root calculations: "))
double = n * 2  # Calculates double of variable n
triple = n * 3  # Calculates triple of variable n
root_multiplying = n ** 0.5  # Calculates the square root of variable n using multiplication
root_sqrt = math.sqrt(n)      # Calculates the square root of variable n using math.sqrt
root_pow = math.pow(n, 1/2)   # Calculates the square root of variable n using math.pow
print(f"for the value {n:.2f} the double is {double:.2f}, the triple is {triple:.2f} and the square root is "
      f"{root_multiplying:.2f} using multiplication, "     
      f"{root_sqrt:.2f} using math.sqrt, "
      f"and {root_pow:.2f} using math.pow")
