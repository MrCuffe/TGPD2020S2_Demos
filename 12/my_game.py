#Sampras Kiriella Year 10
#This is Phase 3 of the Game Code
#This part defines all characters and places and creates the start of the game which the player decides their ->
# character and side, from this a variable of the players choice is made.
#Characters, Settings & Plot
#Allows to put delays between print statements
from time import sleep
#Good Characters placed in list
good_Characters = "Spiderman", "Ironman","Hulk"
#Bad Characters placed in list
bad_Characters = "Thanos", "Docter Doom", "Galactus"
#Value for continuing game
continue_Game = "None"
# One second delay when using ;sleep(seconds)
print("--= Hello Welcome to Marvel Riddlemania =--\n--= See if your a true Marvel Fan =--") ;sleep(1)
print("- Points will be given when answered correctly\n- Points will not be deducted when used help only when giving up\n- Answer alphabetically") ;sleep(2)
print("--= Let's Get Started! =--") ;sleep(3)
print("")
print("--= It's time to choose your side. Are you a Hero or Villain? =--\nType your Answer Here:")
player_Side = "Noone"
player_Name = "None"
# Player chooses their side .upper allows the answer to not be case-sensative
player_Side = input().upper()
#Block of code where player chooses character and code checks,block ends at line 56.

if player_Side == "HERO":
    print("- Which Hero do you want to be:")
    print(good_Characters)
    superhero_Choice = input().upper()
    # All options are listed and choosen character is given value player_Name
    if superhero_Choice == "SPIDERMAN":
        player_Name = 'Spiderman'
    elif superhero_Choice =="IRONMAN":
        player_Name = "Ironman"
    elif superhero_Choice == "HULK":
        player_Name = "Hulk"
    else:
        print("Write a Character shown in box")
elif player_Side == "VILLAIN":
    print("- Welcome to the Darkside...\n Which Character do you want to be?")
    print(bad_Characters)
    superhero_Choice = input().upper()
    # All options are listed and choosen character is given value player_Name
    if superhero_Choice == "THANOS":
        player_Name = 'Thanos'
    elif superhero_Choice == "DOCTOR DOOM":
        player_Name = 'Doctor Doom'

    elif superhero_Choice == "GALACTUS":
        player_Name = 'Galactus'
else:
    print("Write a character shown in box")

print("--= Alright" + " " + str(player_Name) + " " + "time to earn some points =--") ;sleep(1)
print("--= First Question =--") ;sleep(3)
points = 0

#All Riddle questions follow same code in repeat with different questions
while True:
    # prints the question
    print('--= How many Iron Man movies are there? =--')
    # after question is printed player is given a choice to answer, they can also ask for guesses
    print("- Type your guess, or 'I give up' below.")
    # answer is defined as the input of player
    answer = input().upper()
    if "THREE" in answer:
        print("- Great Job your Right!") ;sleep(1)
        # one point is awarded if answered correctly
        points += 1
        print("- You get " + str(points) + " " + "points") ;sleep(2)
        break
    #If the player doesn't know the answer they can give up.
    elif answer.upper() == "I GIVE UP":
        print("The answer was three! Come on seriously?") ;sleep(4)
        points -= 0.5
        break

    else:
        print("Try again!")
print(" ")
print("--= Second Question =--");sleep(3)
while True:
    print("--= What iconic logo is on the t-shirt of the Marvel character, The Punisher? =--")
    print("- Type your guess, or 'I give up' below.")
    answer = input().upper()


    if "SKULL" in answer:
        print("- Nice One!") ;sleep(1)
        print("- You got 4 points! That was a tricky one.")
        points += 4
        print('You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- THE ANSWER WAS skull!, are you really a true fan?")
        points -= 0.5
        break

    else:
        print("Try again!")
print(" ")
print("--= Third Question =--") ;sleep(3)
while True:
    print("--= How many Marvel movies are there? =--")
    print("- Type your guess, or 'I give up' below.")
    answer = input().upper()

    if "TWENTY THREE" in answer:
        print("- Wow your on a roll!") ;sleep(1)
        print("- You got 2 points!")
        points += 2
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- THE ANSWER WAS twenty three!, im questioning whether your a real one!")
        points -= 0.5
        break

    else:
        print("Try again!")
print(" ")
print("--= Fourth Question =--") ;sleep(3)
while True:
    print("--= In which continent is the country from which Black Panther originates? =--")
    print("- Type your guess, or 'I give up' below.")
    answer = input().upper()

    if "AFRICA" in answer:
        print("- That was a easy one!") ;sleep(1)
        print("- You get 1 point!")
        points += 1
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- Seriously the answer was Africa, that was the easiest question")
        points -= 0.5
        break

    else:
        print("- Try again!")
print(" ")
print("--= Fifth Question =--") ;sleep(3)

while True:
    print("--= What is the name of Samuel L Jackson’s character? =--")
    print("- Type your guess, or 'I give up' below.")
    answer = input().upper()

    if "FURY" in answer:
        print("- I see your a pro!") ;sleep(1)
        print("- You got 2 points!")
        points += 2
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- THE ANSWER WAS a fury! Hmm are you a imposter!")
        points -= 0.5
        break

    else:
        print("Try again!")
print(" ") ;sleep(1)

print("--= Sixth Question =--") ;sleep(3)
while True:
    print("--= Who plays Thor? =--")
    print("- Type your guess, or 'i give up' below.")
    answer = input().upper()

    if "CHRIS" in answer:
        print("- Hmm are you cheating mister!") ;sleep(1)
        print("- You got 3 points!")
        points += 3
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- Ok, i don't know what to say.")
        points -= 0.5
        break

    else:
        print("- Try again!")
print(" ");sleep(1)
#This asks the person a If statement whether they want to continue or stop playing
print("--= Do you want to try some harder questions or stop? =--") ;sleep(1)
print("Type Y or N:")
#This will put they input in upper keys
continue_Game = input().upper()
#If player says N it will print their points and it quits the game
if continue_Game == "N":
    print("--= Thanks for playing, you finished with" + " " + str(points) + " " + "points, Nice Job! =--\n Hope you Enjoyed!") ;sleep(4)
    quit()
#The game will continue with further riddles which are harder
elif continue_Game == "Y":
    print("Alright your a tough one! I see...");sleep(2)
while True:
    # prints the question
    print("--= In the X-Men films, what's the name of Professor Xavier's telepathy-enhancing machine? =--")
    # after question is printed player is given a choice to answer, they can also ask for guesses
    print("- Type your guess, or 'I give up' below.")
    # answer is defined as the input of player
    answer = input().upper()
    if "CEREBRO" in answer:
        print("- Nice, i thought these would be too tricky for you!") ;sleep(1)
        # one point is awarded if answered correctly
        points += 3
        print("- You have " + str(points) + " " + "points") ;sleep(2)
        break
    elif answer.upper() == "I GIVE UP":
        print("The answer was Cerebro! Come on seriously?") ;sleep(4)
        points -= 0.5
        break
    else:
        print("Try again!")
print(" ")
print("--= Second Question =--");sleep(3)
while True:
    print("--= How many Infinity Stones are there? =--")
    print("- Type your guess, or 'I give up' below.")
    answer = input().upper()
    if "SIX" in answer:
        print("- Well, that was pretty easy! Right?") ;sleep(1)
        print("- You got 1 point! That was a tricky one.")
        points += 1
        print('You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- THE ANSWER WAS six! Come on that was pretty easy!")
        points -= 0.5
        break

    else:
        print("Try again!")
print(" ")
print("--= Third Question =--") ;sleep(3)
while True:
    print("--= How many Marvel TV series have been created? =--")
    print("- Type your guess, or 'I give up' below.")
    answer = input().upper()

    if "TWELVE" in answer:
        print("- Wow, that was a tricky one... for me at least!") ;sleep(1)
        print("- You got 2 points!")
        points += 2
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break

    elif answer.upper() == "I GIVE UP":
        print("- THE ANSWER WAS TWELVE!, that wasn't to tricky right!")
        points -= 0.5
        break

    else:
        print("Try again!")
print(" ")
print("--= Fourth Question =--") ;sleep(3)
while True:
    print("--= What is the name of Thor’s hammer?\n- No help for this one! =--")
    print("- Type your guess")
    answer = input().upper()

    if "MJOLNIR" in answer:
        print("That was not too hard!") ;sleep(1)
        print("You get 2 point!")
        points += 2
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break
    elif answer.upper() == "I GIVE UP":
        print("- Seriously the answer was Mjolnir. Tongue Twister!")
        points -= 0.5
        break
    else:
        print("Try again!")
print(" ")
print("--= Fifth Question =--") ;sleep(3)

while True:
    print("--= In which film’s post-credit scene did Thanos first appear? =--")
    print("- Type your guess")
    answer = input().upper()

    if "AVENGERS" in answer:
        print("Nice one!") ;sleep(1)
        print("You get 2 point!")
        points += 2
        print('- You currently have' + " " + str(points) + ' ' + 'points') ;sleep(2)
        break
    elif answer.upper() == "I GIVE UP":
            print("- THE ANSWER WAS a The Avengers! Hmm are you a imposter!")
            points -= 0.5
            break
    else:
        print("Try again!")

print(" ") ;sleep(2)
print("--= Good job! You got" + " " + str(points) + " " + "points. =--\n --= You've completed the game!")

if points >= 15:
    print("--= I see your a pro, great job! =--") ;sleep(2)
elif points <= 14:
    print("--= Maybe a little reading up will help i guess? =--") ;sleep(2)

print("--= Thanks for playing hope you enjoyed! =--")
