import time

from functions import slowP



def welcome():
    """
    Welcome message and description for the user
    """
    slowP('Welcome to the Adventure Game: The Nightmare!', 2)
    slowP('As you fall asleep, you enter a terrible nightmare', 2)
    slowP('To be able wake up, you need to find the way out', 2)
    slowP('There are different paths to choose from to find your way out', 2)
    slowP("But first, who does this nightmare belong too?", 2)


def get_name():
    """
    Ask for the user's name and validate it to not be empty
    """
    name = input('Please enter your name:')
    if name != '':
        print(f'Good luck, {name}.\n')
        intro()
    else:
        print("Don't you have a name?")
        get_name()

def intro():
    """
    The start of the game, where the user have to choose a path.
    
    
    """
    directions = ['left', 'forward', 'right']
    slowP('You are standing in a square room.', 2)
    slowP('The room is cold and dark and made of concrete.', 2)
    slowP('You look around and you see 4 doors, 1 on each wall', 2)
    answer = ""
    while answer not in directions:
        slowP('Which door do you choose? (left/forward/right/backward)', 2)
        #Converts player's input to lower case
        answer = input().lower().strip()
        if answer == 'left':
            slowP('You are slowly walking towards the left door', 2)
            slowP('You reach the handle and open the door and step inside', 2)
            leftRoom()
        elif answer == 'forward':
            slowP('You are slowly walking towards the middle door', 2)
            slowP('You reach the handle and open the door and step inside', 2)
            forwardRoom()
        elif answer == 'right':
            slowP('You are slowly walking towards the door on your right', 2)
            slowP('You reach the handle and open the door and step inside', 2)
            rightRoom()
        elif answer == 'backward':
            slowP('You open the door and just see a concret wall', 2)
            slowP('You have to choose another door', 2)
        else:
            print('Please choose a valid path')


welcome()
get_name()