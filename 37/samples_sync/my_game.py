#Sarah David Samuel Year 10 10D

#Sprite representing player
player = Sprite("https://mrcuffe.github.io/openGameArt/dav0017/muffin_avatar_2.png", 0, 50, width = 40 , height = 40)

points = 0

# the sprite will be using the image from the URL below
imageURL1 = "https://mrcuffe.github.io/openGameArt/dav0017/78-783809_blueberries-smoothie-3-blueberry-clipart.png"
#its (x, y) coordinates will be (480, 100)
blueberries = Sprite(imageURL1, x = 580, y = 50, width = 35 , height = 30)
#two more sprites using images from URLs below, applying same logic
#The three sprites below represent the three point gainers in my game
imageURL2 = "https://mrcuffe.github.io/openGameArt/dav0017/91-914558_cherry-png-15-buy-clip-art-cherries-vector.png"
cherry = Sprite(imageURL2, x = 580, y = 150, width = 35 , height = 30 )

imageURL3 = "https://mrcuffe.github.io/openGameArt/dav0017/chocolate-icon-in-cartoon-style-isolated-on-white-vector-12863446(1).jpg"
chocolate = Sprite(imageURL3, x = 580, y = 50, width = 40 , height = 35)

#The three sprites below represent the three point deductors in my game
imageURL4 = "https://mrcuffe.github.io/openGameArt/dav0017/54022662-freehand-drawn-cartoon-butter-knife.jpg"
butter_knife = Sprite(imageURL4, x = 580, y = 50, width = 60 , height = 60)

imageURL5 = "https://mrcuffe.github.io/openGameArt/dav0017/unnamed.gif"
rolling_pin = Sprite(imageURL5, x = 580, y = 100, width = 50 , height = 50)

imageURL6 = "https://mrcuffe.github.io/openGameArt/dav0017/istockphoto-514913808-170667a.jpg"
blender = Sprite(imageURL6, x = 580, y = 150, width = 25 , height = 50)
#These are more copies of the sprites above
blueberries_A = Sprite(imageURL1, x = 580, y = 150, width = 35 , height = 30)
blueberries_AA = Sprite(imageURL1, x = 580, y = 50, width = 35 , height = 30)
cherry_B = Sprite(imageURL2, x = 580, y = 100, width = 35 , height = 30)
cherry_BB = Sprite(imageURL2, x = 580, y = 100, width = 35 , height = 30 )
rolling_pin_B = Sprite(imageURL5, x = 580, y = 100, width = 50 , height = 50 )
blender_C = Sprite(imageURL6, x = 580, y = 150, width = 25 , height = 50)

#function for 'game over' screen 
def game_over():
    graphics.clear(1, 1, 1) 
    graphics.drawText("GAME OVER", 130, 200, fontSize = 30, r = 0, g = 0, b = 0, a = 1)

#function for introducing dinner table at the end of game
def introduce_dinner_table():
    url = "https://mrcuffe.github.io/openGameArt/dav0017/h3ruBeYI11Saofdh4cDpZjl72eJkfbmt4t8yenImKBVvK0kTmF0xjctABnaLJIm9.jpeg"
    dinner_table = Sprite(url, x = 100, y = 0, width = 300 , height = 150)
    player_in_Heaven = Sprite("https://mrcuffe.github.io/openGameArt/dav0017/muffin_avatar_2.png", 40, 300, width = 40 , height = 40)
    player_in_Hell = Sprite("https://mrcuffe.github.io/openGameArt/dav0017/muffin_avatar_2.png", 300, 300, width = 40 , height = 40)
    
    graphics.clear(1, 1, 1)
    graphics.drawSprite(dinner_table)
    graphics.drawText("Muffin Heaven", 40, 350,fontSize = 20, r = 0, g = 0, b = 1, a = 1)
    graphics.drawText("Muffin Hell", 300, 350,fontSize = 20, r = 1, g = 0, b = 0, a = 1)
   # if player has greater than or equal to 80 points then display the following
   #player goes to muffin heaven
    if points >= 80:
        graphics.drawSprite(player_in_Heaven)
        #when displying points value, error may be present as it seems to keep changing the value
        #I am still working on this error
        graphics.drawText(f"{points} Points!", 40, 280,fontSize = 12, r = 0, g = 0, b = 1, a = 1)
    #else player goes to muffin hell
    else:
        graphics.drawSprite(player_in_Hell)
        graphics.drawText(f"{points} Points", 300, 280,fontSize = 12, r = 1, g = 0, b = 0, a = 1)

# records when game starts
start_time = time.time()

#everything under "@loop_animation" will be in a while loop
@loop_animation
# current time minus time when game started will give how much time passed since game started
time_since_game_started = time.time() - start_time

#below, from line 45 to 59, is coding for WADS control keys    
# if the 'W' is pressed update the x coordinate to move 5 pixels up
if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
    player.y = player.y + 5
    
# if the 'S' is pressed update the x coordinate to move 5 pixels down
if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
    player.y = player.y - 5
# also I must learn to limit the screen size because I don't want the player moving all over the screen, only on the platform area.

# moving sprites left a little
blueberries.x = blueberries.x - 1
blender.x = blender.x - 1
# second sprite will move left 1 second after game starts
if (time_since_game_started > 1):
    rolling_pin.x = rolling_pin.x - 1
# applying same logic to other sprites
if (time_since_game_started > 2):
    cherry.x = cherry.x - 1

if (time_since_game_started > 2):
    butter_knife.x = butter_knife.x - 1
    
if (time_since_game_started > 3):
    blender.x = blender.x - 1

if (time_since_game_started > 4):
    blueberries_A.x = blueberries_A.x - 1
    
if (time_since_game_started > 4):
    cherry_B.x = cherry_B.x - 1
    
if (time_since_game_started > 5):
    chocolate.x = chocolate.x - 1
    
if (time_since_game_started > 6):
   rolling_pin_B.x = rolling_pin_B.x - 1
    
if (time_since_game_started > 7):
    blueberries_AA.x = blueberries_AA.x - 1
    
if (time_since_game_started > 7.5):
    blender_C.x = blender_C.x - 1

if (time_since_game_started > 9):
    cherry_BB.x = cherry_BB.x - 1
# detecting collision
if player.overlaps(blueberries):
# add one point if player collided with sprite
    points=points+10
# reset sprite back to the right
    blueberries.x = 580

#applying same logic to the other sprites
if player.overlaps(cherry):
    points=points+20
    cherry.x = 580
if player.overlaps(chocolate):
    points=points+30
    chocolate.x = 580
if player.overlaps(butter_knife):
    points=points-5
    butter_knife.x = 580
if player.overlaps(rolling_pin):
    points=points-15
    rolling_pin.x = 580
if player.overlaps(blender):
    points=points-25
    blender.x = 580
if player.overlaps(blueberries_A):
    points=points+10
    blueberries_A.x = 580
if player.overlaps(cherry_B):
    points=points+20
    cherry_B.x = 580
if player.overlaps(rolling_pin_B):
    points=points-15
    rolling_pin_B.x = 580
if player.overlaps(blueberries_AA):
    points=points+10
    blueberries_AA.x = 580
if player.overlaps(blender_C):
    points=points-25
    blender_C.x = 580
if player.overlaps(cherry_BB):
    points=points+20
    cherry_BB.x = 580

# has it gone off the left without colliding with player?
if blueberries.x == 0:
# reset sprite back to the right
    blueberries.x == 580

#applying same logic to the other sprites
if cherry.x == 0:
    cherry.x = 580
if chocolate.x == 0:
    chocolate.x = 580
if butter_knife.x == 0:
    butter_knife.x = 580
if rolling_pin.x == 0:
    rolling_pin.x = 580
if blender.x == 0:
    blender.x = 580
if blueberries_A.x == 0:
    blueberries_A.x = 580
if cherry_B.x == 0:
    cherry_B.x = 580
if rolling_pin_B.x == 0:
    rolling_pin_B.x = 580
if blueberries_AA.x == 0:
    blueberries_AA.x = 580
if blender_C.x == 0:
    blender_C.x = 580
if cherry_BB.x == 0:
    cherry_BB.x = 580

# clears the screen to white
graphics.clear(1, 1, 1)
#"Points:" text instructions
graphics.drawText(f"Points:{points}", 5, 300, fontSize = 14, r = 0, g = 0, b = 0, a = 1)
# Writing instructions
graphics.drawText("Use the W,A,S,D keys to move Avatar!", 200, 370, fontSize = 12, r=0, g=0, b=0)
# instructions for drawing black platform
box_sprite = Sprite(Rectangle(0, 30, 500, 20), r = 0, g = 0, b = 0)
# draws the sprites at their coordinates
graphics.drawSprite(blueberries)
graphics.drawSprite(cherry)
graphics.drawSprite(butter_knife)
graphics.drawSprite(rolling_pin)
graphics.drawSprite(chocolate)
graphics.drawSprite(blueberries_A)
graphics.drawSprite(cherry_B)
graphics.drawSprite(rolling_pin_B)
graphics.drawSprite(blueberries_AA)
graphics.drawSprite(blender_C)
graphics.drawSprite(cherry_BB)
graphics.drawSprite(player)#sprite representing player
graphics.drawSprite(box_sprite)

#calling on game over function after 60 seconds
if (time_since_game_started > 60):
    game_over()
#calling on introducing dinner table function after 62 seconds    
if (time_since_game_started > 62):
    introduce_dinner_table()
