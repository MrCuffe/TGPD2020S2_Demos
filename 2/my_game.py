# Escape the Desert
# A Python interactive story game

# Author: Anureet

# Imports a module to add pause
import time
import sys
import time
from time import sleep

# Possible responses from player
# If statement will check this for player choice
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

# Faces for player
# Will be used before conversations to show emotions
character_faces = [ "⚆_⚆","(ʘᗩʘ')", "(∩╹o╹∩)","ε=٩(●❛ö❛)۶","(x⸑x)","(◕_◕)=ε/̵͇̿̿/'''̿'''̿ ̿"]

# Villager Faces
james_face = 'ಠoಠ'
old_lady_face = '(✿´‿`)'

# Scientist Faces
robert_face = '( •̀ᴗ•́ )'

# Player name
name = input("What is your name: ")
print (f"Hey {name}!")

# Introduction. Beginning information
def intro():
    print ("~~~~~~~~~~ Escape the Desert ~~~~~~~~~~") # Title
    print ("") # Gap
    # Description for player to understand game.
    print ("You groan as you wake up in the middle of a dry and arid desert. "
           "The last thing you remember is blacking out at a party. You look around and see nothing "
           "but sand, tall rocks and cacti.")
    time.sleep(3)
    print ("Suddenly, the ground starts to rumble. You get up from you laying position "
           "on the ground and slowly walk backwards. The rumbling gets louder and louder "
           "until suddenly, a giant centipede amerges from the ground.")
    print ("") # Gap
    print (f"{character_faces[1]} : What should I do?") # Player's face/thoughts
    print (" ") # Gap
    print("""    A. Hide behind a rock
    B. Lie down and wait to be eaten
    C. Run""") # Printing the possible options for the player
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        hide_behind_rock() # Will begin to run the next scene according to player choice
    elif choice in answer_B:
        lie_down()
    elif choice in answer_C:
        run()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# Hiding behind the rock option
def hide_behind_rock():
    print ("") # Gap
    print ("You run to the tall rock and hide behind it. From years of laziness "
           "and disregarding your health, you run out of breath. The centipede hears you "
           "puffing loudly.")
    time.sleep(1)
    print ("It slithers towards you.")
    print (" ") # Gap
    print (f"{character_faces[3]} : What should I do?") # Player's face/thoughts
    print (" ") # Gap
    print("""    A. Throw a rock
    B. Dig in the sand
    C. Run""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        throw_rock()
    elif choice in answer_B:
        sand()
    elif choice in answer_C:
        run()
    else:
        else_option()

def else_option():
    print ("You failed to make a choice! Due to your indecisiveness, you met your death!")
    time.sleep(1)
    print (" \nWelp. "
           "\n ~~ You died! ~~")

# Lying down on sand option
# Death ending
def lie_down():
    print ("") # Gap
    print ("You decide to lie down and accept your death, surrendering to the centipede."
           "It stares at you and acknowledges your wish.")
    print ("") # Gap
    print (f"{character_faces[4]}")
    print ("") # Gap
    print ("Welp.")
    print ("~~ You died! ~~")

# Running option
def run():
    print ("") # Gap
    print("You run in a random direction. With each step you take, it gets "
          "harder and harder to keep going. You stop when you see "
          "two pathways. The first path leads to an abandoned village and the "
          "second to a temple.")
    time.sleep(3)
    print ("") # Gap
    print (f"{character_faces[0]} : Which path should I take?")
    print (" ") #Gap
    print("""    A. First path
    B. Second path
    C. Lie down and wait to be eaten""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        village()
    elif choice in answer_B:
        temple()
    elif choice in answer_C:
        lie_down()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# Throwing a rock at centipede option
def throw_rock():
    print ("") # Gap
    print ("You grab a rock from the ground. It feels heavy in your hands."
           "You throw the rock at the centipede. It stands in front of you, confused.")
    time.sleep(1)
    print ("") # Gap
    print(f"{character_faces[0]} : What should I do now?")
    print ("") # Gap
    print("""    A. Lie down and wait to be eaten
    B. Dig in the sand
    C. Run""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        lie_down()
    elif choice in answer_B:
        sand()
    elif choice in answer_C:
        run()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# Digging in the sand option
def sand():
    print ("") # Gap
    print ("You dig in the sand. It is very hot and your fingers are burning."
           "You keep digging and find a...")
    time.sleep(2)
    print ("Gun!")
    time.sleep(1)
    print ("The centipede slithers towards you.")
    print ("") # Gap
    print (f"{character_faces[2]} : What should I do now?")
    print ("") # Gap
    print("""    A. Shoot the centipede
    B. Run
    C. Lie down and wait to be eaten""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        print ("") # Gap
        print (f"{character_faces[5]} : Take that!")
        print ("") # Gap
        print ("You shoot the centipede.")
        print ("It lets out a cry and falls to the ground. A wave of relief "
               "washes over you.")
        time.sleep(1)
        print ("") # Gap
        print ("~~ You won! ~~")
    elif choice in answer_B: 
        run()
    elif choice in answer_C:
        lie_down()
    else: # If the player does not pick a stated option, then they will automatically die
        print ("You failed to make a choice! The centipede snuck up on you "
               "and gobbled you up.")
        time.sleep(1)
        print (" \nWelp. "
           "\n ~~ You died! ~~")

# If the player decides to run to the village
def village():
    print("") # Gap
    print("You run to the abandoned village. The run is long and difficult. With each step, "
          "the distance seems to get further and further. Eventually, you make it to the village. "
          "You puff loudly and don't hear the person creeping up behind you. Suddenly, a person "
          "has you in a lock! You try to set yourself free but are unable to.")
    print ("") # Gap
    time.sleep(1)
    print (f"James {james_face}: Who are you?") # Introduction of new characters
    time.sleep(1)
    print ("") # Gap
    print (f"    A. {name}") # F string to input player name
    print ("    B. Your mum")
    print ("    C. I don't know")
    print ("") # Gap
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        crystal_introduction_village()
    elif choice in answer_B:
        tied_up()
    elif choice in answer_C:
        crystal_introduction_village()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# Introduction of crystal in the village for player
def crystal_introduction_village():
    print ("The man cautiously lets you go, never taking his eyes off you. You slowly "
           "move away from him. He looks to be about the same age as you, if not a year or "
           "two older.")
    time.sleep(1)
    print ("") # Gap
    print (f" {character_faces[0]}: If you don't mind me asking, who are you?")
    time.sleep(1)
    print ("") # Gap
    print(f"James {james_face}: I'm James. What are you doing here?")
    time.sleep(1)
    print ("") # Gap
    print (f"{character_faces[0]}: I- I don't know. I was running away from a HUGE centipede "
           "and then I found myself here...")
    time.sleep(1)
    print ("") # Gap
    time.sleep(1)
    print ("James looks at weirdly. He seems to be deep in thought and appears to be a little "
           "surprised. You look around and see more villagers coming towards you. Then, an old "
           "woman walks up to you and asks you to follow her. Out of fear, you decide to do as "
           "she says. James stays nearby, watching you intently.")
    time.sleep(2)
    print ("") # Gap
    print (f"Old Lady {old_lady_face}: Come here dear child.")
    time.sleep(1)
    print ("") # Gap
    print (f"{character_faces[0]}: What are you holding?")
    time.sleep(1)
    print ("") # Gap
    print (f"Old Lady {old_lady_face}: This is a crystal. My dear, if you eat this, you will have "
           "great power. You can save this cursed village. Our village is being hunted by the "
           "scientists. They're killing all of us for 'scientific research'. You can save all of us.")
    # Above is the villager description of crystal
    time.sleep(2)
    print ("") # Gap
    print ("The feeble old lady sounded weak and started coughing loudly. You look at the crystal. It "
           "shimmers in the sunlight but something seemed different about it. You could somehow "
           "feel a sort of energy coming out of it. Eat the crystal? That seems absurd! But what "
           "about how James had you in a lock? They were clearly worried about you suddenly coming "
           "to their little village.")
    time.sleep(2)
    print ("") # Gap
    print("""    A. I will eat the crystal
    B. You're crazy!
    C. No thanks. I'm going to leave this crazy village""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        eat_crystal_village()
    elif choice in answer_B:
        tied_up()
    elif choice in answer_C:
        temple()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# If the player chooses to eat the crystal in the village
def eat_crystal_village():
    print ("After you decide to eat the crystal and assist the villagers, the Old Lady hands you the "
           "crystal. It begins to shine brightly in your hands. You close your eyes and swallow the little "
           "crystal is one large gulp. Suddenly, you feel a rush of power. You feel it in your hands, "
           "mind, your bones.")
    print ("") # Gap
    time.sleep(3)
    print (f"Old Lady {old_lady_face}: Yes! He is the chosen one. We are saved!")
    print ("") # Gap
    time.sleep(1)
    print ("You put your hand out and a holy light emits from it. It appears divine. More than than "
           "anything you've ever seen. You snap your fingers and the small bush beside you sets on "
           "fire. You have superpowers!")
    print ("") # Gap
    time.sleep(2)
    print (f"James {james_face}: Okay. Now you need to train.")
    print ("") # Gap
    time.sleep(1)
    print ("James is asking you to train. Will you train with him? Remember, if you do not train with "
           "him, than you will lose his trust.")
    print ("") # Gap
    time.sleep(3)
    print("""    A. Train with James.
    B. Yeah, no thanks. I'm leaving.
    C. I don't need training.""")
    print ("") # Gap
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
         training_village()
    elif choice in answer_B:
        temple()
    elif choice in answer_C:
        scientist_attack()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# If the player decides to train with James
def training_village():
    print ("") # Gap
    print ("You spend a day with James, training to improve your abilities. The more you train, the "
           "easier it gets for you to control your powers. You start to realise that you can do more "
           "than what you initially thought")
    print ("") # Gap
    print ("Do you wish to train again?")
    print("""    A. Train again
    B. Stop training""")
    choice = input("You will: ") # Player's choice
    while choice in answer_A:
        print ("") # Gap
        print ("*Training* "
               "*Training* "
               "*Training*")
        print ("") # Gap
        choice = input("Again? A for yes and B for no: ") # Player's choice
    else:
        if choice in answer_B:
            points_village()

# Player gets to talk to villagers and understand who they are
def points_village():
    print ("") # Gap
    print (f"James {james_face}: So, why do you want to help this village?")
    print ("") # Gap
    print (f"{character_faces[2]}: What do you mean?")
    print ("") # Gap
    print (f"James {james_face}: I mean, not that I don't appreciate it but you don't even know us. Why?")
    print ("") # Gap
    print("""    A. I just want to help out.
    B. I can have so much power
    C. I just felt like it was what I had to do""")
    choice = input("You will: ") # Player's choice
    print (f"James {james_face}: Interesting. I didn't expect that. We should... Um... Get some rest. I'm going to go talk to "
           "Nanna. See you tomorrow.")
    print ("") # Gap
    print (f"Old Lady {old_lady_face}: Hello, {name}. How has your day been?")
    print ("") # Gap
    print (f"{character_faces[2]}: It has been eventful.")
    print ("") # Gap
    print (f"Old Lady {old_lady_face}: Well I hope you've liked what you've seen.")
    print("""    A. It has been... eventful
    B. It makes me feel like I have a meaning
    C. I just wanna go home""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        scientist_attack()
    elif choice in answer_B:
        scientist_attack()
    elif choice in answer_C:
        scientist_attack()

# When the player is ready, they can defend the village from the scientists
# There is a betrayal option
def scientist_attack():
    print ("") # Gap
    print ("You hear a rumbling from the ground but this type of rumbling is different. This rumbling "
           "is caused by people. The scientists! They're attacking the village. You need to protect it. "
           "Everyone starts to get ready for war.")
    print ("") # Gap
    print ("You know two spells.")
    print("""    A. Fireball
    B. Thunderstorm
    C. Betray""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to interpret player choice
        fireball()
    elif choice in answer_B:
        thunderstorm()
    elif choice in answer_C:
        betray()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# If the player chooses to use fireball
def fireball():
    t = 3 # The number of seconds for countdown
    print ("") # Gap
    print ("You hold your hands out and count outloud.")
    print ("") # Gap
    while t: # Loop to create timer
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) # Format of the timer
        print(timer, end="\r") 
        time.sleep(1) # To give interval between each print
        t -= 1 # Takes away 1 from t, hence, creating seconds
    print("Fireball!!")
    winner() # Takes player to winner ending

# If the player chooses to use thunderstorm
def thunderstorm():
    t = 3 # The number of seconds for countdown
    print ("") # Gap
    print ("You hold your hands out and count outloud.")
    print ("") # Gap
    while t: # Loop to create timer
        mins, secs = divmod(t, 60)  # Format of the timer
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) # To give interval between each print
        t -= 1 # Takes away 1 from t, hence, creating seconds
    print("Thunderstorm!!")
    winner() # Takes player to winner ending

# If the player decides to betray
def betray():
    print ("Just before you're about to cast a spell, stop and magically lift yourself into the air."
           "Everyone stares at you in shock. Your comrades look at you worridly. They don't know what "
           "you are about to you.")
    print ("") # Gap
    print (f"{character_faces[0]}: Hello everyone. I have something to say. I am DONE working for you "
           "and being a pawn in your little war. In fact, I don't even care about this war. From now on "
           "you are MY workers. If anyone steps out of line, death. If anyone disobeys, death. If anyone "
           "even thinks about running away, you know it, death.")
    print ("") # Gap
    print ("Everyone looks at you. You can see the fear in their eyes. They bow down. You are now the "
           "ruler. Everyone bows to you.")

# Getting tied up by villagers
# Death ending
def tied_up():
    print ("") # Gap
    print ("After hearing your reply, the man ties you to a tree. You try to escape but he is too "
           "strong. All your cries were disregarded. More villagers come and begin dancing around you. "
           "You hear a familiar rumbling and realise that they are summoning the centipede. The "
           "centipede slithers up to you and eats you in one bite before you can even react.")
    print ("") # Gap
    print (f"{character_faces[4]}")
    print ("") # Gap
    print ("Welp.")
    print ("~~ You died! ~~") # Death ending.

# Winner ending
# Achived after war from both scientist and villager perspective
def winner():
    print ("You opponents surrender after getting a taste of you powers. They do not have the courage "
           "to keep fighting. Your allies commend you for your help.")
    print ("") # Gap
    print ("You live in the village for a while and then find out who you really are and return to your "
           "family")

# If player chooses temple
def temple():
    print ("") # Gap
    print ("You run as fast as you can towards the temple. You don't dare look back to see where the "
           "centipede is. After what feels like a long time, you finally reach the temple. Walking into "
           "the temple, you realise that it isn't dusty anywhere. Someone or something lives here! "
           "You get distracted and see numbers written on the wall; 21360. "
           "Before you have the chance to figure out what they mean, someone hits you in the head.")
    # The print statement above has the first numnbers that the player needs to remember in order to progress
    time.sleep(2)
    print ("You awake tied to a chair. There is a person in a labcoat staring down at you. You try to "
          "free yourself but fail.")
    print ("") # Gap
    time.sleep(1)
    print (f"Robert {robert_face}: Well, well, well. What do we have here?")
    time.sleep(1)
    print ("") # Gap
    print (f"{character_faces[1]}: I don't mean any harm. Please let me go. I just woke up in the "
           "desert and a HUGE centipede started chasing me. I didn't have a choice.")
    time.sleep(1)
    print ("") # Gap
    print (f"Robert {robert_face}: Centipede... Interesting. Say, have you heard about a crystal?")
    time.sleep(1)
    print ("") # Gap
    time.sleep(1)
    print("""    A. Yes
    B. No
    C. Can you just let me go?""")
    print ("") # Gap
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        crystal_choice_temple()
    elif choice in answer_B:
        crystal_introduction_temple()
    elif choice in answer_C:
        angry_scientist()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

def crystal_choice_temple():
    print ("") # Gap
    print ("Well then, I'm sure you won't mind eating the crystal for me. You should know the power it "
           "holds.")
    print ("") # Gap
    print (f"{character_faces[2]}: Should I eat the crytal?")
    print ("") # Gap
    print("""    A. Yes
    B. No
    C. Can you just let me go?""")
    print ("") # Gap
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        eat_crystal_temple()
    elif choice in answer_B:
        angry_scientist()
    elif choice in answer_C:
        angry_scientist()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# If the player chooses to say "Can you just let me go?", then this will run.
# This leads to the 'Escape' Option.
def angry_scientist():
    print ("") # Gap
    print (f"Robert {robert_face}: Why must you be so stubborn?")
    print ("") # Gap
    print (f"{character_faces[2]}: ...")
    print ("") # Gap
    print (f"Robert {robert_face}: Fine then. You can stay here and rot!")
    print ("") # Gap
    print ("Robert leaves you in the room and you are engulfed by darkness. There is enough light for you "
           "barely see things. Somehow, you manage to free yourself from the robes binding you. Once you "
           "are free, you run to the door. It is asking for a pin code to unlock. Maybe the numbers you "
           "saw on the temple outside will work")
    pin_escape()

# Scientist introduction of the crystal
def crystal_introduction_temple():
    print ("") # Gap
    print (f"Robert {robert_face}: The crystal is the most powerful creation in this world. There is two of "
           "them in the entire world. However, only one person is capable of wielding them. And I "
           "believe that person is you.")
    time.sleep(1)
    print ("") # Gap
    print (f"{character_faces[2]}: I think you have the wrong person. There is no way I am someone that "
           "special. I don't remember much but there's no way it's me.")
    time.sleep(1)
    print ("") # Gap
    print (f"Robert {robert_face}: But think about what you could do with this power. You could rule over the "
           "entire world! Save people. The possibilities are endless.")
    time.sleep(1)
    print ("") # Gap
    print (f"{character_faces[2]}: That does sound a little tempted. I could do anything I've ever "
           "wanted. I could find out who I am.")
    time.sleep(1)
    print ("") # Gap
    print ("You look at the man in front of you, thinking about what he just told you. A crystal that "
           "could let you do anything you've ever wanted. But how? How could something this "
           "supernatural even exist? Should you trust this scientist?")
    time.sleep(1)
    print("""    A. Let's go see that crystal
    B. No. You're crazy
    C. Just let me go. I want to be as far away from you as possible""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        eat_crystal_temple ()
    elif choice in answer_B:
        tied_up()
    elif choice in answer_C:
        angry_scientist()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

# If the player decides to eat the crystal in the temple
def eat_crystal_temple():
    print ("") # Gap
    print ("Robert unties you from the chair and helps you get up. He puts a small crystal in your hand. "
           "It starts to glow brighter as soon as it's in your hand. You close you eyes and swallow it in "
           "one gulp. You begin to feel a divine energy in your body.")
    time.sleep(3)
    print ("") # Gap
    print (f"Robert {robert_face}: Yes, yes, yes. You have the power! We can begin training now.")
    time.sleep(1)
    print ("") # Gap
    print ("Robert is asking you to train with him. WIll you do this? Remember, making choices that are "
           "in line with characters will allow you to make more exlcusive choices.")
    time.sleep(1)
    print ("") # Gap
    print("""    A. Let's train!
    B. Yeah, nah. I'm gonna leave.
    C. I don't need training.""")
    time.sleep(1)
    print ("") # Gap
    choice = input("You will: ") # Player's choice
    if choice in answer_A: # If statement to act upon the player's choice
        training_temple()
    elif choice in answer_B:
        village()
    elif choice in answer_C:
        attack_village()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

def training_temple():
    print ("") # Gap
    print ("Robert takes you into an advanced training facility and begins training you. You learn new "
           "spells and find that you really can do anything you want. You learn defensive and offensive "
           "spells.")
    points_temple()

def pin_escape():
    replay = 1 # The number of times it replays
    lives = 3 # The number of lives/tries for pin
    pin = "21360" # Pin needed to be entered
    while replay == 1: # Loop for the pin to be entered again    
        guesses = 1 # Variable set for number of guesses
        while guesses <= lives:
            guess = str( input("Pin: ") ) # String to allow user input
            if guess == "21360":
                print("Pin Accepted.")
                escape()
                break
            else:
                print("Incorrect Pin.")
            guesses = guesses + 1 # Adds a number to guesses
        if guesses > lives:
            print("You were not able to remember the code. The scientist never came back to save you."
                  "You died from starvation.")
            print ("") # Gap
            print ("Welp.")
            print ("~~ You died! ~~") # Death ending.
            break
        break # Breaks the loop

# If the player is able to remember pin
# Ending
def escape():
    print ("You run out of the room and try to find your way out of the temple. There are a lot of hall"
           "ways. You finally find your way out of the temple. Once you are out, you run in a direction "
           "until you reach civilisation.")
    print ("You promise to never speak about the crystal, village and temple again and live a normal life")

# Scientist perspective of war
def attack_village():
    print ("The scientists tell you to get into a car. The car rides through the desert and you finally "
           "reach the village. All the villagers look at you, scared of what you can do.")
    print ("") # Gap
    print ("You know two spells.")
    print("""    A. Fireball
    B. Thunderstorm
    C. Betray""")
    choice = input("You will: ") # Player's choice
    if choice in answer_A:
        fireball()
    elif choice in answer_B:
        thunderstorm()
    elif choice in answer_C:
        betray()
    else: # If the player does not pick a stated option, then they will automatically die
        else_option()

intro()
