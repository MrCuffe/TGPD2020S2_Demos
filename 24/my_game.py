#riddle game/adventure game
#keira gribben DY2 2020
#print statement at the start to introduce player to game
print("You're have been held captive! Answer the questions how you beleive is correct and escape, fail to do so and your stuck here:)")
#opens file that contains the questions 
file = open("rooms.txt", "r")
#read lines of the file
rooms = file.readlines()
room = 0
#a while loop that bases answers to solutions so far in the game givng people chances to win and lose
while True:

# Sanity check to make sure I don't make mistakes in my rooms.txt file
    if room > len(rooms)-1:
        print("You made a mistake in the rooms.txt file!")
        exit()
    
    current_room = rooms[room].strip().split("|")
#if statment, if you are taken to room/line 1 you have failed and didnt escape
    if(current_room[1] == "RETRY"):
        print(current_room[0] + "\n\n")
        room = 0
        continue

# Convert every second value to be a number, as every second value is a room value
# EG: Room 4
    for i in range(1,len(current_room)):
        if i % 2 == 0:
            current_room[i] = int(current_room[i])
#while loop and if statement
            #possible answers:
    answers = 'abcdefghijklmnopqrstuvwxyz'
    #code starts at room/line 0 because the lines start at 0 the 1,2,3 etc...
    while True:
        print(current_room[0])
        count = 0
        #this part allows the  "|Yes|8|No|7" parts of the code (the numbers 8 & 7 are just examples) to transfer you to the number correlating to the lines in the txt file
        for i in range(1,len(current_room)):
            if i % 2 == 1:
                print(answers[count] + ": " + current_room[i])
                count += 1
        answer = input()
        #if statement, possible answer, anything outside of a and b will repeat the question, so there are no invalid answers
        if answer not in answers or answers.index(answer) > count-1:
            #print statement
            print("Bad answer!")
            continue
#break will stop the code from forever repeating itself
        room = current_room[answers.index(answer)*2+2]
        break
    #end of code
            

    
    
