#Author: Talia

#Game with multiple choices and endings.

#notes to self:
#8. Add more comments lol

#Defining Constants
time = 0
space_text = " "
dash = "-"
section_divider = ("----------------------------")

#Imports
import time

#Defining different pathway points
finding_bart = 0
home_to_stay = 0

#Lists
health_and_deadline = [100,5]
mystery_choices = ["Knife", "Lighter", "Gun"]


#defining functions
def reset_time():
    time = 10
    
def delay():
    time.sleep(1)
    
def delay_two():
    time.sleep(2)

def delay_three():
    time.sleep(3)
    
def stat_display():
    print(section_divider)
    deadline_display = f"Deadline = {health_and_deadline[1]} days"
    health_display = f"Health = {health_and_deadline[0]}"
    print(deadline_display)
    print(health_display)
    delay_two()
    print(section_divider)
    delay()

def space():
    print(space_text)

#defining loop checkers to help repeat when invalid inputs occur
start = 0
intro = 0
intro_choice_loop = 0
first_choice_loop = 0
first_forest_option = 0
forest_or_suburbs = 0
first_suburb_counter = 0
talk_choice_counter = 0
sneak_choice_counter = 0
intro_skip_counter = 0
first_city_counter = 0
final_choice_counter = 0
minigame_counter = 0
sneak_end_choice_counter = 0
sneak_choice_stick = 0
#Start of the Game

    
print("Welcome to Rescue Mission")
delay()
print(section_divider)
delay()

space()
while start < 1:
    
    space()
    start_signal = (input("Please type [start] when you are ready to begin your experience: ").lower())
    if start_signal == "start":
        start += 1

    else:
        space()
        print("We will wait until you are ready")
delay()        
space()
print("Thank you for starting the game!")
delay()
print(section_divider)
delay()
# Explaining how to play if needed

while intro < 1:

    space()
    how = (input("Please type [how] to access the how to play or [no] if you would like to skip: ").lower())
    
    #teaches/informs the player of the beginning of the game    
    if how == "how": 
        
        print("The ending of this game is dependant on Your choices.")
        delay_two()
        space()
        print("When there is a choice to be made, you will have to type your choice.")
        delay_two()
        space()
        print("The options you can type will be in square brackets and you can type your choice after the ':'.")
        delay_two()
        delay_two()
        print("In this game you will start with 100 health points and a 5 day deadline.")
        delay_two()
        space()
        print("These values will be displayed if they are affected.")
        delay()
        space()
        print("However, if you would like to see the stats, type [stats], at any choice, and it will be displayed")
        delay()    
        space()
        delay_two()
        print("Here is an example:")
        delay()
            
        #will help repeat the choice if input is invalid
        while intro_choice_loop < 1:
            
            space()
            intro_choice = str(input("Do you want to go [left] or [right]? ").lower())
        
            if intro_choice == ("left"):
                space()
                delay()
                print("You chose to go left! Good Job :)")
                delay()
                print(section_divider)
                intro += 1
                intro_choice_loop += 1
    
                    
            elif intro_choice == ("right"):
                space()
                delay()
                print("You chose to go right! Good Job :)")
                delay()
                print(section_divider)
                intro += 1
                intro_choice_loop += 1

            else:
                space()
                print("Please re-enter your response, make sure to type the correct spelling!")

    #will skip the tutorial    
    elif how == "no":
            intro += 1
    
    else:
        print("Looks like you haven't quite gotten the hang of it. Try again :)")


#Game Starts
print(section_divider)
delay_three()

#Into of the game
#will help repeat the choice if input is invalid
while intro_skip_counter < 1:
    intro_skip_input = (input("Would you like to [skip] the intro, or [read] it? ").lower())

    #will skip to the next section of the game
    if intro_skip_input == "skip":
        delay()
        space()
        print("The game will now commence")
        delay()
        print(section_divider)
        delay()
        space()
        intro_skip_counter +=1
        pass

    #Will read out the introduction to the player
    elif intro_skip_input == "read":
    
    
        intro_sentence = print("The game will now commence!")
        delay()
        print(section_divider)
        delay_three()
    
        print("It has been around four years since the apocolypse started.")
        delay_two()

        print("I was only 12 when it started.")
        delay_two()
        print("I lost my parents pretty early on....")
        delay_two()
        print("But my best friend was always there for me.")
        space()

        delay_three()

        print("His name is Bartholomew, but I call him Bart.")
        delay_two()
        print("He's a Newfoundland dog and I got him only a year before this world was created.")
        delay_two()
        print("We have always helped each other to survive....")
        delay_two()
        print("Until everything changed yesterday.")
        space()

        delay_three()

        print("Yesterday.... He was taken from me.")
        delay_two()
        print("A group of survivors took him away from me.")
        delay_two()
        print("And I plan to get him back.")
        delay()
        print(section_divider)
        delay_three()
        intro_skip_counter +=1

    else:
        print("Please enter a choice.")

#FIRST SECTION - forest or suburbs

print("First things first, I need to find out where he is.")
space()
delay_two()
print("When they took him, I heard that they that they were going to take him out of the country in a five days.")
space()
delay_three()
print("So I need to get to him before then.")
delay()
space()
stat_display()
delay()

print("They must be heading for the dock at the edge of town.")
delay_two()
space()
print("But there are multiple ways to get there.")
delay_two()    

#Keeps the game in a loop and helps to ensure the multiple endings
while first_choice_loop < 1 :

    #will help repeat the choice of forest of suburbs if input is invalid
    while forest_or_suburbs < 1:
        
        space()
        #Both choices will lead the player on different pathways until the next section.
        print("Now... Should I go through the [forest] or the [suburbs]..?")
        delay()
        space()
        print("I believe the suburbs are the faster option, however there is less cover is I run into any enemies or walkers.")
        space()
        delay_two()

        start_signal = (input("Whereas if I go through the forest, it will be slower, but it will likely be more safe: ").lower())

        #Forst Pathway
        if start_signal == "forest":
            forest_or_suburbs += 1
            delay()
            health_and_deadline[1] -= 1.5
            print("I started to head into the forest.")
            delay()
            print(section_divider)
            delay()
            print("I've been walking for about two and a half days, wondering in the general direction of the docks.")
            space()
            delay()
            print("Suddently, I see a group of zombies migrating in my direction.")
            space()
            delay()
            print("If I keep going the way I'm going, I, going to run into trouble.")
            space()
            delay()
            
            #will help repeat the choice of the knapsack items if input is invalid
            while first_forest_option < 1:
                print("I spot an abandonded knapsack and examine its goods to see that I can use.")
                space()
                delay()
                print("I think I can use something from it to help escape the zombies!")
                space()
                delay()
                print("When I look inside I find-")
                space()
                delay()
                
                #cloak will get player killed,grapple will almost kill, shovel will injure and molotov will get away easily
                
                first_item_choice_forest = (input("A [grapple] hook, a [shovel], and invisability [cloak] and a [molotov] cocktail:").lower())     

                if first_item_choice_forest == "grapple":
                    #choice if player choses grapple
                    print("I reach into the bag, and grabbed the grapple hook.")
                    space()
                    delay()
                    print("I pointed it up into the closest tree to me and set it off")
                    space()
                    delay_two()
                    print("Five seconds later, it came flying right down at me, leaving me defencless against the upcoming zombies...")
                    space()
                    delay_two()
                    print("I guess I should have checked if the tree had any branches first.......oops")
                    space()
                    delay()
                    space()
                    delay()
                    #some health and time is lost
                    health_and_deadline[1] -= 0.1
                    health_and_deadline[0] -= 50
                    print("I barely escaped that... I'll have to be extremly careful now and try to get my health up...")
                    first_forest_option += 1
                        

                elif first_item_choice_forest == "shovel":
                    #choice is player choses a shovel
                    space()
                    delay()
                    print("I reach into the bag, grabbed the shovel, and started digging as fast as I could.")
                    space()
                    delay()
                    print("I was Just able to dig a hole big enough for myself")
                    space()
                    delay()
                    print("The zombies got closer")
                    space()
                    delay()
                    print("And closer")
                    space()
                    delay()
                    print("Until they passed me.")
                    space()
                    delay()
                    print("But not without trampling my head :(")
                    space()
                    delay()
                    print("I guess I forgot to cover my head")
                    #some health is lost
                    health_and_deadline[0] -= 15
                    space()
                    delay()
                    print("At least it isn't that bad")
                    space()
                    delay()
                    print("I might just have to be a little careful for now")
                    space()
                    delay_two()
                    print("I also forgot I couldn't get out of the hole right away...")
                    space()
                    delay()
                    print("so it took me a few hours to get out.")
                    health_and_deadline[1] -= 0.75
                    first_forest_option =+ 1

                elif first_item_choice_forest == "cloak":
                    delay_two()
                    print("I reach into the bag, and grabbed the cloak, put it around me, and waited in the open.")
                    space()
                    delay()
                    print("They can never see me with this and I can walk right by after they leave!")
                    space()
                    delay()
                    print("The zombies got closer.")
                    space()
                    delay()
                    print("And closer.")
                    space()
                    delay_two()
                    print("AND THEN THEY FOUND ME-")
                    space()
                    delay()
                    print("*hint* invisability cloaks exists in the Harry Potter universe, not the zombie apocalype universe.")
                    delay_three()
                    #all health is lost
                    health_and_deadline[0] -= 100
                    first_forest_option =+ 1

                elif first_item_choice_forest == "molotov":
                    print("I reach into the bag, and grabbed the molotov.")
                    space()
                    delay()
                    print("I ran as close to the zombies that I could afford and threw it with all my strength.")
                    space()
                    delay()
                    print("It landed right in the middle of the hoarde and they quickly dispersed into different directions.")
                    space()
                    delay()
                    print("'Yes!!', I thought to myself, as I began to run right past the distressed zombies.")     
                    first_forest_option =+ 1

                elif first_item_choice_forest == "stats":
                    stat_display()

                else:
                    print("Hmmmmm. I need to make a choice.")

            space()
            delay()
            print("In all my excitement, I forget to take the knapsack with me...")
            if health_and_deadline[0] <= 0:
                break
            else:
                pass
            space()
            delay_two()
            stat_display()
            first_choice_loop += 1
                   
        #Suburbs Pathway
        elif start_signal == "suburbs":
            forest_or_suburbs += 1
            space()
            delay()
            print("I decided to head into the suburbs")
            delay()
            print(section_divider)
            space()
            delay_two()
            print("After walking around for around a day, I finally ran into some trouble.")
            health_and_deadline[1] -= 1
            space()
            delay()
            print("A group of people around my age were talking in a group, right nexto the checkpoint tunnel I needed to cross.")
            space()
            delay()
            print("They look friendly enough...")
            space()
            delay()
            #Loop to repeat the choice of talk or sneak if input is invalid
            while first_suburb_counter < 1:
                first_suburb_choice = (input("I'm not sure if I should [talk] with them, or try to [sneak] around them:").lower())
                
                #talking outcome   
                if first_suburb_choice == "talk":
                    print("I walked over to talk to them")
                    space()
                    delay()

                    #Loop to repeat the choice of freindly or aggressive if input is invalid
                    while talk_choice_counter < 1:

                        talk_choice_input = (input("Should I introduce myslef in a [friendly] way, or in an [aggressive] way?").lower())
                        #friendly outcome
                        if talk_choice_input == "friendly":
                            space()
                            delay()
                            print("'Hi... My name is Carmen. I was just passing through here and wondering if you could help me pass the checkpoint?'")
                            space()
                            delay()
                            print("They all turned to look at me")
                            space()
                            delay()
                            print("There were three people in total, all girls that I could see were around my way.")
                            space()
                            delay()
                            print("All were carrying heavy their own firearm")
                            space()
                            delay()
                            print("'Hi! My name is Amelia, and this is Sharon and Nim. Sure we can help, we were just waiting for some others.' the one closest to me said.")
                            space()
                            delay()
                            print("'Thank you So much', I said back")
                            space()
                            delay()
                            print("I ended up goin through a secret tunnel that they found and ended up saving lots of time!")
                            space()
                            delay()
                            print("And they even gave me a medkit for if I need it.")
                            health_and_deadline[1] -= 0.15
                            home_to_stay += 1

                            talk_choice_counter += 1
                            
                        #aggressive outcome
                        elif talk_choice_input == "aggressive":
                        
                            print("'HEY HOW DO I GET THROUGH THERE! YOU GUYS BETTER TELL ME OR ELSE!!', I yelled at them")
                            space()
                            delay()
                            print("They all looked at me quietly, shocked at my presence.")
                            space()
                            delay()
                            print("Then the one on the left reached for something behind her with a sick smile.")
                            space()
                            delay()
                            print("And then a massive RPG appeared")
                            health_and_deadline[0] -= 25
                            space()
                            delay()
                            print("And then, I ran with all my might, as I heard the world around me exploded.")
                            space()
                            delay()
                            print("With all my might, I vaulted myself over the checkpoints wall, and escaped with the consequence of an injured leg, which may slow me down.")
                            health_and_deadline[1] -= 0.5
                            talk_choice_counter += 1
                            if health_and_deadline[0] <= 0:
                                break
                            else:
                                pass
                        
                        #stats will be displayed if needed/wanted
                        elif talk_choice_input == "stats":
                            stat_display()
                            
                        #to keep repeating if input is invalid
                        else:
                            print("I need to make a choice...")
                            space()
                            delay()

                    first_suburb_counter += 1

                #sneaking outcome
                elif first_suburb_choice == "sneak":

                    print("I decided to sneak around them")
                    space()
                    delay()

                    sneak_choice_input = (input("There was some tall [grass] and some [cars] around. Which one should I use as cover?").lower())

                    #Loop to repeat the choice of grass or cars if input is invalid
                    while sneak_choice_counter < 1:
                        
                        #grass outcome  
                        if sneak_choice_input == "grass":
                            print("I decided to go through the grass")
                            space()
                            delay()
                            print("I got down on my stomach and began commando crawling through the grass.")
                            space()
                            delay()
                            print("As I was crawling, I found a small crack in the checkpoint, and I slowly crawled through it.")
                            health_and_deadline[1] -= 0.25     
                            sneak_choice_counter += 1
                            
                        #cars outcome
                        elif sneak_choice_input == "cars":
                            print("I decided to use the empty cars as my cover")
                            deadline -= 1
                            space()
                            delay()
                            print("I slowly got on my stomach and began to commando craw under the cars.")
                            space()
                            delay()
                            print("As I was halfway to a hidden crack in the wall (my escape), I heard a loud 'SPLASH'")
                            space()
                            delay()
                            print("I looked down.")
                            space()
                            delay()
                            print("I had just crawled into a massive puddle.")
                            space()
                            delay()
                            print("My heart pounded and my head snapped to the direction of the people.")
                            space()
                            delay()
                            print("They were staring Right at me!")
                            space()
                            delay()
                            print("Then the one on the left reached for something behind her with a sick smile.")
                            space()
                            delay()
                            print("And then a massive RPG appeared")
                            space()
                            delay()
                            print("I gasped and tried to get out as soon as I could but I was still in the middle of the car... It's going to take awhile to escape!")
                            space()
                            delay()
                            print("I heard the world around me explode, and  I barly escaped the encounter.")
                            space()
                            delay()
                            #health is lost
                            health_and_deadline[0] -= 50
                            health_and_deadline[1] -= 1
                            #if there is no more health the loop will break to the end of the game.
                            if health_and_deadline[0] <= 0:
                                break

                            else:
                                pass
 
                            sneak_choice_counter += 1
                            
                        #stats shown if needed
                        elif sneak_choice_input == "stats":
                            stat_display()
                            
                        #choice will be repeated
                        else:
                            print("Hmmmm.")
                                      
                    first_suburb_counter += 1
                    
                #stats shown if needed
                elif first_suburb_choice == "stats":
                    display_stat()
                    
                #choice will be repeated
                else:
                    space()
                    delay()
                    print("Hmmmm...")
                    
            first_choice_loop += 1

        #Stats printed if needed
        elif start_signal == "stats":
            stat_display()
            
        #If input is invalid, it will repeat           
        else:
            space()
            delay()
            print("I need to make a choice.")
                
    space()
    delay()    
        
    #info prints the stats
    if health_and_deadline[0] <= 0:
        break

    else:
        pass #checking again the health

    #This is where the player two choices forest or suburbs finally intersect as the player makes their way to the end of the game
    #SECTION 2 - THE CITY
    space()
    delay_three()
    print("I finally reached the last stretch to the docks!")
    space()
    delay()
    print("The city...")

    #warning the player to be carefyl if they have low health
    if health_and_deadline[0] < 50:
        space()
        delay()
        print("I'm not doing so well, I need to be really careful from now on.")
        
    #letting the player know to be cautious just in case
    else:
        space()
        delay()
        print("I seem to be doing ok, I better keep being careful to avoid being hurt.")

    space()
    print(section_divider)
    delay_three()
    health_and_deadline[1] -= 1
    print("Its been about a day, and so far I havent encountered anything.")
    space()
    delay()
    print("However, I just noticed a pathway leading to the left, that has a sign that says 'free rations this way'.")
    space()
    delay()
    print("The path I was originally on heads straight, however there is also another way leading right...")
    space()
    delay()

    #Loop to repeat the choice of left, straight or right if input is invalid
    while first_city_counter < 1:
        
        #a choice for when the player is in the city
        first_city_choice = (input("Should I go [left], [straight] or [right]...").lower())

        #left outcome
        if first_city_choice == "left":
            space()
            delay()
            print("I headed left towards the sign.")
            space()
            delay_two()
            print("As soon as I got there.... A group of thugs ambushed me!")
            space()
            delay()
            print("After that fight now, I'm pretty badly injured...")
            health_and_deadline[0] -= 15
            #if player is dead loop will break and go straight to the ending
            if health_and_deadline[0] <= 0:
                break

            else:
                pass

            space()
            delay()
            health_and_deadline[1] -= 1
            print("After a while, I regained my strength and was back on my path to saving Bart.")
            
            first_city_counter += 1
            
        #Straight pathway
        elif first_city_choice == "straight":
            space()
            delay()
            print("I continued on my pathway...")
            space()
            delay()
            print("After walking for a few more hours, I accidentally tripped on a clear tripwire.")
            space()
            delay()
            print("A loud explosion occurred and it took me awhile to get back up.")
            space()
            delay()
            health_and_deadline[0] -= 30
            health_and_deadline[1] -= 0.75
            #if player is dead, code will break striaght to the ending
            if health_and_deadline[0] <= 0:
                break

            else:
                pass
            print("Soon I was back on the path to Bart")
            first_city_counter += 1

        #right pathway
        elif first_city_choice == "right":
            space()
            delay()
            print("I guess right is always the right way.")
            space()
            delay()
            print("I passed through the rest of the way pretty easily without any problems.")
            space()
            delay()
            print("I'm so happy I went this way!")
            health_and_deadline[1] -= 0.15
            first_city_counter += 1
            
        #stats if needed
        elif first_city_choice == "stats":
            space()
            delay()
            print(stat_display)

        #repeats the code if the input is invalid
        else:
            space()
            delay()
            print("Hmmm... Which way should I go...?")

    stat_display()
    space()
    delay()

 #SECTION THREE - THE DOCKS
    
    print("Finally. I have reached the docks.")
    space()
    delay()

    #Loop to repeat the choice of kill or sneak if input is invalid
    while final_choice_counter == 0:

        final_choice = (input("I have one final  big decision to make. Do I [sneak] in and save Bart, or do I bust in and [kill] everyone: ").lower())

        #sneak pathway
        if final_choice == "sneak":
            health_and_deadline[1] -= 1
            space()
            delay()
            print("I decided to sneak in...")
            space()
            delay()
            print("To get into the boat area, I snuck through cover until I reached the door.")
            space()
            delay()
            print("If Bart was anywhere in this place it would be over here with the convenient sign that says 'stolen animals - dogs'")
            space()
            delay()
            print("The only thing is there is a man guarding the door...")
            space()
            delay()
            print("There is a rock next to where I'm hiding")
            space()
            delay()
            
            #Loop to repeat the choice of use or sneak if input is invalid
            while sneak_choice_stick == 0:
                
                sneak_end_choice = (input("Should I [use] it as a distraction, or try and [sneak] around the man: ").lower())
                #use outcome
                if sneak_end_choice == "use":

                    space()
                    delay()
                    print("I threw the stick to the opposite direction I was in..")
                    space()
                    delay()
                    print("And the guy went there to look!")
                    space()
                    delay()
                    print("While he left I made my way to the door of the place that held Bart.")

                    final_choice_counter += 1
                    sneak_choice_stick += 1
                    
                #sneak outcome
                elif sneak_end_choice == "sneak":
                    space()
                    delay()
                    print("The man was standing right in front of the door, but I decided to try and sneak by him anyway.")
                    space()
                    delay()
                    print("Slowly I crawled towards the door in hopes I would blend in with the floor.")
                    space()
                    delay()
                    print("it didnt work...")
                    space()
                    delay()
                    print("He literally saw right through my plan")
                    space()
                    delay()
                    print("And... He had a knife on him...")
                    space()
                    delay()
                    print("I had to dodge his attacks and got stabbed in the arm, but I was eventually able to take him down.")
                    space()
                    delay()
                    print("Luckily no-one else had noticed our squabble.")
                    space()
                    delay()
                    print("Suddently I found myself standing in front of the door where Bart is being held.")
                    


                    health_and_deadline[0] -= 15
                    health_and_deadline[1] -= 0.35
                    #If player is dead the code will cut to the ending
                    if health_and_deadline[0] <= 0:
                        break
                    else:
                        pass

                    final_choice_counter += 1
                    sneak_choice_stick += 1
                #Stats will play if needed
                elif sneak_end_choice == "stats":
                    space()
                    delay()
                    print(stat_display)
                    
                #loop will repeat until input is valid
                else:
                    space()
                    delay()
                    print("Come on.. I'm so close I just have to make this decision.")
            

        #kill pathway      
        elif final_choice == "kill":
            health_and_deadline[1] -= 0.5
            space()
            delay()
            print("I decided to kill everyone one in my path.")
            space()
            delay()
            print("If Bart was anywhere in this place it would be over here with the convenient sign that says 'stolen animals - dogs'")
            space()
            delay()
            print("Everyone who was involved in taking Bart away deserves to DIE...")
            
            #Loop to repeat the choice of 1, 2 or 3 if input is invalid
            while minigame_counter < 1:

                space()
                delay()
                print("I see a drawer full of weapons in front of me. However I if I can't see that I'm taking without being seen by an ememy.")
                space()
                delay()
                minigame_choice = input("Should I grab item [1], [2], or [3].")

                #1 outcome
                if minigame_choice == "1":
                    space()
                    delay()
                    print(f"When I pulled my hand out of the drawer, I saw I had grabbed a {mystery_choices[0]}")
                    space()
                    delay()
                    print("Hmmmmm good for close distance attacks, but wont work from a far...")
                    space()
                    delay()
                    print("So I decided to sneak my way through and kill anyone in my path.")
                    print(section_divider)
                    space()
                    delay_three()
                    print("And it worked... it only took a little longer and I was at the bad end of some of those attacks, but")
                    space()
                    delay()
                    print("Soon I was making my way into the room Bart was being helf in.")
                    
                    health_and_deadline[0] -= 15
                    health_and_deadline[1] -= 0.25
                    #if player is dead, code will cut  to the emding
                    if health_and_deadline[0] <= 0:
                        break
                    else:
                        pass

                    minigame_counter += 1
                    final_choice_counter += 1
                    
                #2 outcome
                elif minigame_choice == "2":
                    space()
                    delay()
                    print("When I pulled my hand out of the drawer, I saw I had grabbed a...")
                    space()
                    delay_two()
                    print(f"{mystery_choices[1]}??")
                    space()
                    delay()
                    print("What am I meant to do with this...?")
                    space()
                    delay_two()
                    print("Then it hit me.")
                    space()
                    delay()
                    print("There was a big oil storage container here")
                    space()
                    delay()
                    print("If I throw the lighter in, it will blow up this place killing them, and attract some zombies to finish the rest off while I get Bart!")
                    print(section_divider)
                    space()
                    delay()
                    print("So I did it.")
                    space()
                    delay()
                    print("And it worked")
                    space()
                    delay()
                    health_and_deadline[0] -= 10
                    print("I was a little late to run from the explosion so I was a little injured.")
                    #if player is dead
                    if health_and_deadline[0] <= 0:
                        break
                    else:
                        pass
                    space()
                    delay()
                    print("But I was finally able to make my way into the room Bart was held!.")

                    minigame_counter += 1
                    final_choice_counter += 1
                #3 outcome
                elif minigame_choice == "3":
                    space()
                    delay()
                    print(f"When I pulled my hand out of the drawer, I saw I grabbed a {mystery_choices[2]}!!")
                    space()
                    delay()
                    print("This was the best thing I could have grabbed.")
                    space()
                    delay()
                    print("And it was fully loaded!")
                    space()
                    delay()
                    print("I stood up from my hiding spot, which immediatly alerted many enemies.")
                    space()
                    delay()
                    print("But it didnt matter...")
                    space()
                    delay()
                    print("Every enemy that came my way I was able to shoot down.")
                    space()
                    delay()
                    print("Until no more came")
                    space()
                    delay()
                    print("I was finally able to make my way into the room Bart was being held.")

                    minigame_counter += 1
                    final_choice_counter += 1
                    
        #stats shown if needed                 
        elif final_choice == "stats":
            space()
            delay()
            print(stat_display)
            
        #looping if input is invalid
        else:
            space()
            delay()
            print("I'm almost there... I need to make a choice!!")
    #ending the code to go the the results section
    break

#RESULTS

#if the deadline is over 0 then the player will have gotten to bart in time
if health_and_deadline[1] > 0:
    finding_bart += 1
    
print(section_divider)
space()
delay_three()
#if health is less than 0 the player is dead
if health_and_deadline[0] <= 0:
    space()
    delay()
    print("Game Over You Have Died")
    space()
    delay()
    print(section_divider)
    space()
    delay()
    print("In my final thoughts I thought only of Bart...")
    space()
    delay()
    print("I had failed him.")
    space()
    delay()
    print("If only I could do it all again, I could have made different choices....")
    space()
    delay()
    
#if the player is still alive:    
else:

    space()
    delay()
    print("I went into the room...")
    space()
    delay_three()

    #
    if finding_bart > 0:

        print("And I found him!")
        space()
        delay()

        if home_to_stay > 0:
            print("With the friends I've made along the way, we were able to live peacefully with them, at least until our next adventure!")
            space()
            delay()

        else:
            print("After I went to find Bart, I had lost contact with out old group.")
            space()
            delay()
            print("We have nowhere to go")
            space()
            delay_three()
            print("But thats ok.")
            space()
            delay_two()
            print("Because I now have Bart by my side....")
    else:
        space()
        delay()
        print("But he wasnt there...")
        space()
        delay()
        print('A quick look around the room told me the boat had already departed...')
        print(section_divider)
        space()
        delay()
        print("After losing Bart I didnt know what to do.")
        space()
        delay()
        print("I had lost contact with my old group when I had first lost Bart.")
        space()
        delay()

        #If the player did not save bart and they took the friendly appraoch with the people, the player will stay with them
        if home_to_stay > 0:
            print("I decided to live with the three friends I made along the way.")
            space()
            delay()
            print("They welcomed me with open arms.")
            space()
            delay_three()
            print("However... I never forgot Bartholomew...")
                
        else:
        #If the player did not save bart and did not take the city path or took the aggressive path, the player will have no where to go
            print("I decided to be a traveller.")
            space()
            delay()
            print("To keep searching for a place to start over.")
            space()
            delay_three()
            print("...But I will never forget Bart.")
        


    print(section_divider)
    space()
    delay()
    print(f"You survived with {health_and_deadline[0]} health left")

    if finding_bart > 0:
        space()
        delay()
        print("And you were able to Rescue Bart! Good job!")


space()
delay_three()
print(section_divider)
space()
delay()
print("Thank you for playing Rescue Mission.")
space()
delay()
print("Please restart the code to play again :)")
