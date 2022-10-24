"""
import slow print from functions.py
"""
from functions import slow_p
from functions import weapon, key


def welcome():
    """
    Welcome message and description for the user
    """
    slow_p('Welcome to the Adventure Game: The Nightmare!', 2)
    slow_p('As you fall asleep, you enter a terrible nightmare', 2)
    slow_p('To be able wake up, you need to find the key', 2)
    slow_p('There are different paths to choose from to find your way out', 2)
    slow_p("But first, who does this nightmare belong too?", 2)


def get_name():
    """
    Ask for the user's name and validate it to not be empty
    """
    #sets the name to global
    global name
    name = input('Please enter your name: ')
    if name != '':
        print(f'Good luck, {name}.\n')
        intro()
    else:
        print("Don't you have a name?")
        get_name()


def intro():
    """
    Sets the scene for the user
    """
    slow_p('You are standing in a square room.', 2)
    slow_p('The room is cold and dark and made of concrete.', 2)
    slow_p('You look around and you see 4 doors, 1 on each wall', 2)
    main_room()
    

def main_room():
    """
    The main room where the user decide which way to take.
    There are 4 doors to choose from
    """
    directions = ['left', 'forward', 'right']
    answer = ""
    while answer not in directions:
        slow_p('Which door do you choose? (left/forward/right/backward)', 1)
        answer = input('>> ').lower().strip()
        # The room to the left to collect the weapon
        if answer == 'left':
            slow_p('You are slowly walking towards the left door', 2)
            slow_p('You reach the door and carefully walk inside \n', 2)
            leftRoom()
        # The middle room to finish the game
        elif answer == 'forward':
            # If the key is collected the game is finished 
            if key:
                slow_p('Congratulations, you managed to wake up', 2)
            else:
                slow_p('You decide to take the middle door', 2)
                slow_p('The door is locked', 2)
                slow_p('Please choose another door', 2)
                main_room()
        # The room to the right to collect the key
        elif answer == 'right':
            slow_p('You are slowly walking towards the door on your right', 2)
            slow_p('You reach the handle and open the door', 2)
            rightRoom()
        # A dead end
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
    slow_p('Do you walk up to the cabinet? (Yes / No)', 1)
    cabinet = input('>> ').lower().strip()
    global weapon
    if cabinet == 'y' or cabinet == 'yes':
        slow_p('You open up the cabinet', 2)
        slow_p('Inside is a big knife laying on a shelf', 2)
        slow_p('The knife might come in handy', 2)
        slow_p('so you deicde to pick it up and head back to the main room', 2)
        weapon = True
        main_room()
    else:
        slow_p('You decide to go back to the main room', 2)
        main_room()


def rightRoom():
    """
    The user can collect the key from this room and gets
    multiple choices which leads to either the user dies, goes
    back to the main room or kill the monster and gets the key.
    To get the key the user needs to collect the weapon and slay 
    the monster.
    """
    slow_p('You step inside the room', 2)
    slow_p('and you can hear a strange sound', 2)
    slow_p('that makes you skin crawl', 2)
    slow_p('While trying to locate where the sound', 2)
    slow_p('comes from, a shiny object caught your eyes', 2)
    slow_p('there is something laying on a table in front of you', 2)
    slow_p('Do you want to go to the table? (Yes / No)', 1)
    table = input('>> ').lower().strip()
    global key
    global weapon
    if table == 'y' or table == 'yes':
        slow_p('When you were just about to take a step', 2)
        slow_p('towards the table', 2)
        slow_p('a big and scary monster dropped from the ceiling', 2)
        slow_p('what are you going to do? (Fight / Flee)', 1)
        encounter = input('>> ').lower().strip()
        if encounter == 'fight':
            if weapon:
                slow_p('You took out your knife and slayed the big monster', 2)
                slow_p('the object on the table is a key', 2)
                slow_p('you pick up the key and head back to the main room', 2)
                key = True
                main_room()
            else:
                slow_p('You have nothing to attack the monster with', 2)
                slow_p('The monster shredded you too pieces', 2)
                slow_p('YOU ARE DEAD', 2)
                play_again()
        else:
            slow_p("HELL NO, i'm not fighting that", 2)
            slow_p('You are heading back', 2)
            main_room()
    else:
        slow_p("You decide it's not worth it and want to try another room", 2)
        main_room()


def play_again():
    """
    Ask if the user want another go
    """
    slow_p('Do you want to play again? (Yes / No)', 2)
    answer = input('>> ').lower().strip()
    if answer == 'y' or answer == 'yes':
        get_name()
    else:
        slow_p(f'Maybe another time {name}', 1)
        slow_p('Hope to see you again', 1)
        exit()


welcome()
get_name()
