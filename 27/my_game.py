# Lucas Bird
# fighting game

# importing the random library, to make random variables in future
import random
# setting the health values for the player
player_head = 10
player_arms = 5
player_legs = 6
fight = "active"

difficulty_choice = input("Welcome to The Ring. Choose your difficulty. Type 1 for easy, 2 for moderate, 3 for hard: ")

# giving the player a choice of what difficulty they want to play on
if difficulty_choice == "1":
    difficulty = 1
elif difficulty_choice == "2":
    difficulty = 2
elif difficulty_choice == "3":
    difficulty = 3
else:
    print("ERROR: Incorrect input given, difficulty set to impossible")
    difficulty = 200


# setting the opponents health values, based on the choice of difficulty
opponent_head = 4*difficulty
opponent_arms = 2*difficulty
opponent_legs = 3*difficulty
opponent_block = "negative"

# explaining the goals for the game
print("In The Ring, your goal is to knock your opponent out.")
print("There are a certain amount of moves you can make. You can make a strike, or block.'")

# staring the fight loop, making the player and their opponent trade blows
while fight == "active":
    # making sure the player isn't constantly blocking even when throwing attacks
    player_block = "negative"
    player_input = input("What move will you make?'1' to punch, '2' to kick the legs, '3' to kick the head,"
                         "'4' to block: ")
    # if the players leg has too little health, then they cannot kick
    if player_legs < 3:
        # both kick inputs
        if player_input == "2" or player_input == "3":
            player_input = "0"
    # the first option for player input, a simple punch
    elif player_input == "1":
        # checking if the opponent has blocked an incoming attack
        if opponent_block == "block":
            print("They blocked your attack!")
        else:
            # if the players arms are too damaged, their punches don't do as much
            if player_arms < 1:
                damage = 1
            else:
                damage = 2
            # punches do a consistent 2 damage, making it more balanced than a kick
            opponent_head -= damage
            # checking the opponents head statistic and giving a different result depending
            if opponent_head == 0:
                # telling the player they won
                print("Bam! You knocked out your opponent. You win!")
                # ending the loop
                fight = "ended"
            elif opponent_head == 3:
                print("Your coach yells to you: 'They seem real hurt! I sense a KO soon!'")
            elif opponent_head == 6:
                print("Their head snaps back, they seem dazed")
            elif opponent_head == 9:
                print("They don't seem too hurt yet, it will take a few more shots to do damage")
    elif player_input == "2":
        print("You kicked their leg!")
        damage = random.randint(1, 2)
        opponent_legs -= damage
        # checking the health of the opponents legs, giving a different result depending
        if opponent_legs == 0:
            print("Their legs are really hurt! They can barely move! You doubt they will be able to kick"
                  "in the remainder of the fight.")
        elif opponent_legs == -1 or opponent_legs == -2 or opponent_legs == -3:
            opponent_leg_break = random.randint(1, 5)
            # checking the chances of a leg break
            if opponent_leg_break == 5:
                print("SNAP! Their leg breaks! The ref calls off the fight, you won.")
                fight = "ended"
            else:
                print("Your coach yells: What are you doing? They are hurt enough! Although you could break their leg")
                opponent_legs = 0
        elif opponent_legs < 4:
            print("Your opponent is hobbling really bad, they are barely able to walk")
        elif opponent_legs < 6:
            print("You can see the pain in your opponents eyes, their legs are seemingly hurt")
    elif player_input == "3":
        # checking if the opponent has blocked the attack
        if opponent_block == "block":
            print("They blocked your attack!")
        else:
            damage = random.randint(1, 3)
            # kicks have the potential to do more damage than punches
            opponent_head -= damage
            print("You kicked their head!")
            # checking the health of the opponents head, giving a different result depending on its status
            if opponent_head == 0:
                # telling the player they won
                print("Bam! You knocked out your opponent. You win!")
                # ending the loop
                fight = "ended"
            elif opponent_head == 3:
                print("Your coach yells to you: 'They seem real hurt! I sense a KO soon!'")
            elif opponent_head == 6:
                print("Their head snaps back, they seem dazed")
            elif opponent_head == 9:
                print("They don't seem too hurt yet, it will take a few more shots to do damage")
    elif player_input == "0":
        print("You try to throw a kick, but you are in too much pain")
    elif player_input == "4":
        player_block = "block"
        print("You put your hands up, protecting your head. Remember, if you block too much, your arms will be weak.")
        player_arms -= 1
    else:
        print("Remember to use numbers such as '1' or '2' to throw an attack")
    opponent_block = "negative"
    opponent_choice = random.randint(0, 3)
    # checking to see if the opponent can kick
    if opponent_legs < 1:
        # changing the input if the leg cannot kick
        if opponent_choice == 2 or opponent_choice == 3:
            opponent_choice = "Undefined"
    # checking for the opponents choice
    if opponent_choice == 1:
        # checking if the player blocked the attack
        if player_block == "block":
            print("You blocked their attack!")
        else:
            # the opponents punch does less damage if their arms are low
            if opponent_arms < 1:
                damage = 1
            else:
                damage = 2
            opponent_head -= damage
        print("Your opponent punched you!")
        # checking for the players head health, giving a different result for each value
        if player_head == 0:
            # telling the player they won
            print("Lights out! Your opponent knocked you out. Game over.")
            # ending the loop
            fight = "ended"
        elif player_head == 3:
            print("Wham! Your sight is getting hazy now, you're close to getting knocked out.")
        elif player_head == 6:
            print("Ouch! Now you're starting to hurt")
        elif player_head == 9:
            print("You are a bit dazed")
    elif opponent_choice == 2:
        print("They kicked your leg!")
        opponent_legs -= 1
        # checking for the players leg health, giving a different result for each value
        if player_legs == 0:
            print("Ow! you can barely move your leg now!")
        elif player_legs == -1:
            player_leg_break = random.randint(1, 5)
            # checking the chance, if the leg has broken
            if player_leg_break == 5:
                print("SNAP! Your leg is broken!! The ref calls off the fight, its over.")
                fight = "ended"
            else:
                print("Ouch! They're still going for your leg?")
                player_legs = 0
        elif player_legs == 3:
            print("Your leg is really hurting now, you start to hobble. You can't kick anymore.")
        elif player_legs == 5:
            print("Wham! That one hurt.")
    elif opponent_choice == 3:
        # checking if the player blocked the attack
        if player_block == "block":
            print("You blocked their attack!")
        else:
            damage = random.randint(1, 3)
            player_head -= damage
            print("Your opponent kicked your head!")
            # checking for the players head health, giving a different result for each value
            if player_head == 0:
                # telling the player they won
                print("Lights out! Your opponent knocked you out. Game over.")
                # ending the loop
                fight = "ended"
            elif player_head == 3:
                print("Wham! Your sight is getting hazy now, you're close to getting knocked out.")
            elif player_head == 6:
                print("Ouch! Now you're starting to hurt")
            elif player_head == 9:
                print("You are a bit dazed")
    elif opponent_choice == 0:
        opponent_block = "block"
        opponent_arms -= 1
    # this is the output given when the opponent attempts to kick, but cannot
    elif opponent_choice == "Undefined":
        print("Your opponent eyes you off, unsure of what move to make")
