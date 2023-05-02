import random

print("*******************************")
print("Welcome to the guessing game.")
print("*******************************")

secret_number = random.randint(1, 100)
difficulty = int(input("choose a difficulty (1)Easy (2)Medium (3)Hard: "))

while True:
    if difficulty == 1:
        attempts = 7
        break
    elif difficulty == 2:
        attempts = 5
        break
    elif difficulty == 3:
        attempts = 3
        break
    else:
        difficulty = int(input("You enter a invalid number, choose a difficulty (1)Easy (2)Medium (3)Hard: "))

for rounds in range(1, attempts + 1):
    print(f"Round {rounds} of {attempts}")
    number_typed = int(input("Type a number between 1 to 100: "))
    if number_typed < 1 or number_typed > 100:
        print("You should type a number between 1 to 100")
        continue

    print(f"You typed: {number_typed}.")

    if number_typed == secret_number:
        print("You got the number right.")
        print("***You Win***")
        break
    else:
        if number_typed > secret_number:
            print("You got the number wrong, you typed a higher number.")
        else:
            print("You got the number wrong, you typed a lower number.")
