#Matthew He
#The Day to graduate, a text based python game

# Basic inputs, the things inputted by the player
#Sets up a list that records the yes and no which can be used later to compare the player input e.g. python asks a input, player puts yes, a if or elif statement uses this list to get an idea pf whether the input was yes or not
yes_no = ["yes", "no"]
#Makes 3 lists of answer inputs, which later will be used when a player inputs A,B or C for a question
answer_A = ["A","a"]
answer_B = ["B","b"]
answer_C = ["C","c"]
hint_set = ["D","d"]
#The variable here is set to global, which means that the variable can be accessed by every function and changes made to it will be the same for all different functions
global score
#Sets the varibale to 0 first, gives it a value so it can be changed later
score=0 
#Defines a function where it would start off the game and the prints within informs the player what their goal would be
global score_2
score_2=0
def start():
    #Makes the playername global, so later on it can be used in other functions for a better player experience
    global playername
    #Asks the player for his/her name using an input 
    playername = input("Hello there player, what is your name?\n") # Gets the player name into the system
    #Print out something to give the player some background info, using the player name from before
    print("Welcome " + playername)
    print("You wake up from bed, realising this is the last day of school and the day of the exam")
    print("You goal is to make it through school, completeing all 3 of your exams")
    #Leads to the next function, which will be the next section of the game
    school_1()

#Defines a function mentioned in the previous code which can also be used to loop back
def school_1():
    #Prints out info telling the player the game has actually started
    print("You head over to your first class, preparing to complete a maths test from your maths teacher")
    #another player input which this time will have ultiple choice, effectively starting actual gameplay
    playerinput2= input("You hear your name get called, what do you do?\nA.Go to your teachers\nB. Ditch school today\n")
    #The if statement sets the premise, the in statement compares the player input to the list in ealier code, if the "in" criteria is met then the code within it will trigger
    if playerinput2 in answer_A: 
        #Goes to the next section of the game through starting another defined function
        test_1a()
    #The elif here sets up another premise regarding the list in the starting codes, trigger the code within the "in" statement if the "answer_B" list criteria is met, so if input = B the code starts
    elif playerinput2 in answer_B:
        print("You ditched school, never to return\nGame Over")
        end_screen_1()
    #The else sets a condition when the input isn't what the game asked for
    else:
        print("Looks like you haven't chosen a correct ooption, try again?")
        #Loops back to the start of the function
        school_1()

#Defines a function with codes within so it's easily accessible
def test_1a():
    print("Hello there, your test will consist of 4 multiple choice question using basic maths we've learnt this year, you pass if you get 3 or more correct") 
    playerinput3_a= input("Here's your first qeustions, what is 2 + 2\n A.3\n B.4\n C.6\n") 
    #If statement so when the input is scanned and it's within the condition, the code will trigger
    if playerinput3_a in answer_A: 
        print("Incorrect, better luck on the next questions") 
        #Moves onto the next function after triggering the code
        test_1b() 
    #Elif statement sets up another premise for the input, so when python scans the input and it's the correct condition, code gets triggered
    elif playerinput3_a in answer_B:
        print("Correct, keep it up!")
        #Pulls up the score from global
        global score
        #Add one to it, signalling that the player has got the answer correct
        score += 1
        #Moves onto the next function
        test_1b()
    #Another Elif setting up another condition for the input
    elif playerinput3_a in answer_C:
        print("Incorrect, better luck on the next question")
        #Moves onto the next part of the game
        test_1b()
    #Else serves as an emergency protocal for when input is incorrect
    else:
        print("Please answer in A,B or C")
        #Loops back to the start
        test_1a()

#Defines the function that was mentioned in test_a()
def test_1b():
    print("here's your 2nd questions, ready or not here it comes")
    #Asks for player input which will be scaned by python
    playerinput3_b= input("If an animal has 3 legs, and a farmer has 5 of said animal, how many combined legs would there be?\n A.20\n B.31\n C.15\n")
    #If statement makes sure that the playerinput will trigger a code when scanned
    if playerinput3_b in answer_A:
        print("Incorrect, better luck on the next questions")
        #Moves onto to the next section of the game
        test_1c()
    #Elif sets another condition for the input scanned by python
    elif playerinput3_b in answer_B:
        print("Incorrect, better luck on the next questions")
        #Moves onto the next part of the game
        test_1c()
    #Another Elif statement which will trigger when the input meets a certain condition
    elif playerinput3_b in answer_C:
        print("Correct, keep it up")
        #Pulls up the score from before again
        global score
        #Add another 1 to it which signals that the answer was corret
        score += 1
        #Mives onto the next section of the game
        test_1c()
    #Else serves as emergency protocal and triggers when the input doesn't fit the correct format
    else:
        print("Please answer in A,B or C format")
        #Loops back to the start 
        test_1b()

#Defines the function mentioned in code above
def test_1c():
    print("3rd questions, are you ready?")
    playerinput3_c= input("If Bob has 3 more cars than John and John has half as many cars as Dwayne, how many cars would Bob have provided Dwayne has 10 cars? \n A.8\n B.9\n C.10\n")
    #If here sets up another premise for the input
    if playerinput3_c in answer_A:
        print("Correct, keep it up!")
        #Pulls up score
        global score
        #Add 1 more to the score
        score += 1
        #Moves onto the next section of the game
        test_1d()
    #Elif which sets a premise for the input
    elif playerinput3_c in answer_B:
        print("Incorrect, better luck on the next questions.")
        #Moves onto the next part
        test_1d()
    #Sets a premise for the input
    elif playerinput3_c in answer_C:
        print("Incorrect, better luck on the next questions")
        #Moves onto the next part
        test_1d()
    #Emergency protocal to catch unmatching player input
    else:
        print("Please answer in only A,B or C format")
        #Loops back to the beginning of this function
        test_1c()

#Defines the last part of the test
def test_1d():
    print("Last question, are you ready?")
    #Asks for playerinput once more
    playerinput3_d= input("If 2 to the power of 3 is 8, what would be 10 minus 2 to the power of 3?\nA. 16\nB. 20\nC. 2\n")
    #Checks the playerinput for the right condition which triggers a code
    if playerinput3_d in answer_A:
        print("Incorrect. Test is now over.")
        #Goes to after the test
        after_test_1()
    elif playerinput3_d in answer_B:
        print("Incorrect. Test is now over.")
        after_test_1
    elif playerinput3_d in answer_C:
        print("Correct! Test is now over.")
        global score
        score += 1
        after_test_1()
    else:
        print("Please answer in only A,B or C format")
        test_1d()

#Defines the function which shows players what happen when they finish the 1st test
def after_test_1():
    #Checks that global variable which keeps track of correct answers, and if it passes the goal, the player passes the test
    if score >= 3:
        #Tells the player he/she has won
        print(playername + ", congradulations! You passed the test! Now you can leave the class")
        #Goes to the next part
        test_2()
    #Checks score and if it doesn't match the goal, another code is triggered
    elif score < 3:
        #Tells the player he/she didn't pass
        print("Unfortunately you didn't pass this time, I'll see you next semester if you want to repeat this test")
        #Goes to the lost screen
        end_screen_1()
    elif score == 4:
        print("Secret achievement unlocked, 'all correct'")
        print(playername + ", congradulations! You passed the test! Now you can leave the class")
        test_2()
        
#Starts the 2nd test
def test_2():
    print("After successfully completing your 1st test of the day, you feel great about yourself as you head for your second assessment, your science test")
    #Bring out the playername from before and used here to better player involvement
    global playername
    playerinput_2= input(playername + ", come up for your test!\nA. go up\nB. Ditch\n")
    if playerinput_2 in answer_A:
        print("You went up and began your test")
        print(playername + ", glad you're here for your science finals, this test is going to be composed of four questions, getting three or more will get you a pass. Let's begin.")
        test_2a()
    elif playerinput_2 in answer_B:
        print("Upon hearing your name, you fled the scene")
        end_screen_1()
    else:
        print("Please put answers as A,B or C")
        test_2()
    
#Defines the start of the new test, so everything in here will be code for question 1 of test 2
def test_2a():
    #Asks the player for an answer to the question
    playerinput_2a = input("Question One. How fast would light travel in a vaccuum? \nA. 10m/s\nB.1,000,000m/s\nC. 299,729km/s\nD. Hint\n")
    #If player answers is in the list then the code underneath the if will trigger
    if playerinput_2a in answer_A:
        #Tells player they got the question wrong and gives the correct answer
        print("Incorrect, " + hint_1a)
        #Moves onto the next quesstion
        test_2b()
    #If the player's input was in this list then the code under the elif will trigger
    elif playerinput_2a in answer_B:
        #Tells the player the answer was wrong and moves to the next question
        print("Incorrect, " + hint_1a)
        test_2b()
    #If the player's input was in this list then the code under the elif will trigger
    elif playerinput_2a in answer_C:
        #Tells the player he's correct
        print("Correct, keep this up")
        #Pulls up the variable recording the amount of right answers for this test and adds 1 to it
        global score_2
        score_2 += 1
        #Moves to the next test
        test_2b()
    #Here the player's in put will be asking for a hint, which triggers this one
    elif playerinput_2a in hint_set:
        #Prints the hint and the question again
        print(hint_1a)
        test_2a()
    #Makes sure the player answer isn't something weird, so if it's not in the right format the question is asked again
    else:
        print("Please only answer in A, B, C or D")
        test_2a()

#Start of the second question
def test_2b():
    #Asks for input after a question
    playerinput_2b = input("Question Two. What is the freezing point of water?\nA. 10 degrees celsius\nB. 30 degrees celsius\nC. 0 degrees celsius\nD. Hint\n")
    #If play answers A then it prints the answer is wrong and goes to the next one
    if playerinput_2b in answer_A:
        print("Incorrect, " + hint_1b)
        test_2c()
    #If the answer is B then it prints its wrong as well and goes to the next question
    elif playerinput_2b in answer_B:
        print("Incorrect, " + hint_1b)
        test_2c()
    #If the player answers C then it prints its correct and adds 1 more point to the scores of the second test
    elif playerinput_2b in answer_C:
        print("Correct! Water does freeze at 0 degree celsius")
        global score_2
        score_2 +=1
        test_2c()
    #Prints a hint if player answers D then asks the question again
    elif playerinput_2b in hint_set:
        print(hint_1b)
        test_2b
    #makes sure player doesn't answer in weird stuff, so it starts the question again telling the player to answer in A B C or D
    else:
        print("Please only answer in A, B, C or D")
        test_2b()

#3rd question of the test
def test_2c():
    #Asks for an answer after giving the 3rd question
    playerinput_2c = input("Question Three. What scale is earthquakes measured in?\nA. Mecalli Scale\nB. Shakey Scale\n Richter Scale\nD. Hint\n")
    #If it's a then yes it's correct and adds a point to the score of test 2 and moves on
    if playerinput_2c in answer_A:
        print("Correct, eatherquakes can be measued by the Mecalli Scale AND the Richter Scale")
        global score_2
        score_2 +=1
        test_2d()
    #If it's B then it's wrong and python tells that to the player and moves on
    elif playerinput_2c in answer_B:
        print("Incorrect, earthquakes are measured in the Mecalli Scale and the RIchter Scale")
        test_2d()
    #If it's C the  it's correct as well and adds a point to the score for test 2 and moves onto the next question
    elif playerinput_2c in answer_C:
        print("Correct! eatherquakes can be measued by the Mecalli Scale AND the Richter Scale")
        score_2 +=1
        test_2d()
    #If the plaeyr wants a hint then python prints the hing
    elif playerinput_2c in hint_set:
        print(hint_1c)
        test_2c
    #Makes sure player doesn't put in things not in the right test foramt
    else:
        print("Please only answer in A, B, C or D")
        test_2c()



global hint_1a
hint_1a = ("light travels at 299,729 kilometers per second")
global hint_1b
hint_1b = ("Water gets cold the lower the celsius")
global hint_1c
hint_1c = ("Earthquakes can be measured by the two scales created by Giuseppe Mercalli and Charles Francis Richter")
global hint_1d
hint_1d = ("The gravity on Earth is roughyl around 10, but not exactly")
#End screen
def end_screen_1():
    #Asks if the player wants to play again
    playerinput_end = input("Looks like you couldn't win this time, wanna try again?\n yes?\n no?\n")
    #If the player says yes then game starts again
    if playerinput_end == "yes":
        print("Great! Better luck this time!")
        start()
    #IF the player says no then the game ends
    elif playerinput_end == "no":
        print("Okay then, hope you return very soon.\n The END")
    #ANything other than yes or no will loop back again, asking the question once more
    else:
        print("Not sure what you meant? Wanna try again?")
        end_screen_1()
                            
    
#In chronological order so the game progresses during sections where manual actions won't lead to game progression    
start()#starts off the quest
