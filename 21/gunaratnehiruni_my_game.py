( MY IDLE WASN’T RESPONDING SO I COULDN’T SAVE A FILE TO SUBMIT) 
COPY AND PASTE ALL THE TEXT STARTING FROM ‘#Hiruni Gunaratne’



#Hiruni Gunaratne
##MouseTrap
#
#INSTRUCTIONS
#1. use 'a''w''d''s' keys to move the mouse around
#2. AIM is to get the cheese without getting trapped by the cats
#3. everytime you overlap the cheese 1 point is added to the score
#4. get as many cheese's as you can wihtout getting trapped by the cat
# GOODLUCK!!
# for picking random numbers
from random import *

# setting up the text sprites
cat1 = TextSprite("😸", x = 195, y = 400)
cat2 = TextSprite("😾", x = 300, y = 400)
cat3 = TextSprite("😻", x = 200, y = 350)
cat4 = TextSprite("😹", x = 150, y = 350)
food1 = TextSprite("🧀", x = 100, y = 100)
food2 = TextSprite("🧀", x = 200, y = 200)
trap1 = TextSprite("💥", x = 30, y = 300)
trap2 = TextSprite("💥", x = 20, y = 30)
trap3 = TextSprite("💥", x = 400, y = 200)
trap4 = TextSprite("💥", x = 110, y = 100)
trap5 = TextSprite("💥", x = 300, y = 330)
trap6 = TextSprite("💥", x = 30, y = 150)
trap7 = TextSprite("💥", x = 300, y = 30)
catcher = TextSprite("🐭", x = 195, y = 10)

score = 0
# the game or show the game over screen
playing= True


@loop_animation

# make the balls fall down at different speeds
cat1.y = cat1.y - 2
cat2.y = cat2.y - 2
cat3.y = cat3.y - 2
cat4.y = cat4.y - 2

# player controls
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    catcher.x = catcher.x - 1
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    catcher.x = catcher.x + 1
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    catcher.y = catcher.y + 1
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    catcher.y = catcher.y - 1

# has the cat caught the mouse?
if catcher.overlaps(cat1):
    # end game 
   playing = False
# same logic for the 2nd cat
if catcher.overlaps(cat2):
    playing = False
# same logic for the 3rd cat
if catcher.overlaps(cat3):
    playing = False
# same logic for the 4th cat
if catcher.overlaps(cat4):
    playing = False

#if mouse overlaps trap then end game 
if catcher.overlaps(trap1):
    playing = False 
#same concept for traps 2,3,4
if catcher.overlaps(trap2):
    playing = False
if catcher.overlaps(trap3):
    playing = False
if catcher.overlaps(trap4):
    playing = False
if catcher.overlaps(trap5):
    playing = False
if catcher.overlaps(trap6):
    playing = False
if catcher.overlaps(trap7):
    playing = False
    
# if mouse overlaps cheese then add points and move cheese to random spot 
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
    
if cat1.y <= 0:
    print(cat1.y)
    # move cat back up to the top
    cat1.y = 400
    # start at a new random x position
    cat1.x = randint (0, 400)
    
if cat2.y <= 0:
    # move cat back up to the top
    cat2.y = 400
    # start at a new random x position
    cat2.x = randint (0, 400)
    
if cat3.y <= 0:
    # move cat back up to the top
    cat3.y = 400
    # start at a new random x position
    cat3.x = randint (0, 400)

if cat4.y <= 0:
    # move cat back up to the top
    cat4.y = 400
    # start at a new random x position
    cat4.x = randint (0, 400)

    
# depending the value of the playing variable: we either play the game,
# or display the end-game screen
if playing == True:
    graphics.clear(0, 0, 0)
    graphics.drawSprite(cat1)
    graphics.drawSprite(cat2)
    graphics.drawSprite(cat3)
    graphics.drawSprite(cat4)
    graphics.drawSprite(food1)
    graphics.drawSprite(food2)
    graphics.drawSprite(trap1)
    graphics.drawSprite(trap2)
    graphics.drawSprite(trap3)
    graphics.drawSprite(trap4)
    graphics.drawSprite(trap5)
    graphics.drawSprite(trap6)
    graphics.drawSprite(trap7)
    graphics.drawSprite(catcher)
    graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
else:
    graphics.clear()
    graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=1, g=0, b=0)
