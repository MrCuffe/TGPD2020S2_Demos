#Author = Dimithri Gunatillake
#date = 15/10/2020
#game_type = text based game
#game_name = Spider Urea Quest

import random
import time
import sys

#these are used to create while loops (variables)
i = 0
intro = 0
part1 = 0

# variables
inventory = ["Empty water bottle", "soda can", "bread knife", "lighter", "long rope"]
health = "90%"


#defining functions



#exits the game
def exit_the_game():
    pass

#logo of the game
def display_game_logo(): 
    print("      ###################################### ")
    print("          #                            #")
    print("          #                            #")
    print("          #     SPIDER UREA QUEST      #")
    print("          #                            #")
    print("          #                            #")
    print("          #                            #")
    print("      ###################################### ")
    
#the introduction to the game
def display_intro(): 
    print("           (       ")
    print("            )")
    print("           (")
    print('     /\  .-"""-.  /\'')
    print("    //\\/  ,,,  \//\\")
    print("    |/\| ,;;;;;, |/\|")
    print('    //\\\;-"""-;///\\')
    print("   //  \/   .   \/  \\")
    print("  (| ,-_| \ | / |_-, |)")
    print("    //`__\.-.-./__`\\")
    print("   // /.-(() ())-.\ \\")
    print("  (\ |)   '---'   (| /)")
    print("   ` (|           |) `")
    print("    \)           (/")

    print()
    print()
    print("A  gigantic spider called Spidereru comes to the city of Maydome in search of humans to eat")
    time.sleep(1) #delays the code by 1 sec
    print()
    print(f"It enters a park where {player_name} is having a picnic.")
    time.sleep(1)
    print()
    print("You see the spider crawling right towards you..with saliva dripping down its large mouth..")
    time.sleep(1)
    print()
    print("You try to move but you can't. Your legs feel like its stuck to the ground..")
    time.sleep(1)
    print()
    print("Your heart was thumping rapdily against your chest. You could hear people's screams all around you, but you stll could not move.")
    time.sleep(1)
    print()
    print("You felt sharp teeth pierce your skin as the spider grabbed you by its mouth and ran towards the forest, that nobody dared to enter.")
    time.sleep(1)
    print()
    print("Tears fell down you cheeks like a stream as you realised what was going to happen")
    time.sleep(1)
    print()
    #printing each character one by one to show that the player is speaking
    player_quote_1 = '"There is no way Im going to die like this... Im too young.. theres just no way.. I have to survive"'
    for character in player_quote_1:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    time.sleep(1)
    print("The slight little hope for survival that you gathered at that time, led to one of the most bravest actions you have ever taken in your whole life")
    time.sleep(1)
    print()
    print("using your fingers your STABBED the spider's eye as hard as you can.....")
    time.sleep(1)
    print()
    print("The spider screamed in pain and as it opened its mouth, you felt to the ground")
    time.sleep(1)
    print()
    print("You did not look back, you did not think twice. You ran as fast as you can through the forest...")
    time.sleep(1)

    print()
    print()
    print()
    print("Now YOU have to escape this forest without getting caught by the spider.")
    time.sleep(1)
    print()
    print("Keep in mind that the spider is NOT the only thing that wants to devour you - there's alot of poisonous snakes, lions and bears that are THIRSTY for you blood")
    time.sleep(1)
    print()




#game instructions for the user
def how_to_play(): 

    #Defining variables:
    health = "90% - The spider attack reduced your health by 10%"
    i=0

    #A while loop that keeps on asking the player the same question until the player answers correctly
    while i< 1:
        print("2) The choices you can make will be provided")
        time.sleep(1) 
        print()
        print("3) Your choices determine your fate!")
        time.sleep(1)
        print()
        print("4) You can see your health status by typing [health]. If health reaches 0, you lose the game :(")
        time.sleep(1)
        print()
        print("5) You need to eat food to regain your health -  you can do this by eating fruits or by hunting animals. ")
        time.sleep(1)
        print()
        print("6) ~~ HuNt At YoUr OwN RiSk~~ --> You can kill animals by typing [attack] when an animal is nearby. You will be notifed when an animal is nearby")
        time.sleep(1)
        print()
        
        print("\nTIPS\n")
        print("-Leave the forest as quick as you can. The longer you stay,the harder it will get because your scent will linger in the forest,making it easier for the spider and other wild animals to find you")
        print()
        print("-Type [inventory] to see the amount of food and weapons you own")
        print()
        print("MAKE SURE TO CHECK YOUR HEALTH  BY TYPING [health]")
        print()

        ready_or_not = (input("\nARE YOU READY TO PLAY NOW? [yes] or [no]: \n").lower()) #input validation
        #makes sure that the player is ready
        if ready_or_not == "yes":
            i+= 1

        elif ready_or_not == "health":
            print(health)
            
        elif ready_or_not == "no":
            print("\nOKAYYYY, read the instructions again and respond when ready\n")
        print("-------------------------------------------------------------------")
        
def display_berry_scene():
    #defining variables
    a = 0
    health = "65%"
    inventory = ["spear", "lighter"]

    #code
    print("As you were walking you saw a tree filled with fruits that looked like blue berries.")
    time.sleep(2)
    print("Your tummy grumbled and saliva dripped down your mouth...")
    time.sleep(1)
    print()
    print("The berries glistened brightly in the sun.. they were un touched.. there was not a single scratch on one.")
    time.sleep(1)
    print()
    print("Not a single bird has touched it")
    print()
    time.sleep(1)
    print("You picked one from the tree and smelled it. It gave of a really pleasant smell")
    print()
    time.sleep(2)
    player_quote_16 = '"Should I pick some and eat it..?" '
    #prints the characters in player quote one by one
    for character in player_quote_16:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    time.sleep(1)

    print("OPTION 1: Eat the berries.")
    time.sleep(1)
    print("OPTION 2: Try to find something better.")
    print()
    time.sleep(1)
    
    while a <1:
        choice_player = input("Enter your choice [1/2]: ")
        #if the players types '1' this piece of code will run
        if choice_player == "1":
            print("You decide to eat the berries")
            time.sleep(1)
            print("You pick a few and shove it in your mouth")
            time.sleep(1)
            print("They were absolutely delicious.. They tasted like blue berries, but much more sweeter")
            time.sleep(2)
            print("Suddenly...")
            time.sleep(1)
            print("You begin to feel a sharp pain in your throat and stomach.. almost like something was eating your from the inside")
            time.sleep(2)
            print("Blood was pouring out of your mouth..")
            time.sleep(1)
            print()
            print("You died aslow painful death..")
            time.sleep(1)
            print(" If birds don't eat it, most likely it's poisonous..")
            time.sleep(1)
            print()
            print("_______________________ GAME OVER_____________________________")
            a+=1 #stops the loop
            
            

        elif choice_player == "2":
            #if the players types '2' this piece of code will run
            player_quote_18 = '"No birds have touched it. Not a single insect comes near it"'
            player_quote_19 = ' "There has to be something wrong with it. There just has to be" '
            #prints the characters in player quote one by one
            for character in player_quote_18:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            #prints the characters in player quote one by one
            for character in player_quote_19:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            print("You continued walking so you can find a place to cook the bear meat")
            time.sleep(1)
            print()
            print("You could no longer run, you are too hungry")
            time.sleep(1)
            print()
            print("You kept on walking, when suddenly you saw a lake in the distance.")
            time.sleep(1)
            print()
            print("Your heart began to thump rapdily against your chest.")
            time.sleep(1)
            print()
            print("You walked rapidly towards it")

            player_quote_20 = ' "Finally! Finally some water and a place to eat" '
            #prints the characters in player quote one by one
            for character in player_quote_20:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            display_lake_scene_1()  
            a+=1

        elif choice_player == 'health':
            #prints the player's current health if they input [health]
            print(health)
        elif choice_player == 'inventory':
            #prints the player's current health if they type [inventory]
            print(inventory)
               
    
    

def display_bear_attack():
    # define variables
    health = "80"
    inventory =  ["spear", "lighter", "long rope"]

    #code
    print()
    print("*************** Animal Nearby***************")
    time.sleep(1)
    print()
    print("*************** Type [attack] to attack the bear************")
    time.sleep(1)
    print()
    print()
    print("Suddenly, you hear the large bushes behind you shake... There was a growling sound..")
    time.sleep(1)
    print()
    print(' "Your heart began to beat so fast, that it felt like it was about to burst out of your chest"')
    time.sleep(1)
    print()
    player_quote_5 = ' "This cannot be happening.. theres no way the spider found me... "'
    #prints characters in player quote one by one
    for character in player_quote_5:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    print("You slowly turn your head...")
    time.sleep(1)
    print()
    print("A large bear with saliva dripping from it's mouth emerged from the bush...")
    time.sleep(1)
    print()
    print("Your heart sank.. It growled loudly as it stared at you with viciosu eyes") #CHECK
    time.sleep(1)
    print()
    player_quote_222 = "I have to do something.. or else..or else it will kill me... I need to find a way"
    print()
    #prints characters in player quote one by one
    for character in player_quote_222:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()

    print("OPTION 1: Get down on the ground and play dead")
    time.sleep(1)
    print("OPTION 2: Turn around and run as fast as you can")
    time.sleep(1)
    print("OPTION 3: Avoid eye contact and slowly move back")
    time.sleep(1)

# if player decides to play dead during the bear attack this piece of code will run
def play_dead():
    print("You laid down on the floor, closed your eyes and acted like you were dead")
    time.sleep(1)
    print()
    print("Suddenly, you felt the bears breath and saliva on your head")
    time.sleep(1)
    print()
    print("It grabbed you by your neck and growled")
    time.sleep(1)
    print()
    print()
    print("You were eaten by the bear.... you died a slow, painful death... ")
    health = "Health: 0% "
    print()
    print("_______________________ GAME OVER_____________________________")

# if player decides to outrun the bear during the bear attack this piece of code will run
def outrun_bear():
    print("You turn around and begin to run as fast as you can with the little energy you have left")
    time.sleep(1)
    print()
    print("The bear runs after you and grabs you")
    time.sleep(1)
    print()
    player_quote_9 = "NOOOOOOOOOOOOOOOO, pls noo"
    for character in player_quote_9:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    print("Did you just try to outrun a bear... I-")
    time.sleep(1)
    print()
    print("You were eaten by the bear, you died a slow painful death...")
    print()
    print("_______________________ GAME OVER_____________________________")




def stay_silent_or_not():
    #defining variables
    y = 0
    inventory = ['spear', 'bear meat', 'lighter']
    health = "75%"
    #loop that continues to ask the player a queston until they respond correctly
    while y < 1: 
        user_choice = input("Enter the option you choose [1/2]: ")
        #if player inputs '1' this will run
        if user_choice == '1':
            print("You decided to just stay silent and not move like before..")
            print("After a few minutes it came up to you and when you reaised your mistake, it was too late..")
            print()
            print("It grabbed you by your neck and snapped it")
            print()
            print("Didn't you remember that your shirt was covered in bear blood and you were holding bear meat??")
            print("The spider smelled the blood on you and found you. :(")
            print()
            print("_______________________ GAME OVER_____________________________")
            y+=1

        elif user_choice == '2':
            #if player inputs '2' this will run
            print("You took a deep breath and took your shirt off as quick as you can and wrapped it around the bear meat")
            print("The spider twisted its head and stared right at you at the sound of you taking your shirt off")
            print("It growled loudly and started running towards you")
            print(" You threw the bear meat wrapped in the shirt as far as you can")
            print("The spider quickly changed direction and started running towards the shirt")
            print("It growled loudly and ran down the direction I threw it, thinking I had run away")
            print(" When it dissapeared out of your view you dropped down on the ground with relief")
            player_quote_15 = '"Im alive..Im alive." '
            #prints characters in player_quote one by one in one line
            for character in player_quote_15:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            print("You quickly grabbed the shirt and the bear meat and started quickly walking, avoiding making sound as much as you could")
            health = "65%"
            print()
            print("WARNING : HEALTH IS AT 65%")
            print()
            display_berry_scene()
            y+=1

        elif user_choice == 'inventory':
            print(inventory)
            print()
        elif user_choice == 'health':
            print(health)
            print()

            
def move_back():
    print("You avoided eye contact and began to slowly move back..")
    print()
    print("The bear began to calm down a little.")
    print("It started to slowly approach you...")
    print("Your closed your eyes and took deep breaths")
    print()
    print("When suddenly, you heard a loud growl")
    print("When you opened your eyes, Spidereru laid on top of the bear and was killing it")
    print("The bears blood sprayed on you..")
    print()
    print("Was the spider mad that the bear was eating it's pray??")
    print("Suddenly, it stopped...")
    print("It was looking around.. almost like it didn't see you.")
    

def display_section_1():
    #defining variables
    y = 0
    health = "80%"
    inventory = ["bread knife", "lighter", "spear"]
    #code
    print("Eventhough you were right infront of it, it kept looking around searching for you..")
    print()
    time.sleep(2)
    player_quote_12 = ' "I need to think quickly, what should I do..?" '
    #prints characters in player_quote one by one in one line
    print()
    for character in player_quote_12:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    time.sleep(1)

    print("OPTION 1: Slowly move back without making any sound and run as fast as you can")
    print("OPTION 2: Stay silent and not move an inch")
    print()
    #loop
    while y < 1:
        player_choice = input("Enter an option [1/2]: ")
        if player_choice == '1':
            #if player inputs '1' this will run
            player_quote_13 = ' "Is this spider blind..? How does it not notice me.. omg. When I stabbed him in the eye, I might have made him blind" '
            for character in player_quote_13:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            print("You moved back slowly and began to run")
            print()
            time.sleep(1)
            health = 'Health: 0%'
            print("When you realised your mistake, it was too late")
            time.sleep(1)
            print()
            print("You were running on dry leaves and grass")
            time.sleep(1)
            print("The spider caught you and snapped your neck in an instance.")
            time.sleep(1)
            print("Although, the spider can't see, it can still hear and smell. Better luck next time..")
            time.sleep(1)
            print()
            print("_______________________ GAME OVER _____________________________")
            y+=1

            
        elif player_choice == '2':
            #if player inputs '2' this will run
            player_quote_13 = ' "Is this spider blind..? How does it not notice me.. omg. When I stabbed him in the eye, I might have made him blind" '
            for character in player_quote_13:
                #prints characters in player_quote one by one in one line
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            print("You decided to stay silent and not move an inch")
            time.sleep(1)
            print("Your heart began to thump rapidly against your chest..")
            time.sleep(1)
            print("It jumped up from the bears body covered in blood and began to sniff the ground..")
            time.sleep(1)
            print(" It was.. it was smelling the blood and following the trail")
            time.sleep(1)
            print()

            player_quote_14 = ' "What should I do?" '
            for character in player_quote_14:
                #prints characters in player_quote one by one in one line
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()

            print("OPTION 1: Stay silent and not move an inch")
            print("OPTION 2: Take off your shirt, wrap it around the bear meat and throw it to the side")
            print()
            stay_silent_or_not()
            y+=1 

        elif player_choice == "health":
            print(health)
            print()
        elif player_choice == "inventory":
            print(inventory)
            print()
            
        #input validation
        else:
            print("invalid")

            ############
    
#player first choice
def display_first_choice():
    #defining variables
    inventory = ["Empty water bottle", "soda can", "bread knife", "lighter", "long rope"]
    health = "90%"

#image of the forest. Credit : https://www.asciiart.eu/    
    print("")
    print("      @@@@@@@     ,@@@@@@@,  @@@@@@@     ")
    print(" ,   @@@@@@/@@,  .oo8888o.  .oo8888o8.   ")
    print("  ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o")
    print(" ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88")
    print("  %&&%&%&/%&&%@@\@@/ /@@@88888\88888")
    print("    %&&%/ %&%%&&@@\ V /@@' `88\8 `/88")
    print("     `&%\ ` /%&'   |.|        \ '|8'")
    print("         |o|       | |         | |")
    print("         |.|       | |         | |")
    print("      \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_")   

    print("\nThere were large trees, bushes and flowers all around you.\n")
    time.sleep(1)
    print("There was a sharp, frosty chill in the air.")
    time.sleep(1)
    print("The dark shadows of the tall trees evoked a sense of grief and fear within you..")
    time.sleep(1)
    print("It was a very very unwelcoming feeling... and Spidereru is coming right behind you.")
    time.sleep(1)
    print("Your body was begining to ache and you could see blood dripping down your leg. You are very hungry and tired ")
    time.sleep(1)

    #prints character one by one
    player_quote_2 = '"What should I do…? "'
    for character in player_quote_2:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    #player options
    print(" OPTION (1) = Ignore the pain and continue walking")
    time.sleep(1)
    print(" OPTION (2) = Hide in a bush")
    time.sleep(1)
    time.sleep(1)
##
##
#OPTION 1 -> PLAYER FATE
def option_1_part_1():
   
    #Defining variables
    health = " Health = 85 %"
    inventory = ["Empty water bottle", "soda can", "bread knife", "lighter", "long rope"] #List 

    print("You decide to ignore the pain for a little bit longer and try to find a way to get out of the forest")
    time.sleep(1)
    print()
    print("You could hear the spider in a distance. It was screaming and growling in anger. It sent shivers down your spine.")
    time.sleep(1)
    print()
    print(" The forest was gradually beginning to fill with darkness as the sun went down.")
    time.sleep(1)
    print()
    #updating the health status
    health = " Health = 80%" 
    print(" *******Your health has deteriorated as you have not rested or eaten for a while. Food and water can restore your health*******")
    time.sleep(1)
    print()
    print("******** Type [health] at anytime to see health status***********")
    time.sleep(1)
    print()
    player_quote_3 = '"I have to keep ongoing, I cannot stay here any longer..."'
    #prints character one by one
    for character in player_quote_3:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    print("As you were walking cautiously through the gloomy forest, you saw a pile of wood")
    print()
    player_quote_4 = '"This could be useful for me to create a weapeon.. I should collect this.."'
    #prints character one by one
    for character in player_quote_4:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()

def display_option_2():
    #Defining variables
    i = 0
    inventory = ["Empty water bottle", "soda can", "bread knife", "lighter", "long rope"]
    health =  90

    #code
    print("You decided to hide in a bush")
    time.sleep(1)
    print("You breathed heavily and tried to get your head around on what just happened")
    time.sleep(1)
    print("You opened your bag and there was a bread knife from the picnic you were having, a lighter and a long rope")
    time.sleep(2)
    
    print("Suddenly, you felt something crawling up your leg...")
    time.sleep(1)
    print("You looked down and it was one of the biggest centipedes you have ever seen in your whole life")
    print()
    print("You felt a sharp pain, it bit you..")
    print("After some painful hours, you died...")
    print("_______________________ GAME OVER_____________________________")
    

def display_spear_story():
    #defining variables
    inventory = ["wood x 3", "bread knife", "lighter", "long rope"] #List 
    health = 80
    
    #code
    player_quote_6 = "Great, now I have all the equipment to make a spear. "
    #prints character one by one
    for character in player_quote_6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    
    print("You take out the bread knife, rope and long stick from your bag")
    time.sleep(1)
    print()
    print("You attach the knife to the end of the stick by wrapping it with the rope.")
    time.sleep(1)
    print()
    player_quote_yee = "I finally feel somewhat safe.. I can hunt, find some food and defend myself"
    #prints character one by one
    for character in player_quote_yee:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    #removing items from the list
    inventory.remove("bread knife")
    inventory.remove("long rope")
    #adding item to the end of the list
    inventory.append("spear")
    print()
    print("A sense of hope rushed through you as you gripped the spear tightly")
    time.sleep(2)
    print()
    
            

                                                       

#final section of the game
def display_final_scene():
    #Defining variables
    i = 0
    health = "80%"
    inventory = ["spear","lighter"]
    #code
    
    print("Your body felt a bit more refreshed. It was a good feeling")
    print()
    time.sleep(1)
    print("You felt that you were near the end of the forest")
    print()
    time.sleep(1)
    print("A sudden rush of hope filled you")
    print()
    time.sleep(1)
    print("When suddenly you felt your whole body fall over")
    print()
    time.sleep(1)
    print("In a matter of seconds you were on the ground. You felt an intolerable pain from every part of your body.")
    print()
    time.sleep(2)
    print("It appeared as if you have fallen of a cliff.")
    print()
    #health status updated
    health = "70%"
    #prints character in player quote one by one
    player_quote_23 = ' "How could this be, I swear the ground infront of me was all flat" '
    for character in player_quote_23:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()

    print("When you stood up there were three entrances to a path that looked like a cave.")
    print()
    time.sleep(1)
    print("There was a really tall rock that blocked you from going anywhere")
    print()
    time.sleep(1)
    print("It was too tall to climb.")
    print()
    player_quote_24 = ' "I have to make a choice on what cave to enter, theres no other way." '
    for character in player_quote_24:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()

    #different player options
    print("CAVE/PATH 1: There were clean human clothes and bags outside of the cave. They were scattered like sand")
    print()
    time.sleep(1)
    print("CAVE/ PATH 2: The entrance was covered with spider webs")
    print()
    time.sleep(1)
    print("CAVE/ PATH 3: There was nothing infront.. not a single spider web.. it was completely clear")
    print()
    time.sleep(1)
    print()
    print()
    time.sleep(2)

    #player thoughts
    player_quote_25 = '  "Why are there clothes outside path 1. Did people explore this cave. Are people living here..?" '
    print("You could not wait to see another human face. Tears rolled down your eyes")
    print()
    time.sleep(1)
    player_quote_26 = ' "I need to listen to my brain right now, not my heart, I need to think." '
    print()
    time.sleep(1)
    player_quote_27 = ' "Why are there spider webs blocking the entrance to cave 2. Is the spider trying to stop people from entering, or is it trying to trick them by making them think that??" '
    print()
    time.sleep(1)
    player_quote_28 = ' "Why is this cave clear, is the spider unable to enter this cave or is it trying to trick me?" '
    #printing each character one by one to show that the player is speaking
    for character in player_quote_25:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    #printing each character one by one to show that the player is speaking
    for character in player_quote_26:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    #printing each character one by one to show that the player is speaking
    for character in player_quote_27:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    #printing each character one by one to show that the player is speaking
    for character in player_quote_28:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    #question loop
    while i < 1:
        user_final_input = input("Enter what option you chose [1/2/3]? ")
        #if player input is '1'  then this piece of code will run:
        if user_final_input == '1':
            print("You decided to enter cave 1")
            print()
            time.sleep(1)
            print("ONCE you entered, there was NO going back.. the cave closed behind you in an instance")
            print()
            time.sleep(1)
            print("When you entered the cave, the smell of rotten flesh and meat lingered to your nose.")
            print()
            time.sleep(1)
            print("You felt like you were about to puke.")
            print()
            time.sleep(1)
            print("You looked up and began to shake in horror")
            print()
            time.sleep(1)
            print()
            print("There were dead bodies trapped in spider webs right above your head")
            print()
            time.sleep(1)
            print("The clothes outside the cave were not of people who lived here but of those who entered the cave and died..")
            print()
            time.sleep(2)
            print()
            print("and YOU are about to become one of them...")
            print()
            time.sleep(1)
            print()
            print("You entered the spder's cave....")
            i+=1

        elif user_final_input == '2':
             #if player input is '2'  then this piece of code will run:
            print("You grabbed your spear and removed the spider webs that covered the entrance")
            print()
            print()
            time.sleep(1)
            print("You entered the cave and a terrible smell lingered to your nose")
            print()
            time.sleep(1)
            print("The entrance to the cave closed in an instant")
            print()
            time.sleep(1)
            print("You looked up and there were purple coloured flowers hanging from the top, it covered the whole cave.")
            print()
            time.sleep(1)
            print("Despite it's beauty, it gave of a horrid smell")
            print()
            time.sleep(1)
            print("Suddenly, a thought ran through your mind..")
            print()
            time.sleep(1)

            player_quote_29 = ' "Is this flower acting like some sort of repellent..?" This flower might be toxic to the spider "'
            player_quote_30 = ' "Is this why there were spider webs blocking the path?? Was it trying to discourage me from chossing this path??" '
            player_quote_31 = ' "It knew that if people chose this path, it will never be able to find them.."'

            #printing each character one by one to show that the player is speaking
            print()
            for character in player_quote_29:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            for character in player_quote_30:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            for character in player_quote_31:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
                
            print()
            print("The cave suddenly got brigher")
            print()
            time.sleep(1)
            print("The exist was near...")
            print()
            time.sleep(1)
            print("You existed the cave..")
            print("You saw mountains and houses in a distance..")
            print()
            time.sleep(1)
            print()
            print("Tears of joy rolled down your cheeks")
            print()
            time.sleep(1)
            print()
            player_quote_32 = ' "I made it, I finally made it..." '
            #printing each character one by one to show that the player is speaking
            for character in player_quote_32:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            #big text to let the player know that they won. Credit - https://www.asciiart.eu/
            print()                                   
            print("                                                                          88     ")
            print(" ,adPPYba,  ,adPPYba,  8b,dPPYba,   ,adPPYb,d8  8b,dPPYba,   ,adPPYYba, MM88MMM  ,adPPYba, ")
            print('a8"     "" a8"     "8a 88P'    "8a a8"     'Y88  88P   "Y8n  ""     `Y8   88     I8[    ""  ')
            print('8b         8b       d8 88       88 8b       88   88          ,adPPPPP88   88     `"Y8ba,'   '')
            print('8a,   ,aa  8a,   ,a8"  88       88 "8a,   ,d88   88          88,    ,88   88,     aa    ]8I')  
            print(' `"Ybbd8"'   "YbbdP"'  88       88  `"YbbdP"Y8   88          `"8bbdP"Y8   "Y888  `"YbbdP"''')
            print('                                    aa,    ,88                                ')
            print('                                    "Y8bbdP"    ')
            i+=1
                        

        elif user_final_input == '3':
             #if player input is '3'  then this piece of code will run:
            print("You entered cave 3")
            print("The entrance closed right behind you")
            time.sleep(1)
            print("At first, it seemed normal..")
            print()
            time.sleep(1)
            print("But no matter how much you walked, the path did not come to an end")
            print()
            time.sleep(1)
            print("It was a never-ending cave.. You died of starvation...")
            print("_______________________ GAME OVER_____________________________")
            i+=1

        elif user_final_input == 'health':
            print(health)

        elif user_final_input == 'inventory':
            print(inventory)
                
                
#lake scene
def display_lake_scene_1():
    #defining variables
    inventory = ["bear meat", "lighter", "spear"]
    health = "60%"
    i = 0
    y = 0

    #code
    print("You wash your face and blood-drenched clothes with the water")
    print()
    time.sleep(1)
    print("When the water splashed against your face, you finally felt alive")
    print()
    time.sleep(1)
    print("Tears came rolling down your eyes at how good the feeling felt")
    print()
    time.sleep(1)
    player_quote_21 = ' "In just one day I have gone through so much" '
    #printing each character one by one to show that the player is speaking
    for character in player_quote_21:   
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.10)
    print()
    print("You decided to start a fire to quickly cook your bear meat and dry your clothes")
    print()
    time.sleep(2)
    print("Using the lighter in your bag you started a small camp fire by setting fire to a few logs")
    print()
    time.sleep(1)
    print("You place the bear meat over the fire and cooked it for a few minutes and in the mean time, you filled your empty water bottle with water")
    print()
    time.sleep(2)
    print("When you bite into the meat, you could not cope with how good it tasted")
    print()
    time.sleep(1)
    print("Eventhough it was not seasoned, it was one of the best meals you ever had after hours of starvation.")
    print()
    time.sleep(1)
    health = "Health: 70%"
    print("The warmth of the fire carried away all your worries for a second. You felt calm and safe")

    player_quote_24 = "Should I rest for a little bit longer?"
    #printing each character one by one to show that the player is speaking
    for character in player_quote_24:   
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.10)
    print()
    #player_options
    print("OPTION 1: Rest for a little bit longer and regain your strength")
    print("OPTION 2: Keep on moving and rest somewhere else")
    print()

    #question loop
    while y < 1:
        user_input_lake = input("Enter your chosen option [1/2]: ")

        if user_input_lake == "1":
            ##if player input is '1'  then this piece of code will run:
            print()
            print("You decide to rest for a little bit longer beside the camp fire")
            print()
            time.sleep(1)
            print("You pack everything in your bag and sleeps for about a half an hour.")
            print()
            time.sleep(1)
            print("Suddenly... a loud growl wakes you up")
            print()
            time.sleep(1)            
            print()
            print("Spidereru was standing right infront of you, with saliva dripping down the side of its mouth")
            print()
            time.sleep(1)
            print("..........The spider pulls you from your leg and chokes you to death...")
            print()
            print("The smell of the fire and cooked bear meat allowed for the spider to easily find you..")
            print()
            time.sleep(1)
            print("It is best to clean up after youself as quick as you can and rest somewhere else because predators have a strong sense of smell.")
            print()
            time.sleep(1)
            health = "0 %"
            print()
            print("_______________________ GAME OVER_____________________________")
            y+=1
            
            
        elif user_input_lake == '2':
            #if player input is '2'  then this piece of code will run:
            player_quote_22 = ' "If I stay here any longer, the bear meat smell might attract predators and the spider." '
            for character in player_quote_22:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()

            print("You pack up everything and destroy anything that could give the slightest hint that you were there")
            print()
            time.sleep(1)
            print("You deassembled the spear so you can use the rope")
            print()
            time.sleep(1)
            #adds and removes items from inventory list
            inventory.remove("spear")
            inventory.append("bread knife")
            inventory.append("rope")
            
            print("You walked for 10 minutes and climbed a nearby tree and sat on a branch")
            print()
            time.sleep(1)
            print("You wrapped your body to the tree using the rope so that you don't fall of")
            print()
            time.sleep(1)
            print("********** 1 hour later ************")
            print()
            health = "80%"
            time.sleep(1)
            print()
            print("When you opened your eyes it was dawn.")
            print()
            time.sleep(1)
            print("You quickly got down from the tree and re-assembled your spear")
            print()
            time.sleep(1)
            #adds and removes items from inventory list
            inventory.append("spear")
            inventory.remove("bread knife")
            inventory.remove("rope")
            
            display_final_scene()
            y+= 1

        elif user_input_lake == "health":
            print(health)
            print()

        elif user_input_lake == 'inventory':
            print(inventory)
            print()

            
                                
        

        
###--------------------------------------------------------------------------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------------------------------------------------------------------------
##
##
##
##
#prints game logo                                                                   #STRUCTURE
display_game_logo()

# Asks for player info and begins the game
while intro < 1:
    begin = (input("\nDo you want to play: \n").lower()) #user information/input

    if begin == "yes":
        intro+= 1

    elif begin == "no":
        print("Thats too bad then")

    else:
        print("Pls enter either 'yes ' or 'no'") #input validation
        
player_name = input("Enter name: ")

# game introduction
display_intro()

print("---------------------------------------------------------------------------")
time.sleep(1) 


#How to play instructions
while part1 < 1:
    user_input = (input("\nDon't know how to play? Type [help]. If not, type [begin]: \n").lower()) 

    if user_input == "help":
        how_to_play()
        part1 += 1

    elif user_input == "begin":
        part1 += 1

    #input validation
    else:
        print("That is not a valid input. Pls enter either [help] or [begin]") 
    









##################################################
                                                        
print("                                       \n~~~~~~~~~~~~~~~~~~~~~~~~ The Game Will Now Begin ~~~~~~~~~~~~~~~~~~~~~~~~~\n")


#The first choice for player
display_first_choice()

#define variables
x = 0
#question loop
while x < 1:
    user_option_1 = input("\nPls enter what option you chose. 1/2? \n")
    if user_option_1 == '1':
        print("You have chosen option 1")
        time.sleep(1)
        print()
        x += 1

    elif user_option_1 == '2':
        print("You have chosen option 2")
        time.sleep(1)
        print()
        x += 1

    elif user_option_1 == 'inventory':
        print(inventory)
        print()

    elif user_option_1 == 'health':
        print(health)
    #input validation
    else:
        print("invalid input, pls enter either 1/2") 

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------


        
                                                                     
        
if user_option_1 == "1":
    #defining variables
    i = 0
    z = 0
    y = 0
    health = "80%"
    inventory = ["bread knife", "lighter", "long rope"]
    option_1_part_1()
 
    #adds to list
    inventory.append('wood x3')
    print(" wood x 3 was added to inventory") 
    print()
    print("REMINDER: Type [inventory] to see what's in your bag at anytime")
    print()
    display_spear_story()
    display_bear_attack()


    while z < 1:
        #defining variables
        health = "80%"
        inventory = ["bread knife", "lighter", "spear"]
        user_input = input("Enter either 1/2/3: ")

        if user_input == "1":
            play_dead() #need to find a way to allow for the player to restart the game
            z+= 1

        elif user_input == "2":
             #if player input is '2'  then this piece of code will run:
            health = "health: 63%"
            outrun_bear()
            z+=1  

        elif user_input == '3':
             #if user input is '3'  then this piece of code will run:
            move_back()
            display_section_1()
            z+=1

        elif user_input == 'inventory':
             #if player input is 'inventory'  then this piece of code will run:
            print(inventory)

        elif user_input == 'health':
             #if player input is 'health'  then this piece of code will run:
            print(health)
            
            
        elif user_input == "attack":
             #if player input is 'attack'  then this piece of code will run:
            print("You grabbed your spear tightly and held it infront of you")
            print(" The bear charged at you")
            print("You dodged it's attack and stabbed the spear through it's neck multiple times until the bear fell silent..")
            print("You laid there with blood covering your shirt.. tears of disbelief fell down your eyes.")
            print("Your white T-shirt was now RED.")
            print()
            player_quote_11 = ' "I did what I had to do.. Im so sorry" '
            for character in player_quote_11:   
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.10)
            print()
            #health status updated
            health =  "Health: 65%"
            print("You loosened the rope and took the knife out, so that you can cut some bear meat to cook")
            inventory.append("bear meat x 5")
            print("You tightened the rope once again to make a spear")
            print()
            print("I just need to find a place to cook this and eat it")
            print()
            print("You got up and started walking.. when suddenly.. you heard the spider growl..")
            print()
            time.sleep(2)
            print("It jumped from a tree and grabbed onto the bears body while screaming from the top of its lungs")
            print()
            print("You shook in disbelief.. but it was acting very weird..")
            time.sleep(2)
            display_section_1()
            z+=1
    

elif user_option_1 =='2':
    display_option_2()
    
    
                          















