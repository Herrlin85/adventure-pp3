"""
import slow print from functions.py
"""
from functions import slow_p

"""
Global variable for weapon
"""
weapon = False


def welcome():
    """
    Welcome message and description for the user
    """
    slow_p('Welcome to the Adventure Game: The Nightmare!', 2)
    slow_p('As you fall asleep, you enter a terrible nightmare', 2)
    slow_p('To be able wake up, you need to find the way out', 2)
    slow_p('There are different paths to choose from to find your way out', 2)
    slow_p("But first, who does this nightmare belong too?", 2)


def get_name():
    """
    Ask for the user's name and validate it to not be empty
    """
    name = input('Please enter your name: ')
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
    slow_p('You are standing in a square room.', 2)
    slow_p('The room is cold and dark and made of concrete.', 2)
    slow_p('You look around and you see 4 doors, 1 on each wall', 2)
    answer = ""
    while answer not in directions:
        slow_p('Which door do you choose? (left/forward/right/backward)', 2)
        answer = input('>> ').lower().strip()
        if answer == 'left':
            slow_p('You are slowly walking towards the left door', 2)
            slow_p('You reach the door and carefully walk inside \n', 2)
            leftRoom()
        elif answer == 'forward':
            slow_p('You decide to take the middle door', 2)
            slow_p('The door is locked', 2)
        elif answer == 'right':
            slow_p('You are slowly walking towards the door on your right', 2)
            slow_p('You reach the handle and open the door and step inside', 2)
            rightRoom()
        elif answer == 'backward':
            slow_p('You open the door and just see a concret wall', 2)
            slow_p('You have to choose another door', 2)
        else:
            print('Please choose a valid path')


def leftRoom():
    """
    Takes the user to the left room and gives the option
    to walk up to a cabinet.
    """
    slow_p("You've entered a small room with dampen lights", 2)
    slow_p('Across the room from where you are standing', 2)
    slow_p('there is an old decayed cabinet.', 2)
    slow_p('Do you walk up to the cabinet? (Yes / No)', 2)
    global weapon
    cabinet = input('>> ').lower().strip()
    if cabinet == 'y' or cabinet == 'yes':
        slow_p('You open up the cabinet', 2)
        slow_p('Inside is a big knife laying on a shelf', 2)
        slow_p('The knife might come in handy', 2)
        slow_p('so you deicde to pick it up', 2)
        weapon = True
        
    else:
        slow_p('You decide to go back to the first room', 2)
        intro()




welcome()
get_name()