#Code by Keiki Shiraishi - Prison Escape 1

#Identifying nouns as variables
items = ["Paperclip","Loose Wire","Copper Sheets","Gloves","Spoon"]

space = " "

invalid = "Invalid option! Start over!"

game_over = "GAME OVER"
#Text that will be used in the game

text_one = "As you are wondering who to recruit in aiding your escape, a small note floats into your cell from the cell next door, but a guard is about to walk past."

#Outcomes of the options

outcome_one_yes = "You mannage to pick up the paper just in time. Since you have known Jacob for a few years now, you ask him to take part in escaping with you and toss the paper back."
outcome_one_no = "The guard notices the piece of paper and picks it up, never to be seen again."

#Defining functions for verbs which will be used in the game

def option_one():
    option_one = input("Pick up the paper?: ")
#If the player chooses "No", the game will end
    if option_one == "Yes":
        print(outcome_one_yes)
    elif option_one == "No":
        print(outcome_one_no)
        print(space)
        sys.exit(print(game_over))
    else:
        print(invalid)
        sys.exit()

def option_two():
    option_two = input(
        "Just before you go to sleep, you notice a thin metal wire hanging from the ceiling. Pull it out? ")
#If the player chooses "Yes", the game will end. The game will also end if the player enters an invalid answer.
    if option_two == "Yes":
        print("Oh no! You were too ambitious and you accidentally electrocute yourself!")
        print(space)
        sys.exit(print(game_over))
    elif option_two == "No":
        print("The prison guard notices the wire and calls an electrician to fix it. It turned out to be live, exposed wire.")
    else:
        print(invalid)
        sys.exit()

#Defining what option_three will include
def option_three():
    option_three = input("As the electrician comes in, you notice that he leaves a screwdriver behind, steal it? ")
#The game will end if the player chooses either "No" or enters an invalid answer.
    if option_three == "Yes":
        print("Congratulations! You have now acquired a screw driver to help you with your escape!")
    elif option_three == "No":
        print("You missed your opportunity to acquire a useful item!")
        print(space)
        sys.exit(print(game_over))
    else:
        print(invalid)
        sys.exit()

#Defining what option_four will include
def option_four():
    option_four = input("It is 3AM in the morning, and the guards have fallen asleep! Unscrew the vent from the wall? ")
#If the player chooses "No", the game will end, as well as if they enter an invalid answer.
    if option_four == "Yes":
        print("The vent was successfully taken out, and an air tunnel has been revealed!")
    elif option_four == "No":
        print("Oh no! You wake up the next morning and guard Davidson has confiscated the screwdriver!")
        print(space)
        sys.exit(print(game_over))
    else:
        print(invalid)
        sys.exit()

#Defining what option_five will include
def option_five():
    option_five = input("You wake up to Sergeant Anthony banging on your cell wall and dropping in a small, suspicious parcel. Open it? ")
#The game will end if the player enters "Yes", as well as if they enter an invalid answer.
    if option_five == "Yes":
        print("It turned out to be an IED sent in by your former enemies! Your cell is destroyed and you are in critical condition in the local hospital.")
        print(space)
        sys.exit(print(game_over))
    elif option_five == "No":
        print("Sergeant Anthony picked up the parcel, it turned out to be an IED sent in by your former enemies.")
    else:
        print(invalid)
        sys.exit()

#Defining what option_six will include
def option_six():
    option_six = input("You are recovering from your injuries and are still in handcuffs, but you notice that the nurse has left a paperclip on the table. Uncuff yourself? ")
#The game will end if the player enters "No", as well as if they enter an invalid answer.
    if option_six == "Yes":
        print("You successfully uncuff yourself and prepare for your escape.")
    elif option_six == "No":
        print("You recover a few days later and miss your opportunity to escape.")
        print(space)
        sys.exit(print(game_over))
    else:
        print(invalid)
        sys.exit()

#Defining what option_seven will include
def option_seven():
    option_seven = input("It is midnight and you secretly get out of bed. There is a guard sitting outside. Knock him out? ")
#The game will end if the player enters "No", as well as if they enter an invalid answer.
    if option_seven == "Yes":
        print("You knock out the guard and change into his uniform.")
        print(space)
        time.sleep(3)
        option_eight_yes = input("Walk out of the hospital? ")
        if option_eight_yes == "Yes":
            print("You are now outside of the hospital!")
            print(space)
            time.sleep(3)
            option_eight_yes_two = input("Go to CMart to get new clothes? ")
            if option_eight_yes_two == "Yes":
                print("Congratulations! You are now a free man!")
                print(space)
                sys.exit(print("Thank You For Playing!"))
            elif option_eight_yes_two == "No":
                print("The officers quickly gather outside and you have been arrested.")
                print(space)
                sys.exit(print(game_over))
            else:
                print(invalid)
                sys.exit()
        elif option_eight_yes == "No":
            print("You were tackled to the floor by a 70 year old veteran!")
            print(space)
            sys.exit(print(game_over))
        else:
            print(invalid)
            sys.exit()
    elif option_seven == "No":
        print("You accidentally step on a nail and woke up the guard!")
        print(space)
        sys.exit(print(game_over))
    else:
        print(invalid)
        sys.exit()

#This shows the rules of the game
print("Rules: You must use a capital letter at the begging of your answer.")
print(space)

#Selecting character name
prisoner_name = input("What is your name?: ")

#Beginning of the story
print("Welcome" ,prisoner_name,", you are an inmate at Starcounty Prison.")

#This is required to add delay to the messages which appear on screen
import time
time.sleep(3)

#This is required to terminate the program when it reaches GAME OVER.
import sys

print(space)
print("You have been here for just over five years now, and you decide that it is finally time to get out.")
time.sleep(4)
print(space)
print("Although you want to escape as soon as possible, you will first need to recruit some fellow inmates to help you with your escape.")
time.sleep(3)

#Start of options
print(space)
print(text_one)
print(space)
time.sleep(3)

#First option in the game
option_one()
time.sleep(3)
print(space)

#Second option in the game
option_two()
time.sleep(3)
print(space)

#Third option in the game
option_three()
time.sleep(3)
print(space)

#Fourth option in the game
option_four()
time.sleep(3)
print(space)

#Fith option in the game
option_five()
time.sleep(3)
print(space)

#Sixth option in the game
option_six()
time.sleep(3)
print(space)

#Seventh option in the game
option_seven()
time.sleep(3)
print(space)





