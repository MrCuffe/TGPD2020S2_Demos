# # Snehita's Python Game at Final Submission. The following program starts off with a prologue explaining the game's current situation and the player's primary objective. To begin their quest, new-time players are allocated a Pokémon which is at random. If they wish to change Pokémon, that option is available. Once set, they enter the game's Main Menu system which carries a list of options for players to interact with. When players choose to travel to another location by selecting Option 1, they are faced with battles and Pokémon to capture. The consistency of battle numbers is randomly generated. In battle, players have the option to attack with their designated moves or escape. The chances of escaping the battle are at 50%. If unsuccessful, players lose HP. When players attack the opposing Pokémon and make the Enemy's HP >10 they have the opportunity to capture the opposing Pokémon. Successfully capturing Pokémon is set at a 30% chance. If the Pokémon is successfully captured, they will be asked to keep or release the Pokémon. There will be occasions where players cannot keep the Pokémon as they have reached their maximum collected amount, which is linked to their Level. The battle is deemed over depending on whose HP reaches >5 first. The merchandise store offers players the opportunity to buy medicinal healing potions. A potion costs $50 and will accelerate the Pokémon's HP by 30%. For the potion to be drunk Option 6 from the Menu must be selected. Options 3 and 4 in the Main Menu offers players to view their captured Pokémon and select their Pokémon for upcoming battles. Option 5 is for players to Return Home once situated in a different location. New Bark Town is the defaulted hometown for all players.

# Author: Snehita Antony
# File: Python Game Code
# Version: 4.3
# Email: ANT0001@jmss.vic.edu.au

# ENSURE TO DOWNLOAD PYGAME AND ZIP FILES ARE EXTRACTED PRIOR TO PLAYING.

# Modules
import time  # Import time module
import pygame  # Requires the download of the pygame library
import random  # Import random variable generator
import sys  # Program flow control
# Open text file;FUNCTION
list_type = open('gamedata/type.txt', 'r',
# line breaks (Value, Type);FUNCTION
                 encoding='utf-8').read().splitlines()
list_attack = open('gamedata/attack.txt', 'r',
# line breaks (Value, Type, Attack 1, Attack 2, Attack 3);FUNCTION
                   encoding='UTF-8').read().splitlines()
list_pokemon = open('gamedata/pokemon.txt', 'r',
# line breaks (Name, Type 1, Type 2, Total, HP, Attack, Defense, Special Attack, Special Defense, Speed);FUNCTION
                    encoding='utf-8').read().splitlines()
list_location = open('gamedata/locations.txt', 'r',
# line breaks (Name, Pokemon_Meter, Enemy_Enabled, PM_to_Hometown);FUNCTION
                     encoding='utf-8').read().splitlines()
list_tips = open('gamedata/tips.txt', 'r',
# line breaks (Value, Type);FUNCTION
                 encoding='utf-8').read().splitlines()

# Essential Game Variables

game_debug = 'NO'
# First Pokemon is Selected by Default (Range: 0~4)
player_pokemon_selected = 0
# Initial value - No Pokemon Owned
player_max_pokemon = 0
# 5 Pokemon Slots, default to Level 1
player_level = [1] * 5
# Initial table for name of Pokemon (Line Number only)
player_pokemon_index = ['None'] * 5
# 5 HP values for Pokemon
player_hp = [0] * 5
# 5 Experience values for each Pokemon
player_exp = [0] * 5
# Initial First Pokemon Type
player_type1 = ['None'] * 2
# Initial Second Pokemon Type
player_type2 = ['None'] * 2
# Initial First Attack Table based on Pokemon Type
player_attack1 = ['None'] * 4
# Initial Second Attack Table based on Pokemon Type
player_attack2 = ['None'] * 4
# Default location - New Bark Town  (Line Number only)
player_location_index = 0
# Player's money (Integer Value only)
player_money = 0
# Player's potion (Default to 3 when game starts)
player_potion = 3

# Enemy Pokemon Level
enemy_level = 1
# Enemy Pokemon identified
enemy_pokemon = ['None'] * 10
# Enemy HP
enemy_hp = 1
# Enemy's Pokemon Type
enemy_type1 = ['None'] * 2
# Enemy's second Pokemon Type
enemy_type2 = ['None'] * 2
# Initial table for the name of Pokemon (Line Number only)
enemy_pokemon_index = 0

# 0: Enemy Attack / 1: Player Attack; Options  ;FUNCTION
def attack(type, player_hp, enemy_hp, option):
    # Player Attacks Enemy;CONDITIONAL STATEMENT
    if type == 1:
        if player_hp > enemy_hp:
            damage = random.randint(1, int(enemy_hp * 0.5))
            enemy_hp -= damage
        else:
            damage = random.randint(int(enemy_hp * 0.5), enemy_hp)
            enemy_hp -= damage
        # BUG FIX - if Enemy HP is too low, you can't complete the battle;CONDITIONAL STATEMENT
        if enemy_hp < 5:
            damage += enemy_hp
            enemy_hp = 0
        print(f'Enemy HP has decreased by: {damage}')
        return enemy_hp
    # Enemy Attacks Player;CONDITIONAL STATEMENT
    else:
        if player_hp > enemy_hp:
            damage = random.randint(1, int(enemy_hp * 0.2))
        else:
            damage = random.randint(int(player_hp * 0.1), enemy_hp)
        # BUG FIX: negative HP damage;CONDITIONAL STATEMENT
        if player_hp < damage:
            # Make sure player_hp reaches zero
            damage = player_hp
        player_hp -= damage
        print(f'Your HP has decreased by: {damage}')
        return player_hp


def escape():
    chance = random.randint(0, 10)
    # 50% chance for the player to escape the battle;CONDITIONAL STATEMENT
    if chance < 5:
        print("Escape Unsuccessful")
        return 0
    else:
        print("Escape Successful!")
        return 1


# Main Menu for the players to explore the game;FUNCTION
def attack_menu():
    print("Your options are:")
    if player_level[player_pokemon_selected] < 5:
        print(f'1: {player_attack1[1]}')
        player_p1_attack_options = 1
        if player_type2[0] != '0':
            print(f'2: {player_attack2[1]}')
            player_p1_attack_options = 2
    elif player_level[player_pokemon_selected] < 10:
        print(f'1: {player_attack1[1]}')
        print(f'2: {player_attack1[2]}')
        player_p1_attack_options = 2
        if player_type2[0] != '0':
            print(f'3: {player_attack2[1]}')
            print(f'4: {player_attack2[2]}')
            player_p1_attack_options = 4
    # Determining Enemy's health;CONDITIONAL STATEMENT
    else:
        print(f'1: {player_attack1[1]}')
        print(f'2: {player_attack1[2]}')
        print(f'3: {player_attack1[3]}')
        player_p1_attack_options = 3
        if player_type2[0] != '0':
            print(f'4: {player_attack2[1]}')
            print(f'5: {player_attack2[2]}')
            print(f'6: {player_attack2[2]}')
            player_p1_attack_options = 6
    # Option to capture the Pokemon will appear once the Enemy's HP is <10;CONDITIONAL STATEMENT
    if enemy_hp < 10:
        print("CAP: Capture this Pokemon")
    print("ESC: Escape the battle")
    return input("What's your move?").upper().strip()


# Declare a function
def typing_effect(text, mode, newline, clear_screen, speed):
    # Sound will adapt to speed;CONDITIONAL STATEMENT
    if speed < 0.02:
        pygame.mixer.music.load('gamedata/typing_fast.wav')
    else:
        pygame.mixer.music.load('gamedata/typing_slow.mp3')
    pygame.mixer.music.play(-1)

    if clear_screen == True:
        print("\n" * 80)
    text_array = list(text)
    text_count = len(text)
    for probe in range(text_count):
        print(text_array[probe], end='')
        # The smaller the time the quicker
        time.sleep(speed)
    if newline == True:
        print("")
    pygame.mixer.music.stop()


# Initialisation of the PyGame Library;FUNCTION
def game_intro():
    pygame.init()
    # Window popped up will be 1x1 pixels in size
    pygame.display.set_mode((1, 1))
    # Open Pokemon Game Introduction text file;FUNCTION
    lines = open('gamedata/intro.txt').read().splitlines()
    if game_debug != 'YES':
        # Print the file, line by line;FUNCTION
        for probe in range(len(lines)):
            typing_effect(lines[probe], 0, True, False, 0.1)
    pygame.mixer.music.load('gamedata/morning_in_forest.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)


def game_first_run():
    global player_max_pokemon

    user_input = 'N'
    while not user_input == 'Y':
        # Randomly Select a line number from the Pokemon Library
        random_line = random.choice(range(len(list_pokemon)))
        # Store the random line into the Array
        player_pokemon_index[0] = random_line
        load_pokemon(random_line, 0, 1)
        player_max_pokemon = 1
        user_input = input("Would you like to commit to this Pokemon? Y/N ").upper()


def load_pokemon(line, reference, force_load):
    global player_type1
    global player_type2
    global player_attack1
    global player_attack2
    # Clear existing values from Array
    player_type1.clear()
    player_type2.clear()
    player_attack1.clear()
    player_attack2.clear()

    # Temporary Variable to load the Pokemon's details
    player_pokemon_current = list_pokemon[int(line)].split(',')
    # This is to ensure we are not resetting the HP if we load the Pokemon;CONDITIONAL STATEMENT
    if force_load == 1:
        # Error Correction - Integer ;FUNCTION
        player_hp[reference] = int(player_pokemon_current[4] * player_level[int(reference)])

    player_type1 = list_type[int(player_pokemon_current[1])].split(',')
    player_type2 = list_type[int(player_pokemon_current[2])].split(',')
    player_attack1 = list_attack[int(player_pokemon_current[1])].split(',')
    player_attack2 = list_attack[int(player_pokemon_current[2])].split(',')
    print(f'The Pokemon selected is:')
    print(f'Name: {player_pokemon_current[0]}; Pokemon Type: {player_type1[1]}, {player_type2[1]}')
    print(f'Pokemon HP: {player_hp[reference]}')
    print(f'Attack Moves: {player_attack1[1]}, {player_attack1[2]}, {player_attack1[3]}')
    # Avoid printing empty list;CONDITIONAL STATEMENT
    if not player_type2[1] == 'NONE':
        print(f'{player_attack2[1]}, {player_attack2[2]}, {player_attack2[3]}, ')


def main_menu():
    global player_location_index
    # Declare a temporary User Input Variable
    menu_input = 0
    while menu_input < 1:
        print("=====MAIN MENU=====")
        print("===What would you like to do?===")
        print("1. Travel to another location")
        print("2. Go Shopping!")
        print("3. Show my Pokemon")
        print("4. Select owned Pokemon")
        print("5. Return Home")
        print("6. Drink Medicinal Healing Potion")
        # Random tips for Player's ease of gameplay
        print(f'Player Tip of the Day: {random.choice(list_tips)}')
        menu_input = input("Please select from options 1~6. ")
        try:
            menu_input = int(menu_input)
        except ValueError:
            print("Invalid User Input!")
            menu_input = 0

    if menu_input == 1:
        travel_return = int(travel_menu())
        travel(travel_return)
    elif menu_input == 2:
        shop_menu()
    elif menu_input == 3:
        show_pokemon()
    elif menu_input == 4:
        select_pokemon()
    elif menu_input == 5:
        return_home()
    elif menu_input == 6:
        drink_potion()
    else:
        print("Invalid User Input!")


def shop_menu():
    global player_money
    global player_potion

    shop_decision = 'NONE'
    print("Purchasing 1x Medicinal Healing Potion will cost you $50!")
    while not (shop_decision == 'N' or shop_decision == 'Y'):
        shop_decision = input("Are you sure about your purchase? Y/N? ").upper().strip()
        if shop_decision == 'N':
            print("TRANSACTION CANCELLED!")
        # Player goes forward with the purchase and has enough money;CONDITIONAL STATEMENT
        elif shop_decision == 'Y' and player_money > 49:
            player_money -= 50
            player_potion += 1
        # Player goes forward with the purchase but does not have enough money;CONDITIONAL STATEMENT
        elif shop_decision == 'Y':
            print("You do not have enough money to go forward with this purchase!")
    print(f'Now, you have {player_potion}x potions!')
    time.sleep(3)


def drink_potion():
    global player_potion
    global player_hp
    global player_pokemon_selected
    global player_pokemon_index

    # Player has potions;CONDITIONAL STATEMENT
    if player_potion > 0:
        # Deduct the number of potions by one.
        player_potion -= 1
        # One potion will increase 30% of health, output as integer to avoid decimal HP;FUNCTION
        player_hp[player_pokemon_selected] += int(player_hp[player_pokemon_selected] * 0.30)
        # Temporary Variable to load the Pokemon details;FUNCTION
        player_pokemon_current = list_pokemon[player_pokemon_index[player_pokemon_selected]].split(',')
        # Determine the max HP for the given Pokemon as an integer;FUNCTION
        player_hp_max = int(player_pokemon_current[4] * player_level[int(player_pokemon_selected)])
        if player_hp[player_pokemon_selected] > player_hp_max:
            print("You have reached the maximum HP for your Pokemon!")
            player_hp[player_pokemon_selected] = player_hp_max
    else:
        print("You do not have enough potions!")
    print(f'The current number of potions left is: {player_potion}')
    print(f'Your new accelerated HP is: {player_hp[player_pokemon_selected]}')
    time.sleep(3)


def show_pokemon():
    current_reference = player_pokemon_selected
    # Player owns more than one Pokemon;CONDITIONAL STATEMENT
    if player_max_pokemon > 1:
        print(f'You currently have {player_max_pokemon} Pokemons!')
    else:
        print(f'You currently have {player_max_pokemon} Pokemon!')
    # List all the Pokemon here
    for probe in range(player_max_pokemon):
        print(f'**Reference: {probe + 1}**')
        load_pokemon(player_pokemon_index[probe], 0, 0)
        time.sleep(3)
    print(f'Currently selected Pokemon: {current_reference + 1}')
    # Load back to current Pokemon;FUNCTION
    load_pokemon(player_pokemon_index[current_reference], 0, 0)
    input("Press Enter to continue...")


def select_pokemon():
    select_input = 0
    while select_input < 1:
        select_input = input("Please type in your Pokemon reference number: ")
        try:
            select_input = int(select_input)
        except ValueError:
            print("Invalid User Input!")
            select_input = 0
        # Invalid reference number;CONDITIONAL STATEMENT
        if select_input > player_max_pokemon:
            print("Invalid User Input!")
            select_input = 0
    print(f'**Your current selected Pokemon reference: {select_input}**')
    load_pokemon(player_pokemon_index[int(select_input) - 1], 0, 0)
    time.sleep(3)


def return_home():
    global player_location_index
    # Make sure player is not at hometown;CONDITIONAL STATEMENT
    if player_location_index > 0:
        current_location = list_location[player_location_index].split(',')
        print(f'Travelling back home will cost you: {current_location[3]} Pokemon meters.')
        return_decision = 'NONE'
        while not (return_decision == 'N' or return_decision == 'Y'):
            return_decision = input("Are you sure? Y/N? ").upper().strip()
            # Player insists to capture and own the Pokemon;CONDITIONAL STATEMENT
            if return_decision == 'N':
                print("TRAVEL CANCELLED!")
            elif return_decision == 'Y':
                travel(0)
    else:
        # BUG FIX
        print("You are already at your hometown!")
        time.sleep(3)


def travel_menu():
    global player_location_index
    # TESTING ONLY
    # player_location_index = 6
    current_location = list_location[player_location_index].split(',')
    # Declare a temporary User Input Variable;FUNCTION
    travel_input = 0
    # Declare first possible location;FUNCTION
    probe_list_1 = 0
    # Declare second possible location;FUNCTION
    probe_list_2 = 0
    # Declare a temporary menu item count;FUNCTION
    menu_upper_limit = 2
    print(f'You are currently in: {current_location[0]}')
    print("***Please indicate which location you would like to travel to?***")
    while travel_input > menu_upper_limit or travel_input < 1:
        # Player is not at hometown;CONDITIONAL STATEMENT
        if player_location_index > 0:
            probe_list_1 = player_location_index - 1
            new_location = list_location[probe_list_1].split(',')
            print(f'1: Return to {new_location[0]} - distance of travel is {new_location[1]} Pokemon meters.')
            probe_list_2 = player_location_index + 1
            new_location = list_location[probe_list_2].split(',')
            print(f'2: {new_location[0]} - distance of travel is {new_location[1]} Pokemon meters.')
            print("3: Exit Travel Menu")
            menu_upper_limit = 3
        # Player is at hometown (player_location_index=0);CONDITIONAL STATEMENT
        else:
            probe_list_1 = player_location_index + 1
            new_location = list_location[probe_list_1].split(',')
            print(f'1: Travel to {new_location[0]} - distance of travel is {new_location[1]} Pokemon meters.')
            print("2: Exit Travel Menu")
            menu_upper_limit = 2
        travel_input = input("Please select from the options listed above! ").strip()
        try:
            travel_input = int(travel_input)
        except ValueError:
            print("Invalid User Input!")
            travel_input = 0

    # Exit Menu command gets treated first;CONDITIONAL STATEMENT
    if travel_input == menu_upper_limit:
        return player_location_index
    # First option is selected;CONDITIONAL STATEMENT
    elif travel_input == 2:
        return probe_list_2
    else:
        return probe_list_1


def travel(reference):
    global player_location_index
    # Update the existing location;FUNCTION
    current_location = list_location[player_location_index].split(',')
    if reference != player_location_index:
        # Current location will become the new index after travelling
        player_location_index = reference
        # Update the existing location again;FUNCTION
        current_location = list_location[player_location_index].split(',')
        print("Now travelling...")
        # Similar code used in typing_effect function
        for probe in range(50):
            print(">", end='')
            if travel_check(5):
                random_enemy()
                battle()
            # The smaller the time the quicker
            time.sleep(0.1)
        print("")
        print(f'Travel journey complete! Now in: {current_location[0]}')
    else:
        print(f'Your current location: {current_location[0]}')
    time.sleep(3)


# Random Enemy Generator;FUNCTION
def travel_check(percentage):
    chance = random.randint(1, 100)
    if chance < percentage:
        return 1
    else:
        return 0


# Declare Global Variables below
def random_enemy():
    global enemy_level
    global enemy_pokemon
    global enemy_hp
    global enemy_type1
    global enemy_type2
    global enemy_pokemon_index

    enemy_level = int(player_level[player_pokemon_selected])
    # Randomly Select a line number from the Pokemon Library;FUNCTION
    enemy_pokemon_index = random.choice(range(len(list_pokemon)))
    # Split Enemy Pokemon (Random) into Strings;FUNCTION
    enemy_pokemon = list_pokemon[enemy_pokemon_index].split(',')
    # Error Correction - Integer ;FUNCTION
    enemy_hp = int(enemy_pokemon[4]) * int(player_level[player_pokemon_selected])
    enemy_type1 = list_type[int(enemy_pokemon[1])].split(',')
    enemy_type2 = list_type[int(enemy_pokemon[2])].split(',')
    # Open text file;FUNCTION
    battle_word_list = open('gamedata/battle.txt').read().splitlines()
    # Adjectives are spilt using commas;FUNCTION
    battle_word = random.choice(battle_word_list).split(',')
    # Generate random Enemy;FUNCTION
    print(f'You encountered {enemy_pokemon[0]}!')
    # Description for encountered Pokemon;FUNCTION
    print(f'This Pokemon is {random.choice(battle_word)}.')


def battle():
    global enemy_hp
    global player_hp
    global player_exp
    global player_money

    pygame.mixer.music.load('gamedata/battle.mp3')
    # BUG FIX: Volume is too load
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    while (enemy_hp > 0) and (player_hp[player_pokemon_selected] > 0):

        # If Not pygame.mixer.music.get_busy():  # No Music playing at this stage, load the music  # Inverse Boolean value, ensures continuous music play

        print(f'Player HP: {player_hp[player_pokemon_selected]}')
        print(f'Enemy HP: {enemy_hp}')
        # BUG FIX, unless stated by Player, the decision will be defaulted to the first available attack
        decision = 1
        decision = attack_menu()
        # Determine if 'ESC' is pressed first;CONDITIONAL STATEMENT
        if decision == 'ESC':
            escape_result = escape()
            if escape_result == 1:
                enemy_hp = 0
                print("You escaped from the battle.")
        elif (decision == 'CAP') and (
                # To ensure Player's are not taking advantage of hidden menus and that the requirements must be met
                enemy_hp < 10):
            capture(decision)
        else:
            enemy_hp = attack(1, player_hp[player_pokemon_selected], enemy_hp, decision)
        if enemy_hp != 0:
            player_hp[player_pokemon_selected] = attack(0, player_hp[player_pokemon_selected], enemy_hp, decision)
    else:
        # Battle is over, music stops, while loop ends here
        pygame.mixer.music.stop()
        # No Music playing at this stage, load the music
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('gamedata/morning_in_forest.mp3')
            # BUG FIX: Reset to default Volume
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)

    if enemy_hp == 0:
        if decision != 'ESC':
            print("You won the battle!")
            player_exp[player_pokemon_selected] += int(enemy_pokemon[4])
            # Choose a random number;FUNCTION
            earn_money = random.randint(0, 100)
            player_money += earn_money
            print(
                f'You earned {int(enemy_pokemon[4])} experience from this battle, now you have {player_exp[player_pokemon_selected]} points!')
            print(f'You earned ${earn_money}, now you have ${player_money}!')
            if player_exp[player_pokemon_selected] > 50:
                player_level[player_pokemon_selected] += int(player_exp[player_pokemon_selected] / 50)
                player_hp[player_pokemon_selected] += 30 * int(player_exp[player_pokemon_selected] / 50)
                # Determine the max Level increase;FUNCTION
                player_exp[player_pokemon_selected] -= int(player_exp[player_pokemon_selected]/50)
                print(f'You leveled up! Now, you are at level: {player_level[int(player_pokemon_selected)]}')
    else:
        game_over()


def game_over():
    pygame.mixer.music.load('gamedata/game_over_01.wav')
    # BUG FIX: Reset to default Volume
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(2)
    print("Game Over!")
    # Wait until music play finishes
    time.sleep(10)
    # Terminate the Program
    sys.exit()


def capture(decision):
    global enemy_hp
    global player_hp
    global player_max_pokemon
    global enemy_pokemon_index
    # Initialise the capture decision
    capture_decision = 'NONE'
    chance = random.randint(0, 10)
    capture_status = 0

    # Bad Luck - Player's capture attempt is Pokemon unsuccessful;CONDITIONAL STATEMENT
    if chance < 3:
        print("Capture Unsuccessful")
        capture_status = 0
    else:
        while not (capture_decision == 'N' or capture_decision == 'Y'):
            print("Congratulations! You have successfully captured this Pokemon!")
            print("Do you want to release this Pokemon into the wild?")
            capture_decision = input("Y/N?").upper().strip()
            # Player insists to capture and own the Pokemon;CONDITIONAL STATEMENT
            if capture_decision == 'N':
                capture_status = 1
            # Player Releases the Pokemon;CONDITIONAL STATEMENT
            elif capture_decision == 'Y':
                print("You released the Pokemon!")
                capture_status = 2

    # Player insists to capture and own the Pokemon;CONDITIONAL STATEMENT
    if capture_status == 1:
        # Play has reached the maximum number of Pokemon;CONDITIONAL STATEMENT
        if player_max_pokemon > 4:
            print("You cannot catch this Pokemon - You can only have a maximum of 5 Pokemon!")
        elif player_max_pokemon > 3 and player_level[player_pokemon_selected] < 30:
            print("You cannot catch this Pokemon - You can only have a maximum of 4 Pokemon!")
        elif player_max_pokemon > 2 and player_level[player_pokemon_selected] < 15:
            print("You cannot catch this Pokemon - You can only have a maximum of 3 Pokemon!")
        elif player_max_pokemon > 1 and player_level[player_pokemon_selected] < 5:
            print("You cannot catch this Pokemon - You can only have a maximum of 2 Pokemon!")
        # Save Data
        else:
            print("Congratulations! You are now the owner of this Pokemon!")
            # Save the Pokemon index into the Array
            player_pokemon_index[int(player_max_pokemon)] = enemy_pokemon_index
            # Save the default HP to Array
            player_hp[player_max_pokemon] = int(enemy_pokemon[4])
            # One new Pokemon added
            player_max_pokemon += 1
            print(f'Number of currently owned Pokemon: {player_max_pokemon}')
            # BUG FIX, reference number starts with 0
            print(f'Reference Number for this Pokemon {player_hp[player_max_pokemon - 1]}')
            print(player_pokemon_index)
            print(player_hp)
            # If Player's escape attempt is successful Enemy's HP is set to 0;FUNCTION
            enemy_hp = 0
    # Player releases the Pokemon, battle complete;CONDITIONAL STATEMENT
    elif capture_status == 2:
        enemy_hp = 0
    # Player fails to capture the Pokemon, now Enemy attacks
    else:
        player_hp[player_pokemon_selected] = attack(0, player_hp[player_pokemon_selected], enemy_hp, decision)


# Program officially starts
game_intro()
game_first_run()
# Main loop here;ITERATIVE LOOP
while True:
    main_menu()