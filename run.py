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
