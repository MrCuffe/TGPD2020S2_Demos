# Author Ashley Harris-Crean
# Description: Phase 3: Players get warnings if the psychopath is near, Players can fight the psychopath

import os, random, time, sys

#is game on or off
gameRunning = True
gameEnd = False

#List of everything the player could find
gameItems = ["Crowbar", "Torch", "Key", "Book", "Knife", "Medkit", "Shotgun", "Photo", "Sandwich", "Drink", "Shield", "Bullet", "Door"]

#list of possible commands
gameCommands = ["Examine", "Open", "Close", "Hit", "Help", "Unlock","Keep", "Pickup", "Putdown","Keep Going","Drink","Eat"]


#welcome to the game, tells the player what the game is called
print("Welcome to House of Horrors")
#select a player   
print("Select a Player: Player A, Player B or Player C?")
#describes the character choices so the player can make an informed choice, based on strenght, weakness and tools.
print("Player A - Strengths: Strong.        Weakness:Large build.  Tool: Torch")
print("Player B - Strengths: Small build.   Weakness: Slow.        Tool: Map")
print("Player C - Strengths: Good Shooter.  Weakness: Dehydration. Tool: Pocket knife")
characterSelection = input("> ")
# ensure they entered a viable option
while characterSelection not in ["Player A", "Player B", "Player C"]:
    if characterSelection == "Player A":
        pass
    elif characterSelection == "Player B":
        pass
    elif characterSelection == "Player C":
        pass
    else:
        print("Invalid Input") 
#background informations / context for the player
print("You wake up and immediately feel a shot of pain through your head. You become aware of your surroundings, you are in a dark cellar, lying in a pool of your blood. The room is lit by a dim lamp in the corner. You need to find objects and avoid Him. Whats your next move?")

#Run while game is active
hungerLevel = 10 
hydrationLevel = 10
while True:
    playerBackpack = [] #List of what the player has
    stepsTaken = 0 #How far the player has moved
    # as the games goes on and the player moves more they will require more food and water
    if stepsTaken %15 == 0:
        hungerLevel += 1
    else:
        pass
    if stepsTaken % 20 == 0:
        hydrationLevel -= 1
    else:
        pass

    playerInput = ""
    while playerInput not in ["W", "A", "S", "D"]:
        #Recieves input from user
        print("")
        print("-------------------------")
        print("Input W to move Forwards.")
        print("Input A to move Left.")
        print("Input S to move Backwards.")
        print("Input D to move Right.")
        playerInput = input("> ")
        print("")
        #Makes sure that they are inputting the right commands to move properly
        if playerInput not in ["W", "A", "S", "D"]:
            print("Invalid Input")
        else:
            pass
    
    # chance of finding an object is 1 in 4
    i = random.randint(0, 3)
    if i%2 == 0:
        item = random.choice(gameItems)
        #checks if player has the item already, to prevent duplicates
        while item in playerBackpack:
            item = random.choice(gameItems)
            # counts how many items in back pack, if 5 there will not be any more items put in
            if len(playerBackpack) == len(gameItems):
                print("you have all the items")
                break
            elif len(playerBackpack) >= 10:
                print("your backpack is full")
                break
            else:
                pass
        #character finds objects they can choose what to do with it
        print("You wonder around and find something")
        print(f"You found a {item}")
        print("What would you like to do with it?")
        print("Options: Examine, Keep, Putdown, Drink, Eat")
        print("")
        #player desicion is equal to nothing
        playerDecision=""
        #add it to list
        while playerDecision not in ["Examine", "Keep", "Putdown", "Drink", "Eat"]:
            playerDecision = input("> ")
            if playerDecision == "Examine":
                    pass #it will give the player a description of the item
            #player can add things to backpack
            elif playerDecision == "Keep":
                    print(f"You have picked up a {item}")
                    playerBackpack.append(item)
                    pass
            elif playerDecision == "Putdown":
                    print("You move on")
                    pass
            elif playerDecision == "Drink":
                    print(f"You drank the {item}")
                    hydrationLevel += 1
                    pass
            elif playerDecision == "Eat":
                    print(f"You ate the {item}")
                    hungerLevel += 1
                    pass
            else:
                print("Invalid Input")

#Chances of being near him are 1 in 8, when near, player gets options
    # bringing charPsychopath into game
    f = random.randint(0,8)
    if f%8 == 0:
        print(" ")
        print("Beware, He is approaching")
        print("What would you like to do?")
        print("You can Run, Hide or Fight")
    
        playerChoice = input("> ")
        #player can simply move away and continue to explore the house
        if playerChoice == "Run":
            print("You have moved away")
        #if the player choose hide they get a selection of places, 1 of which automatically causes them to die as the psychopath finds them
        if playerChoice == "Hide":
            print("where?")
            print("cupboard, under the bed, behind door")
            playerDecide = input("> ")
            if playerDecide == "cupboard":
                print("You hide")
                print("He moves away")
            if playerDecide == "under the bed":
                print("He found you")
                print("You're Dead")
                print("Game Over")
                sys.exit("You lose")
            if playerDecide == "behind door":
                print("You hide")
            else:
                pass
        #player chooses to engage in battle
        if playerChoice == "Fight":
            print("Ready?")
            #waits 3 s before printing next line to add suspence
            time.sleep(3)
            
            if len(playerBackpack) > 0:
                #picking a weapon to fight with
                print("Pick an item from your backpack by number (First item is 0)")
                print(playerBackpack)
                playerChoice = int(input(">> "))
                selectedItem = playerBackpack[playerChoice]
            # if the character has no ites in backpack they fight with their fists
            else:
                selectedItem = "your fists"
            
            playerAlive = True
            charPsychopathAlive = True
            playerHealth = 5
            charPsychopathHealth = 5
            #player and psychopath battle is a battle of chance, runs through battle automatically, updating character at every shot.
            while playerAlive != False or charPsychopathAlive != False:
                playerNum = random.randint(0,4)
                charPsychopathNum = random.randint(0,4) 
                time.sleep(2)               
                if playerNum > charPsychopathNum:
                    playerHealth -= 1
                    print(f"You have been Hit! You now have {playerHealth} health left")
                elif playerNum == charPsychopathNum:
                    print("You both miss")
                    pass
                else:
                    charPsychopathHealth -= 1
                    print(f"You hit Him with the {selectedItem}, he is now on {charPsychopathHealth} health!")
                # if either characters have no health, the game ends, if the player has no health they loose the game
                if playerHealth == 0:
                    print("You died")
                    print("Game Over")
                    sys.exit("You lose")
                elif charPsychopathHealth == 0:
                    print("He died")
                    print("Game Over")
                    sys.exit("You Win")
            
        else:
            pass

