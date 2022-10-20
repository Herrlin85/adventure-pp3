import time

from functions import slowPrint



def welcome():
    """
    Welcome message and description for the user
    """
    slowPrint('Welcome to the Adventure Game: The Nightmare!', 3)
    slowPrint('As you fall asleep, you enter a terrible nightmare', 3)
    slowPrint('To be able wake up, you need to find the way out', 3)
    slowPrint('There are different paths to choose from to find your way out', 3)
    slowPrint("Let's start with your name: ", 3)


def get_name():
    """
    Ask for the user's name and validate it to not be empty
    """
    name = input('Please enter your name:')
    if name != '':
        print(f'Good luck, {name}.\n')
        intro()
    else:
        print('Who does this nightmare belong too? Please enter your name')


def intro():
    """
    The start of the game, where the user have to choose a path
    """
    directions = ['left', 'right', 'forward']
    slowPrint('You are standing in a square room.', 3)
    slowPrint('The room is cold and dark and made of concrete.', 3)
    slowPrint('You look around and you see 4 doors, 1 on each wall', 3)
    userInput = ""
    while userInput not in directions:
        slowPrint('Which door do you choose? ', 3)


welcome()
get_name()