#Surina Chakravorty - This is my phase 4. There are no errors, howvever, I did not get time to change the colour of the background when the player scores 10 points but I did manage to change the overall background.  

# This is for the random numbers
from random import *

# setting up the text sprites, I have also added a the powerup mechanic 
ball1 = TextSprite("◼", x = 195, y = 400)
ball2 = TextSprite("◼", x = 300, y = 400)
powerup = TextSprite("▪", x = 200, y = 195)
catcher = TextSprite("➖ ",x = 195, y = 10)

score = 0
# the playing variable lets the loop_animation decide whether to play
# the game or show the game over screen
playing= True

@loop_animation
#Jazz music will be playing in the background on loop to add to the calm auroa of the game. 
graphics.playSound("https://opengameart.org/sites/default/files/Jazzy%20Vibes%20%2336%20-%20Loop.mp3", volume = 0.1, loop = True)

# The sqaures will fall at different rates to make it 
#harder for the player to catch the sqaures. 
ball1.y = ball1.y - 0.5
ball2.y = ball2.y - 1
powerup.y = powerup.y - 2
# Controls (the a will mean go the the left and the d will be 
#going to the right.)
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    catcher.x = catcher.x - 1
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    catcher.x = catcher.x + 1

# has the player caught the ball(s)?
if catcher.overlaps(ball1):
    # add to score
    score=score+1
    # move ball back up to the top
    ball1.y = 400
    # start at a new random x position
    ball1.x = randint (0, 370)
# same logic for the 2nd ball
if catcher.overlaps(ball2):
    score=score+1
    ball2.y = 400
    ball2.x = randint (0, 370)
#same logic for the powerup 
if catcher.overlaps (powerup):
# adding 5 points instead of 1 
    score=score+5
    powerup.y = 400
    powerup.x = randint (0,370)

# When the sqaures have fallen off the screen, if so, change the
# playing variable to False, as a result the end-game screen will be come up later on. 
if ball1.y <= 0 or ball2.y <= 0:
    playing = False
    
#  The playing variable: we either play the game,
# or display the end-game screen. 
if playing == True:
    graphics.clear(1, 0.7, 0.6)
    graphics.drawSprite(ball1)
    graphics.drawSprite(ball2)
    graphics.drawSprite(catcher)
    graphics.drawSprite(powerup)
    graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
else:
    graphics.clear(0.3, 2, 0.6)
    graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=0, g=1, b=0)

    
