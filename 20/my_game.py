# LAKSHMINARAYANAN, HARINI
import stdiomask
print("Before playing this game, here are a few things you must do:")  #tells the players this MUST be taken into action prior to playing this game
print("1. You MUST install stdiomask, by running the following command: pip install stdiomask")
print("2. Double click on the file. Do not play via Idle.")
set_of_instructions = input("Press 'I' for Instructions OR Press 'P' to proceed to game: ") #communication - what does the player need to do?
after_instructions = ("Press 'C' to continue: ")

if set_of_instructions == "I":
    print("~ This is a 2 player game ~")               #this is the set of instructions which will be displayed when the capital 'I' is pressed
    print("• Hawks, pumas and snakes have not been fed for seemingly forever...") #(these 4 lines including previous line describes the game background & as well as how to play)
    print("• Player 1 and Player 2 have a choice of a hawk (H), puma (P) or snake (S).")
    print("• Those animals will have a battle to the death!")
    print("• If your animal eats the other Player's selected animal, you win!")
    print("• Snake loses against Hawk, Hawk loses against Puma, Puma loses against Snake.")
    print("**NOTE: IF BOTH PLAYERS SELECT THE SAME ANIMAL, NO POINTS ARE REWARDED TO EITHER PLAYER**")
    userinput1 = input(after_instructions)             #another variable is assigned for the user's input because it needs to collect the information typed in
    if userinput1 == "C":
        print("Let's Start!")
    else:
        print("Only 'C' can be pressed to proceed!!")
elif set_of_instructions == "P":                       #if user does not want to view instructions they can go to the game straight away (also saves time and space)
    print("Let's Start!")
else:                                                  #if user does not press either keys then this message below will appear, which notifies them saying they must press I or P+
    print("• Only 'I' or 'P' can be pressed to proceed •")

'''
        Hawk     Snake    Puma
Hawk     0         -1       1
Snake    1          0      -1
Puma    -1          1       0

''' 

player1_score = 0 #setting each player's score at 0 before the game starts
player2_score = 0

# if selected animals is same, no points are rewarded
# snake loses against hawk   # hawk wins against snake
# puma wins against hawk     # puma loses against snake



player1 = input("What is your name, Player 1? ") #we need to ask the user what their name is so we can refer to them that way
player2 = input("What is your name, Player 2? ") #if we didn't ask, the players could possibly forget who Player 1 and Player 2 are, out of each other


# player1_choice =  stdiomask.getpass(player1 + " , select an animal out of Hawk, Puma or Snake: ").upper()
# player2_choice =  stdiomask.getpass(player2 + " , select an animal out of Hawk, Puma or Snake: ").upper()

# if player1_choice == player2_choice:
#     print("Both animals survived!")
#     print(player1 + " and " + player2 + " both played " + player1_choice)
#     print("Score:")
#     print("Player 1: {}".format(player1_score))
#     print("Player 2: {}".format(player2_score))
# elif player1_choice.upper() == "H":
#     if player2_choice.upper() == "P":
#         print(player2 + " " + "claims victory.")
#         print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
#         print("Score:")
#         player1_score=player1_score + 0
#         player2_score=player2_score + 1
#         print("Player 1: {}".format(player1_score))
#         print("Player 2: {}".format(player2_score))
        
#     else:
#         print(player1 + " " + "claims victory.")
#         print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
#         print("Score:")
#         player1_score=player1_score + 1
#         player2_score=player2_score + 0
#         print("Player 1: {}".format(player1_score))
#         print("Player 2: {}".format(player2_score))
# elif player1_choice.upper() == "P":
#     if player2_choice.upper() == "S":
#         print(player2 + " " + "claims victory.")
#         print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
#         print("Score:")
#         player1_score=player1_score + 0
#         player2_score=player2_score + 1
#         print("Player 1: {}".format(player1_score))
#         print("Player 2: {}".format(player2_score))
#     else:
#         print(player1 + " " + "claims victory.")
#         print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
#         print("Score:")
#         player1_score=player1_score + 1
#         player2_score=player2_score + 0
#         print("Player 1: {}".format(player1_score))
#         print("Player 2: {}".format(player2_score))
# elif player1_choice.upper() == "S":
#     if player2_choice.upper() == "H":
#         print(player2 + " " + "claims victory.")
#         print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
#         print("Score:")
#         player1_score=player1_score + 0
#         player2_score=player2_score + 1
#         print("Player 1: {}".format(player1_score))
#         print("Player 2: {}".format(player2_score))
#     else:
#         print(player1 + " " + "claims victory.")
#         print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
#         print("Score:")
#         player1_score=player1_score + 1
#         player2_score=player2_score + 0
#         print("Player 1: {}".format(player1_score))
#         print("Player 2: {}".format(player2_score))
# else:
#     print("Invalid play. Check spelling. MUST BE CAPITAL 'H', 'P' or 'S'")


def isPositiveInt(n):
  try:
    if int(n)>0:
      return True
  except:
    return False


#     requested_rounds
# if requested_rounds >= "2" and <= "11":


def play_game(play_round,player1_score, player2_score):   #here I defined a function, and essentially what it does is repeat the rounds (depending on user's request)
    # if(play_round==1):
    #     print("ROUND 1")
    if play_round == int(requested_rounds) + 1: #this is the limit - the python game cannot print more rounds than what the players' choice
        print("Game Over!")
        return
    proceed_round = input("Let's proceed to Round {}! To continue, press '{}'. To quit, press 'Q': ".format(play_round,play_round)) #at the beginning of every round, this section will run
    if proceed_round == str(play_round):
        player1_choice =  stdiomask.getpass(player1 + ", select an animal out of Hawk, Puma or Snake: ").upper()
        player2_choice =  stdiomask.getpass(player2 + ", select an animal out of Hawk, Puma or Snake: ").upper()
        if player1_choice == player2_choice:
            print("Both animals survived!")
            print(player1 + " and " + player2 + " both played " + player1_choice)
            print("Score:")
            print("Player 1: {}".format(player1_score))
            print("Player 2: {}".format(player2_score))
        elif player1_choice.upper() == "H":
            if player2_choice.upper() == "P":
                print(player2 + " " + "claims victory.")
                print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
                print("Score:")
                # player1_score=player1_score + 0
                player2_score=player2_score + 1
                print("Player 1: {}".format(player1_score))
                print("Player 2: {}".format(player2_score))
            else:
                print(player1 + " " + "claims victory.")
                print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
                print("Score:")
                player1_score = player1_score + 1
                # player2_score=player2_score + 0
                print("Player 1: {}".format(player1_score))
                print("Player 2: {}".format(player2_score))
        elif player1_choice.upper() == "P":
            if player2_choice.upper() == "S":
                print(player2 + " " + "claims victory.")
                print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
                print("Score:")
                # player1_score=player1_score + 0
                player2_score=player2_score + 1
                print("Player 1: {}".format(player1_score))
                print("Player 2: {}".format(player2_score))
            else:
                print(player1 + " " + "claims victory.")
                print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
                print("Score:")
                player1_score=player1_score + 1
                # player2_score=player2_score + 0
                print("Player 1: {}".format(player1_score))
                print("Player 2: {}".format(player2_score))
        elif player1_choice.upper() == "S":
            if player2_choice.upper() == "H":
                print(player2 + " " + "claims victory.")
                print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
                print("Score:")
                # player1_score=player1_score + 0
                player2_score=player2_score + 1
                print("Player 1: {}".format(player1_score))
                print("Player 2: {}".format(player2_score))
            else:
                print(player1 + " " + "claims victory.")
                print(player1 + " played " + player1_choice + ", " + player2 + " played " + player2_choice)
                print("Score:")
                player1_score=player1_score + 1
                # player2_score=player2_score + 0
                print("Player 1: {}".format(player1_score))
                print("Player 2: {}".format(player2_score))
        else:
            print("Invalid play. Check spelling. MUST BE CAPITAL 'H', 'P' or 'S'")
    elif proceed_round == "Q": #if the user accidentally types in a large number of rounds they wish to play or perhaps just want to stop playing, the following will print
        print("Thanks for playing!")
        print("Here are the final scores: ")
        print(player1_score)
        print(player2_score)
        return
    else:
        print("Check spelling. Only P or Q is acceptable.")
    play_game(play_round+1,player1_score,player2_score)

requested_rounds = input("How many rounds do you wish to play? ") #the players will have a choice of how many rounds they wish to play, instead of having a set number
if isPositiveInt(requested_rounds) ==False:
    print('test')
else:
    play_game(1,player1_score,player2_score,)
