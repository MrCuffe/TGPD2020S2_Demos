import random
# create lists for true or false questions and their answers
def get_tof_statements():
    statements = []
    statements.append(["The chemical symbol for silver is Ag.", "T"])
    statements.append(["The human body takes 5,000 breaths daily.", "F"])
    statements.append(["An octopus has 7 hearts.", "F"])
    statements.append(["Angkor Wat is in Cambodia.", "T"])
    statements.append(["The First World War ended in 1919.", "F"])
    statements.append(["Dr No was the first James Bond film.", "T"])
    statements.append(["Micheal Jackson won the 1984 Grammy award for the Record of the Year for the song 'Beat it'.", "T"])
    statements.append(["A scrabble board is 16 x 16 in size.", "F"])
    statements.append(["The artist Henry Matisse is French.", "T"])
    statements.append(["The Beatles first went to the USA in 1970.", "F"])

    return statements

# subroutine for the true or false quiz

def play_tof_quiz():

    # get true or false statements
    tof_statements = get_tof_statements()

    # randomise tof statements
    random.shuffle(tof_statements)

    # set player score to 0
    score = 0

    # show tof statements using a loop
    for s in tof_statements:

        # present statement
        print("True or false: " + s[0])

        # user enter guess
        guess = input("Enter T or F: ")
        # check if guess is correct
        if guess == s[1]:
            print("Correct!")
            # update score
            score = score + 1

        else:
            print("Incorrect :(")
    # show the final score
    print("Your final score is: " + str(score))

# creating lists for general knowledge questions and their answers
def get_gk_statements():
    statements = []
    statements.append(["In what year was the first iPhone released? ", "2007"])
    statements.append(["Beirut is the capital of which country? ", "Lebanon"])
    statements.append(["In the Bible, which character is known for building an ark?", "Noah"])
    statements.append(["Which AFL team won the 2017 Grand Final", "Richmond"])
    statements.append(["What type of animal is Bambi? ", "deer"])
    statements.append(["Who wrote the 'Harry Potter' series? ", "J.K. Rowling"])
    statements.append(["Who was the Greek God of War? ", "Ares"])
    statements.append(["How many syllables make up a Haiku poem? ", "17"])
    statements.append(["Which planet is the closest to the sun? ", "Mercury"])
    statements.append(["What is the name of the poker hand containing three of a kind and a pair? ", "Full house"])

    return statements

# subroutine for the general knowledge quiz

def play_gk_quiz():

    print("Make sure you use capital letters for proper nouns!")

    # get general knowledge statements
    gk_statements = get_gk_statements()

    # randomise gk statements
    random.shuffle(gk_statements)

    # set player score to 0
    score1 = 0

    # show gk statements using a loop
    for a in gk_statements:

        # present statement
        print(a[0])

        # user enter guess
        guess1 = input("Enter your answer: ")
        # check if guess is correct
        if guess1 == a[1]:
            print("Correct!")
            # update score
            score1 = score1 + 1

        else:
            print("Incorrect :(")
    # show the final score
    print("Your final score is: " + str(score1))

def main_menu():

    print("+-----------------------------------+")
    print("|      Welcome to Trivia Time!      |")
    print("+-----------------------------------+")
    print("| Please select an option:          |")
    print("|                                   |")
    print("| 1. Play True or False quiz        |")
    print("| 2. Play General Knowledge quiz    |")
    print("| 0. Quit                           |")
    print("+-----------------------------------+")
    choice = input("Enter 1, 2 or 3: ")
    if choice == "1":
        play_tof_quiz()
    elif choice == "2":
        play_gk_quiz()
    elif choice == "0":
        print("Thanks for playing!")
        quit()
main_menu()

        
