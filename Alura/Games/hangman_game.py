import random


def play_hangman():
    print_opening_message()
    secret_word = load_secret_word("words.txt")
    right_letters = start_right_letter(secret_word)

    hang = False
    right = False
    mistakes = 0

    print(right_letters)
    while not hang and not right:
        guess = ask_a_guess()

        if guess in secret_word:
            mark_correct_guess(secret_word, guess, right_letters)
        else:
            mistakes += 1
            print(f"You have {7 - mistakes} more attempts")
            drawn_gallows(mistakes)

        hang = mistakes == 7
        right = "_" not in right_letters
        print(right_letters)

    if right:
        print_victory_message()
    else:
        print_defeat_message(secret_word)


def print_opening_message():
    print("*******************************")
    print("Welcome to the hangman game.")
    print("*******************************")


def load_secret_word(text):
    words = []
    with open(text, "r+") as file:
        for line in file:
            line = line.strip()
            words.append(line)

    chosen_word = random.randint(0, len(words) - 1)
    secret_word = words[chosen_word].upper()
    return secret_word


def start_right_letter(word):
    return ["_" for letter in word]


def ask_a_guess():
    guess = input("Guess a letter: ").strip().upper()
    return guess


def mark_correct_guess(secret_word, guess, right_letters):
    position = 0
    for letter in secret_word:
        if guess == letter:
            right_letters[position] = letter
        position += 1


def print_victory_message():
    print("You win!! :-P")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_defeat_message(secret_word):
    print(f"You Lose!! :-( the secret word was {secret_word}")
    print("    _______________          ")
    print("   /               \         ")
    print("  /                 \        ")
    print("//                   \/\     ")
    print("\|   XXXX     XXXX   | /     ")
    print(" |   XXXX     XXXX   |/      ")
    print(" |   XXX       XXX   |       ")
    print(" |                   |       ")
    print(" \__      XXX      __/       ")
    print("   |\     XXX     /|         ")
    print("   | |           | |         ")
    print("   | I I I I I I I |         ")
    print("   |  I I I I I I  |         ")
    print("   \_             _/         ")
    print("     \_         _/           ")
    print("       \_______/             ")


def drawn_gallows(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if mistakes == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if mistakes == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if mistakes == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if mistakes == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if mistakes == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if mistakes == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if mistakes == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play_hangman()
