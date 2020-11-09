#Game Name: Riddle Me This
#Author: Deanna Azucena

#Game Development Phase 1
#Introducing the characters in the game and introducing storyline

#Characters
riddle_master = "" #Player inputs their name
boss_master1 = ["Mr Riddle"]
boss_master2 = ["Professor Riddler"]
boss_master3 = ["Dr Riddle"]

#Setup
yes_no = ["yes","no"]

#First Stage Riddles: Part of Phase 3
#First Stage - Easy Riddle
def easy(response):
#Guess will start at 0
  guess = 0
  answer = ("Age").lower()
  #player is given the riddle and has an option to type in an answer or use a hint
  while True:
      print("What goes up but never comes down?")
      print("Type your guess, or type hint below.")
      answer = input()
    #Every guess, will add one onto the previous number of guesses before
      guess += 1
    #get the player to answer the riddle before it falls into the while code
      if "Age" in answer:
        print("Correct!\u2714")
        print("It took you " + str(guess) + " guess/es.")
        break
      #player will be given a hint if they type 'hint' in the input
      elif answer == "hint":
        print("You turn older every year because of this.")
      else:
        print("Try again.\u2717")
        print("This one's pretty easy...")
  #this will print when the player gets the correct answer      
  return "You have gained one coin."
  
#First Stage - Medium Riddle
def medium(response):
#Guess will start at 0
  guess = 0
  answer = ("Clock").lower()
  #player is given the riddle and has an option to type in an answer or use a hint
  while True:
      print("What has hands but can't clap?")
      print("Type your guess, or type hint below.")
      answer = input()
    #Every guess, will add one onto the previous number of guesses before
      guess += 1
    #get the player to answer the riddle before it falls into the while code
      if "Clock" in answer:
        print("Correct!\u2714")
        print("It took you " + str(guess) + " guess/es.")
        break
      #player will be given a hint if they type 'hint' in the input
      elif answer == "hint":
        print("Only time will tell.")
      else:
        print("Try again.\u2717")
        print("Think! Think! Think!")
  #this will print when the player gets the correct answer     
  return "You have gained two coins."

#First Stage - Hard Riddle
def hard(response):
#Guess will start at 0
  guess = 0
  answer = ("River").lower()
  #player is given the riddle and has an option to type in an answer or use a hint
  while True:
      print("What can run but never walks, has a mouth but never talks, has a head but never weeps, has a bed but never sleeps?")
      print("Type your guess, or type hint below.")
      answer = input()
    #Every guess, will add one onto the previous number of guesses before
      guess += 1
    #get the player to answer the riddle before it falls into the while code
      if "River" in answer:
        print("Correct!\u2714")
        print("It took you " + str(guess) + " guess/es.")
        break
    #player will be given a hint if they type 'hint' in the input
      elif answer == "hint":
        print("I am a water source.")
      else:
        print("Try again.\u2717")
        print("Come on, you can do it!")
  #this will print when the player gets the correct answer       
  return "You have gained three coins."

#Second Stage Riddles: Part of Phase 4
#Second Stage - Easy Riddle
def second_easy(response):
#Guess will start at 0
  guess = 0
  answer = ("Future").lower()
  #player is given the riddle and has an option to type in an answer or use a hint
  while True:
    print("What is always in front of you but can't be seen?")
    print("Type your guess, or type hint below.")
    answer = input()
  #Every guess will add one onto the previous number of guesses before
    guess += 1
  #get the player to answer the riddle before it falls into the while loop
    if "Future" in answer:
      print("Correct!\u2714")
      print("It took you " + str(guess) + " guess/es.")
      break
  #player will be given a hint if they type 'hint' in the input
    elif answer == "hint":
      print("The past, the present, the ...")
    else:
      print("Try again.\u2717")
      print("Come on, you can do better than that!")
  #this will print when the player gets the correct answer
  return "You have gained one coin."
  
#Second Stage - Medium Riddle
def second_medium(response):
#Guess will start at 0
  guess = 0
  answer = ("Darkness").lower()
  #player is given the riddle and has an option to type in an answer or use a hint
  while True:
      print("The more of this there is, the less you see. What is it?")
      print("Type your guess, or type hint below.")
      answer = input()
    #Every guess, will add one onto the previous number of guesses before
      guess += 1
    #get the player to answer the riddle before it falls into the while code
      if "Darkness" in answer:
        print("Correct!\u2714")
        print("It took you " + str(guess) + " guess/es.")
        break
      #player will be given a hint if they type 'hint' in the input
      elif answer == "hint":
        print("I appear when the lights are gone.")
      else:
        print("Try again.\u2717")
        print("This one is easy peasy.")
  #this will print when the player gets the correct answer     
  return "You have gained two coins."

#Second Stage - Hard Riddle
def second_hard(response):
#Guess will start at 0
  guess = 0
  answer = ("Silence").lower()
  #player is given the riddle and has an option to type in an answer or use a hint
  while True:
      print("What is so fragile that saying its name breaks it?")
      print("Type your guess, or type hint below.")
      answer = input()
    #Every guess, will add one onto the previous number of guesses before
      guess += 1
    #get the player to answer the riddle before it falls into the while code
      if "Silence" in answer:
        print("Correct!\u2714")
        print("It took you " + str(guess) + " guess/es.")
        break
    #player will be given a hint if they type 'hint' in the input
      elif answer == "hint":
        print("My lips are closed.")
      else:
        print("Try again.\u2717")
        print("Are you really the riddle master?")
  #this will print when the player gets the correct answer       
  return "You have gained three coins."

#Introduction
#Player can input their name to be used in the game
name = input("What is your name, riddle master? ")
print("Hello, " + name + ". You have just moved house and have been told to take out some boxes from the attic.")
print("You see a light coming from behind the shelf and find a box with a strange engravement on its lid.")
print("It feels like a question mark...")
print("'Hmm... I wonder what is in this mysterious box?' You think to yourself.")
 
#Start of game
response = ""
#Player is given their first choice
while response not in yes_no:
    response = input("Will you open the mysterious box?\nyes/no\n")
    if response == "yes":
        print("*WHOOSH* The floor beneath your feet suddenly opens and there is nothing there when you look down but a bright light.")
        print("Your feet touch the ground and you look around to see that you are in a room with a door in front of you.")
        print("You hear a voice that says, 'Welcome to Riddle World, riddle master.'")
    elif response == "no":
        print("You are not ready for this adventure, goodbye.")
        quit()
#Anything other than yes or no will ask for an answer that is either one of those
    else: 
        print("I didn't understand that.\n")

print("You walk towards the door and open it. You hear the voice again...")
print("'In order to return home, you must defeat 3 bosses by solving riddles. Think you can handle it?'")

#Explanation of the game
response = ""
while response not in yes_no:
#Player can learn more about the game or leave (another choice)
    response = input("Would you like to know more?\nyes/no\n")
    if response == "yes":
#If player chooses next, they are given information about how to beat the game
        print("'There are three difficulties that you can choose from depending on what you feel comfortable with.'")
        print("'Once you solve a riddle, you gain a certain amount of coins depending on the difficulty of the riddle you chose.'")
        print("'Easy riddles give you 1 coin, medium riddles give you 2 coins and hard riddles give you 3 coins.'")
        print("'You can make multiple guesses and even use hints to help you solve the riddle.'")
        print("'I wish you the best of luck, " + name + ".")
        print()
    elif response == "no":
        print("Boo, you're no fun.")
        quit()
    else:
        print("I didn't understand that.")

#Phase 2 - Practice riddle
print("'Before, we get into it, let's give you a practice riddle.'\n")

#Function that will print out the practice riddle
def practice_riddle():
    print("David's father has three sons: Snap, Crackle, and _____?")
    print("Fill in the blank.")

practice_riddle()

answer = ["David"]

#Input for practice riddle
response = ""
while response not in answer:
#There is only one correct answer, which is David
    response = input("What is your answer? ")
    if response == "David":
        print('That is the correct answer.')
        print('You would have gained 1 coin for this, however it is only a practice riddle.')
#Answer other than David will print out below and ask for another answer
    else:
        print('That is not the correct answer. Try again.')

#Response for solving the practice riddle
print("Congratulations on solving the practice riddle.")
print("Let's move onto the first level.")
print("You walk through a door with a sign above it saying 'First Stage'.\n")

#Phase 3
#First Stage
print("Welcome " + name + " to the First Stage.")
print("In front of you, there are three boxes that are each labelled easy, medium and hard.")
print("'So you are the riddle master I have been hearing about?' says Mr Riddle.")
print("Well, I don't think you can beat me!")
print("Remember, you can make as many guesses as you want and hints are also available.\n")

print("'Good luck, but I doubt you will end up leaving this place,'Mr Riddle whispers to you.")
difficulty = ["easy", "medium", "hard"]
response = ""

#Choosing your difficulty
while response not in difficulty:
  response = input("Choose your difficulty, easy, medium or hard: ")
  if response == "easy":
    print(easy(response))
  #call function for easy riddle
  elif response == "medium":
     print(medium(response))
  #call function for medium riddle
  elif response == "hard":
     print(hard(response))
  #call function for hard riddle
  else:
    print("Please choose another difficulty.")

#Phase 4: Second Stage
print("'Hmm... I see you are smarter than you look, riddle master.' exclaims Mr Riddle.")
print("'Good luck with Professor Riddle. HAHAHA.'\n")
print("Welcome " + name + " to the Second Stage.")
print("Same rules apply to this level but now you will have to defeat Professor Riddle.")
print("'I see you have beaten Mr Riddle. Well, my riddles are more difficult than his, so I'd like to see you try.'")
print("'Good luck, I guess.' cackled Professer Riddle.")
difficulty = ["easy", "medium", "hard"]
response = ""

#Choosing your difficulty
while response not in difficulty:
  response = input("Choose your difficulty, easy, medium or hard: ")
  if response == "easy":
    print(second_easy(response))
  #call function for second easy riddle
  elif response == "medium":
     print(second_medium(response))
  #call function for second medium riddle
  elif response == "hard":
     print(second_hard(response))
  #call function for second hard riddle
  else:
    print("Please choose another difficulty.")

print()
print("Congratulations " + name + "! You have beaten 2 out of the 3 bosses.")
print("Come back next time for the new update for the last part of Riddle World.")
print("Thanks for playing.\u263A")






    




