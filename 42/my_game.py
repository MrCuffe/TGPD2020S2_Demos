#Author: Sota Kawasaki
#Description: Final phase of game development task
#Phase 4

#resets the variables
player_response = None #one variable being used for responses
player_name = None #name of the player that will be asked later on
player_items = [] #player's inventory, starts off with nothing so a blank list
counter = 0 #counter, used for many phases of the game


#script with some places where the player interacts
print("\"Where am I...\"\n\"What is this place...\"\n*beep... bloop... beep...*\n\"There is an old computer.\"")
#while being used to repeat until the player gives an answer
while player_response != "no" and player_response != "yes":
    player_response = input("\"Should I look at what it says?(yes/no)\" ")
if player_response == "no":
    print("\"... I feel like I should check it though.\"")
player_response = None
print("*Who are you.*")
player_name = input("\"Who am I...?\" ")
print("*Bzzt...*\nThe computer shut down.\n\"I think I should look around the room...\"")
while player_response != "wall" and player_response != "door":
    player_response = input("\"Should I check the wall or the door\" ")
if player_response == "door":
    print("\"... it won't open. I might need to check the walls first\"")
player_response = None

#giving the player items by checking around. items used later on
while counter < 3:
    player_response = input("\"Which wall should I check, the one on my right, left or behind?\" ")
    if  player_response == "right" and "key" not in player_items:
        print("\"I found a key... I wonder what this is for...\"")
        player_items.append("key")
        counter += 1
    elif player_response == "left" and "knife" not in player_items:
        print("\"There is a knife. Maybe I'll take this for safety.\"")
        player_items.append("knife")
        counter += 1
    elif player_response == "behind" and "book" not in player_items:
        print("\"There is a book... I can't read the writting though...\"")
        player_items.append("book")
        counter += 1

#resets variables for later use
player_response = None
counter = 0

print("\"I should check the door now\"\n*creak*\n\"The door opened\"\n*You entered the next room*\n\"What is this...?\"\n\"There is a note\"")
while counter < 4:
    player_response = input("*M, V, E, ?, J, S, U, N. What goes in the \"?\"*").capitalize()
    if player_response == "M":
        print("*Correct, the answer is M.*\n*As a reward, I will give you a piece of info; You are in the M.*\n\"What? I'm on Mars?\"")
        break
    else:
        counter += 1
        print(f"*You have {3-counter} tries left*")
        if counter == 1:
            print("\"Oh, there is a different piece of paper.\"\n*Some people will add a \"P\" at the end*")
        elif counter == 2:
            print("*Boop...*\n\"... Since when was there a screen behind me?\"\n*You think you are in the E...*")
        elif counter == 3:
            print("*Whoosh...*\n\"What is this gas?\"\n\"...\"\n*You died...*")
            exit()

#resets variables again
player_response = None
counter = 0

print("*Creeak...*")
while player_response != "right" and player_response != "left":
    player_response = input("\"Two doors opened. Should I go to the right one or the left one?\" ").lower()
print(f"*{player_response} room chosen*\n\"What is this piece of paper?\"")
if player_response == "right":
    player_response == None
    while counter < 4:
        player_response = input("*J, F, M, A, M, J, ?, A, S, O, N, D. What goes in the \"?\"*").capitalize()
        if player_response == "J":
            print("*Correct, the answer is J.*\n*Same as before, I will give you some info; today is the J.*\n\"Ok... It's July?\"\n\"This could help me later.\"\n*Furthermore, today is a Thursday*\n\"... I am always open to new info\"")
            break
        else:
            counter += 1
            print(f"*You have {3-counter} tries left*")
            if counter == 1:
                print("\"Oh, there is a note.\"\n*Most of them contain 30 or 31 things. Some exceptions exist, however.*")
            elif counter == 2:
                print("*Boop...*\n\"... Since when was there a screen here?\"\n*It is used to count something.*")
            elif counter == 3:
                print("*Bam Bam Bam...*\n*You got shot and died...*")
                exit()
elif player_response == "left":
    player_response == None
    while counter < 4:
        player_response = input("*M, T, W, ?, F, S, S. What goes in the \"?\"*").capitalize()
        if player_response == "T":
            print("*Correct, the answer is T.*\n*Similar to before, I will give you some info; today is the T*\n\"I see, its a Thursday.\"\n*Furthermore, it is July today.*\n\"Cool to know I guess\"")
            break
        else:
            counter += 1
            print(f"*You have {3-counter} tries left*")
            if counter == 1:
                print("\"What is that sound\"\n*... The seven of these repeat*")
            elif counter == 2:
                print("*Boop...*\n*... \n*It is used to count something.*")
            elif counter == 3:
                print("*Drip... Drip...*\n\"What is that sound?\"\n\"It's.... water!\"\n*You drowned*")
                exit()

#resets variables again
player_response = None
counter = 0

print("\"What is this place...?\"\n*Rinnnng rinnnng.... Briiiinggg....*\n\"Huh?... Oh, there is a phone...\"\n*Bzzt... Question:*")
while counter < 4:
    player_response = str(input("*RE{WI} what?*"))
    if player_response == "15":
        print("*Correct*")
        break
    else:
        counter += 1
        print(f"*You have {3-counter} tries left*")
        if counter == 1:
            print("*Have you used a computer before? Look at the key board*")
        if counter == 2:
            print("*Move your finger from \"Q\" to \"P\"")
        if counter == 3:
            print("*Bamn...*\n*The roof fell and you died.*")
            exit()
print("You have survived the trial version of this game.")
