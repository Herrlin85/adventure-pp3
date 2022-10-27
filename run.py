
"""
import slow print from functions.py
import colorama for styling purposes
on ASCII Art and os to be able to 
clear terminal inside code
"""
from functions import slow_p
from functions import weapon, key

import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def welcome():
    """
    Welcome message and description for the user
    """
    slow_p('Welcome to the Adventure Game: The Nightmare!', 1)
    slow_p('As you fall asleep, you enter a terrible nightmare', 2)
    slow_p('To be able wake up, you need to find the key', 2)
    slow_p('There are different paths to choose from to find your way out', 2)
    slow_p("But first, who does this nightmare belong too?", 2)
    

def get_name():
    """
    Ask for the user's name and validate it to not be empty
    and only letters
    """
    global player_name
    player_name = ""
    while True:
        player_name = input('\nPlease enter your name:').capitalize()
        if not player_name.isalpha():
            print('Use only letters please')
            continue
        else:
            print(f'Good luck, {player_name}.\n')
            break
    intro()
    

def intro():
    """
    Sets the scene for the user
    """
    slow_p('You are standing in a square room.', 2)
    slow_p('The room is cold and dark and made of concrete.', 2)
    slow_p('You look around and see 4 doors, 1 on each wall', 2)
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
        # Makes the input in lower case and get rid of whitespaces if any
        answer = input('\n>>').lower().strip()
        # Clears the terminal for better user experience
        os.system('clear')
        # The room to the left to collect the weapon
        if answer == 'left':
            slow_p('You have a good feeling about the left door', 2)
            slow_p('You reach the door and carefully walk inside \n', 2)
            left_room()
        # The middle room to finish the game if key is collected
        elif answer == 'forward':
            if key:
                slow_p('You managed to escape your nightmare', 2)
                # Makes the ASCII text red and bright
                slow_p(Fore.RED + Style.BRIGHT + '''
     ______                                                
    / _____)                                    _          
    | /        ___   ____    ____   ____   ____ | |_    ___ 
    | |       / _ \ |  _ \  / _  | / ___) / _  ||  _)  /___)
    | \_____ | |_| || | | |( ( | || |    ( ( | || |__ |___ |
     \______) \___/ |_| |_| \_|| ||_|     \_||_| \___)(___/ 
                           (_____|                          
                ''', 2)
                play_again()
            else:
                slow_p('You decide to take the middle door', 2)
                slow_p('The door is locked', 2)
                slow_p('Please choose another door', 2)
                main_room()
        # The room to the right to collect the key
        elif answer == 'right':
            slow_p('You slowly walk towards the door to your right', 2)
            slow_p('You reach the handle and open the door \n', 2)
            right_room()
        # A dead end
        elif answer == 'backward':
            slow_p('You open the door and just see a concret wall', 2)
            slow_p('You have to choose another door', 2)
        else:
            print('Please choose a valid path')


def left_room():
    """
    Takes the user to the left room and gives the option
    to walk up to a cabinet and collect the weapon.
    """
    global weapon
    slow_p("You've entered a small room with dampen lights", 2)
    slow_p('Across the room from where you are standing', 2)
    slow_p('there is an old decayed cabinet.', 2)
    slow_p('Do you walk up to the cabinet? (Yes / No)', 1)

    # Makes the input in lower case and get rid of whitespaces if any
    cabinet = input('\n>>').lower().strip()
    if cabinet == 'y' or cabinet == 'yes':
        slow_p('You open up the cabinet', 2)
        slow_p('Inside is a big knife laying on a shelf', 2)
        slow_p('The knife might come in handy', 2)
        slow_p('so you deicde to pick it up and head back to the main room', 2)
        # Sets the global weapon to True
        weapon = True
        main_room()
    else:
        slow_p('You decide to go back to the main room', 2)
        main_room()


def right_room():
    """
    The user can collect the key from this room and gets
    multiple choices which leads to either the user dies, goes
    back to the main room or kill the monster and gets the key.
    To get the key the user needs to collect the weapon and slay 
    the monster.
    """
    
    global key
    slow_p('You step inside the room', 2)
    slow_p('and you can hear a strange sound', 2)
    slow_p('that makes you skin crawl', 2)
    slow_p('While trying to locate where the sound', 2)
    slow_p('is coming from, a shiny object caught your eyes', 2)
    slow_p('there is something laying on a table in front of you', 2)
    slow_p('Do you want to go to the table? (Yes / No)', 1)
    # Makes the input in lower case and get rid of whitespaces if any
    table = input('\n>>').lower().strip()
    if table == 'y' or table == 'yes':
        slow_p('When you where just about to take a step', 2)
        slow_p('towards the table, you hear that sound again', 2)
        slow_p('and a big and scary monster dropped from the ceiling', 2)
        slow_p('what are you going to do? (Fight / Flee)', 1)
        # Makes the input in lower case and get rid of whitespaces if any
        encounter = input('\n>>').lower().strip()
        if encounter == 'fight':
            if weapon:
                slow_p('You took out your knife and slayed the big monster', 2)
                slow_p('The sound that made your skin crawl made sence now', 2)
                slow_p('You head over to the table', 2)
                slow_p('to have a look at the shiny object on the table', 2)
                slow_p("It's a long metal object with a cross-shaped end", 2)
                slow_p('What do you want to do with it? (Take / Leave)', 1)
                # Makes the input in lower case and get rid of whitespaces
                metal_object = input('\n>>').lower().strip()
                if metal_object == 'take':
                    slow_p('You put the metal object in your pocket', 2)
                    slow_p('and head back to the main room', 2)
                    # Change the global key to True
                    key = True
                    main_room()
                else:
                    slow_p('Seems useless, you dedice to leave it be', 2)
                    main_room()
            else:
                slow_p('You have nothing to attack the monster with', 2)
                slow_p('The monster shredded you too pieces', 2)
                # Make the ASCII red and bright
                slow_p(Fore.RED + Style.BRIGHT + '''
                
            ▓█████▄ ▓█████  ▄▄▄      ▓█████▄ 
            ▒██▀ ██▌▓█   ▀ ▒████▄    ▒██▀ ██▌
            ░██   █▌▒███   ▒██  ▀█▄  ░██   █▌
            ░▓█▄   ▌▒▓█  ▄ ░██▄▄▄▄██ ░▓█▄   ▌
            ░▒████▓ ░▒████▒ ▓█   ▓██▒░▒████▓ 
            ▒▒▓  ▒ ░░ ▒░ ░ ▒▒   ▓▒█░ ▒▒▓  ▒ 
            ░ ▒  ▒  ░ ░  ░  ▒   ▒▒ ░ ░ ▒  ▒ 
            ░ ░  ░    ░     ░   ▒    ░ ░  ░ 
            ░       ░  ░      ░  ░   ░    
            ░                        ░      
                ''', 2)
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
    # Makes the input in lower case and get rid of whitespaces
    answer = input('\n>>').lower().strip()
    if answer == 'y' or answer == 'yes':
        # Clears the terminal for better user experience
        os.system('clear')
        get_name()
    else:
        slow_p(f'Maybe another time {player_name}', 1)
        slow_p('Hope to see you again', 1)
        # Ends the game
        exit()


welcome()
get_name()
