# Author: Malavika Harish
# Name of the game: The Adventures of Riri the Stickman

# PLEASE RUN MODULE FROM HERE
# WHEN PROGRAM IS OPENED DIRECTLY, PLAYER IS NOT ABLE TO INPUT

# The following are imported to allow particular features to be run
import sys
import time
import os
import winsound



# def stores infomation in a variable
# for loops loop an instruction
# char stands for characters and is used so that the code can be run on every character
# .write() prints out the characters in story
# .flush() clears the internal buffer
# time.sleep() just pauses the program for the given amount of time

def typewriter(story):
    for char in story:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

# os.system("cls") clears the screen
os.system("cls")

# The following function allows to import sound
# SND_ASYNC allows to let the sound play in the background
# SND_LOOP infinitely loops the track

winsound.PlaySound("light_wind.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

# The following is what pops up first after the player opens the application.
# It asks whether the player would like to play the game, however, the only two options are yes and yes.
# If the player inputs anything but yes, they have to keep answering the question until they say yes.

# Was planning to add exit and pause button throughout the game

# input function allows player to input something

story =(" ~The Adventures of Riri the Stickman~ ")
typewriter(story)

player_input = input ("""


Hello, fellow-being! How would you like to join Riri on an adventure? (yes/yes)
Input your answer here: """)


# answer.lower() converts uppercase to lowercase.
# .strip() gets rid of spaces before and after the word
# While loop -> loops function until it meets the condition

while player_input.lower().strip() != "yes":
    player_input = input("""
That is clearly not one of the options. Let's try again!

Would you like to join Riri on an adventure? (yes/yes)
Input your answer here: """)

#---------------------------------Section 1---------------------------------------
    
# The game officially starts here
# Else is the outcome when the while loop meets it's condition

# This is the start of the story

else:
    story = ("""
Awesome!

Once upon a time, there lived an extremely attractive stick figure named
Riri. With a heart made of nothing but pure innocence and love, Riri was
loved by everyone he met. Except for his ex-wife that is, who left him
for another stickman, a rather unattractive one I should mention.

One faithful day, Riri goes to fetch some apples and oranges from his
local forest. On his way back, however, he is hit on the head by an
object and as a result, instantly faints.

""")
    typewriter(story)

# Changes background audio as Riri is now in a wet cave

winsound.PlaySound("cave_dripping.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""
Riri wakes up inside an unfamiliar place. The ground was rocky, wet, and
slimy. He looks around to see three hungry cavemen, devouring pieces of
flesh and bones, as well as the apples and oranges that Riri had collected.
Suddenly he hears an unfamiliar voice in his head.

""")
typewriter(story)

n = (input("Input something weird: "))

print ("""
The voice in his head says:""")
print (repr(n))

story = ("""
Riri flinches as another voice booms inside of the cave. It says:

╔══════════════════════════════════ஓ๑o๑ஓ══════════════════════════════════╗

“Greetings, fellow stickman. I am the soul and spirit of the stickman that 
the cavemen are currently devouring. I suggest that you escape the cave
before the cavemen finish eating. The voice in your head has the power 
to control your actions. You must communicate well with the voice to make 
collective decisions. Farewell.”

╚══════════════════════════════════ஓ๑o๑ஓ══════════════════════════════════╝

The cavemen just finish chewing the last of the bones. They jerk their
head towards Riri. What should Riri do?

""")
typewriter(story)

# This is the first time in the game where the player makes a big decision for Riri
# Depending on which option the player chooses, the story will change

a = "Help the cavemen to hunt for more food"
b = "Fight them!"
c = "RUN!!"

print (f"a: {a}")
print (f"b: {b}")
print (f"c: {c}")
print ( )

# Setting the input into a variable
# This helps while using if, elif, and else statements

choice = (input("Input your option here: ").lower().strip())

# If loops are to check if a function meets a certain condition
if choice == "a":
    story = ("""
The cavemen are a little too hungry today. They have some steamed Riri
meat for lunch.
""")
    typewriter(story)
    # sys.exit() exits the system
    sys.exit()
    
# Was planning to add "Choose another option" and "Exit game" button

# Elif function is read when the if is read, and the condition isn't met

elif choice == "b":
    story = ("""
That was quite dumb of you! Poor Riri is only a mere stickman and was
snapped in half by one of the cavemen. At least the cavemen are happy;
they are having Riri for lunch.
""")
    typewriter(story)
    sys.exit()

# Was plannig to add "Choose another option" and "Exit game" button

# Was planning to modify this section in case the player inputs something other than "c"

else:
    story = ("""
Thank goodness those cavemen weren't in top shape! With his bag, Riri is
bolting towards the entrance of the cave. Just as Riri is about to escape,
The cave collapses, blocking the entrance. The cavemen continue to run
towards Riri. What should Riri do? 

""")
    typewriter(story)

a = "Befriend the cavemen"
b = "Squish through a tiny gap in the middle of the pile of rocks."

print (f"a: {a}")
print (f"b: {b}")
print ( )
choice = (input("Input your option here: "))

if choice == "a":
    story = ("""
Riri's innocence charms the cavemen, and they became the best of friends.

                        ~ 7 years later~

Riri is now a caveman. He spends the rest of his life eating the flesh
and bones of all the stickmen the find. It was a beautiful friendship.

The end
""")
    typewriter(story)
    sys.exit()
    
# Was planning to add "Choose another option" and "Retry from the beginning" buttons

else:
    # Changes audio as Riri is now outside the cave
    winsound.PlaySound("light_wind.wav",winsound.SND_ASYNC + winsound.SND_LOOP)
    story = ("""
Good choice! As Riri is quite a skinny stick figure, it was easy for him
to fit through. The chubby cavemen groan with anger as they claw at the
gap.

Riri keeps running and running until he loses sight of the cave. But it
seems he ran a bit too far. Which direction should Riri go?
""")
    typewriter(story)

choice = (input("Input your option here: ")).lower().strip()
    
# The following 2 lines of code are called lists
# They store multiple pieces of data(?) inside one variable
# This will make it easier to code this section


directions = ["west","north","east","south"]
sides = ["right","left"]

# != means not equal to
# While loops loop forever until a condition is met
# 'in' helps to see whether something is inside a list

while choice != "stop":
    if choice in directions:
        story = ("""
Unfortunately, Riri doesn't have a compass, or a good sense of direction
Perhaps give him a one-word intruction instead. """)
        typewriter(story)
        choice = (input("Enter a one word instruction: "))

    elif choice in sides:
        story = ("""
Riri had not developed the skill of distinguishing between his right and left
yet. Perhaps give him a one-word instruction instead. """)
        typewriter(story)
        choice = (input("Enter a one word instruction: "))

    elif choice not in directions or sides:
        story = ("I cannot recognize that direction")
        typewriter(story)
        choice = (input("Enter a one word instruction: "))

else:
    story = ("""
Good job! You just saved Riri wandering further into the forest.

Riri's little tummy grumbles loud. That's when he realises he hasn't
eaten all day. He looks around the area for a little while, and he spots
some purple mushrooms on the ground.

a: Eat it!
b: Don't eat it!

What should he do?
""")
    typewriter(story)

choice = (input("Input your option here: "))

if choice.lower().strip() == "b":
    print ("""
Turns out Riri's body cells cannot survive without food for over 12 hours!
Riri falls to his death.
""")
    sys.exit()
# Was planning to add "Choose another option" and "Exit game" button

else:
    story = ("""
Riri gathers the mushrooms and stuffs some in his bag just in case he gets
hungry again. As Riri eats the mushroom he starts to feel weird. He suddenly 
feels a hand on his shoulder. He turns his head very slowly to see a glowing,
semi-transparent figure floating in the air.

"AAAAAHHHH IT'S A GHOST!" Riri screams.

"Don't worry, fellow stick man! I intend to do you no harm! I am the spirit
and soul of a being who was once alive. I believe you gained the ability to
communicate with me by eating those purple mushrooms." says the spirit.

"I've wandered these forests for decades now." he continues. "You seem like
you have lost your way back."

"That's right, spirit. Do you happen to know the way out of this forest?"
Riri asks.

"Sure do! Follow my lead!"

Riri and the spirit continue their journey through the forest, chatting and
sharing stories heartily. """)
typewriter(story)

# Changes audio as Riri is now near a water body
winsound.PlaySound("river.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""

As they arrive at a river, the spirit starts fading. "You are fading into
the air, spirit!" Riri exclaims.

"I presume that the effects of those mushrooms last a rather short while.
I will tell you the rest of the way. You can either cross the river or somehow 
make your way down the waterfa-

The spirit had completely faded, along with his voice. Riri's eyes whelmed
with tears. He will never forget the first paranormal friend, nor will he
forget their memories with him.

He remembers the spirit’s words ‘cross the river’ and ‘make your way 
down the waterfall’. He decides to cross the river like a sensible man.
He sees a boat up the riverbank, a bridge, some lily pads,  and some 
blue crocodiles. What should Riri do?

""")
typewriter(story)

a = "Cross the river using the boat"
b = "Cross the river using the bridge"
c = "Cross the bridge by jumping on the lilypads"
d = "Attempt to communicate to the blue crocodiles to help you cross"

print (f"a: {a}")
print (f"b: {b}")
print (f"c: {c}")
print (f"d: {d}")
choice = (input("Input your option here: "))

if choice == "a":
    story = ("""
The water current was too strong! Riri falls off of the waterfall and
dies.""")
    typewriter(story)
    sys.exit()
# Was planning to add "Choose another option" and "Exit game" button

elif choice == "c":
    story = ("""
It was all fine until Riri got halfway through the river, and then he lost
balance and fell into the river, taking him to the waterfall. You can
already guess what happens next.
""")
    typewriter(story)
    sys.exit()
# Was planning to add "Choose another option" and "Exit game" button

#-----------------------------------Start of Alternative 1-----------------------------
elif choice == "b":
    story = ("""
The bridge breaks and Riri falls into the river. The strong water 
current carries Riri towards the waterfall at the end of the river. He
sees roots of a tree stick out through the side of the river and weirdly 
enough, there is a bag on it. Should Riri grab onto the roots?(yes/no)""")
    typewriter(story)

    choice = (input("Input you answer here: "))
    
    if choice == "no":
        story = ("You're such an idiot. Riri falls off of the waterfall and dies.")
        typewriter(story)
        
        sys.exit()
    
    elif choice == "yes":
        story = ("""
Well, that's what anyone would do. Riri grabs on tight, but the root
snaps. Riri manages to get ahold of the bag. In hopes of having something
useful inside, Riri opens the bag. Just as Riri is about to fall to his
death, a hand grabs him and pulls him to the bank. Riri looks up to see a
wizard??

"A wizard?"

"That's right my child. I am a wizard. You have unleashed me from my prison
and as a reward, I will grant you a wish. You have three options:

a: "A parachute"
b: "A great sense of direction"
c: "A griffon"
""")
        typewriter(story)
        
        choice = (input("Input your choice here: "))

    if choice == "a":
        story = ("""
Riri wears the parachute to jump off of the waterfall. He jumps and pulls
the string. Turns out the wizard gave him the wrong bag; clothes of all
sorts flew out of the bag. All I can say is welp!
""")
        typewriter(story)
        
        sys.exit()
                 
    elif choice == "b":
        story = ("""
Great, he can navigate his way through the Forrest better now. Unfortunately 
for Riri, there were magnets inside the wizard's 'prison'. Riri's sense of
direction becomes soo messed up that he faints into the river, falling off
of the waterfall.
""")
        typewriter(story)
        
        sys.exit()
# Was planning to add an option for the player to choose another option, or exit game

    elif choice == "c":
        story = ("""
Riri waits for a couple of minutes. 'Where is the Griffon?' he asks.

The wizard smiles and walks away. Riri hears a twig snap. He turns around to
see a figure emerging from the dark. It’s the griffon!

'Hey big guy!' says Riri. The Griffon bobs his head with excitement, and bows
to Riri. One of his wings looks crooked, Riri assumes that it’s broken.

The Griffon makes an affectionate noise. Riri feels bad for him. He looks
like he’s hungry.

What should Riri do?

a: Feed the griffon some purple mushrooms
b: Catch some fish from the river
""")
        
    choice = (input("Input your answer here: "))

    if choice == "b":
        story = ("""
Turns out there weren't any fish in the river. One of the blue crocodiles got
tangled in the fishing line. The crocodiles see Riri a threat and they jump
out  of the river to push him in. He falls to his death at the waterfall.
As for the Griffon, he sat there patiently, hoping  that Riri would jump
out of the river soon.""")
        typewriter(story)
            
        sys.exit()
# Was planning to add an option for the player to choose another option, or exit game

    elif choice == "a":
        # Changes audio as Riri is now away from the water body
        winsound.PlaySound("light_wind.wav",winsound.SND_ASYNC + winsound.SND_LOOP)
        story = ("""
Apparently, purple mushrooms have healing abilities. The Griffon's wing
heals instantly. It jumps around with joy and offers Riri a ride on his back
as a ‘thank you’.

Soon, they are both soaring through the evening sky. The sun had already set,
and the sky was a beautiful hue of pink and orange. Riri sees his village in
the distance. He gestures to the Griffon to go in that direction.

Soon enough, Riri is back home, safe and sound. He and the Griffon lived
happily ever after.



                                            ~The End~
""")
        typewriter(story)
        
        sys.exit()
# Was planning to add an option for the player to play for an alternate ending, or to exit game

#---------------------------------End of Alternative 1------------------------

elif choice == "d":
    story = ("""
Turns out the crocodiles were much nicer than they appeared to be! They
offer Riri a ride on one of their backs, and they cross the river together.
Riri thanks the crocodiles and they splash back into the river.
""")
    typewriter(story)
    
# Change sounds as it is now night time
winsound.PlaySound("night_crickets.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""
The sky had shifted colour to a dark gradient of blue and purple. Stars
started to appear one by one. Riri decides that he would spend the night
under a huge oak tree so that he would be energized for tomorrow’s 
adventures.
""")
typewriter(story)
#-----------------------------End of Section 1-------------------------------
    
#----------------------------Start of Section 2------------------------------

# .upper can change lowercase to uppercase, which could indicate that the reader is screaming

# Changes background audio as it is now morning
winsound.PlaySound("morning_birds.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""
It's a bright and beautiful morning. Turns out Riri is a bit of an oversleeper. You
were stuck in his head the whole night, while watching his absurd dreams and
embarrassing memories along with him.

Wake him up!

""")
typewriter(story)

player_input = (input("Input your morning call here: ")).upper()

story = ("""
The voice in Riri's head screams:""")
typewriter(story)

# repr makes the variable 'printable'
print (repr(player_input))

story = ("""
Riri jerks awake. His eyes were wide open, but he closes them immediately. He
sees a wolf right in front of his face. What should Riri do?

a: Feed it some purple mushrooms
b: Pet the wolf
c: Stay still """)

choice = (input("Input your option here: "))

if choice == "a":
    story = ("""
The wolf takes the mushroom and wanders away. You and Riri let out a sigh
of relief. That's when you see a pack of wolves coming towards you. Let's
just say that Riri was not having the best day. """)
    typewriter(story)
    
    sys.exit()

elif choice == "c":
    story = ("""
Waiting there was no good, as a pack of wolves approach Riri later. Now he
cannot escape. Yes he is only a stickman and a very skinny one, but it was 
enough to feed a couple of wolves. """)
    typewriter(story)
    
    sys.exit()
    
else:
    story = ("""
Turns out that the wolf wasn't a wolf; it was a husky! Riri is incredibly
clueless when it comes to animals. Riri, along with the little husky continue
their adventure together.
""")
    typewriter(story)

winsound.PlaySound("light_wind.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""
A couple of hopeless minutes into their hike, Riri sees someone in the
distance. With a perfect circle face, hair shinier than the hair in shampoo
commercials, and an aura that screams queen, she was more stunning
than anyone that he had ever met in his entire life.

She starts to run towards him.

"Don? Oh my god, DON!!" she screams as she hugs the husky that Riri had
found. "Thank you so much for finding him! I don't know what I would've
done without him!"

"Nah, don’t mention it!" Riri says while blushing.

"Well," the girls start, "my name is Lola. I came here for a hike, and Don
ran away from me. As I ran around searching for him, I got lost. Can you
perhaps help me get back?"

"Ah, my name is Riri! I am also lost, so let's just wander around for a
while and see where we can get to."

The three set off on their journey together. They seemed to click instantly;
they share a lot of similar interests, and they enjoy each other’s company.

After about half an hour of wandering, they reach a temple. In front of the
temple was a berry bush. They decided to take a little break to eat the
berries. As they finish eating, they notice a sign covered in moss that says:""")
typewriter(story)

print ("""
 ---------------------------------------------------------------------
|                                                                     |
|  The Temple of Dhasha                                               |
|                                                                     |
|  On the other side of this temple is a village. You must face       |
|  several challenges to reach the village.                           |
|                                                                     |
 ---------------------------------------------------------------------
                                |  |
                                |  |
                                |  |
                                |  |
                                |  |
                                |  |
                                ____

                                """)
story = ("""
What should Riri do?

a: Enter the temple
b: Don't enter the temple

""")
typewriter(story)

choice = (input("Input your option here: "))


if choice == "b":
    story = ("""
Lola disagrees with you and enters the temple. Riri sets off on his lonely
journey. Hours pass and Riri couldn't help but notice that the path he
took looked familiar. That's when he realises that he has been going in 
loops for hours now.
""")
    typewriter(story)
    
 # the audio changes to match the atmoshpere
    winsound.PlaySound("fire.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

    story = ("""
It was weird; he kept walking straight but his path keeps repeating. That's
when a dead leaf right under Riri's feet catches on fire. Riri screams as the
fire grew bigger and bigger until it was taller than the trees that surround
him. A Phoenix emerges from the fire.

"You dare steal the berries of the temple, and then not enter the temple?
This is a sin so unforgivable that I must punish you in the most brutal
way possible!" shouts the Phoenix. 

"I'm s-sorry. B-but umm who are you?" Riri asks, while his hands trembled
with fear.

"Oh why, I'm the spirit of fire, the spirit in charge of guarding the Temple
of Dhasha. I shall now punish you for your sins."

Riri starts to feel warm, incredibly warm. His body is on fire! He screams
and screams until the fire had gone out. His body is covered in feathers,
black, burnt feathers. He was a crow!

Poor Riri spent the rest of his life as a crow, serving the Temple of Dhasha
in hopes that the spirit would lift the curse off of him.

Spoiler alert: It never happened.

                		  ~The End~
                                
""")
    typewriter(story)
    
    sys.exit()
# Was planning to add an option for the player to try another ending, and exit the game

# Now comes a series of riddles
# Use while loops to allow the players to try answering the question again

else:
    story = ("""
They push the heavy metal door with all their strength. Inside the temple
was a damp, cool, and dark atmosphere. The walls were covered in
moss, and some of the lamps on the walls looked like they were about to fall 
off.

Just as they enter the temple, the door slams behind them. Riri and Lola try
to open it with all their strength. Don starts to howl in fear. Suddenly,
lamps on the walls of the temple start to light up, one by one, until it
reaches the goblet in the middle of the room.""")
    typewriter(story)

# The audio changes to fire to match the story
winsound.PlaySound("fire.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""

The goblet lit on fire, and it was soo bright that they had to cover their
eyes. Phoenix emerged from the goblet. The cold, wet, dull room is now warm
and buzzing with energy.

The Phoenix says "Welcome to The Temple of Dhasha. You have chosen to
enter this temple to exit towards the village.."

Riri and Lola nod their heads.

"Behind these doors are 3 creatures of different kinds. Each creature
will ask you a different question and they will let you pass if you can
answer correctly. You have the freedom to leave the temple at any
times, but beware of what follows! You may pass through the first door."
""")
typewriter(story)

winsound.PlaySound("distant_thunder.wav",winsound.SND_ASYNC + winsound.SND_LOOP)

story = ("""
Riri and Lola walk through the door at the end of the room. As they pass
through the door, they see valleys and mountains in the distance, the sky 
was visible, however, it was filled with dark grey clouds. There were trees 
around them, but the door they had come through had disappeared.
Lightning struck, and it started pouring. A Dragon soared above their heads. 
It flew down towards Riri and Lola.

It says "I have cities, but no houses. I have mountains, but no trees.
I have water, but no fish. What am I?"
""")
typewriter(story)

player_input = (input("Input a one-word answer: ")).lower().strip()

while player_input != "map":
    story = ("""
"That is incorrect." says the Dragon. "You may try again."

Hint: Think outside the box! There are roads and streets, but no cars. 
      Think of the word navigation!
         """)
    typewriter(story)
    
    player_input = (input("Input a one-word answer: "))

else:
    #The audio changes here as they move rooms
    winsound.PlaySound("fairy_dust.wav",winsound.SND_ASYNC + winsound.SND_LOOP)
    story = ("""
"That is the correct answer." says the dragon. "You may pass through this
door."

A door appears on a trunk of a tree. Riri, Lola and Don pass through their
first door. They enter an indoor flower garden. The flowers shone so
beautifully, that they seem to glow. They then find out that it isn’t the
flower itself that had shone, but what was inside of it.

Out through the flowers came Fairies of different colours and kinds. One
of the Fairies approached them and swished its little hands. Sparkly words
appeared in the air, and it said: "You measure my life in hours and I
serve you by expiring. I am quick if I am thin, and I am slow if I am
fat. The wind is my enemy. Who am I?"
""")
    typewriter(story)
    
    player_input = (input("Input a one-word answer: "))

while player_input != "candle":
    story = ("""
Words appear in the air. They say "That is incorrect. You may try again."

Hint: The word 'glow' and ‘fire’ may be helpful here!
""")
    typewriter(story)

    player_input = (input("Input a one-word answer: "))

else:
    # The audio changes here because Riri is in another room
    winsound.PlaySound("sea_waves.wav",winsound.SND_ASYNC + winsound.SND_LOOP)
    
    story = ("""
"Wonderful! You may pass." The sparkles faded away and a door is visible
at the other side of the garden. This is the last room which contains the
last challenge that they must face. Once they enter the room, they see stars
twinkling in the sky above them. The reflection of the moon ripples on the
water. They could hear waves, and taste salt on their lips. They were at the 
beach! 

In the distance, they hear a voice singing a tune so beautiful that even Don
gently swayed to the rhythm. The voice got closer and closer until they could
make out the figure. The voice belonged to one of the most beautiful mythical
creature there is; a Siren. She sat upon a rock close to the shores of the
beach. 

In a voice sweeter than honey, she sings "I speak without a mouth and I hear 
with no ears. I have nobody but I come alive with the wind. What am I?"
""")
    typewriter(story)

player_input = (input("Input a one-word answer: "))

while player_input != "echo":
    story = ("""
She sings "That is not correct, I am afraid. You may try once more."

Hint: It has something to do with sound! Think of sound, and how it repeats
      due to a certain phenomenon.
""")
    typewriter(story)

    player_input = (input("Input a one-word answer: "))

else:
    story = ("""
"That is the correct answer!" she sings. "Congratulations! You may now
pass through the door behind you to reach the village."

Riri, Lola and Don walk through the door to see a familiar village. It
is their home-village!

                              ~3 years later~

Riri and Lola are now married, and Don made friends with everyone in the
neighbourhood. They live happily ever after together.

                                  The end
""")
    typewriter(story)
    
    sys.exit()



