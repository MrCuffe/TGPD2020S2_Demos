#MADE BY: VIBHA SRINIVASAN
#TEXT-BASED GAME
#DEVELOPMENT PLAN: PHASE 4 (FINAL PHASE)
#ERRORS: None. It works.
#ADMINISTRATION: All phases have been met. I get that it's complicated, but it works and I do explain how it works with many comments.
#PRESENTATION: All blocks of code have headings and lines that explain what's happening. All grammar and spelling mistakes on QuestionList.txt have been fixed
#GAME DEVELOPMENT DOCUMENT: Has been submitted. APA referencing has been used. Used correct format from template.

import csv #Import the list
def intersection(lst1, lst2):
    lst3=[]
    for i in lst1:
        if i in lst2:
            lst3.append(i)
    return lst3

#A collection of questions that will definitely be asked when the game is played
def getanswerfromuser(questionid): 
    answer='Unknown'
    if questionid==1: #First question asked to user
        answer=input("Enter your year level (1,2,3,4,5 or 6) or enter quit: ").capitalize()
    elif questionid==2: #Second question asked to user
        answer=input("Are you feeling tired or motivated? ").capitalize()
    elif questionid==3: #Third question asked to user
        answer=input("Would you like to study numbers or letters? ").capitalize()
    else: #Last question asked to user
        answer=input("Do you want to play again(Yes/No)?: ").capitalize()
    return answer

#Main program that asks for input, provides questions, checks answers and displays the score
def mainprogram(): #Name of program being repeated
    while True: #Checks grade_i answer in case user wants to quit
        grade_i = getanswerfromuser(1) #Stores their answer for question 1 from collection above
        if  (grade_i=="1" or grade_i=="2" or grade_i=="3" or grade_i=="4" or grade_i=="5" or grade_i=="6" or grade_i=="Quit"):
            break #If their answer is one of the above, the program continues with the next lines of code
    if grade_i=="Quit":
        exit() #If the user writes "quit" (case not sensitive) then the program ends right there
    while True: #Checks mood_i answer in case user wants to quit
        mood_i = getanswerfromuser(2) #Stores their answer for question 2 from collection above
        if (mood_i=="Tired" or mood_i=='Motivated' or mood_i=='Quit'):
            break #If their answer is one of the above, the program continues with the next lines of code
    if mood_i=="Quit":
        exit() #If the user writes "quit" (case not sensitive) then the program ends right there
    while True: #Checks subject_i answer in case user wants to quit
        subject_i = getanswerfromuser(3) #Stores their answer for question 3 from collection above
        if (subject_i=="Numbers" or subject_i=='Letters' or subject_i=='Quit'):
            break #If their answer is one of the above, the program continues with the next lines of code
    if subject_i=="Quit":
        exit() #If the user writes "quit" (case not sensitive) then the program ends right there

    #Column Headers from list
    grades=[]
    moods=[]
    subjects=[]
    questions=[]
    answers=[]
    
    #Using a List
    with open('QuestionList.txt','r') as f:
        next(f) # skip headings
        reader=csv.reader(f,delimiter='\t')
        
        for grade,subject,mood,question,answer in reader:
            grades.append(grade.capitalize()) #adds grade to list
            moods.append(mood.capitalize()) #adds mood to list
            subjects.append(subject.capitalize()) #adds subject to list
            questions.append(question.capitalize()) #adds question to list
            answers.append(answer.capitalize()) #adds corresponding answers to list

    #Decides the Number of Questions Using If Statement
    score=0 #Defined to count correctly answered questions
    if mood_i == "Tired": 
        question_cnt= 5 #if user's input is "Tired", then only ask 5 questions
        print("\nLook's like you are tired, try these 5 questions. Good luck, you got this!!")
    else:
        question_cnt= 10 #if user's input is "Numbers", then ask 10 questions
        print ("\nAwesome, look's like you are motivated! Here are 10 questions for you to try!!")
    
    #Finding Values in List
    indices_m = [i for i, x in enumerate(moods) if x == mood_i] #Values on the list that correspond with chosen mood
    indices_s = [i for i, x in enumerate(subjects) if x == subject_i] #Values on the list that correspond with chosen subject
    indices_g = [i for i, x in enumerate(grades) if x == grade_i] #Values on the list that correspond with the chosen grade
    indices_t=intersection(intersection(indices_m,indices_s),indices_g)#Values with all three above in common

    #Starts Using Corresponding Values to Find Questions
    cnt=0 #Question they are on
    for val in indices_t:
        if cnt < question_cnt:
            answer = input(questions[val]).capitalize() #Makes sure to capitalize the first letter so that the answer isn't case sensitive
            if answer == answers[val]: #If the user's answer is the same as the correct answer, add one to their score and print this
                score+=1 #Counting correct answers
                print("\u2713 Well done. Your answer is correct!! \U0001F603 \n")
            else: #If the user's answer is wrong, print this
                print("\u2718 Wrong answer. Try your best for the next question! You got this!! \U0001F615 \n")
            cnt=cnt+1 #Move on to next question
        else: #If the cnt > question_cnt (finished all the questions) move on to the next line of code
            break
    print("Well Done! You scored " + str(score) + " out of " + str(question_cnt)+ " questions asked!\n")
    return 

while True:
    mainprogram() #Run mainprogram asking questions, checking responses, etc.
    again=getanswerfromuser(4) #Ask user if they want to play again
    if not (again =="Yes" or again=="Y"): #If they say No, or anything other than Yes/Y, the program breaks
        break

   
