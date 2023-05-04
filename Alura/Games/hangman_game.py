
import random

def play_hangman():
    print("*******************************")
    print("Welcome to the hangman game.")
    print("*******************************")

    words = []
    with open("words.txt", "r+") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    chose_word = random.randint(0, len(words)-1)
    secret_world = words[chose_word].upper()
    right_letters = ["_" for letter in secret_world]

    hang = False
    right = False
    mistakes = 0

    print(right_letters)
    while not hang and not right:
        guess = input("Guess a letter: ").strip().upper()

        if guess in secret_world:
            position = 0
            for letter in secret_world:
                if guess == letter:
                    right_letters[position] = letter
                position += 1
        else:
            mistakes += 1
            print(f"You have {6 - mistakes} more attempts")

        hang = mistakes == 6
        right = "_" not in right_letters
        print(right_letters)

    if right:
        print("You Win ;-)")
    else:
        print("You lose :-(")


if __name__ == "__main__":
    play_hangman()
