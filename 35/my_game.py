
print("Welcome to THE SUPERNATURALS! The game where you dodge agile supernatural creatures whilst completing quests and finding out the truth about yourself.")
print("Before we start, let's go through the rules so you know how to attack, wield and defend yourself if ever ambushed")
j="jump".upper()
jj="double jump".upper()
b="backpack".upper()
o="oak stake".upper()
w="wolfsbane".upper()
s="swing".upper()
k="kick".upper()
t="thyme".upper()
wo="wielding oak stake".upper()
wt="wielding thyme".upper()
ww="wielding wolfsbane".upper()
pythonshell = 0
continue_with_game = 0
#Listing rules and how to activate certain herbs to harm/kill
print("""
    j - jump,
    jj - double jump,
    b - see your backpack,
    o - oak stake, (Stake a vampire in the heart to kill them),
    t - thyme, (use against vampires to harm/kill - affects younger vampires more, older vampires less as they've bilt up a tolerance to it),
    w - wolfsbane, (use against werewolves, affects them in the same way thyme affects vampires),
    s - swing
    k - kick
    wo - wield oak stake,
    wt - wield thyme,
    ww - wield wolfsbane""")
#Want to lock double jump feature as character does not know that they are a hybrid yet-activated when they realise


continue_game = input("Press C to Continue: ").upper()
#Transition into actual game - choices start, meet characters etc.
if continue_game == "C":
        print("")
        print("CHECKPOINT 1")
        print("You wake up in a dumpster, unaware of where you are. You look around trying to find something that looks familiar to you but you don't recognise anything. You start to panic and then you hear two men coming your way. You decide to keep quiet to try and figure out where you are and what happened.")
        print("You feel something poking you and see a wooden stake of some sort. You stuff it in your pants just in case you might need it as a weapon.")
        print("~OAK STAKE ACQUIRED. NOW KEPT IN INVENTORY~")
        print("Hey man, do you think that munch woke up yet?")
        print("Munch?? You feel your blood start to boil. Who do they think they are?")
        print("Hahahaha let's go check, hopefully he is, need someone to take my anger out on")
        print("Wow wow whatever you do, make sure that you don't harm him too much, or else Gunnar will kill us")
        print("Ohh yeah, shucks. Do you know why he wants him so bad?")
        print("No idea man, but he threatened my family so I didn't ask any questions")
        print("You hear them rounding the corner and you feel your anger start to bubble over and begin to see red. You're losing control. Five more steps, four, three...")
        print("You crack your eyes open a little and find two large, tall men headed your way")
        print("-CHOICE BREAK-")

def redo():
        print("Do you choose to;")
        print("A - Remain quiet and act like you're still not awake or")
        print("B - Jump out of the dumpster and attack the two guys")
       
        A="You chose to remain quiet and act like you're still not awake"
        B="You chose to jump out of the dumpster and attack the two guys"

        choice = input("Enter A or B:").upper()

        if choice == "B":
                print("Oh no, you chose to attack the two men but acting rashly, they killed you")
                print("JOE WHAT'D YOU DO?! GUNNAR TOLD US TO NOT KILL THE BOY!!!")
                print("I don't know man, I just saw red and attacked")
                print("What're we going to do?")
                print("YOU DIED,you have now lost a life")
                redo()
                
        elif choice == "A":
                print("You have chosen to remain in the dumpster and act as if you are still unconscious. You do not die")
                print(".....")
                checkpoint_2()
                
        else:
                print("Please choose either A or B")
                

def checkpoint_2():
        print("")
        print("CHECKPOINT 2")
        print("The two men, grab you by your arms and hoist you up. 'let us get him to Gunnar before he wakes up.' says one of them.")
        print(".....")
        print("You open your eyes slightly. You find yourself in an abandoned building, and the two men who brought you are talking to a big, hefty man. The man stares at you, noticing that you're awake.")
        print("'Ahhh! Welcome my friend. I'm Gunnar, and I'm under special orders to deliver you to... well, you'll see' he says with a smirk.")
        print("You get up, and see that there's an open door, just a few steps from where you are. It seems like no one is guarding it either.")
        print("-CHOICE BREAK-")
        print("Do you choose to;")
        print("A - Make a run for it or")
        print("B - Stay put and not risk it")

        A="You chose to make a run for it"
        B="You chose to stay put and not risk it"

        choice = input("Enter either A or B: ").upper()

        if choice == "A":
                print("You chose to run for the door. You're halfway there when Gunnar appears right in front of you, even though he was further away from the door than you were. He looks frustrated and pinches the bridge of his nose.")
                print("I suggest that if you want to live a little longer, you don't do anything risky.")
                print("You're confused. How did he get to the door before you. He sees the confusion on your face and laughs.")
                checkpoint_3()

        elif choice == "B":
                print("You chose to stay put and not risk it. Gunnar tilts his head and looks at you and in one swift jump, lands right in front of you.")
                print("You look at him, terrified. What is he? How did he do that? Who exactly are these people?")
                print("He sees the look of terror on your face and laughs")
                checkpoint_3()

def checkpoint_3():
        print(".....")
        print("'Joe, Wes,' he says, looking at the two men who brought you in.'Did you not tell the boy who he's dealing with?'")
        print("'No sir.' answers Joe. 'He wasn't awake yet'")
        print("Gunnar looks at you again. 'You'd think for a werewolf he'd know about his sworn enemies.' He sighs. 'I'm a vampire kid. One of the old vampires. Around 5500 years old. And you, you're a werewolf... well part werewolf. I don't know, you still have to trigger your curse'")
        print("What does he mean werewolf. Curse? What is he on about?")
        print("With skepticism, you ask him 'What do you mean curse. an-and werewolves? I'm human. I'm not a-a freak. That's you guys.'")
        print("Gunnar looks at you. 'Kid, once in ten years, the werewolf curse, or werewolf gene is passed into a family line. 3 years ago, the werewolf gene was passed into your family. And your grandfather umm Don, was it? He killed someone, and triggered the curse, fated to turn into a werewolf every full moon and ultimately being a prisoner to the moon'")
        print("'You're lying. I don't believe you,' you reply")
        print("I don't need you to. I don't even want you. It's Erik that wants you. Apparently you're the only one in your family line that hasn't turned yet and he wants a new hybrid, so here you are. My job is to get you to kill someone'")
        print("He smiles at you, sinisterly. You back away from him. He's lying. He must be. You won't kill anyone and you know that.")
        print("Gunnar throws you in a cellar to keep you quiet until Erik comes. You wait there and see some herbs in the corner. You're hungry so you try eating some. You grab a handful and put them in your mouth but spit it out as your throat starts to burn. You try the other one and feel fine. You're confused. What are they?")
        print("You decide that they might be poisonous and stuff some into your pocket just in case. You collect a handful of one of the herbs and as you go to grab the other one, it burns you again. You decide to leave it behind")
        print(".....")
        print("Two hours pass and Gunnar returns with an old man following behind him.")
        print("'Ok boys, Erik will be here in twenty minutes, let's get this show on the road.'")
        print("'Oi, you' he points at you. 'I need you to kill this man and don't worry I impelled him to be quiet and not be scared.'")
        print("Your eyes widen and you respond 'Absolutely not'")
        print("'Look kid' responds Gunnar, 'You're really starting to get on my nerves. So either you kill this man right now, or I can kill your best friend Jonathan. The choice is yours'")
        print("Gunnar holds up a phone where Wes is currently stalking Jonathan.")
        print("-CHOICE BREAK-")
        print("Do you choose to;")
        print("A - Kill the old man or")
        print("B - Let Wes kill your best friend Jonathan")

        A="You chose to kill the old man"
        B="You chose to let Wes kill your best friend Jonathan"

        choice = input("Enter either A or B: ").upper()
        
        if choice == "A":
                print("You chose to kill the old man")
                print("You wait a beat. Fine, give me a knife. I'll kill the man.")
                print("Gunnar smiles, 'There we go, he has a brain'. He throws you a knife and you catch it, blade first, blood dripping from your hand.")
                print("You see Joe start to lose control and try to come for you, for your blood.")
                print("Gunnar holds him back. 'KILL HIM KID.'")
                print("You look at the man. 'I'm so sorry'")
                print("You drive the knife straight through his heart. He stares at you, and you see the light leave his eyes.")
                print("Guilt overwhelms you, but Gunnar approaches you and pats you on the back. 'Attaboy'")
                print("You shake his hand off of you and then you feel something happening to you.")
                print("You start to levitate, the moon appears out of nowhere, shining through a crack in the ceiling. You feel small fangs starting to come in. The wound on your hand starts to heal, you feel stronger, angrier, and more overwhlemed by what you just did.")
                checkpoint_4()
                
        elif choice == "B":
                print("You chose to let Wes kill your best friend")
                print("'YOU'RE BLUFFING. WES CAN'T POSSIBLY BE THERE, HE WAS HERE LIKE TEN MINUTES AGO.' you shout.")
                print("'He's a vampire boy, he can get anywhere in an eighth of the time that you can.'")
                print("Gunnar gives Wes a signal, and in one swift move, Wes drops the camera, and you can see him dig into Jonathan's coronary artery, blood pouring everywhere.")
                print("'You chose wrong boy, you're going to have to kill this man either way.' He steps towards you and looks into your eyes. 'I want you to kill this man'")
                print("You repeat after him. 'I will kill this man'")
                print("You grab the knife and head towards the man. You lift your hand up and stab him, in his heart. Every part of your screams don't do this, but for some reason, you feel like you need to. You see the light leave his eyes as he falls into you.")
                print("Guilt overwhelms you, but Gunnar approaches you and pats you on the back. 'Attaboy'")
                print("You shake his hand off of you and then you feel something happening to you.")
                print("You start to levitate, the moon appears out of nowhere, shining through a crack in the ceiling. You feel small fangs starting to come in. The wound on your hand starts to heal, you feel stronger, angrier, and more overwhlemed by what you just did.")
                checkpoint_4()

def checkpoint_4():
        print("'There he is. Finally!!'")
        print("You feel stronger, better, more agile. You think you can take them.")
        print("-CHOICE BREAK-")
        print("Do you choose to;")
        print("A - Take them on and try to escape.")
        print("B - Stay put and not try anything risky.")

        A="Take them on and try to escape"
        B="Stay put and not try anything risky"

        choice = input("Enter either A or B: ").upper()

        if choice == "A":
                print("You chose to take them on and try to escape")
                print("You leap at Gunnar")
                print("Gunnar reacts quickly. He moves out of the way and stares at you with shock. His face hardens and he swings at you.")

                choice = input("Do you want to jump (j) or double jump (jj)?: ")

                if choice == "j":
                        print("'jump'")
                        print("You land in front of him and snarl")
                elif choice == "jj":
                        print("'double jump'")
                        print("You jump over him and snarl")

                choice = input("Do you want to swing (s) or kick (k) Gunnar?: ")

                if choice == "s":
                        print("'swing'")
                        print("You hit Gunnar sqaure in the chest with all your strength. He stumbles back and you smirk, thinking you have the upper hand now.")
                        print("However, he recovers in 0.1 seconds like nothing happened and comes at you.")
                elif choice == "k":
                        print("'kick'")
                        print("You move your leg up to kick Gunnar but he catches it and flips you with all his strength. You flip in the air but manage to land on your feet.")
                print("'You're really starting to get on my nerves kid' yells Gunnar")
                print("He closes in on you and hits your ribs. You fall to the ground, clutching your side. You feel something poking you and remember the stake that you found in the dumpster. At the same time, you remember the herbs you found in the cellar. You're not sure if either of them will hurt him, but they're the only weapons you have.")

                choice = input("Do you want to use the oak stake (wo) or use the herbs (wt) you found in the cellar?: ")
                if choice == "wo":
                        print("'wielding oak stake'")
                        print("You pull out the stake and Gunnar's eyes widen.")
                        print("'WHERE THE HELL DID YOU FIND THAT?'")
                        print("Joe moves in going to help Gunnar but you stab him in the gut and pull the stake out.")
                        print("Gunnar falls to the side in pain.")
                elif choice == "wt":
                        print("'wielding thyme'")
                        print("You pull out the herbs you found and Gunnar's eyes widen.")
                        print("'WHERE THE HELL DID YOU FIND THAT?'")
                        print("Joe moves in going to help Gunnar but you crush the herbs in ypur hand and press it onto Gunnar's face.")
                        print("Gunnar falls to the ground in pain, clutching his face, screaming.")
                print("You hear someone clapping. You look to the side, at the entrance of the building and see a lean, tall man with blonde hair. He stands there, staring at you and just...clapping.")
                print("'Very impressive. You'll make quite a fierce hybrid.' he says with a smirk.")
                print("Erik looks at him. 'Stand' he commands. Joe stands, scared out of his mind.")
                print("'Gunnar was fighting this young man, and you just stood to the side watching? You didn't feel the need to go and help him. To keep the boy quiet'")
                print("'Sorry sir. I-i' replies Joe, stuttering and unable to form a sentence. Erik looks at him, hands clasped behind his back and one eyebrow raised, waiting expectantly for his answer.")
                print("'Nevermind' he interrupts, 'you've done your part. You are of no use to me anymore.' And with one swift move, Erik sticks his hand into Joe's body and grabs his heart")
                print("Joe falls to the ground. Dead. You look at Erik with absolute terror.")
                print("'Well, he was always useless. Thank god he's dead.' He looks at you. 'You're an exceptional fighter. I'm excited for you to join my family' he says, smiling calmly")
                print("'So, shall we move on with the process for this to happen?'")
                print("'What're you going to do to me?' you say")
                print("He looks at you, 'Oh, you must be the boy, did Gunnar not inform you? That's quite rude.' He looks at Gunnar, who stands, though he's still bleeding. 'I'm just going ot feed you my blood, you'll go through an excruciating process and may possibly die if you're not strong enough.'")
                checkpoint_5()

        elif choice == "B":
                print("You chose to stay put and not try anything risky")
                print("Gunnar stares at you.")
                print("'I'll admit, that was kinda cool' he says.")
                print("You snarl and then hear someone walking into the abandoned house. You look up and see a lean, tall man with blonde hair.")
                print("Joe moves to him and kneels.")
                print("'Hello Master Erik.'")
                print("Erik. You remember Gunnar mentioning him. The one who wanted to turn you into a... hybrid..?")
                print("You don't wait for a second. 'What're you going to do to me?' you say")
                print("He looks at you, a twinkle in his eyes, 'Oh, you must be the boy, did Gunnar not inform you? That's quite rude. I'm just going ot feed you my blood, you'll go through an excruciating process and may possibly die if you're not strong enough.'")
                checkpoint_5()

def checkpoint_5():
        print("'Strong enough for what?' you reply.")
        print("'Strong enough to handle my blood. Strong enough to become a hybrid. Half vampire, half werewolf.' states Erik")
        print("You're fuming. You never wanted any of this. You want your old life back. Going to school, watching TV shows. Your parents coming in, yelling at you for not doing your homework")
        print("Erik walks down the steps and stands right in front of you.")
        print("He bites his wrist and moves it to your mouth, trying to make you drink it.")
        print("-CHOICE BREAK-")
        print("Do you choose to;")
        print("A - Force him off of you and try to kill him")
        print("B - Allow him to feed you his blood and possibly die.")

        A="Allow him to feed you his blood and possibly die"
        B="Force him off of you and try to kill him"

        choice=input("Enter either A or B: ").upper()

        if choice == "A":
                print("You chose to allow Erik to feed you his blood and possibly die.")
                print("You struggle but then decide that there's no point")
                print("Erik smiles and you drink the blood from his wrist.")
                print("You immediately feel a stab in your chest, and fall to the ground. You feel like you're suffocating, your vision becomes blurry and your heartbeat slows. You look up at Erik and he seems disappoionted and worried.")
                print("You cough up blood. You feel your end coming closer.")
                print("You see Erik turn his back on you, as if he can't bear to watch you die. You take your last breath and feel tears streaming down your face. As you close your eyes, you think of your family, your little sister, your best friend. The last person you see is the old man you killed, and the light leaving his eyes.")
                print("-THE END-")
        elif choice == "B":
                print("You chose to force Erik off of you and try to kill him.")
                print("You snarl at Erik and use all your strength to push him off.")
                print("He falls backwards")

                choice=input("Do you want to swing (s) or kick (k) Erik: ")
                
                if choice == "s":
                        print("'swing'")
                        print("You close in on Erik and go to hit him in the face.")
                        print("He blocks your hit and gets up. He hits you and you fall to the floor")
                elif choice == "k":
                        print("'kick'")
                        print("You close in on Erik and go to kick him in the ribs")
                        print("He grabs your foot and flips you. He then stands up and kicks you.")
                print("You feel something next to you. You realise that they're the herbs and in the corner of your eye see the stake.")

                choice=input("Do you want to use the oak stake (wo) or the thyme (wt)?: ")

                if choice == "wo":
                        print("'wielding oak steak'")
                        print("You move and grab the oak stake. Erik charges at you and you run towards him. You plunge the stake through his heart and he howls. He falls back, writhing in pain")
                        
                elif choice == "wt":
                        print("'wielding thyme'")
                        print("You grab the thyma and crush it, as Erik comes at you, you throw a handful of it onto his face. He falls to the ground, screaming, you go towards him and force the rest down his throat.")
                        print("He starts coughing up blood.")

                        choice=input("Do you want to use the oak stake (wo) or leave it behind and leave (l): ")
                        if choice == "wo":
                                print("'wielding oak stake'")
                                print("You run to the stake, grab it and plunge it into Erik's heart for good measure")
                                checkpoint_6()
                        elif choice == "l":
                                print("You leave the building, running and running.")
                                print("As you look behind you, you see Erik, staggering out of the bulding, still coughing, he looks at you and starts walking towards you. You don't stop, even for a minute, you keep going, your heart pounding.")
                                print("-THE END-")

def checkpoint_6():
        print("You get up and run out of the building. You keep running until you feel a safe distance from it. You fall to the ground and cry, holding your head in your hands. The events that happened the past day start flooding into your mind and you start to break down.")
        print("THE END")
                                

                
                
        
                        
                

        

redo()
