#Two Worlds - Crossing Infinity
#Author: Devindi Bandara

#Python Interactive Story


#In order for text to print sentence by sentence, and not in chunks, time needs to be imported so that sentences can be printed out after the wanted number of seconds
import time


#Need to define and have a place where info about the game will be printed out, therefore a define function would be ideal
def intro ():

#Firstly, have the title of the game printed out and in a different colour
    import os
    os.system("cls") 
    print("\u001b[34m~~~~~~~~~~Two Worlds - Crossing Infinity~~~~~~~~~~")#the first part of the print statement is the colour the text will change to (blue) when in a python executor 
    time.sleep(1) #allows the player to have time to read the title and other sections of the game without full chuncks of text all appearing at once - creates a flow within the game
    print("") #Spaces between the title and beginning of story (makes the text more organised)
    print("\u001b[37mSPOILER ALERT!!!! ") #the rest of the text printed will be white

#Ask the player if they want to continue playing the game as some parts are from the movie Avengers Endgame
    print("Some events within this game happen within Avengers Endgame")
    spoiler_question = input("Still want to continue? Yes or No: ").upper()
    if spoiler_question == "YES":
        continue_()
    elif spoiler_question == "NO":
        print("Go watch Avengers Endgame and come back!! Hehehe. See ya. Have fun!")
    else:
        reenter_spoiler = input("Do you want to play still? Yes or No: ").upper()
        if reenter_spoiler == "YES":
            continue_()
        elif reenter_spoiler == "NO":
            print("See ya")    
                
        else:
            ("Invalid option")
            

#Ask the player if they want to be a hero or villain
def continue_():
    print("")
    print("Before we start, for all the options throughout this game, enter either A, B or C, depending on the question")
    time.sleep(1)
    print("")
    print("Do you wish to be a hero or a villain?")
    print("""   A. Hero
    B. Villain""")
    time.sleep(1)

    player_character = input("Choose your side: ").upper()

#What would happen if the player chooses to be a hero - they will be Iron Man
    if player_character == "A":
        print("")
        print("You are now a HERO!!!")
        time.sleep(1)
        print("")
        print("You are Iron Man! ")#For future development - they player will have different characters to choose from
        iron_man() #Links to the part of code where the Iron Man story begins

#What would happen if the player chooses to be a villain - they will be Thanos
    elif player_character == "B":
        print("") 
        print("You are now a BADDY!!!")
        time.sleep(1)
        print("")
        print("You are Thanos! MWAHAHAHAHA!! ⋋_⋌")#For future development - they player will have different characters to choose from
        print("Let the battle begin!")
        time.sleep(1)
        thanos() ##Links to the part of code where the Thanos story begins

#What would happen if the player enters a different letter which isnt A or B (To be a hero or villian), they will need to restart the game
    else:
        print("Invalid option")
        restart = input("Restart and choose your character again? Yes or No: ").upper()
        if restart == "YES":
            continue_()
        elif restart == "NO":
            print("Goodbye. See ya next time!")
        else:
            print("Invalid")

#List main components within Iron Man story
iron_man_suit = ["Jarvis","PROTON CANNON"]

#Linking back to what would happen if the player chose to be a hero (Iron Man)
def iron_man():
    time.sleep(1)
    print("")
    
#Explain the objective of the game and what their aim is - how to win
    print("As simple as it may sound, all you have to do is defeat the baddies")
    time.sleep(1) 
    print("")
    time.sleep(2)

    print(f"'Welcome! This is {iron_man_suit[0]} speaking. It is currently 50°C out here as it is expected to rise even higher later in the day.'")  
    time.sleep(1)
    print("'It is scorching out here! The sky is clear blue glass. All you can see are the trillions and millions of sand grains leading nowhere to be known - an endless path.'")
    print("") #The two above sentences are describing the match environment. In future development of the game, there will be different match environements which can be played in
    print(" 'There is no sign of threat. You are clear'")
    print("")
    time.sleep(2)
    restart_part_2_iron_man()

def restart_part_2_iron_man():
    print("You start walking for some while and you hear footsteps approaching from behind")
    print(f"At that very instant, {iron_man_suit[0]} warns you, 'There seems to be people trying to attack you from behind - sneak attack!'")
    print(f" 'Would you like to initiate the {iron_man_suit[1]}? - inflicting the most damage in combat, regardless of who it may be?' ")
    first_attack_iron_man = input("Quick, there isn't much time!! Yes or No: ").upper()   #Insert tense music + fast timer - future development 

#What would happen if the player initiated the proton cannon
    if first_attack_iron_man == "YES":
        yes_for_first_attack_iron_man()

#What would happen if the player did not initiated the proton cannon
    elif first_attack_iron_man == "NO":
        print(f"Why didn't you initiate the PROTON CANNON??? Thanos and Voldemort, two of the most powerful villains, were behind youuu!")
        print("You never know who is behind you. Expect the unexpected.")
        print("Your journey does not end here though! The story still awaits you...")
        restart_iron_man = input("Retry? Yes or No ").upper()
        if restart_iron_man == "YES":
            restart_part_1_iron_man()
        elif restart_iron_man == "NO":
            print("AWWWWEE. It was just the beginning. See you next time then")
        else:
            print("Invalid")

    else:
        print("Invalid option")
        restart_iron_man = input("Retry? Yes or No ").upper()
        if restart_iron_man == "YES":
            restart_beginning_1_iron_man()
        elif restart_iron_man == "NO":
            print("AWWWWEE. It was just the beginning. See you next time then")
        else:
            print("Invalid choice")
        
#If player wants to restart the game from part way through Iron Man's Story       
def restart_part_1_iron_man():
    print("")
    print("")
    print("")
    print("~~~~~IRON MAN~~~~~")
    restart_part_2_iron_man()


#What would happen if proton cannon is used
def yes_for_first_attack_iron_man():
    print("")
    print("Good choice! You could have almost died there! Thanos and Voldemort, two of the most powerful villains, were right behind you!!!!!")
    print("Let the real match begin!")
    print("It is only then you realise that the Avengers have assembled and are ready to attack nevertheless, the one and only Harry Potter and some of the greatest wizards, on your side.")
    time.sleep (5)
    print("In that split second, you see everyone giving it their best and putting their full potential and ability, trying to defeat them")
    print("You have no time to look!Immediately, Voldemort casts the Killing Curse - an unforgivable curse of the Dark Arts.")
    print("")
    print("What on Earth do you do??")
    print("""   A. Use your REPULSORS (the blue firery thing you can shoot from your hands) 
    B. Just stand there""")#insert noises that would come out of iron man's suit - future development

    second_attack_iron_man = input("What do you choose? ").upper()
    if second_attack_iron_man == "A":
        repulsors_iron_man()

    elif second_attack_iron_man == "B":
        print("Why would you just stand there?? Are you trying to get killed. Well... You did.")
        proton_cannon_retry = input("Retry from the beginning of Iron Man story? Yes or No: ").upper
        if proton_cannon_retry == "YES":
            iron_man()
        elif proton_cannon_retry == "NO":
            print("See you then! ")
        else:
            print("Invalid")
            


#What would happen if player chooses repulsors
def repulsors_iron_man():
    print("Nice one! You see him shuffle backwards HOWEVER that does not stop him. He regains his balance and decides to cover himself with an Invisibility Cloak") #dun dun daaaaa sound effects inserted
    time.sleep(1)
    print("Uh ooohhh, you cannot see him anymore!")
    print("What do you do??")
    print("""   A. Attack Thanos instead
    B. Use all equipped weapons embodied within your suit and shot everywhere, killing everyone
    C. Let him find his way to you""")
    invisibility_cloak_iron_man = input("You...").upper()
    if invisibility_cloak_iron_man == "A":
        fighting_thanos_iron_man()

    elif invisibility_cloak_iron_man == "B":
        print("Not the best option... You killed your own team mates.")

    elif invisibility_cloak_iron_man == "C":
        print("Now, you are just standing there. Everyone else in battle, but you - cautious of your surroundings.")
        print("You don't know which way he might attack...You don't know when he will strike...")
        print("Suddenly, 'Jarvis here. You are an intended targeted. Would you like to fire-up your Unibeam? (gathers all power and is shot out from your chest)")
        unibeam_fireup_iron_man = input("Yes or No:").upper()
        if unibeam_fireup_iron_man == "YES":
            lasers_iron_man()
        elif unibeam_fireup_iron_man == "NO":
            print("What were you then planning on doing, huh??")
            print("It was an irreversible, death curse. You died")
            time.sleep(1)
        
              

#What would happen if player wants to fight Thanos instead
def fighting_thanos_iron_man():
    print("Nice plan of attack. You see him at a far. ")
    print("You approach him, BUT, as soon as you do, it is clear that he is about to snap his fingers and you know what will happen - all living matter will disappear...")#dun dun daaaa music inserted (shocking noise)
    print("Suddenly, you see spiderman shoot his webs, targeting at Thanos' infinity gauntlet where all the stones are.")
    print("You see him tug and tug untilll..........")
    time.sleep(2)

    print("BAM!!! YESSSS!!! He was able to remove all the powerful stones, BUT the problem is..... He sees you, and chucks them at you!!!")
    print("""What do you do?????
    A. Create your own infinity gauntlet and snap your fingers 
    B. Run away
    C. Pass them to someone else""")
    infinity_stones_iron_man = input("You.... ").upper()
    if infinity_stones_iron_man == "A":
          iron_man_gauntlet()

    elif infinity_stones_iron_man == "B":
        print("Why would you run away...Thanos will win")
        print("He grabs the stone, places them on his infinity gauntlet with a smirk and snaps his fingers in which looks he waited for a long time to do")
        print("Your journey does not end here though! The story still awaits you...")

    elif infinity_stones_iron_man == "C":
        pass_stones_iron_man()

#What would happen if iron man creates own gauntlet
def iron_man_gauntlet():
    print("Oof. Yess. You speedly place the 6 infinity stones on the back side of your repulsor")
    print("Suddenly you feel a strong, powerful sensation of ultimate power. It feels like you have gathered all the energy, power, light, speed within your hand")#music insert (woosh)
    print("With all this great power, all that is left to do it to snap your fingers")
    time.sleep(2)
    x = 4
    while x > 0:
        x -= 1
        print(x)
    time.sleep(1)
    print("")
    print("'I am Iron Man'")
    time.sleep(2)
    #sound inserted - BAM! everything disappearing - future phase
    print("Suddenly, you feel the whole world shaking, you see Thanos' crew, his weapons, his people and he himself, disappearing, into ashes...Into nothing...")
    print("FINALLY!!")
    time.sleep(1)
    print("Victory is ours!")
    print("YOU WON!!")
    time.sleep(2)
    play_again_iron_man = input("Wanna play again but be the baddie? Yes or No?: ").upper()
    if play_again_iron_man == "YES":
        print("")
        print("~~~~~THANOS~~~~~")
        thanos()
    elif play_again_iron_man == "NO":
        ask_again = input("Wanna be Iron Man again, but use different tactics to get different results? ^_^. Yes or No? ").upper()
        if ask_again == "YES":
            print("~~~~~IRON MAN~~~~~")
            iron_man()
        elif ask_again == "NO":
            print("See ya next time!")
          


#What would happen if iron man passes the stones to someone else
def pass_stones_iron_man():
    print("If you pass it to someone else, you are sacrificing their life. The only person, who will enable us to gain victory, is Hulk.")
    time.sleep(1)
    print("If you pass the stones to Hulk and he snaps his fingers with the gauntlet, he might not make it out alive... Do you still want to pass them?")
    pass_stones_again = input("Yes or No: ").upper()
    if pass_stones_again == "YES":
        print("You pass them to him and you see he has snatched and obtained Thanos' infinity gauntlet. The moment you see him snap his fingers you see him...")
        time.sleep(1)
        print("Struggle to cope up with the intense and immense surge of energy building up within the gauntlet. He is eyes squinting in pain. He is screaming in agony")
        time.sleep(2)
        print("And all you are doing is watching him. You could have sacrificed yourself. You had the ability to do it yourself, but you didn't")
        time.sleep(1)
        print("Before it is too late, do you want to save your friend by grab the infinity stones and create your own gauntlet?")
        gauntlet_iron_man = input("Yes or No: ").upper()
        if gauntlet_iron_man == "YES":
            iron_man_gauntlet()

        elif gauntlet_iron_man == "NO":
            print("Why wouldn't you want to save your friend. You let him die... That is not what you stand for.")
              
    elif pass_stones_again == "NO":
        iron_man_gauntlet()
    
    
    
    
#What would happen if player chose lasers, being Iron Man   
#Sectioning out code - small part for iron man using lasers
def lasers_iron_man():
    print("Now there is a strong, powerful connection formed between you two. You feel yourself rising up, away from the ground and so does he.")
    print("You realise that this connection has created something unimaginable... Something that should have not been created...")
    time.sleep(3)
    portal()

#Part where sections link to and continue from here
def portal():
    print("A portal to another universe...")#dun dun dun music insterted in later phase
    time.sleep(1)
    print("It is a place where time does not flow. No wind... no rain...Simply, no life...")
    print("It is just you and him. The last person standing wins")
    time.sleep(2)
    print("You see him from afar")
    time.sleep(1)
    print("You see him sprinting towards you, equipped, and you, yourself, levitating, charging at him. But the thing is...")#intense music
    time.sleep(3)
    print("A place were time does not exist, both of you have formed another portal however, this is different... This is a portal to a parallel universe...")
    time.sleep(2)
    print("")
    print("As you enter this place, you remember this exact moment in the past... It is where you began... It is where this all started...")
    time.sleep(1)
    print("It only then hits you that a time loop has been created...")
    print("You see yourself attacking. Right now, you have the opportunity to intervene with the past in which a new future will be created and who knows what might happen...")
    parallel_universe = input("Do you want to? Yes or No: ").upper()
    if parallel_universe == "YES":
        print("Find out what happens in Chapter 2! Release date: 2021")
        
    elif parallel_universe == "NO":
        print("Find out what happens in Chapter 2! Release date: 2021")

    else:
        print("Invalid choice")

  

#Linking back to what would happen if the player chose to be a villain (Thanos)

#List main components within Thanos story 
thanos_story = ["Infinity Gauntlet","Avengers", "feel someone tugging your gauntlet"]
infinity_stones = ["The Space Stone (blue)", "The Reality Stone (red)", "The Power Stone (purple)", "The Mind Stone (yellow)", "The Time Stone (green)", "The Soul Stone (orange)"]

def thanos():
    print("")
    print("As simple as it may sound, all you have to do is defeat the good guys")
    time.sleep(1)
    print("")
    time.sleep(2)

    print("Welcome! You are currently standing in the scorching, blazing heat. It is 50°C and it is expected to rise even higher later in the day")#decribing match environment
    time.sleep(1)
    print("The sky is clear blue glass. All you can see are the trillions and millions of sand grains leading nowhere to be known - an endless path.'")#decribing match environment
    print("")
    time.sleep(2)
    print(f"Regardless of where you are, all that matters is that you have your {thanos_story[0]} and it obtains all the infinity stones")#insert tense music
    time.sleep(1)
    print(f"There are six of them: {infinity_stones[0]}, {infinity_stones[1]}, {infinity_stones[2]}, {infinity_stones[3]}, {infinity_stones[4]} and {infinity_stones[5]}.")
    print("Each of them posses different powers...")
    print("")
    time.sleep(2)
    print(f"\u001b[34m{infinity_stones[0]}: manipulates space, teleportation")
    time.sleep(1)
    print(f"\u001b[31m{infinity_stones[1]}: ability to alter reality, tranform matter to dark matter")
    time.sleep(1)
    print(f"\u001b[35m{infinity_stones[2]}: manipulate energy, enhance strength and durability")
    time.sleep(1)
    print(f"\u001b[33m{infinity_stones[3]}: telepathy, mind control")
    time.sleep(1)
    print(f"\u001b[32m{infinity_stones[4]}: manipulate time, create time loop")
    time.sleep(1)
    print(f"\u001b[31;1m{infinity_stones[5]}: manipulate the living and the dead, steals soul")
    print("")
    print(f"\u001b[37mSince you have all the stones on your golden gauntlet, you wield unlimited power! MWAHAHAHAHA!!!!!")#evil music inserted (later phase)
    time.sleep(2.5)
    thanos_first_question()

def thanos_first_question():
    print("")
    print("")
    print(f"You suddenly {thanos_story[2]}")

    print("""Quickly, what do you do?
    A. Snap your fingers and all humanity will be erased
    B. Use your other hand to knock whoever it and pull your arm away strongly """)
    first_attack_thanos_input = input("You... ").upper()

    if first_attack_thanos_input == "A":
        print("Only what remains is you...You will age alone and be lonely forever. No where to go... No one to see... You have even erased your loved ones. Did you think about that?")
        restart_thanos = input("Retry? Yes or No: ").upper()
        if restart_thanos == "YES":
            thanos_first_question()
        elif restart_thanos == "NO":
            print("AWWWWEE. It was just the beginning. See you next time then")
        else:
            print("Invalid choice")


    elif first_attack_thanos_input == "B":
        first_attack_thanos()

    else:
        print("Invalid")
        restart_thanos_1 = input("Retry? Yes or No: ").upper()
        if restart_thanos_1 == "YES":
            thanos_first_question()
        elif restart_thanos_1 == "NO":
            print("AWWWWEE. It was just the beginning. See you next time then")
        else:
            print("Invalid choice")

#What would happen if player chooses to shake their hand
def first_attack_thanos():
    print("")
    print("Phew! Good choice. You could have erased your loved ones. Either way, you notice that the Avengers have assembled. It should be easy peasy")
    print("You now see, both Iron Man and Docter Strange charging towards youuuu!")
    print("""Who do you want to battle?
    A. Iron Man
    B. Doctor Strange""")
    thanos_battle = input("A or B: ").upper()

    if thanos_battle == "A":
        iron_man_in_thanos()

    elif thanos_battle == "B":
        doctor_strange_in_battle()

#What would happen if player chooses to fight Iron Man          
def iron_man_in_thanos():
    print("You see him charging at you, all geared up.")
    print("")
    print("But the thing is, it isn't only him, it is literally every single Avenger!")
    print("""What are you going to do?
    A. Stand there and let them try
    B. Use the mind stone  to control their brain""")

    im_ds_thanos = input("What do you?: ").upper()
    if im_ds_thanos == "A":
        power_stone_action() 
                 
    elif im_ds_thanos == "B":
        print("You manipulate their minds to fight each other MWAHAHAHA!!")
        print("You are looking at Iron Man and are planning on huddling everyone together. You see everyone all charging at each other")
        print("You then use spidermans web shooters to wrap them all up in one place, in which they cannot escape")
        print("Isn't this ammusing? MWAHAHAHA")
        time.sleep(2)
        print("Well, wasn't that fun")
        time.sleep(1)
        print("YOU WON!") 

    else:
        print("Invalid choice")


#What would happen if player chooses to fight Doctor Strange
def doctor_strange_in_battle():
    print("Suddenly you see him swirling his hands agile, in a circular motion")
    print("""What do you do?
    A. Use the Space Time
    B. Wait and see what happens """)
    doctor_strange_1 = input("You... ").upper()

    if doctor_strange_1 == "A":
        print("""Where do you want to teleport to? 
    A. Back in time
    B. Into the future""")
        ds_time = input("You... ").upper()
        if ds_time == "A":
            print("Find out what happens in Chapter 2! Release date: 2021")
        
        elif ds_time == "B":
            print("Find out what happens in Chapter 2! Release date: 2021")

        else:
            print("Invalid choice")

    elif doctor_strange_1 == "B":
                 portal()


#What would happen if player chooses to stand there
def power_stone_action():
    print("As you see them coming at you, all you need to do is to activate the power stone which can wipe out everyone")
    power_stone_use = input("Wanna follow through? Yes or No: ").upper()

    if power_stone_use == "YES":
        print("Good choice. You slam your fist hard, down towards the ground. You have created an earthquake BAHAHAHA")
        print("With tremendous power, wind is also generated pushing everyone to the floor, collapsing all at once")
        print("No one can defeat you now. MWAHAHAHA!!")
        time.sleep(1)
        print("YOU WON!!")

    elif power_stone_use== "NO":
            print("What were you planning on doing then?")
    else:
        print("Invalid")


intro ()

