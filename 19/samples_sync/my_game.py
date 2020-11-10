"""PLEASE COPY AND PASTE THIS CODE INTO PYANGELO"""
#player status
playing= True
#initial score
score = 0
#this is for picking random numbers
from random import *
#clear screen
graphics.clear(1.0, 1.0, 1.0, 1.0)
#set sprites
player= Sprite(Rectangle(40, 40, 50, 50), r = 0, g = 1, b = 1)
ball1 = TextSprite("💥 ", x = 195, y = 400)
ball2 = TextSprite("💥", x = 300, y = 400)
ball3 = TextSprite("💥 ", x = 14, y= 400)
ball4 = TextSprite("💥 ", x = 399, y= 400)
food1 = TextSprite ("🍔",x = 399, y= 400)
# loop forever
@loop_animationdwasd
######### moving the player #########
#move the player to the left (key A)
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
       player.x = player.x - 3
       graphics.clear(0.0, 0.0, 0.0, 1.0)
       graphics.drawSprite(player)
#move the player to the right(key D)
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
       player.x = player.x + 3
       graphics.clear(0.0, 0.0, 0.0, 1.0)
       graphics.drawSprite(player)
#move the player up(key W)
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
       player.y = player.y + 3
       graphics.clear(0.0, 0.0, 0.0, 1.0)
       graphics.drawSprite(player)
#move the player down(key S)
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
       player.y = player.y - 3
       graphics.clear(0.0, 0.0, 0.0, 1.0)
       graphics.drawSprite(player)

########### not lettin the player bypasses the edge of screen#####
# set up player direction (and speed)
dir_x = 4
dir_y = 4
# check if player passes the left edge
if player.x < 0:
    # snap it back to place
    player.x = 0
    # reverse direction
    dir_x *= -1
# check if player passes the bottom edge
if player.y < 0:
    player.y = 0
    dir_y *= -1
# check if player passes the right edge
if player.x > graphics.width - player.getWidth():
    player.x = graphics.width - player.getWidth()
    dir_x *= -1
# check if player passes the top edge
if player.y > graphics.height - player.getHeight():
    player.y = graphics.height - player.getHeight()
    dir_y *= -1
    
############# if player touches bomb it dies, if player eat food score increases#################
# make the bombs fall down at different speeds
ball1.y = ball1.y - 1
ball2.y = ball2.y - 2
ball3.y = ball3.y - 3
ball4.y = ball4.y - 4
food1.y = food1.y - 2
#dies once touch bomb
if player.overlaps(ball1):
    playing = False
if player.overlaps(ball2):
     playing = False
if player.overlaps(ball3):
     playing = False
if player.overlaps(ball4):
     playing = False 
#score increases once eat food
if player.overlaps(food1):
    # move food back up to the top
    food1.y = 400
    # start at a new random x position
    food1.x = randint (0, 370)
    #score+1
    score=score+1
#sprites return to top once fall out of screen
if ball1.y <= 0:
    ball1.y = 400
    ball1.x = randint (0, 370)
if ball2.y <= 0:
    ball2.y = 400
    ball2.x = randint (0, 370)
if ball3.y <= 0:
    ball3.y = 400
    ball3.x = randint (0, 370)
if ball4.y <= 0:
    ball4.y = 400
    ball4.x = randint (0, 370)
if food1.y <= 0:
    food1.y = 400
    food1.x = randint (0, 370)
#drawing the sprites
if playing == True:
    graphics.clear(0, 0, 0)
    graphics.drawSprite(ball1)
    graphics.drawSprite(ball2)
    graphics.drawSprite(ball3)
    graphics.drawSprite(ball4)
    graphics.drawSprite(food1)
    graphics.drawSprite(player)
#drawing the score
    graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
#if playing is False
else:
    graphics.clear()
    graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=1, g=0, b=0)
#final score
    graphics.drawText("Final score: " + str(score), x=120, y=170, fontSize=30, r=1, g=1, b=1)
