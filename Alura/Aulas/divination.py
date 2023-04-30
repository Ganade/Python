print("*******************************")
print("Welcome to the divination game.")
print("*******************************")

secret_number = 43
attempts = 5

for rounds in range(1, attempts + 1):
    print("Round {} of {}".format(rounds, attempts))
    number_typed = int(input("Type a number between 1 to 100: "))
    if number_typed < 1 or number_typed > 100:
        print("You should type a number between 1 to 100")
        continue
    win = number_typed == secret_number
    higher = number_typed > secret_number

    print("You typed:", number_typed, ".")

    if win:
        print("You got the number right.")
        print("***You Win***")
        break
    else:
        if higher:
            print("You got the number wrong, you typed a higher number.")
        else:
            print("You got the number wrong, you typed a lower number.")
