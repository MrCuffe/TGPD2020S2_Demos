
#changes the game between setup and play and defines values, also creates a variable for the ground
class game:
    SETUP = 0
    PLAY = 1
    state = PLAY
    ground = 0
#creates the sprite, as well as defining its position as well as sizing. Defines the velocity of the sprite    
class player:
    def_velocity = 6
    start_x = 0
    start_y = 0
    start_h = 100
    start_w = 100
    background = Sprite("https://raw.githubusercontent.com/pretz445/bruh/images/pixil-frame-0%20(5).png", 0, 0, 500, 400)
    sprite = Sprite("https://mrcuffe.github.io/openGameArt/goo0010/cooked_cat.png", start_x, start_y, start_h, start_w)
  
    velocity = 6
    

    
@loop_animation

#loads and plays music (may not work because i have been trying to upload it myself as mr cuffe sent me the wrong files)
graphics.loadSound("https://raw.githubusercontent.com/pretz445/bruh/gregory.mp3")
graphics.playSound("https://raw.githubusercontent.com/pretz445/bruh/gregory.mp3", volume = 0.5, loop = True)

#sets world borders
if player.sprite.y <= 0:
     player.sprite.y = 0
if player.sprite.y >= 300:
     player.sprite.y = 300
    
#Creates movement controls, allowing sidewards and upwards movement 
def check_inputs():
    if graphics.isKeyPressed(KEY_A):
        if player.sprite.x > 0:
            player.sprite.x -= player.velocity
    if graphics.isKeyPressed(KEY_D):
        if player.sprite.x < 440:
            player.sprite.x += player.velocity
    if graphics.isKeyPressed(KEY_W):
        if player.sprite.y > -1:
            player.sprite.y += player.velocity
    if graphics.isKeyPressed(KEY_S):
        if player.sprite.y < 401:
            player.sprite.y -= player.velocity      

        
  #makes the setup state mentioned earlier do something, not allowing gameplay but making debug easier

def setup():
    if game.state == game.SETUP:
        game.state = game.PLAY
        graphics.clear(0.0, 0.0, 0.0, 1.0)
        graphics.drawSprite(player.sprite)
#defines play state, allowing the sprite to move as well as play the game in general
def start():
    if game.state == game.PLAY:
        check_inputs()
        graphics.clear(0.0, 0.0, 0.0, 1.0)
        graphics.drawSprite(player.background)
        graphics.drawSprite(player.sprite)
        
 
 #activates setup or start states       
setup()

start()