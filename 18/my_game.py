#Hamish Handoll Stage 6
#credit Peter Handoll, https://www.w3schools.com/python/default.asp

import random
import math

#introduction to the game, sets up the story line.
print ("As you look around you can see the daylight slowly leaving the world around you, an event you still haven’t become used to happening so early in the day, but the Himalayas will do that.  The sun is creeping slowly downward, not toward the horizon yet, but towards the ridgeline which will have the same effect, darkness.  As you check your map you realise the campsite you had planned to reach today would not be an option, hiking in the dark would simply be too dangerous.  There is a second campsite much nearer though, far enough out of your way that originally you didn’t choose it.  Well, that and the stories surrounding the place, stories of people disappearing there for centuries, vanishing without a trace, and then reappearing days, sometimes weeks later.  Usually reappearing in the same place but sometimes impossibly far away, sometimes mountains away with no explanation of how they got there.  But in an environment like this shelter is shelter, so you pick a route on your map and begin the trek for a place to stay the night.  As you walk you notice small discrepancies between the map and what is going on around you, creeks out of place, a different shaped path, and landmarks and creeks that aren’t marked at all.  As you near what is supposed to be the campsite you realise something is very wrong with the topography.  One of the ridgelines simply doesn’t exist, instead there is a sheer, weathered cliff face.  As you look around, trying to pinpoint your location you realise that one of two things must be true.  Either you are reasonably lost, or the information on this section of the map is old, hundreds of years old to give the land time to change into what it is today.  With a growing sense of concern, you look for the actual site of the campsite, trying as best you can to combine the map with the world around you.  After a few minutes of searching you find not the campsite you were expecting, but a bamboo hut of some sort.  You walk inside to have a look, slipping your pack onto the ground as you enter. You find yourself in a well-lit, simple bamboo structure without any adornments or features at all.  The surprising part is the cleanness of the hut, no leaves or animal prints inside, not even a speck of dirt.  But no sign of any human presence either, nothing to indicate how it was kept so miraculously clean.  You begin preparing to stay in the hut overnight, separating the food out and stacking inside the hut when the sun finally slips below the ridge, plunging the valley into a greyness, not quite night.  As if in reaction you feel a strange sensation beneath you, as if the floor is changing, angling inwards.")
input("press enter to continue:  ")
print ()
print()


def ask_question(question, game_statistics):
    #prints description of puzzle and it's place within the room.
    print (question["query"])

    #resets progress through puzzle.
    attempt_counter = 0
    #sets boundary conditions for each individual puzzle.
    while question["solved"] == False and attempt_counter < question["maximum_attempts"]:
        #prompts the player to input an answer then stores it.
        answer = input(question["prompt"])
        #checks if the users answer is the correct answer
        if answer.lower() == question["correct_answer"].lower():
            #narrates progress after completing puzzle.
            print (question["success_message"])
            #exits while loop.
            question["solved"] = True
            #increases the global variable counting the number of puzzles solved
            game_statistics["solve_counter"] += 1
        #makes user retry and counts number of failed attampts.
        else:
            print (question["failure_message"])
            attempt_counter += 1
    #forces/allows user to skip puzzle if they use too many attempts.
    if attempt_counter == question["maximum_attempts"]:
        #increases the global variable counting number of puzzles failed/skipped.
        game_statistics["skip_counter"] += 1
        print (question["too_many_attempts_message"])


def roomer (room):
    #provides space on screen.
    print()
    print()
    #describes room
    print(room["room_info"]["room_description"])
    #selects the number of puzzles to display within a given room, and accesses random puzzles from within a given room.
    question_list = random.sample(list(room["question_list"]), room["room_info"]["room_questions"])
    #displays the correct number of randomly selected rooms, and accesses the global variables for counting skips and completion. 
    for value in question_list:
        ask_question(room["question_list"][value], game_statistics)
    #describes completion of a room and progression into the next
    print(room["room_info"]["room_solved"])


def game():
    #presents rooms in desired order.
    roomer (antechamber)
    roomer(room_one)
    roomer(room_two)
    #tells player how many puzzles they completed, and how many they skipped.
    print ("skip counter: ", game_statistics["skip_counter"], "solve counter: ", game_statistics["solve_counter"])
    #gives ending message appropriate to number of puzzles skipped.
    if game_statistics["skip_counter"] < 1:
        print ("you suddenly see the gears and cogs that have been artfully hidden in the room start to move, grinding away.  Then with a clunk the roof starts to slide open, slowly unwinding through ancient clockwork.  Soon enough it comes to a halt, leaving an open sky above your head.  With a sigh of relief you climb out of the structure, wondering how and why any of it happened in the first place.")
    elif game_statistics["skip_counter"] < 3 and game_statistics["skip_counter"] > 0:
        print ("you suddenly see the gears and cogs that have been artfully hidden in the room start to move, grinding away.  Then with a clunk the roof starts  to slide open, slowly unwinding through ancient clockwork.  With the roof mostly open you hear something snap and everyhting stops moving.  You  climb up and out of the structure, glad to escape the confines of that dark, mysterious place.")
    elif game_statistics["skip_counter"] < 5 and game_statistics["skip_counter"] > 2:
        print ("you suddenly see the gears and cogs that have been artfully hidden in the room start to move, grinding away.  Then with a clunk the roof starts  to slide open, slowly unwinding through ancient clockwork.  With the roof partly open you hear the sounds of a failing machine.  Snapping and groaning in protest, the roof stops moving, leaving just enough room for you to climb out.  And climb out you do, squeezing past the gap to the sky and finally getting a breath of fresh air.")
    else:
        print ("you suddenly see the gears and cogs that have been artfully hidden in the room start to move, grinding away.  Then with a clunk the roof starts  to slide open, only to stop again, leaving you with the tantalising sight of sunlight, but unable to reach it.  After all your efforts you broke to many things on the way out, and now the mechanism to let you escape has failed, leaving you stuck down here.")

#global variables throughout game stored in dictionary so they can be changed
game_statistics = {
    "skip_counter" : 0,
    "solve_counter" : 0
    }

#creates a dictionary for each room.
antechamber = {
    #describes entrance to, exit from and number if puzzles to be displayed in this particular room.
    "room_info" : {
        "room_questions": 1,
        "room_description": "Starting to panic, you feel yourself sliding down, into the middle of the floor and then below until you know is darkness, a complete absence of light.  You wake up to a barely lit room and your supplies sitting next to you.  As you peer into the gloom the only thing you notice out of place is a pipe running along the the courner of the wall and floor.",
        "room_solved": "Now that the lock is open you are able to turn the lamp on and look at the room around you."
    },
    #holds data of individual puzzle within room
    "question_list" : {
        "first_puzzle" : {
            "query":"  You follow it to what looks like a lamp, in the attempt to turn it on you find there is a three digit combination lock placed around the ignition switch, blocking it from use.  With disgust you sag down next to the lamp when something catches your eye, a number sequence on the inside of the shutter, but it appears to be missing a number.",
            "prompt" : "7, 49, 8, 64, 9, 81, 10, 100, 11, ___, 12, 144, 13, 169.  Enter the missing number in the sequence: ",
            "correct_answer" : "121",
            "success_message" : "you try the number into the combination lock and it clicks open",
            "failure_message" : "incorrect combination",
            "maximum_attempts" : 10,
            "too_many_attempts_message" : "after an excessive number of attempts the lock breaks open in your hands, you got lucky this time",
            "solved" : False
            }
    }
}
room_one = {
    #describes entrance to, exit from and number if puzzles to be displayed in this particular room.
    "room_info" : {
        "room_questions": 2,
        "room_description": "You find yourself in a dim, simple room, a few meters in diameter.  At first glance it appears to be completely uniform, made entirely of bamboo with no obvious way out, or anything to help you escape.",
        "room_solved": "                                                                                                                                                                                                                                                                                                   Solving, or somehow completing all these puzzles has completed whatever mechanism is at work, hidden behind the walls.  Silently, without making a scratch, a small portion of one of the walls slides away, leaving a space big enough to crawl through."
    },
    #holds data of individual puzzles within room
    "question_list" : {
        "colour_puzzle" : {
            "query" : "Sitting on it's own in a corner of the room is a light box, shining white light through a filter.  This filter blocks red light from hitting the sensor",
            "prompt" : "With no ability to see red, what colour do you see the purple material as? ",
            "correct_answer" : "blue",
            "success_message" : "you slide the correct coloured panel into place.  This changes the colour of thelight beam and the box springs open.  A deep grumbling noise echoes from somewhere within the building.",
            "failure_message" : "you clearly have never been colourblind",
            "maximum_attempts" : 7,
            "too_many_attempts_message" : "you must be one of those people who think green isn't a primary colour, there is no hope for you to ever complete this.",
            "solved" : False        
        },
        "darkness_riddle" : {
            "query" : "As you walk around the room, feeling along the walls you find a scratch pad nestled in a courner on the ground, only visible when you are right on top of it.  When you bend down to investigate you find a steel rod next to it, and inscribed on the wall a riddle: ",
            "prompt" : "It cannot be seen, cannot be felt,Cannot be heard, cannot be smelt.It lies behind stars and under hills,And empty holes it fills.It comes first and follows after,Ends life, kills laughter. type the answer to the riddle: ",
            "correct_answer" : "dark",
            "success_message" : "As you scratch the word onto the pad you see a panel of the wall slide to the side, revealing a doorway.  A resounding clunk sounds around the room.",
            "failure_message" : "despite your efforts, nothing happens",
            "maximum_attempts" : 7,
            "too_many_attempts_message" : "You have scratched away the entire pad, probably breaking it, but it causes a panel of the wall slide to the side, revealing a doorway",
            "solved" : False
        },
        "compass_puzzle" : {
            "query" : "In the center of the ceiling you spot a compass, but one that looks like it was used to colonise Australia.  Then realise there is something wrong with it, there is only one needle on it, the red black one.  As you stand directly underneath it to have a better look you nearly trip over another combination lock, although you can't see what it is used for.  Then you realise it has three digits, and is directly underneath a compass, probably not a coincidence.",
            "prompt" : "what angle is the black needle of the compass pointing to? ",
            "correct_answer" : "180",
            "success_message" : "You enter the angle for south in, and see the dials retract below to be replced by floor, as if nothing was ever there.  Then you hear the creaking sound of springs being tensioned, and pushing against their surroundings.",
            "failure_message" : "wrong hemisphere",
            "maximum_attempts" : 5,
            "too_many_attempts_message" : "you keep spinning the dials but with no succes, then the dials start spinning loosely, no longer engaging with the tumblers, rendering them useless.",
            "solved" : False

        }
    }
}

room_two = {
    #describes entrance to, exit from and number if puzzles to be displayed in this particular room.
    "room_info" : {
        "room_questions": 2,
        "room_description": "With a sigh you squeeze your way through the opening and into another, nearly identical room, except this one is taller, and appears to have an upward slant.  Could this possibly be leading to a way out? ",
        "room_solved": "Did you solve enough puzzles to escape?"
    },
    #holds data of individual puzzles within room
    "question_list" : {
        "magnetic_puzzle" : {
            "query" : "you spot a section of the wall that is a different colour, when you go to inspect it you realise that it is made of iron.  You also discover a mechanism infront of the iron slab with a selection of materials infront of it",
            "prompt" : "Which material will be able pull Iron away? Copper, Cobalt, Platinum, Silver  ",
            "correct_answer" : "Cobalt",
            "success_message" : "As you slide the Cobalt into place the iron starts to wobble, then slide forward of the ledge and fall to the ground, revealing the space behind it. Again you hear that groaning noise, and realise it wasn't limited to the first room.",
            "failure_message" : "",
            "maximum_attempts" : 1,
            "too_many_attempts_message" : "This metal appears to have an adverse reaction with it's container, smashing it and breaking the mechanism.",
            "solved" : False
        },
        "hidden_message" : {
            "query" : "as you search the room for anything to help you get out you find a door hidden inside the walls.  When you try to open it you find it locked, with a strange message written on the handle.",     
            "prompt" : "my oranges made evil nests to undermine me. what is the hidden technique to get through the door? ",
            "correct_answer" : "momentum",
            "success_message" : "Wondering why you never thought of it, you get a run up and burst through the door.  You hear the sound of iron clamping together, in your ears  and in your chest.",
            "failure_message" : "Is that actually going to get you through a door",
            "maximum_attempts" : 3,
            "too_many_attempts_message" : "In frustration you shove the door angrily, snapping the lock and breaking in",
            "solved" : False
        },
        "difference_product" : {
            "query" : "",
            "prompt" : "6, 4 : 210.  13, 2 : 1115.  8, 9 : 117.  24, 31 : ______.  18, 16 : 234.  What is the missing number? ",
            "correct_answer" : "755",
            "success_message" : "You push down the keys to the rudimentary keypad in order.  When you finish, the keypad retracts into the wall, and you see an easing of tension throughout the walls of the room.",
            "failure_message" : "despite your best attempts, nothing happens",
            "maximum_attempts" : 7,
            "too_many_attempts_message" : "when yet another attempt yields no results you slam your palm against the center button.  When you hear a snap and see the wood crack open then jam all the way in you realise you have broken the keypad.",
            "solved" : False
        }
    }
}


game()


