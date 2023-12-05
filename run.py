import random # Random doc. https://www.w3schools.com/python/module_random.asp
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

    return random.choice(game_words)


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
            print(f"{letter} ", end="")
        else:
            print("_ ", end="")


def take_guess(used_letters):
    """
    Takes input from the user to guess the letters.
    """
    while True:
        guess = input("Guess letter here: ")
        if guess.isalpha() and len(guess) == 1:
            if guess in used_letters:
                print(f"You already guessed {guess}. Try a different letter.")
            else:
                print(f"You guessed {guess}")
                return guess
        else:
            print(f"You entered {guess}, please enter a single letter, a-z.")


def lives(lives_left):
    """
    Keep track of how many lives are left and draw the hangman.
    Backslash info found here:
    https://sites.pitt.edu/~naraehan/python3/mbb6.html
    """
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
