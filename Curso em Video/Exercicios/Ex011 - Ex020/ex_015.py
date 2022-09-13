"""
Exercise 015
"""
# Write a program that asks the number of kilometers traveled by a rented car and the number of
# days for which it was rented. Calculate the price to pay, knowing that the car costs R$60 per
# day and R$0.15 per km driven.

# days of use of the car
days = int(input("Enter the number of days you had the car: "))
# Kilometers drove
kilometers = float(input("Enter the kilometers you ride the car: "))
# calculates the price to be paid
price_to_pay = days * 60 + kilometers * 0.15
print(f"The cost of the rent will be ${price_to_pay}")
