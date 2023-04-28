print("*******************************")
print("Welcome to the divination game.")
print("*******************************")

secret_number = 43 #teste
attempts = 5
current_round = 1

while current_round <= attempts:
    print("Round {} of {}".format(current_round, attempts))
    number_typed = int(input("Type a number between 1 to 100: "))

    win = number_typed == secret_number
    higher = number_typed > secret_number

    print("You typed:", number_typed, ".")

    if win:
        print("You got the number right.")
        print("***You Win***")
    else:
        if higher:
            print("You got the number wrong, you typed a higher number.")
        else:
            print("You got the number wrong, you typed a lower number.")
    current_round = current_round + 1
