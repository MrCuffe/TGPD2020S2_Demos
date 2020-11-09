# The print function simply prints out what you want it to, and I have used it to print out a welcome note and the instructions
print('|    |  ----  |      |       -------    |')
print('|    | |      |      |      |       |   |')
print('-----  -----  |      |      |       |   |')
print('|    | |      |      |      |       |   |')
print('|    |  ----  -----  -----   -------    .')
print('Welcome to the trivia!')
print('First letters of your answers need to be upper case.')
print('For each correct answer, you get 10 points and for each incorrect answer, you lose 5 points')
print('Try to get as many questions correct as possible... Best of Luck!')
print('There are four categories:\n(1)General Knowledge\n(2)Maths\n(3)Music\n(4)Harry Potter\n')


# The list allows me to put all my questions and anwers in together
questions = {
'What is the capital of Australia?\n': 'Canberra',
'Who is the author of Charlie and the Chocolate Factory?\n':'Roald Dahl',
'Which country is Novak Djokovic from?\n':'Serbia',
'Who is the singer of cant help falling in love with you?\n(a)Bob Dylan\n(b)Elvis Presley\n(c)Dean Martin\n\n':'b',
'Which of these is not an official language of Singapore?\n(a)English\n(b)Tamil\n(c)Mandarin Chinese\n(d)Telugu\n(e)Malay\n\n':'d',
'Also the national flower of India, which is the sacred flower of the Buddhist religion?\n':'Lotus',
'What does DC stand for in electrical terminology?\n':'Direct Current','In which city was the first Olympics held?\n':'Athens',
'Which is the largest landlocked country in the world?\n(a)Kazakhstan\n(b)Chad\n(c)Bolivia\n(d)Mongolia\n':'a',
'In a website browser address bar, what does www stand for?\n':'World Wide Web'
    }
# I have used a variable named score_gk for the marks in the game and points_gk to keep in count how many questions the player gets right
# I have defined the function play_gk for the general knowledge trivia, a function allows to me to be able to run the trivia anywhere in the code just by typing play_gk so I can use it when/if the player wants to play the trivia again
def play_gk():
    score_gk = 0
    points_gk = 0
# The for loop runs until, in this case, it has gone through each element in the list, which includes the questions and answers to the trivia
    for q in questions.keys():
        player_answer = input(q)
# The if statement only works if the answer the player inputs matches the answer in the list
        if questions.get(q) == player_answer:
            print('Well done! That is the correct answer!')
            score_gk += 10
            points_gk += 1
            print('Your current score is ' + str(score_gk) + '/100')
# If the answer the player inputs doesn't match the criteria in the if statement, then the else statement runs
        else:
            print('Oops... that is incorrect!')
            score_gk -= 5
            print('Your current score is ' + str(score_gk) + '/100')
    print('You got ' + str(points_gk) + '/10 questions right')              
    print('That is the end, thankyou for playing!')
# import random allows me to use a set of functions, such as random.choice, which I have used to create a random maths quiz generator
import random
# I have used another function for the maths trivia
def play_maths():
    questions = {}
    score = 0
    points = 0
#i have used a range of 15 numbers for the maths quiz so the numbers arent too big
    for i in range(15):
        int_1 = random.randint(0,15)
        int_2 = random.randint(0,15)
        operators = ['+','-','*']
        operator_value = random.choice(operators)
        question = str(int_1)+' '+str(operator_value)+' '+str(int_2)
        answer = eval(question)
        question += ': '

        questions.update({question:str(answer)})
    for q in questions.keys():
        user_answer = input(q)
        if questions.get(q) == str(user_answer):
            score += 10
            points += 1
            print('Well done that is correct!')
        else:
            score -= 5
            print('Oops...that is incorrect!')
    print('You got ' + str(points) + '/15 correct\nThanks for playing!')
# I have created another list for the music trivia questions
music_questions = {
'Which one of these was the U.S no.1 song for Billie Eilish?\n(a)Good Guy\n(b)Cute Guy\n(c)Bad Guy\n(d)Stupid Guy\n':'c',
'What country is Shawn Mendes from?':'Canada','Which Ariana Grande song starts with the line: Thought Id end up with Sean, but he wasnt a match...?\nnote:This title had no capital letters\n':'thank u, next',
'What are Justin Beibers fans called?\n(a)Beliebers\n(b)Justinites\n(c)JayBeebees\n(d)Beiber Fevers\n':'a',
'Who is the singer of the song photograph?\n':'Ed Sheeran','Which one of these is a Bruno Mars song?\n(D)ownton soul\n(U)ptown Funk\n(I)nner City Life\n(C)ountry living\n':'U',
'Which T.V show were Little Mix discovered on?\n(a)Britains Got Talent\n(b)The Voice\n(c)X Factor\n(d)Fame Academy\n':'c',
'Complete the title of this band group... Panic! at the...':'Disco','Complete the song title...Kill em with...':'Kindness',
'Who is the singer of the song Dont start now?':'Dua Lipa'
    }
def play_music():
    score_music = 0
    points_music = 0
    for q in music_questions.keys():
        player_answer = input(q)
        if music_questions.get(q) == player_answer:
            print('Well done! That is the correct answer!')
            score_music += 10
            points_music += 1
            print('Your current score is ' + str(score_music) + '/100')
        else:
            print('Oops... that is incorrect!')
            score_music -= 5
            print('Your current score is ' + str(score_music) + '/100')
    print('You got ' + str(points_music) + '/10 questions right')              
    print('That is the end, thankyou for playing!')

harrypotter_questions = {
'The author of history of magic is...\n':'Bathilda Bagshot','What is a niffler and what does it do?\n(a)It turns invisible\n(b)It steals all shiny things\n(c)It makes time faster\n':'b',
'What position does Harry play in his Quidditch team?\n':'Seeker','What does the Sorcerers stone do?\n(a)It produces gold and produces the elixir of life\n(b)Gives you all the deathly hallows\n(c)It takes you back in time\n(d)It transforms the one who holds it into an animal\n':'a',
'Who bets all the time?\n(a)Allistor Moody\n(b)Ludo Bagman\n(c)Remius Lupin\n(d)Ron Weasley\n':'b','Who take away all your happiness?\n(a)Blast ended swrewts\n(b)Ron Weasley\n(c)Dolores Umbridge\n(d)Dementors\n':'d',
'What kind of animal is Aragog and whos pet is he?\n(a)Snake and Draco Malfoy\n(b)Cat and Hermione Grainger\n(c)Rat and Ronald Weasley\n(d)Spider and Hagrid\n':'d',
'Who is Dudley?\n(a)Harrys best friend\n(b)Harrys crazy evil cousin\n(c)Headmaster at Hogwarts\n(d)Harrys owl\n':'b','What is the name of Hermione Graingers cat?\n(a)Crookshanks\n(b)Aragog\n(c)Scabbers\n(d)Ron\n':'a',
'What is an auror?\n(a)One of Voldemorts supporters\n(b)A career counselor at Hogwarts\n(c)A dark wizard catcher\n(d)A poisonous plant\n':'c'
}

def play_harrypotter():
    score_harrypotter = 0
    points_harrypotter = 0
    for q in harrypotter_questions.keys():
        gamer_answer = input(q)
        if harrypotter_questions.get(q) == gamer_answer:
            print('Well done! That is the correct answer!')
            score_harrypotter += 10
            points_harrypotter += 1
            print('Your current score is ' + str(score_harrypotter) + '/100')
        else:
            print('Oops... that is incorrect!')
            score_harrypotter -= 5
            print('Your current score is ' + str(score_harrypotter) + '/100')
    print('You got ' + str(points_harrypotter) + '/10 questions right')              
    print('That is the end, thankyou for playing!')

response = input('Which one would you like to play?')
if response == "1":
# To create some space after the instructions, I used a for loop, which will print out ('     ') x the number of range, which is 10.
    for x in range(10):
        print(' ')
    play_gk()
elif response == "2":
    for x in range(10):
        print(' ')
    play_maths()
elif response == "3":
    for x in range(10):
        print(' ')
    play_music()
elif response == "4":
    play_harrypotter()
else:
    print('Okay')
# I have used another variable and asked the player if they want to play again
after = input('Would you like to play again?')
# The if statement means that if the response to after put in by the player is yes then it will ask which trivia they want to play, and the else statement works only if the player said anything other than yes
if after == "Yes" or "yes":
    ask = input('Which category of trivia would you like to play?:\n(1)General Knowledge\n(2)Maths\n(3)Music\n(4)Harry Potter\n')
    if ask == "1":
        play_gk()
    elif ask == "2":
        play_maths()
    elif ask == "3":
        play_music()
    elif ask == "4":
        play_harrypotter()
else:
    print('Thankyou for playing!')
