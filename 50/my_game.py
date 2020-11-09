#Author: James Liu
#Description: text-based coding adventure game
#date: 06/11/2020
#phase: final 

name = input("what's your name?\n") #asks the player for their name, define their input as a variable 
age = int(input("how old are you?\n")) #asks the age of the player, converting answer to a numerical value 
if age < 8:  #compares the player's input with 8
    print("this game may be confronting before players under the age of 8, sorry you can't yet play this game ") #if age is less than 8 years, then display this text and exit the code
    exit() #shuts the code 
else:
    print(f"great {name}! you are old enough to play the game") #using f strings to display player's name in this line of text 

answer = input(f"dear {name}: the hidden treasure of kylum is rumoured to be hidden in the land of mulyk; do you think you have what it takes to find the hidden treasure?(yes/no) ")#background information and asks if the person wants to play the game.
if answer.lower() == "yes":
    answer = input("your courage is respected! you are now teleported to the front gate of the kylum castle, would you like to enter?(yes/no) ")#asks whether the player wants to enter or not
    
    if answer == "yes":
        answer = input("you entered the castle, would you like to go left or right?(left/right) ")#if answer is yes, the player is then prompted with this question, this is repeated throughout the game.

        if answer == "left":
            answer = input("you decided to walk left and witnessed a man abusing a cat, would you ignore him or confront him?(ignore/confront) ")
            if answer == "ignore":
                answer = input("you ignored the man, would you stay in the castle or stay around for a little longer?(stay/leave) ")
                if answer == "stay":
                    print("the ghost of the abused cat lingered around the castle and haunted you,game over! ")#when the player reaches an ending path, they are given statements whether they won or not

                elif answer == "leave":
                    print("you chose to leave the castle, however accidentally slipped and fell off the cliff,game over! ")

            elif answer == "confront":
                print("the man charged towards you with a knife,game over! ")
                    

        elif answer == "right": #if and elif statements repeated 
            answer = input("you decided to walk right and witnessed a dog chasing angrily behind a child, would you help the child or ignore the situation? (help/ignore) ")
            if answer == "help":
                answer = input("you decided to help the kid,the kid tells you that the grand treasure is not in the castle, would you leave or keep exploring the castle? (stay/leave) ")
                if answer == "stay":
                    answer = input("you decided to stay in the castle, would you go to the first floor, or keep exploring the ground floor? (first/ground) ")
                    if answer == "first":
                        print(f"you decided to explore the first floor, and found the hidden treasure! congratulations {name}, you win! ")#using F strings to import different texts in this line

                    elif answer == "ground":
                        print("you kept exploring on the ground floor and was attacked by the ghost of the child from before, game over! ")

                elif answer == "leave":
                    answer = input("you decided to leave the castle, would you go left towards the mountains or right towards the forests? (left/right) ")
                    if answer == "left":
                        print("you decided to walk left towards the mountains, and is attacked by a pack of wolves, game over! ")

                    elif answer == "right":
                        answer = input("you decided to walk right towards the forests, you see a fish dying on the ground, would you eat it or would you save it? (eat/save) ")
                        if answer == "eat":
                            print("the fish was poisonous! game over! ")

                        elif answer == "save":
                            print(f"you saved the fish, and it spit out a diamond! you found the treasure, congratulations {name}! ")
                    
                    
            elif answer == "ignore":
                answer = input("you decided to ignore the kid and kept walking until you reached a room gleaming with golden light, would you like to explore the room? (yes/no) ")
                if answer == "yes":
                    answer = input("you entered the room and saw a treasure box, would you open it? (yes/no) ")
                    if answer == "yes":
                        print("you opened the treasure box and it contained a blackhole, game over! ")

                    elif answer == "no":
                        answer = input("you decided to not open the treasure box and saw a diamond like gem in the corner, would you pick it up? (yes/no) ")
                        if answer == "yes":
                            print(f"you obtained the real treasure, congratulations {name}, you win! ")#using F strings to import different texts in this line

                        elif answer == "no":
                            print("you hesitated and did not take the gem, and was attacked by the ghost of the child you ignored earlier,game over! ")

                elif answer == "no":
                    print("you decided to stay still, and is attacked by the ghost of the child you ignored earlier, game over! ")
                


    elif answer == "no":
        answer = input("you waited outside of the castle,would you like to explore the surrounding?(yes/no) ")#if answer is no, the player is then prompted with this question
        if answer == "yes":
            answer = input("would you go the forest or the mountain?(forest/mountain) ")
            if answer == "forest":
                answer = input("you wondered into the forests and see a dying fish lying on the grass, would you save it? (save/ignore) ")
                if answer == "save":
                    answer = input("you decided to save the fish, would you choose to return it to the lake or the sea?(lake/sea) ")
                    if answer == "lake":
                        print("you returned the fish into the lake and it swam away safely, however, you are now lost in the forest! game over! ")

                    elif answer == "sea":
                        answer = input("you decided to return the fish into the sea, would you give the fish a final gentle pat or a violent blow?(pat/blow) ")
                        if answer == "pat":
                            print("achievement (RSPCA) unlocked! you gave the fish a gentle pat and released it into the ocean, you didn't find the treasure but you saved a fish! ")
                        elif answer == "blow":
                            print(f"you violently hit the fish and it spit out a diamond! the treasure you were looking for! congratulations {name},you win! ")#using F strings to import different texts in this line


                elif answer == "ignore":
                    answer = input("you decided to ignore the fish, would you now take the left path or the right path?(left/right) ")
                    if answer == "left":
                        print("you wondered aimlessly left and got lost in the forest, game over! ")

                    elif answer == "right":
                        answer = input("you decided to walk right, you see a dying bird, would you save it or ignore it? (save/ignore) ")
                        if answer == "save":
                            print("you saved the bird, however the fish you didn't save before turned into a monster and was hungry for the bird, unfortunately it also swallowed you in the process, game over!")

                        elif answer =="ignore":
                            print("achievement (savage) unlocked! you failed to find the hidden treasure however demonstrated the true trait of a savage! congratulations? ")
                
                    

            elif answer == "mountain":
                answer = input("you chose to explore the mountains, and see a lone wolf injured, would you save it? (save/ignore) ")
                if answer == "save":
                    answer = input("you saved the wolf and saw a group of people with treasure like possession, would you rob them or leave them? (rob/leave) ")
                    if answer == "rob":
                        print(f"you sucessfully robbed the group of people with your new found companion, the wolf, congratulations {name},you win! ") #using F strings to import different texts in this line

                    elif answer == "leave":
                        print("you decided to leave the group of people alone, however, they were interested in you and your wolf and shot you from behind! game over! ")
                    

                elif answer == "ignore":
                    print("you were accidentally shot by the hunter while turning back (he's clearly very good at aiming), game over! ")
                    

        elif answer == "no":
            print("you were frozen to death outside of the castle since you stood still, game over! ")
            

elif answer == "no":
    print(f"oh well, that's too bad, come back anytime when you feel ready {name} ")#if the person responds with no, then this statement would appear. using F strings to import different texts in this line
