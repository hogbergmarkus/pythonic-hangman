import random  # Random doc. https://www.w3schools.com/python/module_random.asp
import sys
from words import words


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
        game_select = input("Select game mode here:")
        if game_select == "1" or game_select == "2" or game_select == "3":
            break
        else:
            print(f"Please select 1, 2 or 3. You pressed {game_select}")

    if game_select == "1":
        word = game_word(5)
    elif game_select == "2":
        word = game_word(6)
    else:
        word = game_word(7)

    return word


def game_word(length):
    """
    Finds the correct length of word depending on game mode
    and then selects a random one to be used for the game.
    """
    if length == 5 or length == 6:
        game_words = [word for word in words if len(word) == length]
    else:
        game_words = [word for word in words if len(word) > 6]

    return random.choice(game_words).upper()


def word_field(word, correct_guesses):
    """
    Prints out _ for every letter in the word chosen for each game.
    The underscores will act as placeholders for the letters until
    the player guesses letters correctly.
    end= parameter found here:
    https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
    """
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
            guess = input("Guess letter here: ")
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


def lives(lives_left, guess, word):
    """
    Keep track of how many lives are left and draw the hangman.
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
    https://stackoverflow.com/questions/40026651/how-to-stop-script-if-user-inputs-certain-characters-python
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
    """
    correct_guesses = []
    used_letters = []
    lives_left = 8

    while lives_left > 0:
        word_field(word, correct_guesses)
        print(f"\nUsed Letters: {', '.join(used_letters)}")
        print(f"Lives Left: {lives_left}")

        guess = take_guess(used_letters)
        if guess in word:
            print("Correct!")
            correct_guesses.append(guess)
            used_letters.append(guess)
        else:
            print("Incorrect!")
            used_letters.append(guess)
            lives(lives_left, guess, word)
            lives_left -= 1

        if all(letter in correct_guesses for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            end_of_game()

    if lives_left == 0:
        print(f"Sorry, you ran out of lives. The correct word was: {word}")
        end_of_game()


def main():
    selected_word = welcome_game_select()
    main_game(selected_word)


main()
