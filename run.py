import random  # Random doc. https://www.w3schools.com/python/module_random.asp
import sys
from words import words


LEVEL_EASY = 5
LEVEL_MEDIUM = 6
LEVEL_HARD = 7


def welcome_game_select():
    """
    Display welcome message and ask user to select game mode.
    Based on user input select appropriate word and start game.
    """
    print("Welcome to this game of Hangman!\n")
    print("Pick a difficulty and start playing, either win or get hung!")
    print("Press '1', '2', or '3' followed by Enter to select game mode.\n")
    print("1 = Easy, 2 = Medium, 3 = Hard\n")

    while True:
        game_select = input("Select game mode here:\n")
        if game_select in ["1", "2", "3"]:
            break
        else:
            print(f"Please select 1, 2 or 3. You pressed {game_select}")

    if game_select == "1":
        print("You selected Easy, your word contains 5 letters.")
        word = game_word(LEVEL_EASY)
    elif game_select == "2":
        print("You selected Medium, your word contains 6 letters.")
        word = game_word(LEVEL_MEDIUM)
    else:
        print("You selected Hard, your word contains 7 letters or more.")
        word = game_word(LEVEL_HARD)

    return word


def game_word(difficulty_level):
    """
    Finds the correct length of word depending on game mode
    and then selects a random one to be used for the game.
    """
    if difficulty_level == LEVEL_EASY or difficulty_level == LEVEL_MEDIUM:
        game_words = [word for word in words if len(word) == difficulty_level]
    else:
        game_words = [word for word in words if len(word) > LEVEL_MEDIUM]

    return random.choice(game_words).upper()


def word_field(word, correct_guesses):
    """
    Prints out _ for every letter in the word chosen for each game.
    The underscores will act as placeholders for the letters until
    the player guesses letters correctly.
    end= parameter found here:
    https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
    """
    print("-----------------------------------------------------------")
    print("")

    for letter in word:
        if letter in correct_guesses:
            print(f"{letter.upper()} ", end="")
        else:
            print("_ ", end="")


def take_guess(used_letters):
    """
    Takes input from the user to guess the letters.
    The try block raises a ValueError if input is not in alphabet,
    or the length of the guess is longer than one letter.
    After it checks if letter is already used.
    The method isalpha found here:
    https://www.w3schools.com/python/ref_string_isalpha.asp
    """
    while True:
        try:
            guess = input("\nGuess letter here:\n")
            if not guess.isalpha() or len(guess) != 1:
                raise ValueError(
                    f"Enter a single letter A-Z, you entered {guess}"
                    )

            if guess.upper() in used_letters:
                print(
                    f"You already guessed {guess.upper()}. Try again!"
                    )
            else:
                print(f"You guessed {guess.upper()}")
                return guess.upper()
        except ValueError as e:
            print(f"Invalid input, {e}")


def lives_display_hangman(lives_left, guess, word):
    """
    Draw a new hangman every time the user guesses wrong,
    until they win or lose.
    Backslash info found here:
    https://sites.pitt.edu/~naraehan/python3/mbb6.html
    """
    if guess not in word:
        lives_left -= 1

    if lives_left == 8:
        print("\n")
    elif lives_left == 7:
        print("\n")
        print("\n_____|_____")
    elif lives_left == 6:
        print("\n")
        print("\n     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____|_____")
    elif lives_left == 5:
        print("\n")
        print("\n     ______")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("     |")
        print("_____|_____")
    elif lives_left == 4:
        print("\n")
        print("\n     ______")
        print("     | /")
        print("     |/")
        print("     |")
        print("     |")
        print("     |")
        print("_____|_____")
    elif lives_left == 3:
        print("\n")
        print("\n     ______")
        print("     | /   |")
        print("     |/")
        print("     |")
        print("     |")
        print("     |")
        print("_____|_____")
    elif lives_left == 2:
        print("\n")
        print("\n     ______")
        print("     | /   |")
        print("     |/    O")
        print("     |     |")
        print("     |")
        print("     |")
        print("_____|_____")
    elif lives_left == 1:
        print("\n")
        print("\n     ______")
        print("     | /   |")
        print("     |/    O")
        print("     |   --|--")
        print("     |")
        print("     |")
        print("_____|_____")
    elif lives_left == 0:
        print("\n")
        print("\n     ______")
        print("     | /   |")
        print("     |/    O")
        print("     |   --|--")
        print("     |    / \\")
        print("     |")
        print("_____|_____")


def end_of_game():
    """
    Handles end of game and user can choose to play again or not.
    The exit function was found on stackoverflow:
    https://stackoverflow.com/questions/19747371/python-exit-commands-why-so-many-and-when-should-each-be-used/19747562#19747562
    """
    while True:
        play_again = input("\nWant to play again? Y/N\n")
        if play_again.upper() == "Y":
            main()
        elif play_again.upper() == "N":
            print("Hope you had fun playing, see you next time!")
            sys.exit()
        else:
            print(f"Select Y for yes, or N for no. You selected {play_again}")


def main_game(word):
    """
    Main game loop.
    Lives are displayed both with the hangman, and a number,
    just to make it very clear how many tries you have left.
    This site helped with the join method:
    https://www.w3schools.com/python/ref_string_join.asp
    """
    correct_guesses = []
    used_letters = []
    lives_left = 8

    while lives_left > 0:
        word_field(word, correct_guesses)
        print(f"\nUsed Letters: {', '.join(used_letters)}")
        print(f"\nLives Left: {lives_left}")

        guess = take_guess(used_letters)
        if guess in word:
            print("\nCorrect!")
            correct_guesses.append(guess)
            used_letters.append(guess)
        else:
            print("\nIncorrect!")
            used_letters.append(guess)
            lives_display_hangman(lives_left, guess, word)
            lives_left -= 1

        if all(letter in correct_guesses for letter in word):
            print("--------------------------------------------------------\n")
            print(f"Congratulations! You guessed the word: {word}")
            end_of_game()

    if lives_left == 0:
        print("-----------------------------------------------------------\n")
        print(f"Sorry, you ran out of lives. The correct word was: {word}")
        end_of_game()


def main():
    """
    Start of the game, display welcome message and choose difficulty.
    """
    selected_word = welcome_game_select()
    main_game(selected_word)


main()
