
# Tara Najibi- FUNNY SENTENCE QUIZ

#Say hello and ask them to answer the quesions- multiple choice+ tell them what they are supposed to do
print("hey, let's make a funny sentence together!")

player_choice1 =str(input("Question 1: Please choose between Black, Red, Pink, Purple, and Cyan:  "))
player_points = 0
level = 0

#while loop and if statements showing what would happen depending on the player's choice + calculating their points (add breaks and to not repeat it forever).
while player_choice1 != "":
    
#use or to make sure both capitalised and lower-case words count
    if player_choice1 == "Black" or player_choice1 == "black":
     player_points += 1
     break
    
    elif player_choice1 == "Red" or player_choice1 == "red":
     player_points += 2
     break

    elif player_choice1 == "Pink" or player_choice1 == "pink":
      player_points += 3
      break
    
    elif player_choice1 == "Purple" or player_choice1 == "purple":
     player_points += 4
     break
    
    elif player_choice1 == "Cyan" or player_choice1 == "cyan":
      player_points += 5
      break

    else:
      print("Sorry, choose one of the options!!")
      player_choice1 =str(input("Please choose between Black, Red, Pink, Purple, and Cyan:  "))

#give them their points and direct them to the next level
print(f"Your Points ={player_points},"" You can go to the next question!")


#starting the next question:

player_choice2 = str(input("Question 2: Where is your dream house? Beach, Forest, Mountain, or Desert:  "))

while player_choice2 != "":
       
    if player_choice2 == "Desert" or player_choice2 == "desert":
         player_points += 1
         break
    elif player_choice2 == "Mountain" or player_choice2 == "mountain":
        player_points += 2
        break

    elif player_choice2 == "Forest" or player_choice2 == "forest":
           player_points += 3
           break
    elif player_choice2 == "Beach" or player_choice2 == "beach":
        player_points += 4
        break
    else:
      print("Sorry, choose one of the options!!")
      player_choice2 = str(input("Question 2: Where is your dream house? Beach, Forest, Mountain, or Desert:  "))
   
print(f"Your Points ={player_points},"" You can go to the next question!")      
    
#starting question 3 with the same strategy:
player_choice3 = str(input("Question 3: Which city would you rather travel to? London, Cairo, Beijing, or New York:  "))

while player_choice3 != "":
       
    if player_choice3 == "New York" or player_choice3 == "new york" or player_choice2 == "New york" :
        player_points += 1
        break

    elif player_choice3 == "cairo" or player_choice3 == "Cairo":
        player_points += 2
        break
        
    elif player_choice3 == "beijing" or player_choice3 == "Beijing":
         player_points += 3
         break

    elif player_choice3 == "london" or player_choice3 == "London":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice3 = str(input("Question 3: Which city would you rather travel to? London, Cairo, Beijing, or New York:  "))         
      
print(f"Your Points ={player_points},"" You can go to the next question!")      

#Question 4 of the first question set:
player_choice4 = str(input("Question 4: Which number gives you a better feeling? 2, 8, 9, or 5:  "))

while player_choice4 != "":
       
    if player_choice4 == "five" or player_choice4 == "Five" or player_choice4 == "5" :
        player_points += 1
        break

    elif player_choice4 == "nine" or player_choice4 == "Nine" or player_choice4 == "9":
        player_points += 2
        break
        
    elif player_choice4 == "two" or player_choice4 == "Two" or player_choice4 == "2":
         player_points += 3
         break

    elif player_choice4 == "eight" or player_choice4 == "Eight" or player_choice4 == "8":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice4 = str(input("Question 4: Which number gives you a better feeling? 2, 8, 9, or 5:  "))        
      
print(f"Your Points ={player_points},"" You can go to the next question!")      

#Question 5 of the first question set:
player_choice5 = str(input("Question 5: What is your favourite season?  "))

while player_choice5 != "":
       
    if player_choice5 == "Summer" or player_choice5 == "summer":
        player_points += 1
        break

    elif player_choice5 == "Spring" or player_choice5 == "spring":
        player_points += 2
        break
        
    elif player_choice5 == "Winter" or player_choice5 == "winter":
         player_points += 3
         break

    elif player_choice5 == "Autumn" or player_choice5 == "autumn" or player_choice5 == "Fall" or player_choice5 == "fall":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice5 = str(input("Question 5: What is your favourite season?  "))
      
      
print(f"Your Points ={player_points},"" You can go to the next question!")      

#Question 6 of the first question set:
player_choice6 = str(input("Question 6: Your favourite drink: Tea, Coffee, Coke or Juice?  "))

while player_choice6 != "":
       
    if player_choice6 == "Juice" or player_choice6 == "juice":
        player_points += 1
        break

    elif player_choice6 == "Coffee" or player_choice6 == "coffee":
        player_points += 2
        break
        
    elif player_choice6 == "Tea" or player_choice6 == "tea":
         player_points += 3
         break

    elif player_choice6 == "Coke" or player_choice6 == "coke":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice6 = str(input("Question 6: Your favourite drink: Tea, Coffee, Coke or Juice?  "))        
      
print(f"Your Points ={player_points},"" You can go to the next question!")

#Question 7 of the first question set:
player_choice7 = str(input("Question 7: If you could meet one of these scientists, which one would you choose? Einstein, Hawking, Tesla, or Newton:   "))

while player_choice7!= "":
       
    if player_choice7 == "Einstein" or player_choice7 == "einstein":
        player_points += 1
        break

    elif player_choice7 == "Hawking" or player_choice7 == "hawking":
        player_points += 2
        break
        
    elif player_choice7 == "Tesla" or player_choice7 == "tesla":
         player_points += 3
         break

    elif player_choice7 == "Newton" or player_choice7 == "newton":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice7 = str(input("Question 7: If you could meet one of these scientists, which one would you choose? Einstein, Hawking, Tesla, or Newton:   "))       
      
print(f"Your Points ={player_points},"" You can go to the next question!")

#Question 8 of the first question set:
player_choice8 = str(input("Question 8: Question 8: Which sport do you like to play? Tennis, Soccer, Footy, or Volleyball :   ")) 

while player_choice8 != "":
       
    if player_choice8 == "Soccer" or player_choice8 == "soccer":
        player_points += 1
        break

    elif player_choice8 == "Tennis" or player_choice8 == "tennis":
        player_points += 2
        break
        
    elif player_choice8 == "Volleyball" or player_choice8 == "volleyball":
         player_points += 3
         break

    elif player_choice8 == "Footy" or player_choice8 == "footy":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice8 = str(input("Question : Question 8: Which sport do you like to play? Tennis, Soccer, Footy, or Volleyball :   "))      
      
print(f"Your Points ={player_points},"" You can go to the next question!")

#Question 9 of the first question set:
player_choice9 = str(input("Question 9: Choose a JMSS House- Wood, Doherty, Blackburn, or Flannery :   ")) 

while player_choice8 != "":
       
    if player_choice9 == "Blackburn" or player_choice9 == "blackburn":
        player_points += 1
        break

    elif player_choice9 == "Flanerry" or player_choice9 == "flannery":
        player_points += 2
        break
        
    elif player_choice9 == "Doherty" or player_choice9 == "doherty":
         player_points += 3
         break

    elif player_choice9 == "Wood" or player_choice9 == "wood":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice9 = str(input("Question : Question 9: Choose a JMSS House- Wood, Doerty, Blackburn, or Flannery :   "))      
      
print(f"Your Points ={player_points},"" You can go to the next question!")

#Question 10 of the first question set:
player_choice10 = str(input("Question 10: Which one would you order? Fries, Burger, Pizza, or Hot Dog :   ")) 

while player_choice8 != "":
       
    if player_choice10 == "Fries" or player_choice10 == "fries":
        player_points += 1
        break

    elif player_choice10 == "Burger" or player_choice10 == "burger":
        player_points += 2
        break
        
    elif player_choice10 == "hot dog" or player_choice10 == "Hot Dog" or player_choice10 == "Hot dog":
         player_points += 3
         break

    elif player_choice10 == "Pizza" or player_choice10 == "pizza":
         player_points += 4
         break
        
    else:
        print("Sorry, choose one of the options!!")
        player_choice10 = str(input("Question : Question 10: Which one would you order? Fries, Burger, Pizza, or Hot Dog :   "))      


#ideas: which celebrity, ur fav sport, harry potter stuff, friends, what language wanna learn, fav food
      
mushrooms=["Indigo Milk Cap Mushroom","Jelly Mushroom", "Lion's Mane Mushroom", "Meow Meow Mushroom","Boomers mushroom","Killer Mushroom","Big Bang Mushroom","Minecraft Mushroom","Mush Mush Mushroom", "Teeth Mushrom","Corona Mushroom"]

#define the mushrrom name here so I can use it in the last section
if player_points <= 15:
    your_mushroom_name = mushrooms[0]
elif player_points > 15 and player_points <= 18:
    your_mushroom_name = mushrooms[1]
elif player_points > 20 and player_points <= 22:
    your_mushroom_name = mushrooms[2]
elif player_points > 22 and player_points <= 24:
    your_mushroom_name = mushrooms[3]
elif player_points > 24 and player_points <= 26:
    your_mushroom_name = mushrooms[4]
elif player_points > 26 and player_points <= 28:
    your_mushroom_name = mushrooms[5]
elif player_points > 28 and player_points <= 30:
    your_mushroom_name = mushrooms[6]
elif player_points > 30 and player_points <= 32:
    your_mushroom_name = mushrooms[7]
elif player_points > 32 and player_points <= 34:
    your_mushroom_name = mushrooms[8]
elif player_points > 34 and player_points <= 36:
    your_mushroom_name = mushrooms[9]
elif player_points > 36 and player_points <= 38:
    your_mushroom_name = mushrooms[10]
elif player_points > 38 and player_points <= 41:
    your_mushroom_name = mushrooms[11]

#print spaces before and after the quiz result so it is easier to see the result
print("")
print(f"You are a {your_mushroom_name}!! ")


#Starting the next Question set which determines their fictional name

print("")
print("WELCOME TO THE FICTIONAL NAME QUIZ !!")

#Use if statements to check their answers (a condition, therefore if statement)

#Question 1 of set 2:
set2_choice1 = str(input("Question 1: Which singer do you like better? Conan Gray, Shawn Mendes, Harry Styles, or Zayn Malik:   ")) 
set2_points = 0
while set2_choice1 != "":
       
    if set2_choice1 == "Conan gray" or set2_choice1 == "conan gray" or set2_choice1 == "Conan Gray":
        set2_points += 1
        break

    elif set2_choice1 == "Harry Styles" or set2_choice1 == "harry styles" or set2_choice1 == "Harry styles":
        set2_points += 2
        break
        
    elif set2_choice1 == "zayn malik" or set2_choice1 == "Zayn Malik" or set2_choice1 == "Zayn malik":
        set2_points += 3
        break

    elif set2_choice1 == "shawn mendes" or set2_choice1 == "Shawn Mendes" or set2_choice1 == "Shawn mendes":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice1 = str(input("Question 1: Which singer do you like better? Conan Gray, Shawn Mendes, Harry Styles, or Zayn Malik:   "))      

#Use f string to print their points and direct them to the next question
print(f"Your Points ={set2_points},"" You can go to the next question!")



#ideas ; which celebrity, ur fav sport, harry potter stuff, friends, what language wanna learn, fav food, disnay villains

#Question 2 of set 2:
set2_choice2 = str(input("Question 2: Which language would you like to learn? Italian, Spanish, German, or French:   ")) 
set2_points = 0
while set2_choice2 != "":
       
    if set2_choice2 == "French" or set2_choice2 == "french":
        set2_points += 1
        break

    elif set2_choice2 == "German" or set2_choice2 == "german":
        set2_points += 2
        break
        
    elif set2_choice2 == "spanish" or set2_choice2 == "Spanish":
        set2_points += 3
        break

    elif set2_choice2 == "Italian" or set2_choice2 == "italian":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice2 = str(input("Question 2: Which language would you like to learn? Italian, Spanish, German, or French:   "))      

print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 3 of set 2:
set2_choice3 = str(input("Question 3: Which one do you like better? East, West, North or South:   ")) 
set2_points = 0
while set2_choice3 != "":
       
    if set2_choice3 == "north" or set2_choice3 == "North":
        set2_points += 1
        break

    elif set2_choice3 == "west" or set2_choice3 == "West":
        set2_points += 2
        break
        
    elif set2_choice3 == "East" or set2_choice3 == "east":
        set2_points += 3
        break

    elif set2_choice3 == "South" or set2_choice3 == "south":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice3 = str(input("Question 3: Which one do you like better? East, West, North or South:   "))  

print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 4 of set 2:
set2_choice4 = str(input("Question 4: Which Australian city is better? Melbourne, Sydney, Brisbane, or Perth:   ")) 
set2_points = 0
while set2_choice4 != "":
       
    if set2_choice4 == "brisbane" or set2_choice4 == "Brisbane":
        set2_points += 1
        break

    elif set2_choice4 == "sydney" or set2_choice4 == "Sydney":
        set2_points += 2
        break
        
    elif set2_choice4 == "perth" or set2_choice4 == "Perth":
        set2_points += 3
        break

    elif set2_choice4 == "melbourne" or set2_choice4 == "Melbourne":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice4 = str(input("Question 4: Which Australian city is better? Melbourne, Sydney, Brisbane, or Perth:   ")) 

print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 5 of set 2:
set2_choice5 = str(input("Question 5: Which kind of park? Amusement Park, Water Park, Nature Park, or Lake Park:   ")) 
set2_points = 0
while set2_choice5 != "":
       
    if set2_choice5 == "nature park" or set2_choice5 == "Nature park" or set2_choice5 == "Nature Park":
        set2_points += 1
        break

    elif set2_choice5 == "Amusement Park" or set2_choice5 == "amusement park" or set2_choice5 == "Amusement park":
        set2_points += 2
        break
        
    elif set2_choice5 == "Lake Park" or set2_choice5 == "lake park" or set2_choice5 == "Lake park":
        set2_points += 3
        break

    elif set2_choice5 == "water park" or set2_choice5 == "Water Park" or set2_choice5 == "Water park":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice5 = str(input("Question 5: Which kind of park? Amusement Park, Water Park, Nature Park, or Lake Park:   ")) 
print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 6 of set 2:
set2_choice6 = str(input("Question 6: Which genre? Comedy, Romance, Thriller, or Horror:   ")) 
set3_points = 0
while set2_choice6 != "":
       
    if set2_choice6 == "horror" or set2_choice6 == "Horror":
        set2_points += 1
        break

    elif set2_choice6 == "thriller" or set2_choice6 == "Thriller":
        set2_points += 2
        break
        
    elif set2_choice6 == "romance" or set2_choice6 == "Romance":
        set2_points += 3
        break

    elif set2_choice6 == "comedy" or set2_choice6 == "Comedy":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice6 = str(input("Question 7: Which genre? Comedy, Romance, Thriller, or Horror:   ")) 
print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 7 of set 2:
set2_choice7 = str(input("Question 7: Books, Movies, Both, or None?:   ")) 
set3_points = 0
while set2_choice7 != "":
       
    if set2_choice7 == "movies" or set2_choice7 == "Movies":
        set2_points += 1
        break

    elif set2_choice7 == "none" or set2_choice7 == "None":
        set2_points += 2
        break
        
    elif set2_choice7 == "both" or set2_choice7 == "Both":
        set2_points += 3
        break

    elif set2_choice7 == "books" or set2_choice7 == "Books":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice7 = str(input("Question 7: Books, Movies, Both, or None?:   ")) 
print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 8 of set 2:
set2_choice8 = str(input("Question 8:How many languages can you speak? 1,2,3, or more than 3?   ")) 
set3_points = 0
while set2_choice8 != "":
       
    if set2_choice8 == "1" or set2_choice8 == "one" or set2_choice8 == "One":
        set2_points += 1
        break

    elif set2_choice8 == "2" or set2_choice8 == "two" or set2_choice8 == "Two":
        set2_points += 2
        break
        
    elif set2_choice8 == "3" or set2_choice8 == "three" or set2_choice8 == "Three":
        set2_points += 3
        break

    elif set2_choice8 == "more than 3" or set2_choice8 == "More than 3" or set2_choice8 == "more than three" or set2_choice8 == "More tha three":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice7 = str(input("Question 6: Books, Movies, Both, or None?:   ")) 
print(f"Your Points ={set2_points},"" You can go to the next question!")


#Question 9 of set 2:
set2_choice9 = str(input("Question 9: Which one of these common English names would you give to your child?: Peter, David, Michael, or Oliver:  ")) 
set3_points = 0
while set2_choice9 != "":
       
    if set2_choice9 == "david" or set2_choice9 == "David":
        set2_points += 1
        break

    elif set2_choice9 == "michael" or set2_choice9 == "Michael":
        set2_points += 2
        break
        
    elif set2_choice9 == "oliver" or set2_choice9 == "Oliver":
        set2_points += 3
        break

    elif set2_choice9 == "peter" or set2_choice9 == "Peter":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice9 = str(input("Question 9: Which one of these common English names would you give to your child?: Peter, David, Michael, or Oliver:  ")) 
print(f"Your Points ={set2_points},"" You can go to the next question!")

#Question 10 of set 2:
set2_choice10 = str(input("Question 10: Which Disney Princess? Cindrella, Aurora, Snow White, or Elsa:  ")) 
set3_points = 0
while set2_choice10 != "":
       
    if set2_choice10 == "snow white" or set2_choice10 == "Snow White" or set2_choice10 =="Snow white":
        set2_points += 1
        break

    elif set2_choice10.lower() == "aurora" or set2_choice10 == "Aurora":
        set2_points += 2
        break
        
    elif set2_choice10 == "cindrella" or set2_choice10 == "Cindrella":
        set2_points += 3
        break

    elif set2_choice10 == "Elsa" or set2_choice10 == "elsa":
        set2_points += 4
        break
        
    else:
        print("Sorry, choose one of the options!!")
        set2_choice10 = str(input("Question 10: Which Disney Princess? Cindrella, Aurora, Snow White, or Elsa:  ")) 

fictional_names=["Oompa Loompa","Upsy Daisy", "Makka Pakka", "Hocus Pocus", "Josh Josh", "Tinky Winky"]

if set2_points <= 13:
    your_fictional_name = fictional_names[0]
elif set2_points > 13 and set2_points <= 18:
    your_fictional_name = fictional_names[1]
elif set2_points > 18 and set2_points <= 23:
    your_fictional_name = fictional_names[2]
elif set2_points > 23 and set2_points <= 28:
    your_fictional_name = fictional_names[3]
elif set2_points > 28 and set2_points <= 33:
    your_fictional_name = fictional_names[4]
elif set2_points > 33 and set2_points <= 40:
    your_fictional_name = fictional_names[5]

print("")
print(f"Your fictional name is {your_fictional_name}!!")
print("")    
       
#ideas ; which celebrity, ur fav sport, harry potter stuff, friends, what language wanna learn, fav food, disnay villains  

#Using a dictionary for set 3 of questions:

#Use a dictionary to have all the questions in one place

points = 0
Questions = {
    "Q1" : "Which Disney villain? Scar, Jafar, Maleficent, or The Evil Queen",
    "Q2" : "Favourite subject? Maths, Science, English, or Coding?",
    "Q3" : "Which Harry Potter character? Harry, Hermione, Ron, or Draco?",
    "Q4" : "What time of the day? Morning, Evening, Afternoon, or Night?",
    "Q5" : "How many meals a day should humans eat? 1,2,3, or more?"
}

#Use a dictionary to store all the answers- also use lists within the dictionary so it is easier to check the answers and give points later

Answers = {
    "A1" : ["scar", "maleficent", "jafar", "the evil queen"],
    "A2" : ["maths", "science", "english", "coding"],
    "A3" : ["harry", "hermione", "ron", "draco"],
    "A4" : ["morning", "evening", "afternoon", "night"],
    "A5" : ["1","2", "3", "more"]
}

#Start printing the questions and use if statements to check answers and give points


#Q1:

#Using if statements, check their answers for each question and give them points
print(Questions["Q1"])

set3_player_choice1 = str(input("Your Answer:  ")) 
if set3_player_choice1.lower() == Answers["A1"][0]:
    points += 1
elif set3_player_choice1.lower() == Answers["A1"][1]:
    points += 2
elif set3_player_choice1.lower() == Answers["A1"][2]:
    points += 3
elif set3_player_choice1.lower() == Answers["A1"][3]:
    points += 4
else:
    print("Sorry, choose one of the options!!")
    print(Questions["Q1"])
    
print(f"Your Points ={points},"" You can go to the next question!")


#Q2:

print(Questions["Q2"])
set3_player_choice2 = str(input("Your Answer:  ")) 
if set3_player_choice2.lower() == Answers["A2"][0]:
    points += 4
elif set3_player_choice2.lower() == Answers["A2"][1]:
    points += 3
elif set3_player_choice2.lower() == Answers["A2"][2]:
    points += 2
elif set3_player_choice2.lower() == Answers["A2"][3]:
    points += 1
else:
    print("Sorry, choose one of the options!!")
    print(Questions["Q2"])
    
print(f"Your Points ={points},"" You can go to the next question!")


#Q3:

print(Questions["Q3"])
set3_player_choice3 = str(input("Your Answer:  ")) 
if set3_player_choice3.lower() == Answers["A3"][0]:
    points += 4
elif set3_player_choice3.lower() == Answers["A3"][1]:
    points += 1
elif set3_player_choice3.lower() == Answers["A3"][2]:
    points += 2
elif set3_player_choice3.lower() == Answers["A3"][3]:
    points += 3
else:
    print("Sorry, choose one of the options!!")
    print(Questions["Q3"])
    
print(f"Your Points ={points},"" You can go to the next question!")



#Q4:

print(Questions["Q4"])
set3_player_choice4 = str(input("Your Answer:  ")) 
if set3_player_choice4.lower() == Answers["A4"][0]:
    points += 3
elif set3_player_choice4.lower() == Answers["A4"][1]:
    points += 4
elif set3_player_choice4.lower() == Answers["A4"][2]:
    points += 1
elif set3_player_choice4.lower() == Answers["A4"][3]:
    points += 2
else:
    print("Sorry, choose one of the options!!")
    print(Questions["Q4"])
    
print(f"Your Points ={points},"" You can go to the next question!")

#Q5:

print(Questions["Q5"])
set3_player_choice5 = str(input("Your Answer:  ")) 
if set3_player_choice5.lower() == Answers["A5"][0]:
    points += 1
elif set3_player_choice5.lower() == Answers["A5"][1]:
    points += 2
elif set3_player_choice5.lower() == Answers["A5"][2]:
    points += 3
elif set3_player_choice5.lower() == Answers["A5"][3]:
    points += 4
else:
    print("Sorry, choose one of the options!!")
    print(Questions["Q5"])

#There are 13 verbs in the verbs list to make the game less repetetive, as only 1 point difference can change the verb
verbs=["eats","loves", "kills", "tells a secret to", "steals", "receives","buys","destroys","plays with","makes fun of", "examines","explodes", "haunts"]

#Using if statements, check their number of points and allocate a verb from the dictionary (and lists) to them. Define this verb as a variable to be used later.
if points <= 4:
    your_verb = verbs[0]
elif points > 4 and points <= 6:
    your_verb = verbs[1]
elif points > 6 and points <= 8:
    your_verb = verbs[2]
elif points == 9:
    your_verb = verbs[3]
elif points == 10:
    your_verb = verbs[4]
elif points == 11:
    your_verb = verbs[5]
elif points == 12:
    your_verb = verbs[6]
elif points == 13:
    your_verb = verbs[7]
elif points == 14:
    your_verb = verbs[8]
elif points == 15:
    your_verb = verbs[9]
elif points == 16:
    your_verb = verbs[10]
elif points > 16 and points <= 18:
    your_verb = verbs[11]
elif points > 18 and points <= 20:
    your_verb = verbs[12]
    
#Now, print the sentence by using an f strong that puts these variables (from sets 1,2, and 3) together
#Use an f string to put all three variables together in a sentence and give the final result
print("")   
print(f"Your sentence is: {your_fictional_name} {your_verb} {your_mushroom_name}")
print("")
print("Hope you enjoyed this quiz! Now play again :D ")



