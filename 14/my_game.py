#Author: Elizabeth Chan
#Description: final version of the game (before early release)

import random
import time
from threading import Timer

#NOUNS
i = 0

# characters
player_1 = ""
player_1_talk = ""
player_1_spacing = 100 - len(player_1_talk)
p1_spacing_new = 105
viscount = ""
viscount_talk = ""
viscount_talk_spacing = 9
shopkeeper = ""
shopkeeper_talk = ""
shopkeeper_talk_spacing = 11


#code_decipher_quiz_generator
random_number_list = []
random_character_list = ""
final_letter_string = ""
letters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
j = [0,1,2,3,4,5]

#treasure_quiz generator
k = 3 

# VERBS
#An introduction to the game that asks for player's name and gender
def welcome_to_the_game(player_1):
    player_1 = input(f"Viscount: Before beginning, please enter your name.\n{' ' * player_1_spacing} You: ")
    #Asking the gender of the player_1 to determine whether the program will say "Sir {player_1}" or "Madam {player_1}" or just "{player_1}". 
    gender = input(f"\nViscount: If I may ask, what is your gender? (Male/Female) \n{' ' * viscount_talk_spacing} If you would prefer not to say, please press ENTER. \n{' ' * player_1_spacing} You: ").lower()
    #Response that is specific to the player's gender
    if gender == "Male".lower():
        sir_madam = "Sir"
        input(f"\nViscount: Greetings Sir {player_1}! Welcome to the Coded Treasure! \n{' ' * viscount_talk_spacing} You are in the Medieval Times. Robbers have stolen the treasure from the ruler, Lord the King. \n{' ' * viscount_talk_spacing} As a valiant knight of Lord the King, it's your job to take back the treasure. ")
    elif gender == "Female".lower():
        sir_madam = "Lady"
        input(f"\nViscount: Greetings Lady {player_1}! Welcome to the Coded Treasure! \n{' ' * viscount_talk_spacing} You are in the Medieval Times. Robbers have stolen the treasure from the ruler, Lord the King. \n{' ' * viscount_talk_spacing} As a valiant knight of Lord the King, it's your job to take back the treasure. ")
    else:
        input(f"\nViscount: Greetings {player_1}! Welcome to the Coded Treasure! \n{' ' * viscount_talk_spacing} You are in the Medieval Times. Robbers have stolen the treasure from the ruler, Lord the King. \n{' ' * viscount_talk_spacing} As a valiant knight of Lord the King, it's your job to take back the treasure. ")
    # description of the game
    challenge_accepted(player_1)

#Will the challenge be accepted by the player?
def challenge_accepted(player_1):
    challenge_accepted = input(f"\nDo you accept the challenge? Yes/No\n{' ' * player_1_spacing} You: ").lower()
    complaint = (f"Viscount: Hmm, I'm afraid you have a hard time following instructions. Nevertheless, challenge accepted! \n{' ' * viscount_talk_spacing} A passerby has given me the hint that the shopkeeper of the General Store is hiding something. \n{' ' * viscount_talk_spacing} I have been told it's the treasure? I commmission you to find out the truth.")
    #if the challenge is accepted by the player, the game will proceed
    if challenge_accepted == "Yes".lower():
        print(f"\nViscount: Challenge accepted! \n{' ' * viscount_talk_spacing} A villager has given me a hint that the shopkeeper of the General Store is hiding something. \n{' ' * viscount_talk_spacing} Suppose it be the treasure? I commmission you to find out the truth.")
        talk_to_the_viscount(player_1,viscount)
    #The following statements catch any errors in the user's input
    elif challenge_accepted == "Yes ".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Yep".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Yeah".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Ye".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Yea".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Ya".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Y".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Yeh".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    elif challenge_accepted == "Ok".lower():
        print(complaint)
        talk_to_the_viscount(player_1,viscount)
    #Any input other than the ones listed above will cause the game to close 
    else:
        print("Viscount: What? You did not accept the challenge? What type of knight are you? CLOSING DOWN.")
        time.sleep(4)
        exit()
        # Will the player accept the challenge?
    time.sleep(3)

#prints the conversation between the Viscount and player_1    
def print_conversation_viscount(player_1_talk,viscount_talk):
    input(f"\n{viscount_talk}")
    input(f"{' ' * player_1_spacing} {player_1_talk}")

#This is a conversation between the Viscount and player_1. The Viscount introduces the background of the game. 
def talk_to_the_viscount(player_1,viscount):
    #Exchange 1 with Viscount
    viscount_talk = f"Viscount: Do you see that ramshackle building over there? (Press ENTER to proceed)"
    player_1_talk = "You: Yes"
    print_conversation_viscount(player_1_talk,viscount_talk)
    #Exchange 2 with Viscount
    viscount_talk = f"Viscount: Well, inside lives a despicable sort of man - the general store shopkeeper.  \n{' ' * viscount_talk_spacing} A drunkard, cruel and full of himself. Fortunately for us though, he  \n{' ' * viscount_talk_spacing} believes himself to be the smartest person in the world."
    player_1_talk = f"You: Right...that sounds pleasant. But what does that \n{' ' * p1_spacing_new} have to do with me?"
    print_conversation_viscount(player_1_talk,viscount_talk)
    #Exchange 3 with Viscount
    viscount_talk = f"Viscount: He has created what he believes is an unsolvable quiz for anyone who wants to \n{' ' * viscount_talk_spacing} gain access to the treasure.  Most of the villagers, while intelligent \n{' ' * viscount_talk_spacing} in other fields, are not learned and would not stand a chance."
    player_1_talk = f"You: That should be pretty easy. What's the catch?"
    print_conversation_viscount(player_1_talk,viscount_talk)
    #Exchange 4 with Viscount
    viscount_talk = f"Viscount: The catch is...if you fail the quiz, well, the shopkeeper has quite a punish\n{' ' * viscount_talk_spacing} ment. One villager tried to defeat the shopkeeper and disappeared. Some believe \n{' ' * viscount_talk_spacing} the shopkeeper kidnapped him."
    player_1_talk = f"You: Woah! Spooky! I see now why you wanted ME to do \n{' ' * p1_spacing_new} the job (and not yourself!)!"
    print_conversation_viscount(player_1_talk,viscount_talk)
    #Exchange 5 with Viscount
    viscount_talk = f"Viscount: Well, I..I sincerely wish you all the best. As I said, you were brave to \n{' ' * viscount_talk_spacing} sign up to this. May some good goblin protect you! Goodbye now!"
    player_1_talk = f"You: ..."
    print_conversation_viscount(player_1_talk,viscount_talk)
    #Game Narration 1
    print("\n\nYou enter the the dark, dingy shop to find a man sitting behind the counter. His hair is black and grimy, but he is surprisingly well dressed. He looks up at you with cold, narrowed eyes...")
    talk_to_the_shopkeeper(player_1, viscount)

#prints the conversation between the shopkeeper and the player
def print_conversation_shopkeeper(player_1_talk, shopkeeper_talk):
    input(f"\n{shopkeeper_talk}")
    input(f"{' ' * player_1_spacing} {player_1_talk}")    

#This is a conversaton between the shokeeper and player_1. It is the lead up to the first code decipher quiz. 
def talk_to_the_shopkeeper(player_1, viscount):
    #Exchange 1 with shopkeeper
    shopkeeper_talk = "Shopkeeper: What do ye want, ye 'n yer fine clothes?"
    player_1_talk = "You: Uhh, I was wondering..."
    print_conversation_shopkeeper(player_1_talk, shopkeeper_talk)
    #Exchange 2 with shopkeeper
    shopkeeper_talk = "Shopkeeper: Ey, I know. Ye wanted t' look at me fine treasure!"
    player_1_talk = "You: ..."
    print_conversation_shopkeeper(player_1_talk, shopkeeper_talk)
    #Exchange 3 with shopkeeper
    shopkeeper_talk = "Shopkeeper: Aye. I saw ye 'n that other fine clothed scallywag yabberin' in th' street! "
    player_1_talk = "You: (That's wonderful)"
    print_conversation_shopkeeper(player_1_talk, shopkeeper_talk)
    #Exchange 4 with shopkeeper
    shopkeeper_talk = f"Shopkeeper: So, if ye wants t' pass me th' Shopkeeper, ye do me quiz. If ye fail, I do wha' \n{' ' * shopkeeper_talk_spacing} I wants wit' ye. I kidnap ye"
    player_1_talk = "You: (Yeesh!) Fine, whatever. I'm ready."
    print_conversation_shopkeeper(player_1_talk, shopkeeper_talk)
    intro_code_decipher_quiz()
    
# the shopkeeper's code decipher quiz
def intro_code_decipher_quiz():
    input("\n\nThe shopkeeper shows you down a dark corridor. At the end of the dark hallway, you see a strange dusty box. Upon opening the dusty box, you read the words..")
    input("\n                                       \"One and a half minutes precisely til' yer death, landlubber.\"")
    input("\nYou turn to find the shopkeeper has disappeared and the hall is almost pitch black. You lean closer to the box.")
    input("\nFacing you is a string of numbers. Beneath the string of numbers are rows of buttons with what looks like letters on them. It is clearly not a keyboard, because keyboards didn't exist in the Middle Ages.\n")
    code_decipher_quiz_generator()

#on timeout, the timer will redirect to the (not yet completed) intro_waterfall_detour()
def on_timeout():
    intro_waterfall_detour()

#This generates random numbers, which correspond to letters of the alphabet. 
def code_decipher_quiz_generator():
    timeout = 90
    #generates random number sequence    
    t = Timer(timeout, on_timeout)
    random_number_list = random.sample(range(1, 26), 6)
    input(random_number_list)
    #converts numbers to letters and stores them in a variable
    random_character_list = (letters[random_number_list[0]-1],letters[random_number_list[1]-1],letters[random_number_list[2]-1],letters[random_number_list[3]-1],letters[random_number_list[4]-1],letters[random_number_list[5]-1]) 
    t.start()
    #user inputs code here
    user_string = input(f"\n You have 90 seconds to solve the number puzzle! (Clue: you have a \"keyboard\") \n{' ' * player_1_spacing} You: ")
    #if the length of the user_string is greater or smaller than 6 (meaning the answer is incorrect), the player will be sent on a detour
    if len(user_string) > 6:
        t.cancel()
        intro_waterfall_detour()
    elif len(user_string) < 6:
        t.cancel()
        intro_waterfall_detour()
    #if the user inputs the correct string of letters, the user will be able to keep going
    elif len(user_string) == 6:
        #checks user_string for errors. If these statements catch an error, the player will be sent on a detour
        if user_string[0] != random_character_list[0]:
            t.cancel()
            intro_waterfall_detour()
        elif user_string[1] != random_character_list[1]:
            t.cancel()
            intro_waterfall_detour()
        elif user_string[2] != random_character_list[2]:
            t.cancel()
            intro_waterfall_detour()
        elif user_string[3] != random_character_list[3]:
            t.cancel()
            intro_waterfall_detour()
        elif user_string[4] != random_character_list[4]:
            t.cancel()
            intro_waterfall_detour()
        elif user_string[5] != random_character_list[5]:
            t.cancel()
            intro_waterfall_detour()
        #if the user_string is correct, the player will be able to keep going (no detour)
        else:
            t.cancel()
            intro_to_collect_treasure()

              
#The waterfall detour
#The player gets sent on a detour if they fail the code_decipher_quiz
def intro_waterfall_detour():
    print("\n\nBEEP! ", end="")
    time.sleep(1)
    print("BEEP! ", end="")
    time.sleep(1)
    print("BEEP! ", end="")
    time.sleep(1)
    print(" An ominous red light flickers on. You hear the loud thudding of footsteps behind you...")
    time.sleep(3)
    input("Story to be continued. NEXT TIME!")
    exit()


#If the player passes the code_decipher_quiz, they continue on their path to the treasure
def intro_to_collect_treasure():
    input("\nA candle bursts into flame on the wall beside the box, revealing the faint indentation of a door. You touch the stone face of the door and it slides open, revealing a cold, dark passage. You slowly edge your way into the tunnel. Suddenly you hear a grating noise behind you, the door is now shut. ")
    input("\nYou struggle with the door, but it refuses to budge. You have no choice but to find out what is at the end of the tunnel.\n")
    user_choice()

#The user must choose what to do next by entering "A", "B", "C". 
def user_choice():
    user_selection = input(f"\n\nYou reach the end of the tunnel to find a sheet of glass. What should you do? \nA: Break the glass\nB: Say a prayer\nC: Wait\n{' ' * player_1_spacing} You: ").lower()
    #runs different scenarios depending on user response (A,B,C)
    if user_selection == "A".lower():
        break_the_glass()
    elif user_selection == "B".lower():
        say_a_prayer()
    elif user_selection == "C".lower():
        wait()
    #catches any player typing errors and loops back to user_choice
    else:
        print("Sorry?")
        user_choice()

#The first option leads to automatic death    
def break_the_glass():
    print("\nYou break the glass, cutting your hand in the process. You begin to bleed....")
    time.sleep(3)
    print("and bleed...")
    time.sleep(1)
    print("and bleed...")
    time.sleep(2)
    print("\nShopkeeper: ", end = "")
    time.sleep(1)
    print("GAME", end = "")
    time.sleep(1)
    print(" OVER")
    time.sleep(1)
    input("\nBut before you go, you would like to know that the Viscount paid for his crimes and is now in the Royal Jail awaiting trial.")
    exit()

#The second option is the right one. It will lead to the treasure quiz. 
def say_a_prayer():
    print("\nYou say a prayer out loud and something begins to glow behind the glass. ", end="")
    time.sleep(2)
    print("So it turns out that the glass is voice activated! Again, we don't know how the Shopkeeper manages to get these gadgets. He, uh, just does. Anyway...")
    time.sleep(5)
    input("...suddenly, a  table of numbers appears behind the glass. (Upcoming quiz! Click enter to proceed)")
    take_the_treasure_quiz()

#The third option loops back to user_option
def wait():
    print("You wait...")
    time.sleep(2)
    print("and wait...")
    time.sleep(1)
    print("and wait. ",end="")
    time.sleep(1)
    print("But of couse nothing happens...")
    user_choice()

#The player must take the treasure quiz in order to access the treasure   
def take_the_treasure_quiz():
    #k is the number of lives
    global k
    while True:
        #While the number of lives is above 0, the user may repeat the quiz
        if k > 0:
            #This generates a table of random numbers
            random_number_list_2 = random.sample(range(0, 99), 25)
            nestedList = [[[random_number_list_2[0]],[random_number_list_2[1]],[random_number_list_2[2]],[random_number_list_2[3]],[random_number_list_2[4]]],
                          [[random_number_list_2[5]],[random_number_list_2[6]],[random_number_list_2[7]],[random_number_list_2[8]],[random_number_list_2[9]]],
                          [[random_number_list_2[10]],[random_number_list_2[11]],[random_number_list_2[12]],[random_number_list_2[13]],[random_number_list_2[14]]],
                          [[random_number_list_2[15]],[random_number_list_2[16]],[random_number_list_2[17]],[random_number_list_2[18]],[random_number_list_2[19]]],
                          [[random_number_list_2[20]],[random_number_list_2[21]],[random_number_list_2[22]],[random_number_list_2[23]],[random_number_list_2[24]]]]
            
            print(("|       ||___1___|___2___|___3___|___4___|___5___|"))
            print(f"|   A   ||   {random_number_list_2[0]}", " "*( 2 - (len(str(random_number_list_2[0])))), "|",f"  {random_number_list_2[1]}", " "*( 2 - (len(str(random_number_list_2[1])))) , "|", f"  {random_number_list_2[2]}", " "*( 2 - (len(str(random_number_list_2[2])))), "|", f"  {random_number_list_2[3]}", " "*( 2 - (len(str(random_number_list_2[3])))), "|", f"  {random_number_list_2[4]}", " "*( 2 - (len(str(random_number_list_2[4])))), "|")
            print(f"|   B   ||   {random_number_list_2[5]}", " "*( 2 - (len(str(random_number_list_2[5])))), "|",f"  {random_number_list_2[6]}", " "*( 2 - (len(str(random_number_list_2[6])))) , "|", f"  {random_number_list_2[7]}", " "*( 2 - (len(str(random_number_list_2[7])))), "|", f"  {random_number_list_2[8]}", " "*( 2 - (len(str(random_number_list_2[8])))), "|", f"  {random_number_list_2[9]}", " "*( 2 - (len(str(random_number_list_2[9])))), "|")
            print(f"|   C   ||   {random_number_list_2[10]}", " "*( 2 - (len(str(random_number_list_2[10])))), "|",f"  {random_number_list_2[11]}", " "*( 2 - (len(str(random_number_list_2[11])))) , "|", f"  {random_number_list_2[12]}", " "*( 2 - (len(str(random_number_list_2[12])))), "|", f"  {random_number_list_2[13]}", " "*( 2 - (len(str(random_number_list_2[13])))), "|", f"  {random_number_list_2[14]}", " "*( 2 - (len(str(random_number_list_2[14])))), "|")
            print(f"|   D   ||   {random_number_list_2[15]}", " "*( 2 - (len(str(random_number_list_2[15])))), "|",f"  {random_number_list_2[16]}", " "*( 2 - (len(str(random_number_list_2[16])))) , "|", f"  {random_number_list_2[17]}", " "*( 2 - (len(str(random_number_list_2[17])))), "|", f"  {random_number_list_2[18]}", " "*( 2 - (len(str(random_number_list_2[18])))), "|", f"  {random_number_list_2[19]}", " "*( 2 - (len(str(random_number_list_2[19])))), "|")
            print(f"|   E   ||   {random_number_list_2[20]}", " "*( 2 - (len(str(random_number_list_2[20])))), "|",f"  {random_number_list_2[21]}", " "*( 2 - (len(str(random_number_list_2[21])))) , "|", f"  {random_number_list_2[22]}", " "*( 2 - (len(str(random_number_list_2[22])))), "|", f"  {random_number_list_2[23]}", " "*( 2 - (len(str(random_number_list_2[23])))), "|", f"  {random_number_list_2[24]}", " "*( 2 - (len(str(random_number_list_2[24])))), "|")
            #This will generate 3 random coordinates. These coordinates will correspond to a certain number in the table. 
            coordinates = ("A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5")
            three_coordinates = str(random.choice(coordinates)) + " " + str(random.choice(coordinates)) + " " + str(random.choice(coordinates))
            print("\nYou have 30 seconds to solve the quiz! Separate your answers with spaces. Your time starts now!")
            print(f"Here are your clues: {three_coordinates}")

            #Coordinates that correspond to a particular number in the table
            list_coordinates = {'A1': random_number_list_2[0],
                                'A2': random_number_list_2[1],
                                'A3': random_number_list_2[2],
                                'A4': random_number_list_2[3],
                                'A5': random_number_list_2[4],
                                'B1': random_number_list_2[5],
                                'B2': random_number_list_2[6],
                                'B3': random_number_list_2[7],
                                'B4': random_number_list_2[8],
                                'B5': random_number_list_2[9],
                                'C1': random_number_list_2[10],
                                'C2': random_number_list_2[11],
                                'C3': random_number_list_2[12],
                                'C4': random_number_list_2[13],
                                'C5': random_number_list_2[14],
                                'D1': random_number_list_2[15],
                                'D2': random_number_list_2[16],
                                'D3': random_number_list_2[17],
                                'D4': random_number_list_2[18],
                                'D5': random_number_list_2[19],
                                'E1': random_number_list_2[20],
                                'E2': random_number_list_2[21],
                                'E3': random_number_list_2[22],
                                'E4': random_number_list_2[23],
                                'E5': random_number_list_2[24]}

            #Stores the three numbers in a variable
            first_number = list_coordinates[f'{three_coordinates[0]+three_coordinates[1]}']
            second_number = list_coordinates[f'{three_coordinates[3]+three_coordinates[4]}']
            third_number = list_coordinates[f'{three_coordinates[6]+three_coordinates[7]}']

            #cocentates the three variable strings together to give the answer string
            answer = str(first_number) + " " + str(second_number) + " " + str(third_number)

            #This quiz also has a time limit of 30 seconds
            timeout_2 = 30
            t2 = Timer(timeout_2, on_timeout_2)
            t2.start()
            user_treasure_input = input(f"\n{' ' * player_1_spacing} You: ")
            #if the player answers the quiz correctly (and the player's input matches the answer string), they will proceed to the finish
            if user_treasure_input == answer:
                t2.cancel()
                print("\nThe wall splits in two, shattering the glass. Behind the wall you find a room. In the centre of the room is a large oaken chest. You lift the lid and see...")
                time.sleep(5)
                print("GOLD! JEWELS! You have found the treasure!!\n")
                time.sleep(3)
                ending()
            #if the players answers the quiz incorrectly, they will lose one life.
            else:
                t2.cancel()
                k -= 1
                losing_lives_treasure()
        else:
            time.sleep(2)
            you_die()

#Automatic loss of one life if time limit is exceeded    
def on_timeout_2():
    global k
    k -= 1
    losing_lives_treasure()

#Causes the player to lose one life
def losing_lives_treasure():
    print(f"\nArgh!! Writing on the glass indicates that you have lost one life. You now have {k} lives.")
    take_the_treasure_quiz()

#If the player loses all their lives, they will die and the game will end. 
def you_die():
    print("\nThe Shopkeeper clubbed you from behind.")
    time.sleep(2)
    print("YOU ARE DEAD!!!")
    time.sleep(5)
    exit()

#If the player successfully answers the treasure quiz, they win the game! 
def ending():
    print("The Shopkeeper comes behind you to club you, but you sense his presence before he gets to you. ", end="")
    time.sleep(3)
    print("Picking up one of the king's sword, you defend yourself. ", end="")
    time.sleep(3)
    print("30 seconds later, the Shopkeeper lies dead at your feet.")
    time.sleep(4)
    print("\nWhat a triumph! You heroically march outside with the treasure. Upon looking at the jewels, you decide that you just might forgive the Viscount for abandoning you....")
    time.sleep(5)
    input("\n\nCONGRATULATIONS!! YOU WON!")
    exit()

#start function
welcome_to_the_game(player_1)
