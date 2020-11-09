'''
Parallel (Text Based Game 2020)
Text-Based Game Project
By Danna Pabayo
'''

####### IMPORTS #######

#This section imports script from another Python file or module.
import cmd
import textwrap
import sys
import os
import time
import random
from time import sleep
screen_width = 400


####### PLAYER SETUP/INFO ########

#This section is for storing player information throughout the game.
class player: 
    def __init__(self):
        #player name
        self.name = "" 

        #player's current location
        self.location = "C1" 

        #if game is over for player
        self.gameover = False 

        #no. puzzles solved by player
        self.puzzles_solved = 0 

        #points which determine whether player survives in the ending.
        self.antidote_end = 0
        self.final_stage_points = 0

#sets the class player to player function
player1 = player()


####### TEXT FILES ######

#This section has text files containing dialogue and endings.
#It opens and reads these text files, which will be printed to the player later on.

#Introduction text files
with open("Introduction.txt", encoding = "utf8") as file:
    intro_exposition_contents = file.readlines()
with open("Intro_Choice1_1.txt", encoding="utf8") as file:
    choice_1_ans_1_con = file.readlines()
with open("Intro_Choice1_2.txt", encoding="utf8")as file:
    choice_1_ans_2_con = file.readlines()

#Main game (puzzles) text files
with open("Map.txt", encoding = "utf8") as file:
    visualmap = file.readlines()
with open("shortend.txt", encoding = "utf8") as file:
    shortend = file.readlines()
with open("lobbydialogue.txt", encoding = "utf8") as file:
    lobbydialogue = file.readlines()
with open("archiveone.txt", encoding = "utf8") as file:
    archiveone = file.readlines()
with open("archivetwo.txt", encoding = "utf8") as file:
    archivetwo = file.readlines()
with open("mp3player.txt", encoding = "utf8") as file:
    mp3player = file.readlines()
with open("checklist.txt", encoding = "utf8") as file:
    checklist = file.readlines()
with open("secretdocument.txt", encoding = "utf8") as file:
    hologram = file.readlines()

#Final stage text files
with open("finalstagedialogue.txt", encoding = "utf8") as file:
    exposition = file.readlines()
with open("staystill.txt", encoding = "utf8") as file:
    stay_still = file.readlines()
with open("dodge.txt", encoding = "utf8") as file:
    dodge = file.readlines()
with open("breakglass.txt", encoding = "utf8") as file:
    break_glass = file.readlines()
with open("don'tbreakglass.txt", encoding = "utf8") as file:
    no_break_glass = file.readlines()
with open("pressblue.txt", encoding = "utf8") as file:
    press_blue = file.readlines()
with open("pressalarm.txt", encoding = "utf8") as file:
    press_alarm = file.readlines()

#Epilogue text files
with open("goodending(1).txt", encoding = "utf8") as file:
    goodend = file.readlines()
with open ("badending(2).txt", encoding = "utf8") as file:
    badend = file.readlines()
with open("stalemateend(3).txt", encoding = "utf8") as file:
    stalemate1 = file.readlines()
with open("stalemateend(4).txt", encoding = "utf8") as file:
    stalemate2 = file.readlines()
    
#These are functions which prints a text file
#containing a specific ending/outcome to the game
def good_ending():
    for character in goodend:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)

def bad_ending():
    for character in badend:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)
    
def stalemate_1():
    for character in stalemate1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)

def stalemate_2():
    for character in stalemate2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.3)    
    

####### GAME FUNCTIONALITY/SECTIONS #######
#Functions for different sections of the game/plot.

#This allows player to make a choice after intro exposition
#Their first choice influences "player survives" ending.
def choice_1():
    choice_1 = "Enter 1 or 2: \n"
    #typing effect for variable choice_1
    for character in choice_1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

    #player types input here
    choice_1_ans = input("> ")
    if choice_1_ans.lower() == "1":
        #If they select 1 (the correct choice), they get a point.
        player1.antidote_end += 1
        #Prints text file when choice 1 is selected.
        for character in choice_1_ans_1_con:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
    elif choice_1_ans.lower() == "2":
        #Prints text file when choice 2 is selected.
        for character in choice_1_ans_2_con:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)

    #This while loop is to deal with invalid inputs
    #It will continue to ask player for a choice until
        #they type 1 or 2.
    while choice_1_ans.lower() not in ["1","2"]:
        print("Enter a valid option.")
        choice_1_ans = input("> ")
        if choice_1_ans.lower() == "1":
            player1.antidote_end += 1
            for character in choice_1_ans_1_con:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(1)
        elif choice_1_ans.lower() == "2":
            for character in choice_1_ans_2_con:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(1)
    
#Outlines the choices that can be made for the final challenge on the third floor.
#Similar process to the one outlined above:
#if player makes the correct choice, they get a point.
def final_challenge():
    #prints exposition text file
    for character in exposition:
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(1)

    #Choice 1: Dodge/Stay Still

    #Asks player what choice to make
    choice_1 = input("Enter 1 or 2: > ")
    
    if choice_1.lower() == "1":
        #Prints what happens if you dodge
        for character in dodge:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
    elif choice_1.lower() == "2":
        #Prints what happens if you stay still
        for character in stay_still:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
        #Correct choice, so point is gained.
        player1.final_stage_points += 1
    else:
        #If player types in invalid response,
        #the player will die.
        print()
        print("I do neither of these. The alien wraps its hands around my throat, choking me...")
        print("********")
        print("YOU DIED")

        #Function which asks user to play again.
        play_again()

    #Choice 2: Break glass/don't break glass.
        #Similar process to above.
    choice_2 = input("Enter 1 or 2: > ")
    if choice_2.lower() == "1":
        for character in break_glass:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
    elif choice_2.lower() == "2":
        for character in no_break_glass:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
        #Correct choice, so point is gained.
            #Two points gained here which influence
            #player's survival and whether ship is destroyed.
        player1.final_stage_points += 1
        player1.antidote_end += 1
    else:
        print()
        print("I do neither of these. The alien wraps its hands around my throat, choking me...")
        print("********")
        print("YOU DIED")
        play_again()

    ##Choice 2: Press blue button/sound alarm
        #Similar process to above.
    choice_3 = input("Enter 1 or 2: > ")
    if choice_3.lower() == "1":
        for character in press_blue:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
        player1.final_stage_points += 1
    elif choice_3.lower() == "2":
        for character in press_alarm:
            sys.stdout.write(character) 
            sys.stdout.flush()
            time.sleep(1)
    else:
        print()
        print("I do neither of these. The alien wraps its hands around my throat, choking me...")
        print("********")
        print("YOU DIED")
        play_again()

    #After this challenge, the game ends and
        #moves onto epilogue() function which prints endings

#This section handles intro exposition of the game
def introduction():
    #for loop adds typing effect, as seen above.
    #this prints exposition at beginning of game.
    for character in intro_exposition_contents:
        sys.stdout.write(character) 
        sys.stdout.flush()
        time.sleep(1)
    
    #Choice 1 which influences whether player dies at end
        #this function handles what happens in choice_1
    choice_1()
    

#Function that manages which ending should be printed
    #Depends on player's overall points at end of game.
def epilogue():
    if player1.antidote_end == 3 and player1.final_stage_points == 3:
        good_ending()
    elif player1.antidote_end < 3 and player1.final_stage_points < 3:
        bad_ending()
    elif player1.antidote_end == 3 and player1.final_stage_points < 3:
        stalemate_1()
    elif player1.antidote_end < 3 and player1.final_stage_points == 3:
        stalemate_2()
    #After ending is printed, asks the player if they want to play again.
    play_again()

#main game loop which continues to prompt user what they want to do until game ends.
def main_game_loop():
    print_location()
    while player1.gameover == False:
        prompt()
        
    #once game has ended (i.e. gameover == True)
        #an ending will be printed. 
    epilogue() 
        
def setup_game():

    #this command clears the screen. 
    os.system("cls")
    
    #Asks player for name and stores it in player info at top
    ask_name = "What's your name?\n"
    for character in ask_name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    player1.name = player_name
    os.system("cls")

    #Indication of game starting
    print()
    print()
    print("G A M E   S T A R T")
    print("*******************")
    print()

    #For players that have played before and would like to skip the lengthy intro
    print("For returning players, skip intro?")
    intro_play = input("Type yes to skip, otherwise game will continue with intro:  > ")

    #Skips straight to choice 1 if yes
    if intro_play.lower() == "yes":
        choice_1()
    #Plays introduction for other response
    else:
        introduction()
    
    #Starts main gameplay
    main_game_loop()

#Asked if user dies early in the game or at the end. 
def play_again():
    print()
    play_again = input(player1.name + ", play again? Yes or no: ")

    #Takes player back to title screen where they can start over.
    if play_again.lower() == "yes":
        title_screen()
    #Otherwise program exits.
    else:
        exit()
    
####### MENU ########

#Function which prints out help menu
def help_menu():
    print()
    print("H E L P")
    print("*******")
    print()
    print("> Type in one of the presented choices when prompted.")
    print("> ")
    print()
    
    #Asks player what to do after help menu
    play = input("Ready to play?: ")
    if play.lower() == "yes":
        setup_game()
    elif play.lower() == "no":
        print("Exiting Game")
        quit()
    else:
        print("Please type in yes or no")

#Options for title screen
def title_screen_selections():
    option = input("Please type an option: ")
    if option.lower() == ("play"):
        #Game is initiated
        setup_game()
    elif option.lower() == ("quit"):
        #Program exits
        quit()
    elif option.lower() == ("help"):
        #Goes to help menu
        help_menu()
        
    #Deals with invalid options that player types in
        #player will continue to be prompted until they type in dictionary options
    while option.lower() not in ["play","quit","help"]:
        print("Please enter a valid option")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("quit"):
            quit()
        elif option.lower() == ("help"):
            help_menu()

#Title screen setup design
def title_screen():
    os.system("cls")

    #Prints title screen design
    print("*********************")
    print("   P A R A L L E L   ")
    print("*********************")
    print("      - play -       ")
    print("      - quit -       ")
    print("      - help -       ")
    print("                     ")
    print("2020 Project by Danna")

    #Function which allows player to
    #type in an option from title screen.
    title_screen_selections()


###### MAP ########

#Map of spaceship for own reference

'''
Spaceship

      -----------
       |   A   |                  Third Floor (1 room)
--------------------------
| B1  |  B2  | B3  |  B4 |        Second Floor (4 rooms to explore)
   -------------------
     |C1   | C2 | C3 |            First floor (3 rooms to explore)
A - control room
     
B1 - Large room filled with food, seeds, etc. 
B2 - Room with a locked door w/passcode. Leads up to control room. 
B3 - Library. Has information about the black hole trip
B4 - Large room filled with empty cryosleeping pods. 

C1 - Entrance of spaceship. Place to store mini spaceships. 
C2 - Lobby. 
C3 - Storage area for weapons, etc.
'''

#variables to do with rooms
ROOMNAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False

UP = "up"
LEFT = "left"
RIGHT = "right"

#Dictionary to check whether puzzles in each room are solved.
solved_room_puzzles = {"C1": False, "C3": False, "C2": False,
                       "B3": False, "B2": False, "B1": False, "B4": False,
                       "A": False} 

#Another dictionary used mainly for player movement and room descriptions.
zonemap = {
    "C1": {
        ROOMNAME: "> SPACESHIP HANGAR <",
        DESCRIPTION: "Nothing but a cavernous hangar housing parked spaceships.",
        EXAMINATION: "I search around the hangar. I spot a piece of paper lying on the floor. Should I pick it up? (Yes or No)",
        SOLVED: False,
        
        LEFT: "Nothing there...",
        RIGHT: "C2",
        UP: "Nothing there...",
    },
    "C2": {
        ROOMNAME: "> LOBBY <",
        DESCRIPTION: "An eery resemblance of what looks to be an old-fashioned hotel lobby.",
        EXAMINATION: "An alien is seated on one hover couch, immobile. The flickering lights prevent me from taking a closer look. Should I approach it?(Yes or No)",
        SOLVED: False,
        
        LEFT: "C1",
        RIGHT: "C3",
        UP: "B2",
    },    
    "C3": {
        ROOMNAME: "> WEAPONS & GADGETS ZONE <",
        DESCRIPTION: "The door is locked by a passcode.",
        EXAMINATION: "I should try to guess the passcode. There should be clues here on the first floor.",
        SOLVED: False,
        
        LEFT: "C2",
        RIGHT: "Nothing there...",
        UP: "Nothing there...",
        
    },
    "B1": {
        ROOMNAME: "> STORAGE <",
        DESCRIPTION: "A room filled with... Food and seeds? Did these aliens come from an Earth-like planet?",
        EXAMINATION: "There's an old mp3 player on the ground.",
        SOLVED: False,
        
        UP: "Nothing there...",
        LEFT: "Nothing there...",
        RIGHT: "B2",
    },
    "B2": {
        ROOMNAME: "> RESTRICTED ZONE <",
        DESCRIPTION: "A long hallway leading to another passcode-locked door. There must be something that I need here.",
        EXAMINATION: "Looks like the first two digits have been left in: [ Enter password: 14 __ ____ ]",
        SOLVED: False,
        
        UP: "A",
        LEFT: "B1",
        RIGHT: "B3",
    },
    "B3": {
        ROOMNAME: "> LIBRARY <",
        DESCRIPTION: "A room filled with digi-books. Maybe there could be information about Squad 256's condition here.",
        EXAMINATION: "I won't have time to go through all these archives, but I can read one. Should I read archive 1 or 2? (1 or 2)",
        SOLVED: False,
        
        UP: "Nothing there...",
        LEFT: "B2",
        RIGHT: "B4",
    },
    "B4": {
        ROOMNAME: "> CRYOSLEEP POD ZONE <",
        DESCRIPTION: "Strange... Why would aliens have a room filled with empty cryosleep pods?",
        EXAMINATION: "Should I take a closer look? (Yes or No)",
        SOLVED: False,
        
        UP: "Nothing there...",
        LEFT: "B3",
        RIGHT: "Nothing there...",
    },
    "A": {
        ROOMNAME: "> CONTROL ROOM <",
        DESCRIPTION: "A small area surrounded by controls to help fly the ship. A figure hidden in shadow sits at the captain's chair.",
        EXAMINATION: "This is it. The control room... I need to find the self-destruct controls, should I approach the figure? (Yes or No)",
        SOLVED: False,
        
        UP: "Nothing there...",
        LEFT: "Nothing there...",
        RIGHT:"Nothing there...",
    },

}

######## PUZZLE #########

#Checks player answers to puzzles
#Answers are in response to 'examine' action 
def puzzlecheck(puzzle_answer):

    #Final stage in control room
    if player1.location == "A":
        os.system("cls")
        if puzzle_answer == "yes":
            solved_room_puzzles["A"] = True
            player1.puzzles_solved += 1

            #once the player answers yes, main game ends
            #code will stop prompting and final challenge begins
            player1.gameover = True
            
            #Final challenge starts
            final_challenge()
        else:
            print("I'll stay here and think for a bit, but I think I'll eventually have to approach the figure to get to the controls.")
            print()
            prompt()
        
    #Checking answer on First Floor puzzles
    elif player1.location == "C1":
        if puzzle_answer == "yes":
            #prints puzzle's corresponding text file 
            for character in visualmap:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(0.5)
            #if correct, puzzles solved increases by 1
            #the room will also be set to solved = True in dictionary
            solved_room_puzzles["C1"] = True
            #this prevents player from redoing puzzles
            player1.puzzles_solved += 1
        else:
            print("I'll leave it for now.")
            prompt()
    elif player1.location == "C2":
        if puzzle_answer == "yes":
            if solved_room_puzzles["C3"] == False:
                print("{"+player1.name+"}")
                for character in shortend:
                    sys.stdout.write(character) 
                    sys.stdout.flush()
                    time.sleep(0.5)
                play_again()
            elif solved_room_puzzles["C3"] == True:
                print("{"+player1.name+"}")
                for character in lobbydialogue:
                    sys.stdout.write(character) 
                    sys.stdout.flush()
                    time.sleep(0.5)
                solved_room_puzzles[player1.location] = True
                player1.puzzles_solved += 1
        else:
            print("I should avoid it for now and find a weapon.")
            prompt()
    elif player1.location == "C3":
        if puzzle_answer.lower() == "e":
            solved_room_puzzles[player1.location] = True
            player1.puzzles_solved += 1
            print("[Weapon Equipped]")
            print("The passcode was correct! It's just an arms storeroom. Maybe these weapons will be useful in attacking the aliens. I'll take one.")
        else:
            print("Argh, the passcode is wrong. I should try again.")
            prompt()

    #Checking answer on Second Floor puzzles
    elif player1.location == "B1":
        if puzzle_answer.lower() == "space song":
            for character in checklist:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(0.5)
            player1.puzzles_solved += 1
            solved_room_puzzles[player1.location] = True
        else:
            print("The song isn't playing. Maybe I should try renaming it again.")
    elif player1.location == "B2":
        if puzzle_answer == "14 10 2050":
            player1.puzzles_solved += 1
            solved_room_puzzles[player1.location] = True
            for character in hologram:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(0.5)
        else:
            print("The passcode is incorrect.")
            prompt()
    elif player1.location == "B3":
        if puzzle_answer.lower() == "1":
            player1.puzzles_solved += 1
            solved_room_puzzles[player1.location] = True
            player1.antidote_end += 1
            for character in archiveone:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(0.5)
        elif puzzle_answer.lower() == "2":
            player1.puzzles_solved += 1
            solved_room_puzzles[player1.location] = True
            for character in archivetwo:
                sys.stdout.write(character) 
                sys.stdout.flush()
                time.sleep(0.5)
        else:
            print("I guess I'll search the other rooms for now...")
            prompt()
    elif player1.location == "B4":
        if puzzle_answer == "yes":
            print("These cryosleep beds... I've seen this model back in a museum on Earth. Something's inscribed on this one.")
            print("[ THEY LEFT US HERE ]")
            player1.puzzles_solved += 1
            solved_room_puzzles[player1.location] = True
        else:
            print("I'll inspect the room later.")

######## GAME ACTIONS ##########

#Outlines what will happen when player examines a room
def player_examine(action):
    #Checks whether player has already examined and completed the room's puzzle
        #this uses the dictionary solved_room_puzzles to find out
    if solved_room_puzzles[player1.location] == True:
        print("I've already searched this area.")
        print("")
    else:
        print(zonemap[player1.location][EXAMINATION])

        #This is something extra for room B1's puzzle
        if player1.location == "B1":
            for character in mp3player:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.5)

        #Asks player their answer to puzzle
        puzzle_answer = input("> ")

        #Checks the variable puzzle answer using puzzlecheck() function.
        puzzlecheck(puzzle_answer)

#Takes care of player movement, if they want to go up/left/right
def player_move(myAction):
    ask = "Where should I go: left, right or up?: > "
    dest = input(ask)

    acceptable_directions = ["left","right","up"]
    
    if dest.lower() == "left":
        destination = zonemap[player1.location][LEFT]
        movement_command(destination)
    elif dest.lower() == "right":
        destination = zonemap[player1.location][RIGHT]
        movement_command(destination)
    elif dest.lower() == "up":
        #Prevents players from moving up a floor if they haven't completed
        #puzzles on current floor.
        if player1.location == "C2":
            if player1.puzzles_solved == 3:
                destination = zonemap[player1.location][UP]
                movement_command(destination)
            else:
                print("I shouldn't go up yet until I've explored this floor.")
                prompt()
        elif player1.location == "B2":
             if player1.puzzles_solved == 7:
                destination = zonemap[player1.location][UP]
                movement_command(destination)
             else:
                print("I shouldn't go up yet until I've explored this floor.")
                prompt()
        else:
            destination = zonemap[player1.location][UP]
            movement_command(destination)
                    
    #To take care of invalid responses
    while dest.lower() not in acceptable_directions:
        print("No, that doesn't seem right.")
        dest = input(ask)
        if dest.lower() == "left":
            destination = zonemap[player1.location][LEFT]
            movement_command(destination)
        elif dest.lower() == "right":
            destination = zonemap[player1.location][RIGHT]
            movement_command(destination)
        elif dest.lower() == "up":
            if player1.location == "C2":
                if player1.puzzles_solved == 3:
                    destination = zonemap[player1.location][UP]
                    movement_command(destination)
                else:
                    print("I shouldn't go up yet until I've explored this floor.")
                    prompt()
            elif player1.location == "B2":
                if player1.puzzles_solved == 7:
                    destination = zonemap[player1.location][UP]
                    movement_command(destination)
                else:
                    print("I shouldn't go up yet until I've explored this floor.")
                    prompt()
            else:
                destination = zonemap[player1.location][UP]
                movement_command(destination)

def movement_command(destination):
    #To take care of areas in the map where there is nothing/no room.
    if destination == "Nothing there...":
        print("Nothing there...")
        prompt()
        
    #Takes care of rooms where you can move a certain direction.
    else:
        print("")
        player1.location = destination
        print_location()

def print_location():
    #Prints current room name of the player using zonemap dictionary
    print(zonemap[player1.location.upper()][ROOMNAME])
    #Prints current room description of the player using zonemap dictionary
    print("Location Description:")
    print(zonemap[player1.location][DESCRIPTION])
    print("")

#Asks player what action they want to do
def prompt():
    print("")
    print("What should I do?")
    print("Choose: Examine, Move (type quit to exit game)")

    #Takes input of their desired action
    action = input("> ")
    print("")
    acceptable_actions = ["examine", "move", "quit"]
    
    #If player quits game, program will exit.
    if action.lower() == "quit":
        sys.exit()

    #Takes care of move action through player_move() function
    elif action.lower() == "move":
        player_move(action.lower())

    #Takes care of examine action through player_move() function
    elif action.lower() == "examine":
        player_examine(action.lower())
    
    #If player types invalid action, they are prompted again.
    while action.lower() not in acceptable_actions:
        print("I should move or examine.")
        action = input("> ")
        if action.lower() == "quit":
            sys.exit()
        elif action.lower() == "move":
            player_move(action.lower())
        elif action.lower() == "examine":
            player_examine(action.lower())

    

######## GAME EXECUTION ##########

#Starts the game off with the title screen. 
title_screen()
    
