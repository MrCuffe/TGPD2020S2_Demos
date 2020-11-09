#AUTHOR : KYM MINT
#this allows for radom generation of the aim circle which increases the score
from random import *
#Links to images used for sprites, the names do not match the actual image
imageURL = "https://mrcuffe.github.io/openGameArt/min0006/square%20green.png"
circle = "https://mrcuffe.github.io/openGameArt/min0006/circle.png"
circle_2 = "https://mrcuffe.github.io/openGameArt/min0006/square.png"
#this sets up the base for the game
class game:
    SETUP = 0
    PLAY = 1
    STOPPED = 2
    state = SETUP
    finish = 0
    trial = 0
    ground = 0
    score = 5
#this is the moveable character
class player:
    start_x = 0
    start_y = 0
    start_w = 30
    start_h = 30
    sprite = Sprite(imageURL, start_x, start_y, start_w, start_h)
    score = 0
#this is the first collision character: the aim is to collide with it
class aim:
    start_x = 100
    start_y = 100
    start_w = 30
    start_h = 30
    sprite = Sprite(circle, start_x, start_y, start_w, start_h)
#another collision character: the aim is to avoid colliding with it
class murder:
    start_x = 75
    start_y = 75
    start_w = 30
    start_h = 30
    dir_y = 3.5
    sprite = Sprite(circle_2, start_x, start_y, start_w, start_h)
#another collision character: the aim is to avoid colliding with it
class murderaswell:
    start_x = 150
    start_y = 150
    start_w = 30
    start_h = 30
    dir_y = 4
    sprite = Sprite(circle_2, start_x, start_y, start_w, start_h)
#another collision character: the aim is to avoid colliding with it
class murder_3:
    start_x = 400
    start_y = 350
    start_w = 30
    start_h = 30
    dir_y = 5
    sprite = Sprite(circle_2, start_x, start_y, start_w, start_h)
#another collision character: the aim is to avoid colliding with it
class murder_4:
    start_x = 300
    start_y = 50
    start_w = 30
    start_h = 30
    dir_y = 4
    sprite = Sprite(circle_2, start_x, start_y, start_w, start_h)
#defines score 
score_1 = 0
#loops coding below
@loop_animation 

    
#updates the display and movements of characters (a_char)
def update (a_char):
    #direction defining so the sprite can bounce off of walls
    murder.sprite.y += murder.dir_y
    murder_3.sprite.y += murder_3.dir_y
    murder_4.sprite.y += murder_4.dir_y
    murderaswell.sprite.y += murderaswell.dir_y
    #clears screen so that previous images dont stay on the screen as sprite moves
    graphics.clear (0.0, 0.0, 0.0, 1.0)
    #draws sprites
    graphics.drawSprite (a_char.sprite)
    graphics.drawSprite (aim.sprite)
    graphics.drawSprite (murder.sprite)
    graphics.drawSprite (murder_3.sprite)
    graphics.drawSprite (murder_4.sprite)
    graphics.drawSprite (murderaswell.sprite)
    #draws score and updates it as the score increases
    graphics.drawText("Score: "  + str(player.score), 200, 370, fontSize = 15)
    #if collides with bottom edge this changes the direction
    if murder.sprite.y < 0:
        # snaps it back to place
        murder.sprite.y = 0
        # reverses direction
        murder.dir_y *= -1
    #if collides with top edge this changes the direction
    elif murder.sprite.y > graphics.height - murder.sprite.getHeight():
        # snap it back to place
        murder.sprite.y = graphics.height - murder.sprite.getHeight()
        # reverse direction
        murder.dir_y *= -1
    #if collides with bottom edge this changes the direction
    if murder_4.sprite.y < 0:
        # snap it back to place
        murder_4.sprite.y = 0
        # reverse direction
        murder_4.dir_y *= -1
    #if collides with top edge this changes the direction
    elif murder_4.sprite.y > graphics.height - murder_4.sprite.getHeight():
        # snap it back to place
        murder_4.sprite.y = graphics.height - murder_4.sprite.getHeight()
        # reverse direction
        murder_4.dir_y *= -1
    #if collides with bottom edge this changes the direction
    if murderaswell.sprite.y < 0:
        # snap it back to place
        murderaswell.sprite.y = 0
        # reverse direction
        murderaswell.dir_y *= -1
    #if collides with top edge this changes the direction
    elif murderaswell.sprite.y > graphics.height - murderaswell.sprite.getHeight():
        # snap it back to place
        murderaswell.sprite.y = graphics.height - murderaswell.sprite.getHeight()
        # reverse direction
        murderaswell.dir_y *= -1
    #if collides with bottom edge this changes the direction
    if murder_3.sprite.y < 0:
        # snap it back to place
        murder_3.sprite.y = 0
        # reverse direction
        murder_3.dir_y *= -1
    #if collides with top edge this changes the direction
    elif murder_3.sprite.y > graphics.height - murder_3.sprite.getHeight():
        # snap it back to place
        murder_3.sprite.y = graphics.height - murder_3.sprite.getHeight()
        # reverse direction
        murder_3.dir_y *= -1
    
    
    
# checks when keys are pressed and when sprites collide etc.
def check_inputs():
    #allows the game to stop once collision with murder sprite is recorded
    if game.state == game.STOPPED:
        graphics.clear()
    #allows the game to play if the game has not stopped    
    else:
        # if the 'A' is pressed update the x coordinate to move 5 pixel left
        if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
            player.sprite.x = player.sprite.x - 5
            
        # if the 'D' is pressed update the x coordinate to move 5 pixel right
        if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
            player.sprite.x = player.sprite.x + 5
            
        # if the 'W' is pressed update the x coordinate to move 5 pixel up
        if graphics.isKeyPressed(KEY_W) or graphics.isKeyPressed(KEY_V_UP):
            player.sprite.y = player.sprite.y + 5
            
        # if the 'S' is pressed update the x coordinate to move 5 pixel down
        if graphics.isKeyPressed(KEY_S) or graphics.isKeyPressed(KEY_V_DOWN):
            player.sprite.y = player.sprite.y - 5
    #allows the player to travel through one wall and exit out the opposite one
        if (player.sprite.x < 0):
            player.sprite.x = graphics.width
          #allows the player to travel through one wall and exit out the opposite one   
        if (player.sprite.y < 0):
            player.sprite.y = graphics.height
         #allows the player to travel through one wall and exit out the opposite one    
        if (player.sprite.x > graphics.width):
            player.sprite.x = 0
         #allows the player to travel through one wall and exit out the opposite one    
        if (player.sprite.y > graphics.height):
            player.sprite.y = 0    
        #collision and spawning
        #collison for aim sprite
        if (player.sprite).contains (aim.sprite):
            player.score = player.score + 5
            aim.sprite.y = randint(0, 300) 
            aim.sprite.x = randint(0, 400)
        if (aim.sprite).contains (player.sprite):
            player.score = player.score + 5
            aim.sprite.y = randint(0, 300) 
            aim.sprite.x = randint(0, 400) 
        #changes direction
        if (player.score > game.score):
            murder.dir_y += 3
            murderaswell.dir_y += 3
            murder_3.dir_y += 3
            murder_4.dir_y += 3
            game.score += 5
        #collision with murder sprites
        if (player.sprite).contains (murder.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            #these were attempts at collecting the time stamp to elongate the period that 'game over' was printed on the screen
            #however they are now used to end the game 
            finish_time = time.time()
            game.finish = time.time()
        if (player.sprite).contains (murder_3.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time()
        if (player.sprite).contains (murderaswell.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time()
        if (player.sprite).contains (murder_4.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time()
        #repetition makes the collision more accurate
        if (murder.sprite).contains (player.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time()
        if (murderaswell.sprite).contains (player.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time()
        if (murder_3.sprite).contains (player.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time()
        if (murder_4.sprite).contains (player.sprite):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            finish_time = time.time()
            game.finish = time.time() 
        #this was my attempt at delaying the print screen
        if (game.finish > 0):
            graphics.clear()
            game.finish = game.finish +50
        #doesnt allow aim sprite to spawn outside of screen boundaries    
        if (aim.sprite.y > graphics.height -5):
            aim.sprite.y = 0
        if (aim.sprite.x > graphics.height -5):
            aim.sprite.x = 0
        #ends game    
        if (game.finish > 0):
            graphics.drawText("game over", 100, 150, fontSize = 42)
            
            game.state = STOPPED
#setting up the game - loads images
def setup():
    #make sure we only setup the game once
    if game.state == game.SETUP:
        game.state = game.PLAY
            
        #clears the screen to black
        graphics.clear (0.0, 0.0, 0.0, 1.0)
        #draws the sprite image on the screen
        graphics.drawSprite (player.sprite)
        #sound to play when game starts
        sound = graphics.loadSound("https://mrcuffe.github.io/openGameArt/min0006/free-music-for-youtube-videos-no-copyright-download-overdrive-corbyn-kites-vlog-background-music.mp3")
        graphics.playSound(sound)

#checks inputs and allows for gameplay
def start (score_1):
    if game.state == game.PLAY:
        #let the game begin!
        check_inputs()
        update(player)
        
#call the setup function before we start the game
setup()
#starts the game
start (score_1)
            
