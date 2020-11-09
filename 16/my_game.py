
print ("Welcome to level 1 of the geography quiz, you need to get 5 questions right to pass!")

score = 0
# QUESTION 1
answer1 = input ("What is the capital city of Spain? \na. Barcelona \nb. Granada \nc. Madrid \nanswer: ")
if answer1 == "c" or answer1 == "Madrid":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Madrid.")
    print ("Score: ", score)
    print ("\n")
    

# QUESTION 2
answer1 = input ("What is the capital city of Vietnam? \na. Hanoi \nb. Ho Chi Minh City \nc. Dalat \nanswer: ")
if answer1 == "a" or answer1 == "Hanoi":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Hanoi.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 3
answer1 = input ("What is the capital city of Australia? \na. Sydney \nb. Melbourne \nc. Canberra \nanswer: ")
if answer1 == "c" or answer1 == "Canberra":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Canberra.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 4
answer1 = input ("What is the capital city of New Zealand? \na. Auckland \nb. Wellington \nc. Hamilton \nanswer: ")
if answer1 == "b" or answer1 == "Wellington":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Wellington.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 5
answer1 = input ("What is the capital city of Canada? \na. Ottawa \nb. Toronto \nc. Brampton \nanswer: ")
if answer1 == "a" or answer1 == "Ottawa":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Ottawa.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 6
answer1 = input ("What country is Zurich in? \na. Germany \nb. Greece \nc. Switzerland \nanswer: ")
if answer1 == "c" or answer1 == "Switzerland":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Switzerland.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 7
answer1 = input ("What country is Osaka in? \na. Japan \nb. Thailand \nc. The Phillippines \nanswer: ")
if answer1 == "a" or answer1 == "Japan":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Japan.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 8
answer1 = input ("What country is Agra in? \na. India \nb. Myanmar \nc. Malaysia \nanswer: ")
if answer1 == "a" or answer1 == "India":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is India.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 9
answer1 = input ("What country is Amsterdam in? \na. Greece \nb. Germany \nc. Netherlands \nanswer: ")
if answer1 == "c" or answer1 == "Netherlands":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Netherlands.")
    print ("Score: ", score)
    print ("\n")
    
# QUESTION 10
answer1 = input ("What country is Bern in? \na. Switzerland \nb. Greece \nc. Germany \nanswer: ")
if answer1 == "a" or answer1 == "Switzerland":
    score += 1 
    print ("Correct!")
    print ("Score: ", score)
    print ("\n")
else:
    print ("Incorrect! The answer is Switzerland.")
    print ("Score: ", score)
    print ("\n")
    
# LEVEL 1 COMPLETE: FINAL MESSAGE
if score <= 5:
    print ("Your total score is:", score, "Failed, better next time?")
elif score <= 8:
    print ("Your total score is:", score, "Passed, you did good!" )
else:
    print ("You did very good! Well done!")
