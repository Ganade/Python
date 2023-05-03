def play_hangman():
    print("*******************************")
    print("Welcome to the hangman game.")
    print("*******************************")

    secret_world = "banana"

    hang = False
    right = False

    while (not hang and not right):
        guess = input("Guess a letter: ").strip().lower()

        position = 1
        for letter in secret_world:
            if guess == letter:
                print(f"letter {letter.upper()} in position {position}")
            position = position + 1

        print("Still Gaming")


if __name__ == "__main__":
    play_hangman()
