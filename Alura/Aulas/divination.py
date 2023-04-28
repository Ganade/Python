print("*******************************")
print("Welcome to the divination game.")
print("*******************************")

secret_number = 43

number_typed = int(input("Type a number between 1 to 100: "))

print("You typed:",number_typed,".")

if secret_number == number_typed:
    print("You got the number right.")
else:
    print("You got the number wrong.")