#SIREKSHNA NANTHAKRAN
#The time travel game

#Assigning variables - Phase 1
#Directions are North, East, South and West.
#Directions also include actions.

actionsandDirections = ["N","E","S","W","K","A","B","C","D"] #These are the assigned directions and actions the player can choose from.
inventoryList = []
currentLocation = 0


def direction_function(): #This is defining the variable to print the text written below when ever "direction_function" in mentioned after while loops. 
    print ("To go North, press 'N'")
    print ("To go East, press 'E'")
    print ("To go South, press 'S'")
    print ("To go West, press 'W'")

def code_options(): #The below items will print in the game when "code_options" are mentioned in the code.
                print("A) 2131")
                print("B) 6071")
                print("C) 1788")
                print("D) 2020")

runGame = True 

go = True
print("Welcome to the Time Travel Game!")#greeting the player. 
print("You are a physicist and have been experimenting with your newly invented time machine.")#Giving the background stroy to the game so they have an motivation to play.
print("To your uttuer surprise have time travelled back into the 1600s! But you have lost your time machine:((")
print("You must complete these tasks by following the instructions below to find your time machine in order to go back.")
print("There are 3 levels to this game")#Telling the player about the levels in the game.
print("you can choose options from  the multiple choice given by tapping the keys on your computer")

while go == True:

    while currentLocation == 0: #Location 0 is the level known as the warm up before level 1.
        print("You are in the beginner's level! a beautiful enchanted garden... Blue butterflies spin around you, seeking your attention.")
        print("But you must stay focused! Now in order to move further you must choose a direction")
        print("")


        direction_function()#This will print the defined direction function variables.
        print("")
        action = input("Which direction do you want to go?")#Player must give the answer here.
        print("")

        if action.upper() == "N": #if the player enters "N" or "n", python will it up as a capital "N" becaue of ".upper".
            print("Oh doesn't seem right. You almost got it! Try again please.")
        elif action.upper() == "E":
            print("Yes! You got the right direction.")
            currentLocation = 1 #The player will be moved to level 1 because the player succeeded beginner's level.
            break #This stops the above printing text to be repeated on the game in a loop.
        elif action.upper() == "S":
            print("Oh doesn't seem right. You almost got it! Try again please.")
        elif action.upper() == "W":
            print("Oh doesn't seem right. You almost got it! Try again please.")
        else: #Any other answer other than "E" will print the text below. 
            print("Oh doesn't seem right. You almost got it! Try again please.")
#Adding levels to the game - Phase 2
    while currentLocation == 1: # This shows they're in level 1 and the code below will be printed when the player successfully makes it to level 1.
        print("Congratulations! You have successfully reached level 1. Now you are in a mystical palace. The key to operate your time machine is in one of the rooms of this luxurious palace.")
        print("Now please read the instructions carefully.") #This is a sign that tells the player that its important to pay attention and read between the lines for the next text.
        print("- The first room in front of you has a precious golden box hoarding something highly valuable.")
        print("- The room to your right has guards on off shift taking a nap.")
        print("- The room to your left is a sealed door.")#This is a sealed door. This is a very important information that the player should keep in memory for the next level.
        print("Now choose one of the options carefully in order to move on. Yes they are tricky:)")
        while True: #The text below will only print when the above is true. While the current location 2 is true...
            print("i) Press 'N' to enter room in North")
            print("ii) Press 'E' to enter room in East")
            print("iii) Press 'S' to enter room in West")
            print("iv) Press 'W' to see what happens")
            print("")

            direction_function()#This will print the options of directions.
            print("")
            action = input("What would you choose? Remember your one and only aim!")#The question that is asked. This is where the input of the player is required.
            print("")

            if action.upper() == "N": #If the player presses 'N' the print statement will appear.
                print("Yes!! you are so clever! You got it right. Keep going")
                currentLocation = 2 # The player will move to level 2 because they got the answer right.
                break #This will break the loop text.
            elif action.upper() == "E":
                print("You did not get that right. You will be directed to the beginner's level again.")
            elif action.upper() == "S":
                print("You did not get that right. You will be directed to the beginner's level again.")
            elif action.upper() == "W":
                print("You did not get that right. You will be directed to the beginner's level again.")
            else: #Anything other than the correct answer will print this text below as feedback.
                print("You did not get that right. You will be directed to the beginner's level again.")
#making the next level complicated - Phase 3
        while currentLocation == 2: #This is the code for level 2
            print("Fantastic job! You have successfully made it to level 2. You chose to go into the room in front of you holding something precious...")
            print("You guessed it right! The precious item in the box is the key indeed")
            print("Your next choice will determine your way back to time travel!")
            print("You are once again back in the corridor facing the same room in front of you while holding the key in your hand.")#The player is back with the key. This is the time to remember that a sealed door can be opened with a key.
            print("Choose carefully. Remeber this is life or death. You really want to go back to your family...")
            while True:
                print("i) Press 'N' to see what happens")
                print("ii) Press 'E' to see what happens")
                print("iii) Press 'S' to see what happens")
                print("iv) Press 'W' to see what happens")
                print("")
                
                direction_function()
                print("")
                action = input("Hmmm... What would you choose scientist??")
                print("")

                if action.upper() == "N":
                    print("Ohh noo. You could have gotten that one. Come on try again! You can do it")
                    currentLocation = 0
                elif action.upper() == "E":
                    print("Ohh noo. You could have gotten that one. Come on try again! You can do it")
                    currentLocation = 0
                elif action.upper() == "S":
                    print("Ohh noo. You could have gotten that one. Come on try again! You can do it")
                    currentLocation = 0
                elif action.upper() == "W":
                    print("This is a miracle! You got it right.")
                    currentLocation = 3 # The player will move to level 3 because they passed level 2.
                    break
                else:
                    print("Ohh noo. You could have gotten that one. Come on try again! You can do it")

        while currentLocation == 3: #This is the code for level 3.
            print("You have made it to level 3! That is fabulous.")
            print("But now here's the catch! What will you do to unlock the door?")
            while True:
                print("'K' Would you use the 'key' to unlock the door?")
                print("or")
                print("'S' Would you go back 'South'?")
                print("")

                direction_function()
                print("")
                print("Or should you press 'K'?...")
                action = input("Quick! Quick! Make a smart choice. Dont lose this chance...")#This makes the player think fast and boost their adrenaline.

                if action.upper() == "K": #if the player presses 'K' on their key.
                    print("Smart choice! You have opened the door.")
                    currentLocation = 4 #The player will be moved to level 4. Where the instructions for level 4 are given. 
                    break
                elif action.upper() == "S":
                    print("Incorrect. You almost go it! Please try again")
                else:
                    print("Ohh. That's not right. Please read the description carefully again. You can do it!")

        while currentLocation == 4: #This is level 4 where the final question is asked before the player can win.
            print("Amazing! You have reached the final level. The grand finale!")
            print("Okay. Its time to go back but when the king of the palace found your time machine, he sealed it with a code that only the king magically knows of.")
            print("However since you are the inventor of the machine, you can guess the answer to this! Give this a shot so you can go back.")
            while True:
                print("Here's the question.")
                print("There's 4 sets of codes. Only one can be the answer. These numbers somehow relate to you. Can you guess the right one?")
                print("Quick!! Time's running!")
                print("")
                

                code_options()#This will print the options of code as it was defined above.
                print("")
                action = input("What is your final answer to go back for once and for all?")
                print("")

                if action.upper() == "D":
                    print("You did it again! Now you can enter into the time machine and reunite with your family.")
                    currentLocation = 5 #The player will reach vicotry level and have the ability to exit.
                    break
                else:
                    print("Oh noo... You were so close! Please try again.")

        while currentLocation == 5: #This is the end of game where the player is congratulated and the exit code is written.
            print("You are the WINNER!")
            while True:
                print("You can now exit by pressing 'Ctr D' or play again by running it again. Thank you")
                import sys #This is to exit game.
                sys.exit()#The player will exit game using Ctr D as instructed above in the print statement.

                
            
                

            

                    
        

