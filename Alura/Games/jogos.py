import guessing_game
import hangman_game

print("********************")
print("   Python Games")
print("********************")


def chose_game():
    game = int(input("Chose a game: (1)Guessing or (2)Hangman: "))

    while True:
        if game == 1:
            print("You chose Guessing Game")
            guessing_game.play_guessing()
            break
        elif game == 2:
            print("You chose Hangman Game")
            hangman_game.play_hangman()
            break
        else:
            game = int(input("you enter a invalid number, please (1)Guessing or (2)Hangman "))


if __name__ == "__main__":
    chose_game()
