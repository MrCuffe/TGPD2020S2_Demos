#Game Title: Hello Stranger!
#AUTHOR: Moin Vohra
#Description: text-based adventure game
from time import sleep
#all variables that will build the player and set up system messages
confidence = 50
player_dead= False
player_dead_message= "DISCONNECTED"
user=["(6_6)","(o_o)"]
player=["(o_o)","(0_0)","(~_~)"]
stalker="(ʘ‿ʘ)"
choice_1=False
choice_2=False
#code that will be needed repeatedly
#npc text will be on right side and should take time to give feel of typing
def npc_text(message):
  sleep(2)
  side_space=((60-len(message))*" ")
  print(f"{side_space}{message}{player[0]}\n")

#happy npc text refes to the emoji on the side- it will have a happy expression
def npc_text_happy(message):
  sleep(2)
  side_space=((60-len(message))*" ")
  print(f"{side_space}{message}{player[2]}\n")
  
#scared emoji
def npc_text_scared(message):
  sleep(2)
  side_space=((60-len(message))*" ")
  print(f"{side_space}{message}{player[1]}\n")
  
#system message in the center
def sys_message(message):
  sleep(2)
  message="["+str(message.upper())+"]"
  mid_space=((30-((len(message))//2))*" ")
  print(f"{mid_space}{message}\n")

#for some parts for when the stalker speaks
def stalker_text(message):
  #sleep(2)
  print(f"{stalker}{message}\n")
  
#choice message will look for keywords for both choice 1 and 2 in user input
def choice_msg(player_choice1,player_choice2,kword_choice1,kword_choice2):
  global choice_1
  global choice_2
  choice_1=False
  choice_2=False
  prompt=f"What do you think?"
  choice= f"{player_choice1} or {player_choice2}?"
  choice_side_space=((60-len(choice))*" ")
  prompt_side_space=((60-len(prompt))*" ")
  sleep(1)
  print(f"{prompt_side_space}{prompt}{player[1]}\n")
  sleep(1)
  print(f"{choice_side_space}{choice}{player[0]}\n")
  user_input= str(input(user[1])).lower()
  count_1= int(user_input.count(kword_choice1))+int(user_input.count("first"))
  count_2= int(user_input.count(kword_choice2))+int(user_input.count("second")) 
  if count_1==count_2:
    sleep(1)
    error=f"I am sorry what was that?"
    error_side_space=((60-len(error))*" ")
    print(f"{error_side_space}{error}{player[0]}\n")
    sleep(1)
    choice_msg(player_choice1,player_choice2,kword_choice1,kword_choice2)
  elif count_1>0 and count_2==0:
    choice_1=True
    choice_2=False
  elif count_2>0 and count_1==0:
    choice_1=False
    choice_2=True
  return (choice_1,choice_2)

#when choices are made to alter confidence levels
#NOT WORKING???
def confidence_change(number,change):
  global confidence
  if change=="increase" and confidence<=(100-number):
    confidence+= number
  elif change=="decrease" and confidence>=number:
    confidence-= number
  elif change=="increase" and confidence>(100-number):
    confidence=100
  elif change=="decrease" and confidence< number:
    confidence= 0
  sys_message(f"Your Confidence Percentage is now at {confidence}%")

def ending():
  sys_message(player_dead_message)
  sys_message(f"ending confidence:{confidence}%")
  sleep(2)
  sys_message("RECONNECTING")
  sys_message("NEW UNREAD MESSAGE")
  stalker_text(f"Hello {user_name}")
  str(input(user[1]))
  stalker_text("You did well...")
  stalker_text("Better than I expected to be honest")
  stalker_text("This will make things much more fun")
  stalker_text(f"I will see you soon, {user_name}")
  stalker_text("Try not to keep your door unlocked like Alex")
  sleep(1)
  stalker_text(":)")
  sys_message(player_dead_message)
  sys_message("Thank you for playing my game")
  sys_message("Until next time...")
  sys_message("Hello Stranger - By Moin Vohra")

#use this function for same result of different choices for generator scene
def generator_choice():
  npc_text("The generator is broken-")
  npc_text_scared("and by broken I mean destroyed...")
  npc_text_scared("it's still smoking meaning the damage was recent")
  npc_text_scared("he's already inside.")
  confidence_change(10,"decrease")
  npc_text_scared("and if he is inside...")
  npc_text_scared("then he knows I am here.")
  npc_text_scared("he knows where my room is too...")
  npc_text("wait...")
  sleep(1)
  npc_text("I can hear him - listen")
  stalker_text(f"{user_name}!")
  npc_text_scared("di-did he just say your name?")
  npc_text("no, I must be hearing things.")
  npc_text("His voice is coming from upstairs though")
  npc_text("if I be quiet I might be able to escape from the back")
  npc_text("or I can play it safe and stay here in the basement")
  choice_result=choice_msg("try to escape","stay in the basement","escape","stay")
  return choice_result

#asks user to type start to start game
sys_message("to start ~hello stranger~ type \'start\'")
user_input=str(input(user[0])).lower()
while user_input!= "start":
  sys_message("to start ~hello stranger~ type \'start\'")
  user_input=str(input(user[0])).lower()
#game starts
sys_message("establishing connection")
sys_message(f"starting confidence:{confidence}%")
sys_message("one unread message")
npc_text_scared("PLEASE HELP ME")
npc_text_scared("I-I am sorry for sounding so panicked")
npc_text("What's your name?")
#make sure name is inputted- useful in code later (gives personal feel to player)
user_name=str(input(user[0])).capitalize()
while len(user_name)==0:
    npc_text("Sorry what was that?")
    user_name=str(input(user[0])).capitalize()
if user_name=="Alex":
  npc_text_happy("Ayy I am Alex too")
npc_text_happy(f"Hello {user_name}")
npc_text("I am Alex...")
npc_text("and I need your help.")
#input with no effect on storyline at this point
str(input(user[1]))
npc_text("Let me start from the beginning")
npc_text("My parents are out of town")
npc_text("and I was home studying in this storm")
npc_text_scared("when suddenly the power went out")
npc_text("my phone was dead and phone lines weren't working")
npc_text_scared("-that's when I saw him")
str(input(user[1]))
npc_text_scared("him- this man in a coat")
npc_text_scared("he was just standing in the rain")
npc_text("no-not just standing...")
npc_text_scared("staring... right at me.")
npc_text("I called the police before my phone died")
npc_text("but the area is flooded, it'll be a while")
npc_text_happy("luckily i found this old phone in a drawer")
npc_text("but there was only one contact-yours...")
#instruct player on how to pick a choice
sys_message("you are about to face your first choice")
sys_message("please type one of the choices mentioned by NPC")
#if and elif statement allows for different answers depending on choice chosen.
choice_result=choice_msg("something is off","I might be too paranoid","something","paranoid")
if choice_result[0]==True:
  npc_text_scared("yes- I shouldn't take any chances")
elif choice_result[1]==True:
  npc_text_scared("maybe, but my gut doesn't agree")
#----PHASE TWO----
#The code after this point is purely phase 2, however some phase 1 code has been altered for phase 2
npc_text("I just remembered there is a backup generator")
npc_text("Maybe I can get it to work?")
npc_text_scared("WAIT. I JUST LOOKED OUT THE WINDOW AND THE MAN IS GONE")
npc_text_scared("What if he is trying to find a way in?")
npc_text_scared("I can't see anything downstairs")
npc_text("I think I left my back door unlocked")
npc_text("the generator is on the opposite side of the back door...")
npc_text("I won't be able to see anything if I go to doors first")
npc_text("and if i go to the generator first it might be too late...")
choice_result=choice_msg("check all door locks", "go to the generator","door","generator")
if choice_result[0]:
  npc_text("Ok yes, better to close off entry points")
elif choice_result[1]:
  npc_text("Ok yes, remove the element of surprise")
#shared part for both choices to avoid keeping the code long
npc_text("I am making my way downstairs right now")
sys_message("alex switched to speech-to-text settings")
npc_text_happy("Now I don't have to type out everything")
npc_text("I can hardly hear anything except the stairs creaking")
npc_text("not to mention I am blind in this darkness")
npc_text_happy("anyways I am glad I have you to help me through this")
#to keep user occupied - and for a twist at the end
npc_text_happy("tell me... where are you from?")
user_location=str(input(user[0]))
npc_text("Never heard of it")
npc_text("I am still confused about why yours was the only contact")
npc_text("Any chance you know me?")
str(input(user[1]))
npc_text(f"Oh well I know that I definitely don't know any {user_name}")
if user_name=="Alex":
  npc_text("Other than me of course...")
npc_text("Anyways...")
npc_text_happy("I made it.")
npc_text("hmm this is weird...")
str(input(user[0]))

#create different branches of storyline here
#let the user see their choices have reactions.
if choice_result[0]:
  story_line=1
  npc_text("The door is locked?")
  npc_text("I clearly remember leaving it unlocked though...?")
  npc_text("Maybe I am just shaken up")
  npc_text_happy("at least I know I am safe inside")
  confidence_change(10,"increase")
  npc_text("I can go to the generator now")
  npc_text("Or I can go upstairs to see if he is back outside")
  choice_result=choice_msg("go to the generator","go upstairs","generator","upstairs")
elif choice_result[1]:
  story_line=2
  choice_result=generator_choice()

#use the difference in storylines in if statement according to previous path
#2nd Branch - Choices from backdoor
if choice_result[0] and story_line==1:
  story_line=2
  npc_text("ok wait let me make my way there")
  sleep(2)
  choice_result=generator_choice()
elif choice_result[1] and story_line==1:
  story_line=3
  npc_text_happy("better to keep an eye on him I guess")
  npc_text("ok let me make my way up")
  sleep(2)
  npc_text_scared("I can hear him...")
  npc_text_scared("he is in my room.")
  confidence_change(10,"decrease")
  npc_text("I don't think he has heard me yet though")
  npc_text("I can tiptoe back out")
  npc_text("or...")
  npc_text_happy("I can get a leg up")
  npc_text("and lock him in.")
  choice_result=choice_msg("lock him in","go back","lock","back")

#2nd Branch - Choices from Generator
#Choices from escape
if choice_result[0] and story_line==2:
  npc_text_scared("alright... here goes nothing")
  npc_text("I hear the floorboards creaking upstairs...")
  npc_text("the front door is closest")
  npc_text("but I have to jump the gate")
  npc_text("Ok, I got this, run like hell")
  npc_text_scared("...and don't look back.")
  sleep(1)
  npc_text("OH SHI-")
  str(input(user[0]))
  if confidence<50:
    npc_text("Sorry- I slipped in the mud")
    npc_text_scared("OH NO-NO-NO")
    npc_text_scared("HE IS HERE")
    ending()
  else:
    npc_text("I almost slipped in mud")
    npc_text_happy("but I am out")
    confidence_change(10,"increase")
    npc_text("What do I do now?")
    choice_result=choice_msg("knock at someone's door","hide in forest","knock","hide")
    #knock on someone's door
    if choice_result[0]:
      sleep(1)
      npc_text("Ok I am knocking right now")
      npc_text("WAIT THEY'RE HOME")
      confidence_change(20,"increase")
      npc_text_happy("THANK GOD! PLEASE HELP ME")
      npc_text_scared("YES THERE'S THIS MAN IN MY HOUSE")
      sys_message("2 minutes later")
      npc_text_happy("YES, THANK YOU SO MUCH")
      npc_text_happy(f"{user_name}, I think I am safe now")
      npc_text_happy("Thank you for everything")
      npc_text("I hope I get to meet you sometime")
      npc_text_happy("Goodbye...")
      ending()
    #hide in forest
    elif choice_result[1]:
      npc_text("Ok the forest is straight ahead")
      sleep(1)
      npc_text("I n-need to be probably exercise more often")
      npc_text("this is farther than I thought")
      npc_text_scared("Damn- the forest is scary at night")
      npc_text_scared("not to mention cold")
      npc_text("I remember learning how to start a fire in boy scouts")
      npc_text("That could be helpful...")
      choice_result=choice_msg("light a fire","find shelter","fire","shelter")
      #set fire
      if choice_result[0]:
        npc_text("Ok I will try to find some wood")
        sleep(1)
        sys_message("15 minutes later")
        npc_text("Ok I got a fire")
        npc_text("Maybe I'll just stay here the night")
        npc_text_scared("Wait I hear something...")
        npc_text("I think he found me...")
        npc_text_scared("AHHHHH-")
        npc_text("OH SHI- I am sorry")
        npc_text("I thought you were someone else sir...")
        input(str(user[1]))
        npc_text_happy("It was a police officer")
        confidence_change(20,"increase")
        npc_text("They arrived at my house but he is gone...")
        npc_text_happy("Luckily the fire alerted them of my position")
        npc_text(f"{user_name}...")
        npc_text("I can't thank you enough for helping me...")
        npc_text_happy("I hope to meet you one day")
        npc_text_happy("Goodbye.")
        ending()
      #go further into forest
      elif choice_result[1]:
        npc_text("Ok I will go further in")
        npc_text("I m going to catch my breathe until then")
        sys_message("5 minutes later")
        npc_text("S-so c-cold")
        npc_text_scared("I n-need t-to clo-close e-eyes")
        npc_text_scared("S-sleep...")
        sleep(1)
        sys_message("Hypothermia is a thing")
        ending()
#stay in basment
elif choice_result[1] and story_line==2:
  npc_text("Ok that's safer for now")
  npc_text("It's dark in here...")
  npc_text("And I can't hear him anymore")
  npc_text_scared("What if he is waiting for me to come upstairs?")
  npc_text_scared("the thought makes me shiver.")
  confidence_change(10,"decrease")
  npc_text("This old phone surprisingly has a flashlight")
  npc_text_scared("and the man seems to be quite stealthy")
  npc_text("light could mean revealing our location or our safety")
  choice_result=choice_msg("turn it on","keep it off","on","off")
  #turn flashlight on
  if choice_result[0]:
    npc_text("Better to see him coming then not see at all")
    npc_text("Wait, now that I can see...")
    npc_text_scared("There are cameras here...")
    npc_text_scared("I need to get out of the house now.")
    npc_text("He knows where I was the whole time")
    npc_text("He is trying to trap me.")
    npc_text_scared("I was dead the minute I decided to stay here.")
    npc_text_scared("NO-")
    ending()
  elif choice_result[1]:
    npc_text("Right, safer that way")
    npc_text("Well, I am going to find a corner to sit in")
    npc_text("Wait what is this?")
    npc_text_scared("WAIT NO-")
    ending()
#3rd branch - Choices from upstairs
if choice_result[0] and story_line==3:
  npc_text("Ok I need to get closer without being heard")
  npc_text("I can see him...")
  npc_text("He is... just staring out the window?")
  npc_text_scared("Wait...")
  npc_text_scared("he is looking at me from the reflection...")
  confidence_change(10,"decrease")
  npc_text_scared("There's not many options left now...")
  choice_result=choice_msg("fight him","stall him","fight","stall")
  #fight - get 2 out of 3 choices right to win
  if choice_result[0]:
    npc_text("This has to be one of my dumbest ideas")
    npc_text("Alright guide me through this")
    sys_message("Get 2 out of 3 choices right")
    choice_result=choice_msg("fight aggressive","fight defensive","aggressive","defensive")
    npc_text_scared("HE HAS A KNIFE-")
    npc_text_scared("WHY AM I SUPRISED")
    if choice_result[0]:
      npc_text_scared("my-my arm...")
      npc_text_scared("he got me...")
      confidence_change(10,"decrease")
    elif choice_result[1]:
      npc_text_happy("good thing I went defensive")
      confidence_change(10,"increase")
    npc_text_scared("INCOMING KNIFE ATTACK.")
    choice_result=choice_msg("duck","deflect","duck","deflect")
    if choice_result[0]:
      confidence_change(10,"increase")
      npc_text_happy("HA. HE THOUGHT")
    elif choice_result[1]:
      confidence_change(10,"decrease")
      npc_text_scared("AH, My- Shoulder...")
    npc_text("Enough play.")
    stalker_text("Agreed.")
    choice_result=choice_msg("get him in a choke","use his knife on him","choke","knife")
    if choice_result[0]:
      confidence_change(10,"decrease")
      npc_text_scared("HE STILL HAS THE DAMN KNIFE")
    elif choice_result[1]:
      confidence_change(10,"increase")
      npc_text_happy("GOOD THINKING")
      npc_text_happy("He's wounded")
    if confidence >=50:
      npc_text_happy("I GOT HIM.")
      npc_text_happy("HE FELL UNCONCIOUS!")
      npc_text_happy("I THINK I HEAR THE POLICE TOO")
      npc_text_happy("THANK YOU SO MUCH")
      npc_text_happy(f"I'll never forgot this, {user_name}")
      ending()
    else:
      npc_text_scared("I-, I have too much blood pouring")
      npc_text_scared("I can't s...")
      ending()
  #stall
  elif choice_result[1]:
    npc_text("Ok the police should be here soon")
    npc_text("What's the point, when you can run?")
    stalker_text("You should be the one running...")
    npc_text_scared("Who are you?")
    stalker_text("just someone trying to have fun")
    stalker_text("Like I will with you now")
    stalker_text(f"and with you, {user_name}, next.")
    stalker_text("Now run, so I can catch you")
    ending()
#Sneak back from upstairs
elif choice_result[1] and story_line==3:
  npc_text("I'll just retrace my steps...")
  npc_text_scared("WHY ARE THE FLOORBOARDS SO CREAKY")
  npc_text_scared("He definitely heard me")
  confidence_change(10,"decrease")
  npc_text("Alright, time to run")
  npc_text("Where should I go?")
  choice_result=choice_msg("kitchen","bathroom","kitchen","bathroom")
  if choice_result[0]:
    npc_text("Alright I am going to get a knife")
    npc_text("to defend myself...")
    npc_text("He is coming...")
    npc_text_scared("I have to make a stand")
    stalker_text("Put the knife down kid")
    sys_message("Get 2 out of 3 moves right")
    choice_result=choice_msg("go for the ribs","go for the neck","ribs","neck")
    if choice_result[0]:
      confidence_change(10,"increase")
      npc_text_happy("I GOT HIM")
    elif choice_result[1]:
      confidence_change(10,"decrease")
      npc_text_scared("GAH. He turned it on me.")
    choice_result=choice_msg("slash his thigh","kick his balls","thigh","kick")
    if choice_result[0]:
      confidence_change(10,"decrease")
      npc_text_scared("He's too quick...")
    elif choice_result[1]:
      confidence_change(10,"increase")
      npc_text_happy("OOh... I can feel that")
    choice_result=choice_msg("throw the knife at him","charge","throw","charge")
    if choice_result[0]:
      confidence_change(10,"increase")
      npc_text_happy("How- how did that work?")
    elif choice_result[1]:
      confidence_change(10,"decrease")
      npc_text_scared("Gah, that hurts.")
    if confidence >=50:
      npc_text_happy("HA HE'S DOWN.")
      npc_text_happy("I HEAR THE POLICE SIRENS TOO")
      npc_text_happy(f"THANK YOU SO MUCH {user_name}")
      npc_text_happy("Goodbye, hope to see you some day.")
      ending()
    else:
      npc_text_scared("Ah... it hurts so much")
      npc_text_scared("I-I...")
      ending()
  elif choice_result[1]:
    npc_text("Ok I looked myself in the bathroom")
    npc_text_scared("Wait...")
    npc_text_scared("HOW DOES HE KNOW WHERE I AM")
    npc_text("He must have cameras")
    stalker_text("HERE COMES JOHNNY")
    npc_text_scared("Great I am dying to a \'The Shining\' Fan")
    npc_text_scared(f"Well... Thank you {user_name}")
    npc_text("Even if I didn't make it...")
    ending()


