#This is for picking random numbers (randint)
from random import *


# the sprites will use the image from the URLs above and be placed on coordinates as shown
pyangelo =  TextSprite("🧙‍♂‍", x = 235, y = 25)
pyangelo2 =  TextSprite("💎",x = 225, y = 350)
dino1 = TextSprite("🦖", x = 100, y = 80)
dino2 = TextSprite("🦖", x = 150, y = 250)
dino3 = TextSprite("🦕", x = 350, y = 150)
dino4 = TextSprite("🦕", x = 380, y = 100)
dino5 = TextSprite("🦕", x = 60, y = 210)



# tells loop_animation to continue playing or show 'game over' screen if it is false
playing= True
# Variable set up for levels in the game
level = 1

# everything in the loop animation will be constant throughout the game
@loop_animation


# changes the screen to green
graphics.clear(0.30, 0.85, 0.10, 0.50)   


    
# draws the sprite at the coordinates it was set up with
graphics.drawSprite(pyangelo)
graphics.drawSprite(pyangelo2)
graphics.drawSprite(dino1)
graphics.drawSprite(dino2)
graphics.drawSprite(dino3)
graphics.drawSprite(dino4)
graphics.drawSprite(dino5)



# if the 'A' is pressed, x coordinate of red dot is moved 1 pixel left (key_v_left means the console buttons on screen)
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    pyangelo.x = pyangelo.x - 1
    
# if the 'D' is pressed, x coordinate of red dot is moved 1 pixel right
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    pyangelo.x = pyangelo.x + 1
    
# if the 'W' is pressed, Y coordinate of red dot is moved 1 pixel up
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    pyangelo.y = pyangelo.y + 1
    
# if the 'S' is pressed, y coordinate of red dot is moved 1 pixel down
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    pyangelo.y = pyangelo.y - 1
 
# if the charcter touches gem, score + 1 and goes back to starting coordinates   
if pyangelo.overlaps(pyangelo2):
    #Play sound effect for the gem
    graphics.playSound("https://opengameart.org/sites/default/files/Accept.mp3", volume = 0.1)
    #new level begins when gem is collected therefore, level is increased by 1
    level = level + 1
    #player character goes back to the beginning spot to continue next level
    pyangelo.y = 25
    #dinosaur locations are randomaly selected along x axis for next level
    dino1.x = randint (0,80)
    dino2.x = randint (0,250)
    dino3.x = randint (0,150)
    dino4.x = randint (0,100)
    dino5.x = randint (0,210)
    #^this happens everytime player touches gem

#If player touches the dinosaurs, then game is over and levels restart 
#turns playing variable to false
if pyangelo.overlaps(dino1) or pyangelo.overlaps(dino2) or pyangelo.overlaps(dino3) or pyangelo.overlaps(dino4) or pyangelo.overlaps(dino5):
    graphics.playSound("https://mrcuffe.github.io/openGameArt/sin0041/as_d_roar.wav", volume = 0.1)
    playing = False

#makes dino1 move to the right
dino1.x = dino1.x + 1
dino2.x = dino2.x + 1
dino3.x = dino3.x + 1
dino4.x = dino4.x + 1
dino5.x = dino5.x + 1

# check if the box passes the right edge
if dino1.x > 425:
    #move it back to coordinate 0
    dino1.x = 0
if dino2.x > 425:
    dino2.x = 1
if dino3.x > 425:
    dino3.x = 2
if dino4.x > 425:
    dino4.x = 3
if dino5.x > 425:
    dino5.x = 7

#if character goes below 0 on x axis (left side) stop so player cannot go beyond the walls 
if pyangelo.x < 0:
    # snap it back to place
    pyangelo.x = 0
if pyangelo.x > 460:
    pyangelo.x = 460
if pyangelo.y < 0:
    pyangelo.y = 0
if pyangelo.y > 363:
    pyangelo.y = 363

    
    

#If playing is still true, continue drawing the text on the top left corner showing the level number
if playing == True:
    graphics.drawText("Level: " + str(level),x=0, y=370, fontSize=20)
#If playing is false (when touch dinosaur), game over sign is shown
else:
    graphics.clear()
    graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=1, g=0, b=0)
    
    









