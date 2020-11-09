# student name: Nikki Li
# game: escape room
# define variables in lists
# import function to slow the printing of statements so it is easier for the player to read
from time import sleep

furniture = ["couch", "coffee table", "rug", "door"]


# function for starting the game and the beginning of the narrative
def start_game():
    print("welcome to Escape Room!")
    sleep(2)
    print("you find yourself alone in a room")
    sleep(2)
    print("the only door is locked and there are no windows")
    sleep(2)
    print(f"the furniture in the room include {furniture}")
    sleep(2)
    inspect_furniture()


# inspect furniture function, when player chooses which piece of furniture to interact with using if statements to
# player can inspect 4 different pieces of furniture
def inspect_furniture():
    insp_1 = input("which piece of furniture would you like to inspect? ")
    sleep(2)
    if insp_1 == furniture[0]:
        print(f"you choose to inspect {furniture[0]}")
        couch()
    elif insp_1 == furniture[1]:
        print(f"you choose to inspect {furniture[1]}")
        coffee_table()
    elif insp_1 == furniture[2]:
        print(f"you choose to inspect {furniture[2]}")
    elif insp_1 == furniture[3]:
        print(f"you choose to inspect {furniture[3]}")
        door()
    else:
        print("please choose one of the following options: couch, coffee table, rug, or door")
        inspect_furniture()


# what happens when the couch is chosen
# there is a note under the couch that is part of the password
def couch():
    print("the couch is made of leather and looks very worn")
    sleep(2)
    print("you can either look between the cushions or under the couch")
    action_1 = input("enter 'under' or 'between':")
    if action_1 == "between":
        sleep(2)
        print("there is nothing between the cushions")
        choice_couch()
    elif action_1 == "under":
        sleep(2)
        print("you find a note that says '1'")
        choice_couch()


# choice function for the couch, determine whether the player would like to keep inspecting the couch or not
def choice_couch():
    print("would you like to keep inspecting the couch or inspect another piece of furniture?")
    choice_1 = input("type 'couch' or 'other': ")
    if choice_1 == 'couch':
        couch()
    elif choice_1 == "other":
        inspect_furniture()


# define function to determine what happens when the coffee table is inspected
# there is a coffee cup and a sugar packet on top of the table
# if player pours the sugar out of the packet there is a note at the bottom
def coffee_table():
    print("the table is wooden, with a coffee cup on top of it")
    sleep(2)
    print("there is cold black coffee in the cup and a sugar packet next to it")
    sleep(3)
    print("would you like to keep inspecting the table, inspect the cup of coffee, or inspect the sugar packet?")
    action_2 = input("type 'table','coffee' or 'sugar': ")
    if action_2 == "table":
        print("the table is mostly smooth, burnished wood")
        sleep(2)
        print("as you inspect the top right corner of the table, you notice 3 scratches")
        sleep(3)
        print("there is nothing else noteworthy of the table")
        sleep(2)
        choice()
    elif action_2 == "coffee":
        print("the mug is normal white ceramic. you cannot see the bottom of the mug because of the coffee inside")
        sleep(2)
        print("would you like to drink the coffee, pour it out, or inspect something else?")
        insp_3 = input("type 'drink','pour' or 'inspect something else'")
        if insp_3 == "drink":
            print("you drink all the coffee. it is cold and extremely bitter. you hate it.")
            sleep(2)
            print("you look at the bottom of the mug when you finish")
            sleep(3)
            print("there is nothing there. you've been scammed")
            sleep(2)
            choice()
        elif insp_3 == "pour":
            print("you pour the coffee all over yourself. you now have a soggy shirt")
            sleep(2)
            print("you look at the bottom of the mug. There is nothing. You've been scammed")
            sleep(1)
            choice()
        elif insp_3 == "inspect something else":
            choice()
    elif action_2 == "sugar":
        print("the sugar packet looks completely normal, but you notice something other than sugar might be inside")
        sleep(2)
        print("would you like to open it?")
        insp_4 = input("enter 'yes' or 'no': ")
        if insp_4 == "yes":
            print("you find a note that says '5'")
            choice()
        if insp_4 == "no":
            choice()


# choice function helps player decide whether to continue inspecting the same piece of furniture or move on to
# something else
def choice():
    print(f"would you like to inspect other parts of the coffee table or inspect other furniture?")
    insp_2 = input("type 'coffee table' or 'other': ")
    if insp_2 == "coffee table":
        coffee_table()
    elif insp_2 == "other":
        inspect_furniture()


# function codes for last piece of furniture-the rug
# the secret message is hidden in the pattern of the rug(the secret message is 10)
def rug():
    print("the rug is thick and soft, with an intricate woven pattern that looks a little like tne number 1")
    sleep(2)
    print("would you like to look under the rug?")
    action_3 = input("type 'yes' or 'no':")
    if action_3 == "yes":
        print("you look under the rug and notice the pattern resembles this: 0000")
        print("would you like to inspect other furniture or continue inspecting the rug?")
        action_4 = input("type 'rug' or other': ")
        if action_4 == "other":
            inspect_furniture()
        elif action_4 == "rug":
            rug()
    elif action_3 == "no":
        print("would you like to inspect other furniture or continue inspecting the rug?")
        action_4 = input("type 'rug' or other': ")
        if action_4 == "other":
            inspect_furniture()
        elif action_4 == "rug":
            rug()


# function to determine what happens when the door is chosen-if the password is correct the door opens, if not,
# the player is encouraged to try again
def door():
    print("the door is wooden, with a digital lock")
    password = input("please enter the correct password to exit the room:")
    if password == "1015":
        print("The door unlocks. you are now able to exit the room \u263A")
        play_again()
    else:
        print("incorrect password. would you like to try again or inspect other furniture?")
        action_3 = input("enter 'try again' or 'other': ")
        if action_3 == "try again":
            door()
        elif action_3 == "other":
            inspect_furniture()


# play again function: player can replay the game after one round ends if chosen to do so
def play_again():
    print("would you like to play this game again?")
    action_5 = input("type 'yes' or 'no': ")
    if action_5 == "yes":
        start_game()
    elif action_5 == 'no':
        exit()


start_game()
