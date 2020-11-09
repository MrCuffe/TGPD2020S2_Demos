# Bennett Christy Moses
# Disney Princess Mania Game

# Code to make a main menu for the player to choose if they want to play the game or quit
def main_menu():
 print("+-------------------------------+")
print("+-------------------------------+")
print("|   WELCOME TO DISNEY MANIA     |")
print("+-------------------------------+")
print("|   please select an option     |")
print("|                               |")
print("| 1.Play Disney Princess Mania  |")
print("| 0.Quit                        |")
choice = input("Enter 1 or 0:")

# Provide the player with instructions in how to play the game

instructions = input("Press 'I' to see Instructions or 'P' to Proceed: ")

if instructions == "I":
    print("You will be given a set of questions that relate to the specific Disney Princess")
    print("You will have to type the answers in")
    print("If you get a questions right then you will earn one point")
    print("if you get a question wrong you will not earn a point")
    print("Try and get all the answers right, you will get a mark at the end")
elif instructions == "P":
    print("Welcome to Disney Mania! Will you be able save Disney land! Answer all the following questions to save DisneyLand!")
else:
    print("Check Spelling")
    
# Defining the Disney Mania game
def play_disney_mania():

    #Give an introduction to players to ask them if they still want to play the game
    # variables for the final mark and the starting line

    ans = input('Are you ready to play and save Disney Land, name (yes/no):')
    score = 0
    total_q = 20

    # if and else statements
    # or statement being used to have multiple answers
    # ans.lower() statement
    # score += used to keep track of points to that it can be calculated at the end of code
    # First question for enter the Disney Land
    
    if ans.lower() == 'yes':
        ans = input('ARE YOU READY TO TEST YOU SKILLS ON DISNEY!!! (yes I am / no I am not')

        if ans.lower() == 'yes i am':
            print('Well done you have now entered DisneyLand! Meet Ariel answer her 3 questions to save her!')

# Questions to be answered for Princess Ariel

            ans = input('1. What is my fathers assistant name?')
        if ans.lower() == 'sebastian':
            score += 1
            print('Well done you answered correctly')
        else:
            print('Your answer is incorrect!')

        ans = input('2. Finish the Lyrics of my song Part of your World! How many wonders can one _____ hold')
        if ans.lower() == 'cavern':
            score += 1
            print('Well done your on a roll')
        else:
            print('Your answer is incorrect, unlucky!')

        ans = input('3. What is my close fish friend name?')
        if ans.lower() == 'flounder':
            score += 1
            print('Well done your on a roll! Well done you saved Tiana! Now you must save Princess Rapunzel. Answer her 3 questions to save her')
        else:
            print('Your answer is incorrect. Oh well try and answer Princess Tianas Questions ')

# Questions to be answered for Princess Tiana

        ans = input('1. What food does Tiana make with her Dad?')
        if ans.lower() == 'gumbo':
           score += 1
           print('Well done your on a roll')
        else:
            print('Your answer is incorrect.')

        ans = input('2. What does Tiana call Charlotte?')
        if ans.lower() == 'lottie':
            score += 1
            print('Well done your on a roll')
        else:
            print('Your answer is incorrect.') 

        ans = input('3. What is Tianas restaurant called?')
        if ans.lower() == 'tianas palace':
            score += 1
            print('Well done you saved Tiana! Now you must save Princess Rapunzel. Answer her 4 questions to save her')
        else:
            print('Your answer is incorrect! Oh Well try and answer Princess Rapunzel questions')

# Questions to be answered for Princess Rapunzel

        ans = input('1. What is my pet chameleon named?')
        if ans.lower() == 'pascal':
            score += 1
            print('Well done your on a roll')
        else:
            print('Your answer is incorrect')

        ans = input('2. What created the Magic flower? HINT rises from the east and sets in')
        if ans.lower() == 'sun':
            score += 1
            print('Well done your on a roll')
        else:
            print('Your answer is incorrect')

        ans = input('3. What is the name of the taven Flynn took Rapunzel to?')
        if ans.lower() == 'The Snuggly Duckling' or 'the snuggly duckling':
            score += 1
            print('Well done your answer is correct')
        else:
            print('Your answer is incorrect')

        ans = input('4. Finish the lyric. Flower gleam and glow let your power shine ____ ___ _____ _______...?')
        if ans.lower() =='make the clock reverse':
            score += 1
            print('Well done you saved Rapanzel! Now you must save Princess Moana. Answer her 3 questions to save her!')
        else:
            print('Your answer is incorrect! Oh well try and save Princess Moanas questions')

# Questions to be answered for Princess Moana

            ans = input('1. What is the name of the Demi God of the Wind and see, hero to all')
        if ans.lower() =='maui':
            score += 1
            print('Good job you are doing great!')
        else:
            print('oh no you got the question wrong move on')

            ans = input('2. Where does Tamatoa live?')
        if ans.lower() == 'realm of monsters':
            score += 1
            print('Good job you are great!')
        else:
            print('oh no you got the question wrong move on')

            ans = input('3.During Where You Are when Gramma Tala sings You are your fathers daughter, which traits does she say they both have? ?')
        if ans.lower() == 'stubbornness and pride':
            score += 1
            print('Good job you are great!Now you must save Princess Merida. Answer her 3 questions to save her!')
        else:
            print('oh no you got the question wrong move on! Oh well try and answer Princess Meridas questions ')

# Questions to be answered for Princess Merida

            ans = input('1. In what leg did Meridas lose in a fight with Mordu?')
        if ans.lower() == 'left':
            score += 1
            print('Good job you are great!')
        else:
            print('oh no you got the question wrong move on')

            ans = input('2. What does Meridas mum turn into?')
        if ans.lower() == 'bear':
            score += 1
            print('WEll DONE you are doing great!')
        else:
            print('oh no you got the question wrong move on')

            ans = input('3. How many siblings does Merida have? Write your answer as a number')
        if ans.lower() == '3':
            score += 1
            print('WEll DONE!Now you must save Princess Elsa and Anna. Answer her 3 questions to save her!')
        else:
            print('oh no you got the question wrong move on! Oh well try and answer Princess Elsa and Annas questions')

#Questions to be answered for Princess Elsa and Anna

            ans = input('1. What is the name of the song that Elsa sings in Frozen after she runs away from her coronation after party')
        if ans.lower() == 'Let it go':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong move on! Oh well try and answer Princess Elsas questions')

            ans = input('2. What is the name of the snowman that Elsa made')
        if ans.lower() == 'olaf':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong move on!')

            ans = input('3. Who does Anna end up loving at the end of Frozen?')
        if ans.lower() == 'kristoff':
            score += 1
            print('WEll DONE!Now you must save Princess Jasmine. Answer her 3 questions to save her!')
        else:
            print('oh no you got the question wrong move on! Oh well try and answer Princess Jasmine questions')

#Questions to be answered for Princess Jasmine

            ans = input('1. What is Princess Jasmines Tiger called? ')
        if ans.lower() == 'raja':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong move on!')

            ans = input('2. Finish the lyrics A whole ___ _____ ')
        if ans.lower() == 'new world':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong move on!')

            ans = input('2. What is the name of Jasmines lover? ')
        if ans.lower() == 'Aladdin':
            score += 1
            print('WEll DONE! Now you must save Princess Mulan. Answer her 3 questions to save her!')
        else:
            print('oh no you got the question wrong move on! Oh well try and answer Princess Mulans questions')

#Questions to be answered for Princess Mulan

            ans = input('1. What is the name of the dragon?')
        if ans.lower() == 'Mushu':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong move on!')

            ans = input('2. Finish the lyrics Who is that girl I see staring _______ ____ __ __ ')
        if ans.lower() == 'staight back at me':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong move on!')

            ans = input('How does Mulan save after the glacier?')
        if ans.lower() == 'Shang':
            score += 1
            print('WEll DONE!')
        else:
            print('oh no you got the question wrong!')
            
    # print being used for final statement
    # Equation for working out percentage used

    print('Thank you for playing, you got', score, "questions correct.")
    mark = (score / total_q) * 100

    # string used to add percentage sign after the final mark
    print("Mark:", str(mark) + '%')
    print('Play the game again to get 100% and save all the princessess')

# Use if and elif statements start Disney Mania game or end code.
if choice =="1":
    play_disney_mania()
    
elif choice == "0":
    print("Thanks for playing!")
    quit()

