# Instructions:
print("Welcome to the jungle marathon!")
print("Your aim is to capture all the treasure")
print("The follwing commands can be used")
print("In order to move left or right use respective A and D keys")
print("In order to move up use W  key")
print("In order to move down use S key")
######################################### for picking random numbers
from random import *
# setting up the text
spritesfood1 = TextSprite("￿", x = 100, y = 100)
food2 = TextSprite("￿", x = 235, y = 120)
food3 = TextSprite("￿", x = 380, y = 130)
food4 = TextSprite("￿", x = 450, y = 110)
catcher = TextSprite("￿", x = 195, y = 10)
score = 0
# the playing variable lets the loop_animation decide whether to play
# the game or show the game over screenplaying= True
@loop_animation
# player key controls
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    catcher.x = catcher.x - 1
    if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
        catcher.x = catcher.x + 1
    if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
        catcher.y = catcher.y + 1
    if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
        catcher.y = catcher.y - 1
# if catcher overlaps food then add points
if catcher.overlaps(food1):
    # add to score
    score=score+1
    food1.y = 200    
    # start at a new random x position    
    food1.x = randint (0, 200)
if catcher.overlaps(food2):   
    # add to score    
    score=score+1
    food2.y = 200    
    # start at a new random x position    
    food2.x = randint (0, 200)
if catcher.overlaps(food3):
    # add to score    
    score=score+1    
    food3.y = 200    
    # start at a new random x position    
    food3.x = randint (0, 200)
    if catcher.overlaps(food4):    
        # add to score    
        score=score+1    
        food4.y = 200    
        # start at a new random x position    
        food4.x = randint (0, 200)
        # depending the value of the playing variable: we either play the game,
        # or display the end-game screen
    if playing == True:    
        graphics.clear(0, 0, 0)    
        graphics.drawSprite(food1)    
        graphics.drawSprite(food2)    
        graphics.drawSprite(food3)    
        graphics.drawSprite(food4)    
        graphics.drawSprite(catcher)    
        graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
    else:    
        graphics.clear()    
        graphics.drawText("Game over how sad, better luck next time!", x=100, y=230, fontSize=20, r=1, g=0, b=0)