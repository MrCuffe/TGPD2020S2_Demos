# Dom's mirror jump game! 
# Get the player to the end of each level by jumping over the platforms.
# But keep an eye on the other player as if he touches the red you have to restart the level.
# Below sets the sprites and there starting position
pyangelo = Sprite("https://mrcuffe.github.io/openGameArt/deg0006/cube%20head%20green.png", 0, 0, 32, 32)
pyangelo2 = Sprite("https://mrcuffe.github.io/openGameArt/deg0006/cube%20head%20yellow.png", 468, 368, 32, 32)
flag = Sprite("https://mrcuffe.github.io/openGameArt/deg0006/flag.png", 468, 164, 32, 32)
death1 = Sprite("https://mrcuffe.github.io/openGameArt/deg0006/death.png", 300, 310, 24, 24)
death2 = Sprite("https://mrcuffe.github.io/openGameArt/deg0006/death.png", 220, 290, 24, 24)
death3 = Sprite("https://mrcuffe.github.io/openGameArt/deg0006/death.png", 130, 270, 24, 24)
# Below sets the variable used later in the game
xv = 0
yv = 0
level = 1
air = 0
won = 0
# Below line loops the rest
@loop_animation
if graphics.overlaps(pyangelo.x, pyangelo.y, 32, 32, flag.x, flag.y, 32, 32):
    pyangelo.x = 0
    pyangelo.y = 0
    pyangelo2.x = 468
    pyangelo2.y = 368
    level += 1
# Below sets the platforms for level 1
if level == 1:
    graphics.drawText("_", 100, 50, fontSize = 50)
    graphics.drawText("_", 200, 80, fontSize = 50)
    graphics.drawText("_", 300, 100, fontSize = 50)
    graphics.drawText("_", 400, 120, fontSize = 50)
    if (70 < pyangelo.x < 135 and 53 < pyangelo.y < 60) or (175 < pyangelo.x < 230 and 80 < pyangelo.y < 87) or (270 < pyangelo.x < 330 and 100 < pyangelo.y < 107) or (370 < pyangelo.x < 430 and 123 < pyangelo.y < 130):
        if yv <= 0:
            air = 0
        else:
            air = 2
    else:
        air = 1
# Below tells you its the end as there is only 1 level    
if level == 2:
    graphics.drawText("You win. More levels coming soon!", 10, 200, fontSize = 20)
    won = 1
# Below is the gravity and makes the player slow its acent and then speed up its decent if its above the ground
if pyangelo.y > 0 and yv > -8:
    yv = yv - 0.5
# Below makes it so if the 'A' key is pressed it decreases the x velocity
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_LEFT):
    xv = xv - 0.5
    
# Below makes it so if the 'D' key is pressed it increases the x velocity
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_RIGHT):
    xv = xv + 0.5
    
# Below makes it so if the 'W' key is pressed it jumps if on the ground
if pyangelo.y <= 0 or air == 0:
    yv = 0
    if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_UP):
        yv += 8
# Below slows the players horizontal movement gradually
xv = xv*0.9
# Below updates the players position
pyangelo.y = pyangelo.y + yv
pyangelo.x = pyangelo.x + xv
pyangelo2.y = pyangelo2.y - yv
pyangelo2.x = pyangelo2.x - xv
# Below makes sure the players doesnt go off screen
if pyangelo.x < 0:
    pyangelo.x = 0
if pyangelo2.x < 0:
    pyangelo2.x = 0
if pyangelo.x > 468:
    pyangelo.x = 468
if pyangelo2.x > 468:
    pyangelo2.x = 468
if pyangelo.y > 165:
    pyangelo.y = 165
    yv = 0
if pyangelo2.y < 200:
    pyangelo2.y = 200
    yv = 0
if pyangelo.y < 0:
    pyangelo.y = 0
if pyangelo2.y > 368:
    pyangelo2.y = 368

# Below checks if there is a collision and if so puts you back to the start 
if (graphics.overlaps(pyangelo2.x, pyangelo2.y, 32, 32, death1.x, death1.y, 24, 24) or graphics.overlaps(pyangelo2.x, pyangelo2.y, 32, 32, death2.x, death2.y, 24, 24) or graphics.overlaps(pyangelo2.x, pyangelo2.y, 32, 32, death3.x, death3.y, 24, 24)) and won == 0:
    pyangelo.x = 0
    pyangelo.y = 0
    pyangelo2.x = 468
    pyangelo2.y = 368
# Below clears the screen to black and allows trails
graphics.clear(0, 0.0, 0.0, 0.1)

# Below puts in the center line
graphics.drawText("__________________________________", 0, 195, fontSize = 50)
# Below draws the sprites at their updated x and y coordinates
graphics.drawSprite(pyangelo)
graphics.drawSprite(pyangelo2)
if won == 0:
    graphics.drawSprite(flag)
    graphics.drawSprite(death1)
    graphics.drawSprite(death2)
    graphics.drawSprite(death3)