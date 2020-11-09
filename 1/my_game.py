# Description: A Story In Code

# imports a module to add pause
import time

# nouns
character1 = "spy"
setting = "the castle"
character2 = "the king"
the_crown = ""
money_amount = 0
has_the_crown = False
castle_description = "old, dusty"
on_a_mission = []
choice = ""
beginning = "You wake up to find it's early in the morning. The sun hasn't risen yet so you start your journey to Hogwarts Castle. The biggest and most *magical* castle in world, even you cant deny it."" To be prepared, you pack a few items in your sleek coat, prepared for any situation. After all, it was full of magic and traps. All you need now is a wand."
continue_game = ""

# possible responses from the player and defining them
directions = ["left", "right", "forward", "backward"]

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_D = ["D", "d"]

Y = ["Yes","y","yes"]

N = ["No","n","no"]

        
# Introduction: The Beginning

def intro():
    print("~~~~~~~~~~~~~~~~~~~~~~Steal the Stone: The Choose Your Own Adventure Story~~~~~~~~~~~~~~~~~~~~~~")
    #the title
    print("")
    # a gap
    name = input("What is your name: ")
    print (f"Hey {name}!")
    # asking for player name using input function
    print("")
    # a gap
    print("The most wanted jewel in the wizarding world, the Philospher's Stone."
          " And you, one of the best former wizards in the world, have been chosen by the Dark Lord himself for a very special mission."
          " Your duty is to capture the stone and return back without getting caught.")
    # introducing the plot using print function
    
    print("Do you accept this mission? Yes or No? (type in lowercase)")
    print("")
    # ask the question
    # give the player a choice and ask for input
    choice = input("Your choice: ")
    if choice in 'no':
         quit_game()
            
    if choice in 'yes':
         continue_the_game()

def quit_game() :
    print("")
    print("Game Over! Thank you for playing!")
    print("")

def continue_the_game() :
    print("Your wand was destroyed in the case of your banishment from the wizarding world.")
    print("")
    print("You were deprived of all your belongings forcing you to start over amougnst muggles.")
    print("")
    print("Thinking to yourself, wondering where you would get a wand from.")
    print("")
    time.sleep(1)
    # pauses loading the text for 1 second
    
    print("A) Steal from an innocent wizard in the muggle world")
    time.sleep(0.5)
    print("B) Go without one")
    time.sleep(0.5)
    print("C) Steal in the wizarding world")
    time.sleep(0.5)
    print("")
    
    
    # display the available options and using choice to allow the player to type it in
    choice = input("A, B or C? (write in CAPSLOCK): ")
    if choice in 'A':
        steal_1()

    if choice in 'B':
        have_none()

    if choice in 'C':
        steal_2()
            
# first choice storyline
def steal_1() :
    print("")
    print("You knew exactly where to go.")
    print("")
    print("Getting out of your car, you look up to see what looks like a normal street full of houses.")
    print("")
    print("You make your way to the end of the street to the last house. First, you knock, you dont want to be THAT rude. To your surprise, its empty but the door is locked. Normally, you could have just unlocked it with magic but not anymore.")
    print("The only downsides to being an outcast. Not being able to do what your good at. Nonetheless, you stil have physical strength so you break the door down. The house looks the same from when you last saw it.")
    print("")
    print("As you walk through the house, you notice a small box sitting in the corner.")
    time.sleep(1)
    # pauses loading the text for 1 seconds
    
    print("")
    print("A) Open the box")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("B) Leave it alone and keep walking")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("")
    # giving another choice using input function
    choice = input("A or B? (CAPSLOCK): ")
    if choice in 'A':
        open_box()

    if choice in 'B':
        leave_it()

# second option story
def have_none() :
    print("")
    print("Knowing this is a risky move, you do it anyway. You start to form a plan in your head since you have no wand, no powers, nothing.")
    print("")
    print("Once you get home, you start packing a small bag to help you on your journey.")
    print("You pack a small ration of food and supplies incase of an emergency but you rely mostly on your wits which is what made you a star and caused the dowfall of your career.")
    print("")
    print("")
    print("Quite a few hours have passed now...")
    print("")
    print("You have finally reached the wizarding world and made a stop at Number 12, Grimmauld Place. The most secretive place, which will keep you safe for the time being.")
    print("What will you do next?")
    # the story developing with print function
    time.sleep(1)
    # pauses loading the text for 1 second
    
    print("")
    print("A) Rest and Plan")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("B) Go straight to Hogwarts")
    print("")
    print("")
    choice = input("A or B (CAPSLOCK): ")
    if choice in 'A':
        rest_plan()

    if choice in 'B':
        go_to_hogwarts()

    
# third option storyline
def steal_2() :
    print("")
    print("You reassure yourself. This is a smart move and your looking out for yourself.")
    print("")
    print("Once you get home, you start packing a small bag to help you on your journey.")
    print("You pack a small ration of food and supplies incase of an emergency but you rely mostly on your wits which is what made you a star and caused the dowfall of your career.")
    # the story developing with print function
    print("")
    print("")
    time.sleep(1)
    # pauses loading the text for 1 second
    # a time pass
    print("Quite a few hours have passed now...")
    print("")
    print("You have finally reached the wizarding world and made a stop at Number 12, Grimmauld Place. The most secretive place, which will keep you safe for the time being.")
    print("What will you do next?")
    print("")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("A) Rest and Plan")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("B) Go straight to Hogwarts")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("")
    print("")
    # gives choice to player
    choice = input("A or B (CAPSLOCK): ")
    if choice in 'A':
        rest_plan() # variable

    if choice in 'B':
        go_to_hogwarts()


# option to open the box
def open_box() :
    print("")
    print("You start to make your way across to the suspicious box. Without any knowledge of whats inside, you carefully open the lid and scan the inside.")
    print("")
    print("All there is is a letter and some photos. All of a sudden, you hear noises coming from the front of the house and you jump up and start to panick. You grab the box, run upstairs and head straight to your hiding place.")
    print("You grab the wand youve been hiding then look out to the window, unsure if someone is there. You hear the doors open with a loud creak. In comes a loud flock of people. You head to the window and without thinking you jump.")
    print("Once you get home, you start packing a small bag to help you on your journey. You are already risking everything.")
    print("")
    print("")
    # the story developing with print function
    time.sleep(1)
    # pauses loading the text for 1 second

    # indicating time pass
    print("Quite a few hours have passed now...")
    print("")
    print("You have finally reached the wizarding world and made a stop at Number 12, Grimmauld Place. The most secretive place, which will keep you safe for the time being.")
    print("What will yu do next?")
    print("")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("A) Rest and Plan")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("B) Go straight to Hogwarts")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("")
    print("")
    choice = input("A or B (CAPSLOCK): ")
    if choice in 'A':
        rest_plan() # variable

    if choice in 'B':
        go_to_hogwarts()

# defining variable
# option to leave it
def leave_it() :
    print("Ignoring the box, you keep walking through the house hoping to find what your looking for. You decide to finally go upstairs after a quick examination of the house.")
    print("Going to the normal hiding spot, you grab the wand youve been looking for. You hear the doors open with a loud creak. In comes a loud flock of people. You head to the window and without thinking you jump.")
    print("Once you get home, you start packing a small bag to help you on your journey. You are already risking everything.")
    # more code to expand the story
    print("")
    print("")
    # indicating time pass
    print("Quite a few hours have passed now...")
    print("")
    print("You have finally reached the wizarding world and made a stop at Number 12, Grimmauld Place. The most secretive place, which will keep you safe for the time being.")
    print("What will yu do next?")
    print("")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("A) Rest and Plan")
    time.sleep(0.5)
    print("B) Go straight to Hogwarts")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("")
    print("")
    # input function to give choice
    choice = input("A or B (CAPSLOCK): ")
    if choice in 'A':
        rest_plan()

    if choice in 'B':
        go_to_hogwarts()
# defining variables 
def rest_plan() :
    print("")
    print("You sigh. Some rest and planning will do you good you think to yourself. ")
    print("")
    print("But you have to move without being recognised or thrown out. You walk at a normal pace, not too slow and not too fast.")
    print("As you walk, you pass slightly familiar faces but avoid any eye contact. Finally you make it to a small empty room.")
    print("This is safe, You think. You lay on the floor letting the coldness of the wooden floor touch you. You lay awake thinking of your plan.")
    print("")
    print("After thinking of your plan you make your way to the exit.")
    print("You hop onto a train going directly to Hogwarts. You dont want to seem suspicious so you blend in with the parents.")
    print("It takes ages to reach the castle but the train finally comes to a stop and you look out to see what once was your home.")
    print("")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("A) Go to the chamber and start your mission")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("B) Go through a secret tunnel")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("")         
    choice = input("A or B (CAPSLOCK): ")
    if choice in 'A':
        chamber_start()

    if choice in 'B':
        secret_tunnel()
    # defining variables 
 
def go_to_hogwarts() :
    print("")
    print("Hurry! You think to yourself. Not wanting to get caught.")
    print("")
    print("If you get caught its over for you and you'll never make it back alive.")
    print("")
    print("You hop onto a train going directly to Hogwarts. You dont want to seem suspicious so you blend in with the parents.")
    print("It takes ages to reach the castle but the train finally comes to a stop and you look out to see what once was your home.")
    print("")
    print("A) Go to the chamber and start your mission")
    print("B) Go through a secret tunnel")
    print("")
    # choice input function to allow player choice
    choice = input("A or B (CAPSLOCK): ")
    if choice in 'A':
        chamber_start()
        # variable mentioned
        
    if choice in 'B':
        secret_tunnel()
        # variable mentioned

# variable defined
def chamber_start() :
    print("")
    print("Tune in for Part 2.....")
    print("")
    print("")
    # added stay tune to alret players of the unreleased/ future release

def secret_tunnel() :
    print("")
    print("You try to find a secret way to get to the stone. PERFECT! The secret tunnel can be opened by only you. ")
    print("")
    time.sleep(0.5)
    #pauses text before loading it for the amount time in the brackets
    print("Tune in for Part 2.....")
    print("")
    print("")

intro()
