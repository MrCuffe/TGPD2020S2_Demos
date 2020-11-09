
import time
space = " "

#Rules
print("THESE ARE THE RULES")
time.sleep(1)
print(space)
print("This is a game simulating what it is like leading a state out of a pandemic.")
time.sleep(1)
print("When Typing you must check your spelling so that the game works.")
time.sleep(1)
print("Alright lets get started  :D  ")
time.sleep(1)
print(space)
print("WARNING")
time.sleep(1)
print(space)
print("THIS GAME CONTAINS CUSS WORDS")
time.sleep(1)
print(space)
print("NOT FOR CHILDREN UNDER 14 YRS OLD")
time.sleep(1)
print(space)
print("Les get started")


#Selecting the character name

print(space)
time.sleep(1)
print("You are a premier of a state and there is a pandemic.")
print(space)
time.sleep(1)
print("It is your job to make sure the state stays safe and gets back to normal with as little deaths possible.")
time.sleep(1)
premier = input("Enter Your Premier Name:")


print("Hello " + premier + ", you are the premier of the state")
print(space)
time.sleep(2)
print("It is your job to keep the state safe and lead them out of the pandemic")
time.sleep(2)

print("Are you ready " + premier)
time.sleep(1)
ready = (input("Yes or No: "))

if ready == "Yes" or ready == "yes" or ready == "yea":
    time.sleep(1)
    print("Good, lets go.")
elif ready == "No" or ready == "no" or ready == "nope":
    print("You suck bitch.")
    time.sleep(1)
    print(space)
    print("Game Over")
    import sys
    sys.exit()


#what is going to happen in the game.
time.sleep(1)
print(space)
print("There is an outbreak of the virus in your city")
time.sleep(1)
print(space)

#making the first decisions


answer = input("what do you do " + premier + " Lockdown or Stay Open?:")
if answer == "Lockdown" or answer == "lockdown" or answer == "lock down":
    time.sleep(1)
    print(space)
    print("Ok, people are not happy but they are safe.")
    time.sleep(2)
    print(space)
    print("Now that people are safe the state can re open")
    time.sleep(1)
    print(space)
    ans1 = input("Do you re-open or stay locked down " + premier + "?:")

    if ans1 == "re-open" or ans1 == "re open" or ans1 == "Re-Open" or ans1 == "Re Open" or ans1 == "Re open":
        print("All but 5 cases remain but the people are happy")
        print(space)
        time.sleep(1)
        print("Well done " + premier)

    elif ans1 == "stay locked down" or ans1 == "Stay Locked Down" or ans1 == "Stay locked down" or ans1 == "Stay Locked down":
        time.sleep(1)
        print(space)
        print("Big mistake")
        print(space)
        time.sleep(1)
        print("That was unnecessary ")
        time.sleep(1)
        print(space)
        print("There is a riot against you and the people hang you, just like in the olden days")
        time.sleep(1)
        print(space)
        print("Anger the people and they will kill u, people are crazy...")
        print(space)
        time.sleep(1)
        print("and you are dead")
        time.sleep(1)
        print("Game over fuccboi")
        import sys
        sys.exit()

    else:
        time.sleep(2)
        print("You may have made a grammatical error, check your spelling and capitol letters.")
        time.sleep(1)
        print(space)
        print("Ok, people are not happy but they are safe.")
        time.sleep(2)
        print(space)
        print("Now that people are safe the state can re open")
        time.sleep(1)
        print(space)
        ans1 = input("Do you re-open or stay locked down " + premier + "?:")

        #seccond try

        if ans1 == "re-open" or ans1 == "re open" or ans1 == "Re-Open" or ans1 == "Re Open" or ans1 == "Re open":
            print("All but 5 cases remain but the people are happy")
            print(space)
            time.sleep(1)
            print("Well done " + premier)

        elif ans1 == "stay locked down" or ans1 == "Stay Locked Down" or ans1 == "Stay locked down" or ans1 == "Stay Locked down":
            print("Big mistake")
            print(space)
            print("There is a riot against you and the people hang you, just like in the olden days")
            time.sleep(1)
            print(space)
            print("Game over fuccboi")
            import sys
            sys.exit()

        else:
            time.sleep(2)
            print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
            time.sleep(1.5)
            print("You have failed the game, ngl you kinda suck")
            print(space)
            time.sleep(1)
            print("Send this game to your friends if you have them :) ")
            import sys
            sys.exit()

elif answer == "Stay Open" or answer == "stay open" or answer == "Stay open" or answer == "stay Open":
    time.sleep(1)
    print(space)
    print("The cases continue to rise and someone dies.")
    time.sleep(1)
    print(space)
    print("You need to make the right decision here or more people will die!")
    ans2 = input("What do you do, lockdown or do nothing?: ")

    #more choices for the player

    if ans2 == "Lockdown" or ans2 == "lockdown" or ans2 == "lock down" or ans2 == "Lock Down":
        time.sleep(1)
        print(space)
        print("Good choice")
        time.sleep(1)
        print(space)
        print("You are on the right track to getting the people to safety")
        time.sleep(1)
        print(space)
        ans3 = input("What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                 "suburbs?: ")

        if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
            time.sleep(1)
            print(space)
            print("Foolish")
            time.sleep(1)
            print(space)
            print("You made the whole state angry")
            time.sleep(1)
            print(space)
            print("There is a vote of no confidence")
            time.sleep(1)
            print(space)
            print("You lose the vote.....")
            time.sleep(1)
            print(space)
            print("And the game")
            time.sleep(2)
            print(space)
            print("LOOSER")
            time.sleep(1)
            print(space)
            print("Game over fuccboi")
            print("Send this game to your friends if you have them :) ")
            import sys
            sys.exit()

        elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
            time.sleep(1)
            print(space)
            print("Bravo")
            time.sleep(1)
            print(space)
            print("You are doing well")
            time.sleep(1)
            print(space)
            print("The state is down to 5 cases")

        else:
            time.sleep(2)
            print(space)
            print("You may have made a grammatical error, check your spelling and capitol letters.")
            ans3 = input("What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                     "suburbs?: ")
            if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                time.sleep(1)
                print(space)
                print("Foolish")
                time.sleep(1)
                print(space)
                print("You made the whole state angry")
                time.sleep(1)
                print(space)
                print("There is a vote of no confidence")
                time.sleep(1)
                print(space)
                print("You lose the vote.....")
                time.sleep(1)
                print(space)
                print("And the game")
                time.sleep(2)
                print(space)
                print("LOOSER")
                time.sleep(1)
                print(space)
                print("Game over fuccboi")
                print("Send this game to your friends if you have them :) ")
                import sys
                sys.exit()

            elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                time.sleep(1)
                print(space)
                print("Bravo")
                time.sleep(1)
                print(space)
                print("You are doing well")
                time.sleep(1)
                print(space)
                print("The state is down to 5 cases")

            else:
                time.sleep(2)
                print(space)
                print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                time.sleep(1.5)
                print(space)
                print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                time.sleep(1)
                print(space)
                print("Send this game to your friends if you have them :) ")
                time.sleep(1)
                print(space)
                print("Game over")
                import sys
                sys.exit()

    elif ans2 == "Nothing" or ans2 == "nothing":
        time.sleep(1)
        print(space)
        print("You are making some questionable decisions " + premier + ".")
        time.sleep(1)
        print(space)
        print("This is your last chance to turn things around premier")
        ans4 = input("Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

        if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
            time.sleep(1)
            print(space)
            print("FFS what is wrong with you")
            time.sleep(1)
            print(space)
            print("You have literally caused the death of hundreds of people")
            time.sleep(1)
            print(space)
            print("You are sent to prison for being a dumb f**k")
            time.sleep(1)
            print(space)
            print("Go play another game like among us or something")
            time.sleep(1)
            print(space)
            print("Send this game to your friends if you have them :) ")
            time.sleep(1)
            print(space)
            print("Game over")
            import sys
            sys.exit()

        elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
            time.sleep(1)
            print(space)
            print("OMG you did something good")
            time.sleep(1)
            print(space)
            print("The cases start going down after a few weeks of lockdown")
            time.sleep(1)
            print(space)
            print("Well done for redeeming your self")
            time.sleep(1)
            print(space)
            print("There are now just 5 cases in the city")

        else:
            time.sleep(1)
            print(space)
            print("You may have made a grammatical error, check your spelling and capitol letters.")
            ans4 = input("Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

            if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                time.sleep(1)
                print(space)
                print("FFS what is wrong with you")
                time.sleep(1)
                print(space)
                print("You have literally caused the death of hundreds of people")
                time.sleep(1)
                print(space)
                print("You are sent to prison for being a dumb f**k")
                time.sleep(1)
                print(space)
                print("Go play another game like among us or something")
                time.sleep(1)
                print(space)
                print("Send this game to your friends if you have them :) ")
                time.sleep(1)
                print(space)
                print("Game over")
                import sys

                sys.exit()

            elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                time.sleep(1)
                print(space)
                print("OMG you did something good")
                time.sleep(1)
                print(space)
                print("The cases start going down after a few weeks of lockdown")
                time.sleep(1)
                print(space)
                print("Well done for redeeming your self")
                time.sleep(1)
                print(space)
                print("There are now just 5 cases in the city")

            else:
                time.sleep(2)
                print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                time.sleep(1.5)
                print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                time.sleep(1)
                print("Send this game to your friends if you have them :) ")
                import sys

                sys.exit()
    else:
        time.sleep(1)
        print(space)
        print("You may have made a grammatical error, check your spelling and capitol letters.")
        time.sleep(1)
        print(space)
        ans2 = input("What do you do, lockdown or do nothing?: ")

        if ans2 == "Lockdown" or ans2 == "lockdown" or ans2 == "lock down" or ans2 == "Lock Down":
            time.sleep(1)
            print(space)
            print("Good choice")
            time.sleep(1)
            print(space)
            print("You are on the right track to getting the people to safety")
            time.sleep(1)
            print(space)
            ans3 = input("What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                     "suburbs?: ")

            if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                time.sleep(1)
                print(space)
                print("Foolish")
                time.sleep(1)
                print(space)
                print("You made the whole state angry")
                time.sleep(1)
                print(space)
                print("There is a vote of no confidence")
                time.sleep(1)
                print(space)
                print("You lose the vote.....")
                time.sleep(1)
                print(space)
                print("And the game")
                time.sleep(2)
                print(space)
                print("LOOSER")
                time.sleep(1)
                print(space)
                print("Game over fuccboi")
                print("Send this game to your friends if you have them :) ")
                import sys

                sys.exit()

            elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                time.sleep(1)
                print(space)
                print("Bravo")
                time.sleep(1)
                print(space)
                print("You are doing well")
                time.sleep(1)
                print(space)
                print("The state is down to 5 cases")

            else:
                time.sleep(2)
                print(space)
                print("You may have made a grammatical error, check your spelling and capitol letters.")
                ans3 = input(
                    "What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                "suburbs?: ")
                if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                    time.sleep(1)
                    print(space)
                    print("Foolish")
                    time.sleep(1)
                    print(space)
                    print("You made the whole state angry")
                    time.sleep(1)
                    print(space)
                    print("There is a vote of no confidence")
                    time.sleep(1)
                    print(space)
                    print("You lose the vote.....")
                    time.sleep(1)
                    print(space)
                    print("And the game")
                    time.sleep(2)
                    print(space)
                    print("LOOSER")
                    time.sleep(1)
                    print(space)
                    print("Game over fuccboi")
                    print("Send this game to your friends if you have them :) ")
                    import sys

                    sys.exit()

                elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                    time.sleep(1)
                    print(space)
                    print("Bravo")
                    time.sleep(1)
                    print(space)
                    print("You are doing well")
                    time.sleep(1)
                    print(space)
                    print("The state is down to 5 cases")

                else:
                    time.sleep(2)
                    print(space)
                    print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                    time.sleep(1.5)
                    print(space)
                    print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                    time.sleep(1)
                    print(space)
                    print("Send this game to your friends if you have them :) ")
                    time.sleep(1)
                    print(space)
                    print("Game over")
                    import sys

                    sys.exit()

        elif ans2 == "Nothing" or ans2 == "nothing":
            time.sleep(1)
            print(space)
            print("You are making some questionable decisions " + premier + ".")
            time.sleep(1)
            print(space)
            print("This is your last chance to turn things around premier")
            ans4 = input("Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

            if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                time.sleep(1)
                print(space)
                print("FFS what is wrong with you")
                time.sleep(1)
                print(space)
                print("You have literally caused the death of hundreds of people")
                time.sleep(1)
                print(space)
                print("You are sent to prison for being a dumb f**k")
                time.sleep(1)
                print(space)
                print("Go play another game like among us or something")
                time.sleep(1)
                print(space)
                print("Send this game to your friends if you have them :) ")
                time.sleep(1)
                print(space)
                print("Game over")
                import sys

                sys.exit()

            elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                time.sleep(1)
                print(space)
                print("OMG you did something good")
                time.sleep(1)
                print(space)
                print("The cases start going down after a few weeks of lockdown")
                time.sleep(1)
                print(space)
                print("Well done for redeeming your self")
                time.sleep(1)
                print(space)
                print("There are now just 5 cases in the city")

            else:
                time.sleep(1)
                print(space)
                print("You may have made a grammatical error, check your spelling and capitol letters.")
                ans4 = input(
                    "Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

                if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                    time.sleep(1)
                    print(space)
                    print("FFS what is wrong with you")
                    time.sleep(1)
                    print(space)
                    print("You have literally caused the death of hundreds of people")
                    time.sleep(1)
                    print(space)
                    print("You are sent to prison for being a dumb f**k")
                    time.sleep(1)
                    print(space)
                    print("Go play another game like among us or something")
                    time.sleep(1)
                    print(space)
                    print("Send this game to your friends if you have them :) ")
                    time.sleep(1)
                    print(space)
                    print("Game over")
                    import sys

                    sys.exit()

                elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                    time.sleep(1)
                    print(space)
                    print("OMG you did something good")
                    time.sleep(1)
                    print(space)
                    print("The cases start going down after a few weeks of lockdown")
                    time.sleep(1)
                    print(space)
                    print("Well done for redeeming your self")
                    time.sleep(1)
                    print(space)
                    print("There are now just 5 cases in the city")

                else:
                    time.sleep(2)
                    print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                    time.sleep(1.5)
                    print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                    time.sleep(1)
                    print("Send this game to your friends if you have them :) ")
                    import sys

                    sys.exit()







else:
    time.sleep(2)
    print("You may have made a grammatical error, check your spelling and capitol letters.")
    answer = input("what do you do " + premier + " Lockdown or Stay Open?:")

    #seccond try

    if answer == "Lockdown" or answer == "lockdown" or answer == "lock down":
        time.sleep(1)
        print(space)
        print("Ok, people are not happy but they are safe.")
        time.sleep(2)
        print(space)
        print("Now that people are safe the state can re open")
        time.sleep(1)
        print(space)
        ans1 = input("Do you re-open or stay locked down " + premier + "?:")

        if ans1 == "re-open" or ans1 == "re open" or ans1 == "Re-Open" or ans1 == "Re Open" or ans1 == "Re open":
            print("All but 5 cases remain but the people are happy")
            print(space)
            time.sleep(1)
            print("Well done " + premier)

        elif ans1 == "stay locked down" or ans1 == "Stay Locked Down" or ans1 == "Stay locked down" or ans1 == "Stay Locked down":
            time.sleep(1)
            print(space)
            print("Big mistake")
            time.sleep(1)
            print(space)
            print("That was unnecessary")
            time.sleep(1)
            print(space)
            print("There is a riot against you and the people hang you, just like in the olden days")
            time.sleep(1)
            print(space)
            print("Anger the people and they will kill u, people are crazy...")
            print(space)
            time.sleep(1)
            print("and you are dead")
            print("Game over fuccboi")
            import sys
            sys.exit()

        else:
            time.sleep(2)
            print("You may have made a grammatical error, check your spelling and capitol letters.")
            time.sleep(1)
            print(space)
            print("Ok, people are not happy but they are safe.")
            time.sleep(2)
            print(space)
            print("Now that people are safe the state can re open")
            time.sleep(1)
            print(space)
            ans1 = input("Do you re-open or stay locked down " + premier + "?:")

            # second try

            if ans1 == "re-open" or ans1 == "re open" or ans1 == "Re-Open" or ans1 == "Re Open" or ans1 == "Re open":
                print("All but 5 cases remain but the people are happy")
                print(space)
                time.sleep(1)
                print("Well done " + premier)

            elif ans1 == "stay locked down" or ans1 == "Stay Locked Down" or ans1 == "Stay locked down" or ans1 == "Stay Locked down":
                print("Big mistake")
                print(space)
                print("There is a riot against you and the people hang you, just like in the olden days")
                time.sleep(1)
                print(space)
                print("Game over fuccboi")
                import sys

                sys.exit()

            else:
                time.sleep(2)
                print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                time.sleep(1.5)
                print("You have failed the game, ngl you kinda suck")
                time.sleep(1)
                print(space)
                print("Send this game to your friends if you have them :) ")
                import sys
                sys.exit()

    elif answer == "Stay Open" or answer == "stay open" or answer == "Stay open" or answer == "stay Open":
        time.sleep(1)
        print(space)
        print("The cases continue to rise and someone dies.")
        time.sleep(1)
        print(space)
        print("You need to make the right decision here or more people will die!")
        ans2 = input("What do you do, lockdown or do nothing?: ")

        # more choices for the player

        if ans2 == "Lockdown" or ans2 == "lockdown" or ans2 == "lock down" or ans2 == "Lock Down":
            time.sleep(1)
            print(space)
            print("Good choice")
            time.sleep(1)
            print(space)
            print("You are on the right track to getting the people to safety")
            time.sleep(1)
            print(space)
            ans3 = input("What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                     "suburbs?: ")

            if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                time.sleep(1)
                print(space)
                print("Foolish")
                time.sleep(1)
                print(space)
                print("You made the whole state angry")
                time.sleep(1)
                print(space)
                print("There is a vote of no confidence")
                time.sleep(1)
                print(space)
                print("You lose the vote.....")
                time.sleep(1)
                print(space)
                print("And the game")
                time.sleep(2)
                print(space)
                print("LOOSER")
                time.sleep(1)
                print(space)
                print("Game over fuccboi")
                print("Send this game to your friends if you have them :) ")
                import sys

                sys.exit()

            elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                time.sleep(1)
                print(space)
                print("Bravo")
                time.sleep(1)
                print(space)
                print("You are doing well")
                time.sleep(1)
                print(space)
                print("The state is down to 5 cases")

            else:
                time.sleep(2)
                print(space)
                print("You may have made a grammatical error, check your spelling and capitol letters.")
                ans3 = input(
                    "What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                "suburbs?: ")
                if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                    time.sleep(1)
                    print(space)
                    print("Foolish")
                    time.sleep(1)
                    print(space)
                    print("You made the whole state angry")
                    time.sleep(1)
                    print(space)
                    print("There is a vote of no confidence")
                    time.sleep(1)
                    print(space)
                    print("You lose the vote.....")
                    time.sleep(1)
                    print(space)
                    print("And the game")
                    time.sleep(2)
                    print(space)
                    print("LOOSER")
                    time.sleep(1)
                    print(space)
                    print("Game over fuccboi")
                    print("Send this game to your friends if you have them :) ")
                    import sys

                    sys.exit()

                elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                    time.sleep(1)
                    print(space)
                    print("Bravo")
                    time.sleep(1)
                    print(space)
                    print("You are doing well")
                    time.sleep(1)
                    print(space)
                    print("The state is down to 5 cases")

                else:
                    time.sleep(2)
                    print(space)
                    print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                    time.sleep(1.5)
                    print(space)
                    print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                    time.sleep(1)
                    print(space)
                    print("Send this game to your friends if you have them :) ")
                    time.sleep(1)
                    print(space)
                    print("Game over")
                    import sys

                    sys.exit()

        elif ans2 == "Nothing" or ans2 == "nothing":
            time.sleep(1)
            print(space)
            print("You are making some questionable decisions " + premier + ".")
            time.sleep(1)
            print(space)
            print("This is your last chance to turn things around premier")
            ans4 = input("Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

            if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                time.sleep(1)
                print(space)
                print("FFS what is wrong with you")
                time.sleep(1)
                print(space)
                print("You have literally caused the death of hundreds of people")
                time.sleep(1)
                print(space)
                print("You are sent to prison for being a dumb f**k")
                time.sleep(1)
                print(space)
                print("Go play another game like among us or something")
                time.sleep(1)
                print(space)
                print("Send this game to your friends if you have them :) ")
                time.sleep(1)
                print(space)
                print("Game over")
                import sys

                sys.exit()

            elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                time.sleep(1)
                print(space)
                print("OMG you did something good")
                time.sleep(1)
                print(space)
                print("The cases start going down after a few weeks of lockdown")
                time.sleep(1)
                print(space)
                print("Well done for redeeming your self")
                time.sleep(1)
                print(space)
                print("There are now just 5 cases in the city")

            else:
                time.sleep(1)
                print(space)
                print("You may have made a grammatical error, check your spelling and capitol letters.")
                ans4 = input(
                    "Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

                if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                    time.sleep(1)
                    print(space)
                    print("FFS what is wrong with you")
                    time.sleep(1)
                    print(space)
                    print("You have literally caused the death of hundreds of people")
                    time.sleep(1)
                    print(space)
                    print("You are sent to prison for being a dumb f**k")
                    time.sleep(1)
                    print(space)
                    print("Go play another game like among us or something")
                    time.sleep(1)
                    print(space)
                    print("Send this game to your friends if you have them :) ")
                    time.sleep(1)
                    print(space)
                    print("Game over")
                    import sys

                    sys.exit()

                elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                    time.sleep(1)
                    print(space)
                    print("OMG you did something good")
                    time.sleep(1)
                    print(space)
                    print("The cases start going down after a few weeks of lockdown")
                    time.sleep(1)
                    print(space)
                    print("Well done for redeeming your self")
                    time.sleep(1)
                    print(space)
                    print("There are now just 5 cases in the city")
        else:
            time.sleep(1)
            print(space)
            print("You may have made a grammatical error, check your spelling and capitol letters.")
            time.sleep(1)
            print(space)
            ans2 = input("What do you do, lockdown or do nothing?: ")

            if ans2 == "Lockdown" or ans2 == "lockdown" or ans2 == "lock down" or ans2 == "Lock Down":
                time.sleep(1)
                print(space)
                print("Good choice")
                time.sleep(1)
                print(space)
                print("You are on the right track to getting the people to safety")
                time.sleep(1)
                print(space)
                ans3 = input(
                    "What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                "suburbs?: ")

                if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                    time.sleep(1)
                    print(space)
                    print("Foolish")
                    time.sleep(1)
                    print(space)
                    print("You made the whole state angry")
                    time.sleep(1)
                    print(space)
                    print("There is a vote of no confidence")
                    time.sleep(1)
                    print(space)
                    print("You lose the vote.....")
                    time.sleep(1)
                    print(space)
                    print("And the game")
                    time.sleep(2)
                    print(space)
                    print("LOOSER")
                    time.sleep(1)
                    print(space)
                    print("Game over fuccboi")
                    print("Send this game to your friends if you have them :) ")
                    import sys

                    sys.exit()

                elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                    time.sleep(1)
                    print(space)
                    print("Bravo")
                    time.sleep(1)
                    print(space)
                    print("You are doing well")
                    time.sleep(1)
                    print(space)
                    print("The state is down to 5 cases")

                else:
                    time.sleep(2)
                    print(space)
                    print("You may have made a grammatical error, check your spelling and capitol letters.")
                    ans3 = input(
                        "What do you want to lockdown " + premier + "? The whole state, just the city, or just a few "
                                                                    "suburbs?: ")
                    if ans3 == "The whole state" or ans3 == "The Whole State" or ans3 == "the whole state" or ans3 == "The Whole state":
                        time.sleep(1)
                        print(space)
                        print("Foolish")
                        time.sleep(1)
                        print(space)
                        print("You made the whole state angry")
                        time.sleep(1)
                        print(space)
                        print("There is a vote of no confidence")
                        time.sleep(1)
                        print(space)
                        print("You lose the vote.....")
                        time.sleep(1)
                        print(space)
                        print("And the game")
                        time.sleep(2)
                        print(space)
                        print("LOOSER")
                        time.sleep(1)
                        print(space)
                        print("Game over fuccboi")
                        print("Send this game to your friends if you have them :) ")
                        import sys

                        sys.exit()

                    elif ans3 == "Just the city" or ans3 == "just the city" or ans3 == "Just The City" or ans3 == "Just The city" or ans3 == "Just a few suburbs" or ans3 == "just a few suburbs" or ans3 == "Just A Few Suburbs":
                        time.sleep(1)
                        print(space)
                        print("Bravo")
                        time.sleep(1)
                        print(space)
                        print("You are doing well")
                        time.sleep(1)
                        print(space)
                        print("The state is down to 5 cases")

                    else:
                        time.sleep(2)
                        print(space)
                        print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                        time.sleep(1.5)
                        print(space)
                        print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                        time.sleep(1)
                        print(space)
                        print("Send this game to your friends if you have them :) ")
                        time.sleep(1)
                        print(space)
                        print("Game over")
                        import sys

                        sys.exit()

            elif ans2 == "Nothing" or ans2 == "nothing":
                time.sleep(1)
                print(space)
                print("You are making some questionable decisions " + premier + ".")
                time.sleep(1)
                print(space)
                print("This is your last chance to turn things around premier")
                ans4 = input(
                    "Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

                if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                    time.sleep(1)
                    print(space)
                    print("FFS what is wrong with you")
                    time.sleep(1)
                    print(space)
                    print("You have literally caused the death of hundreds of people")
                    time.sleep(1)
                    print(space)
                    print("You are sent to prison for being a dumb f**k")
                    time.sleep(1)
                    print(space)
                    print("Go play another game like among us or something")
                    time.sleep(1)
                    print(space)
                    print("Send this game to your friends if you have them :) ")
                    time.sleep(1)
                    print(space)
                    print("Game over")
                    import sys

                    sys.exit()

                elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                    time.sleep(1)
                    print(space)
                    print("OMG you did something good")
                    time.sleep(1)
                    print(space)
                    print("The cases start going down after a few weeks of lockdown")
                    time.sleep(1)
                    print(space)
                    print("Well done for redeeming your self")
                    time.sleep(1)
                    print(space)
                    print("There are now just 5 cases in the city")

                else:
                    time.sleep(1)
                    print(space)
                    print("You may have made a grammatical error, check your spelling and capitol letters.")
                    ans4 = input(
                        "Do you continue to do nothing or do you finally take some action and 'lockdown' the state?:")

                    if ans4 == "Nothing" or ans4 == "nothing" or ans4 == "Do nothing" or ans4 == " do nothing" or ans4 == "Do Nothing":
                        time.sleep(1)
                        print(space)
                        print("FFS what is wrong with you")
                        time.sleep(1)
                        print(space)
                        print("You have literally caused the death of hundreds of people")
                        time.sleep(1)
                        print(space)
                        print("You are sent to prison for being a dumb f**k")
                        time.sleep(1)
                        print(space)
                        print("Go play another game like among us or something")
                        time.sleep(1)
                        print(space)
                        print("Send this game to your friends if you have them :) ")
                        time.sleep(1)
                        print(space)
                        print("Game over")
                        import sys

                        sys.exit()

                    elif ans4 == "lockdown" or ans4 == "Lockdown" or ans4 == "Finally lockdown" or ans4 == "finally lockdown" or ans4 == "Finally Lockdown":
                        time.sleep(1)
                        print(space)
                        print("OMG you did something good")
                        time.sleep(1)
                        print(space)
                        print("The cases start going down after a few weeks of lockdown")
                        time.sleep(1)
                        print(space)
                        print("Well done for redeeming your self")
                        time.sleep(1)
                        print(space)
                        print("There are now just 5 cases in the city")

                    else:
                        time.sleep(2)
                        print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
                        time.sleep(1.5)
                        print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
                        time.sleep(1)
                        print("Send this game to your friends if you have them :) ")
                        import sys

                        sys.exit()

    else:
        time.sleep(2)
        print("You are clearly illiterate and are not fit to lead us out of a pandemic.")
        time.sleep(1.5)
        print("You have failed the game, at this point it is rather disappointing, ngl you kinda suck")
        time.sleep(1)
        print("Send this game to your friends if you have them :) ")
        import sys
        sys.exit()

#                             part 2


time.sleep(1)
print(space)
print("Ok now that there are only 5 cases things can start returning to normal")
time.sleep(1)
print(space)
opt1 = input("What do you do, do you ease all the restrictions at once, or do you just open schools?:")

if opt1 == "ease all the restrictions at once" or opt1 == "Ease all the restrictions at once" or opt1 == "Ease all the restrictions" or opt1 == "ease all restrictions" or opt1 == "ease all":
    time.sleep(1)
    print(space)
    print("Risky move")
    time.sleep(1)
    print(space)
    print("The cases are on the rise again")
    time.sleep(1)
    print(space)
    print("What do you do to stop wave 2 " + premier + "?")
    time.sleep(1)
    print(space)
    print("Option 1: Nothing. Or Option 2: Make a 5km rule and to lots of tests?")
    time.sleep(1)
    print("(And yes that does mean closing the schools again)")
    opt2 = input("Type 1 or 2: ")

    if opt2 == "1":
        time.sleep(1)
        print(space)
        print("You were doing soo well")
        time.sleep(1)
        print(space)
        print("Wave 2 is well and truly upon you")
        time.sleep(1)
        print(space)
        print("Everyone starts getting sick and you are sacked")
        time.sleep(1)
        print(space)
        print("This is the end of the line for you " + premier + ", your rival politian is now the premier of the state.")
        time.sleep(1)
        print(space)
        print("GAME OVER")
        time.sleep(1)
        print(space)
        print("Botch")
        time.sleep(1)
        print(space)
        print("Send this game to your friends if you have them :) ")
        import sys
        sys.exit()

    elif opt2 == "2":
        time.sleep(1)
        print(space)
        print("Good save")
        time.sleep(1)
        print(space)
        print("You successfully avoided the second wave")
        time.sleep(1)
        print(space)
        print("You just need to make one more correct decision and then you are out of the pandemic")
        time.sleep(1)
        print(space)
        print("Do you: "
              "A) Let all the restrictions easy slowly and let people do what they want, or"
              "B) Tell the people that you are a russian spy and that you have sided with the motherland and then proceed to nuke "
              "the whole country?")
        time.sleep(1)
        print(space)
        opt3 = input("Which one, A or B?:")

        if opt3 == "A" or opt3 == "a":
            time.sleep(1)
            print(space)
            print("I"
                  "N"
                  "C"
                  "O"
                  "R"
                  "R"
                  "E"
                  "C"
                  "T")
            time.sleep(1)
            print(space)
            print("There is a wild spike in cases and things turn violent")
            time.sleep(1)
            print(space)
            print("The people come after you and eat your body")
            time.sleep(1)
            print(space)
            print("At least you tried")
            time.sleep(1)
            print(space)
            print("but ya still failed you dumb fu***k")
            time.sleep(1)
            print(space)
            print("Send this game to your friends if you have them :) ")
            import sys

            sys.exit()

        elif opt3 == "B" or opt3 == "b":
            time.sleep(1)
            print(space)
            print("Well done")
            time.sleep(1)
            print(space)
            print("You made good choice commrade")
            time.sleep(1)
            print(space)
            print("The bombs will destroy the country in 3, 2, 1..")
            time.sleep(1)
            print(space)
            print("ViCTORY")
            time.sleep(1)
            print(space)
            print("If there are no more people there is no more virus")
            print("mega stonks")
            time.sleep(1)
            print(space)
            print("You Win")
            print("Send this game to your friends if you have them :) ")
            import sys

            sys.exit()

elif opt1 == "Just the schools" or opt1 == "just open schools" or opt1 == "Just open schools":
    time.sleep(1)
    print(space)
    print("Correct")
    time.sleep(1)
    print(space)
    print("You are good at this")

else:
    time.sleep(1)
    print(space)
    print("                       eRROR")
    time.sleep(1)
    print(space)
    print("syntax . sys  />>......")
    time.sleep(1)
    print(space)
    print("WINNER")
    time.sleep(1)
    print(space)
    print("Congratulations on reaching the sex dungeon")
    time.sleep(1)
    print(space)
    print("Have fun ;) ")
    time.sleep(1)
    print(space)
    print("End of game")

time.sleep(1)
print(space)
print("Ok now what to open up next?")
time.sleep(1)
print(space)
print("Do you open A. Gyms or B. Schoping centers")
opt4 = input("A or B? :")

if opt4 == "A" or opt4 == "a":
    time.sleep(1)
    print(space)
    print("Correct")

elif opt4 == "B" or opt4 == "b":
    time.sleep(1)
    print(space)
    print("Nope")
    time.sleep(1)
    print(space)
    print("try again")
    opt4 = input("A or B? :")

    if opt4 == "A" or opt4 == "a":
        time.sleep(1)
        print(space)
        print("Correct")

    elif opt4 == "b" or opt4 == "B":
        time.sleep(1)
        print(space)
        print("Are u actually dumb bro???")
        time.sleep(1)
        print(space)
        print("Game over")
        time.sleep(1)
        print(space)
        print("This is what happens when you take the piss")
        import sys
        sys.exit()

time.sleep(1)
print(space)
print("You are very close to then end of the pandemic")
time.sleep(1)
print(space)
print("This last step is very important")
time.sleep(1)
print(space)
print("What do you do?"
      "Do you 1. order a large amount of the not yet finished vaccine"
      "or 2. Do you open up small businesses to keep the economy going?")
time.sleep(1)
print(space)

final_option = input("Option 1 or 2 or 3?: ")

if final_option == "1" or final_option == "2":
    time.sleep(1)
    print(space)
    print("Both are valid answers")
    time.sleep(1)
    print(space)
    print("Bravo")
    time.sleep(1)
    print(space)
    print("Well done on leading the state out of a deadly pandemic")
    time.sleep(1)
    print(space)
    print("I am pround of you " + premier + ".")
    time.sleep(1)
    print(space)
    print("You have officially won the game")
    time.sleep(1)
    print(space)
    print("Now you can go play again and see what happens if you don't pick the right options :) ")
    time.sleep(1)
    print(space)
    time.sleep(1)
    print("Send this game to your friends if you have them :) and have a good day ")
    import sys

    sys.exit()

elif final_option == "3":
    print(space)
    time.sleep(1)
    print("To Be Continued....")

else:
    print("You are actually illiterate")
    import sys

    sys.exit()


















