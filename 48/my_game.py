#Phase 3
#Angelo Ng
from random import seed
from random import randint
seed(1)
@loop_animation

#Creates random numbers to generate where the platforms are generated which the player can jump on.
def random_num():
    for _ in range():
        random1 = randint (30,300)

        random2 = randient (20,200)

#Defines the main floor of the game and gives the game the information the game will need. Also where the main character will spawn.
def floor1(): 
    floor1 = Sprite("https://media.indiumgames.com/medialibrary/2014/07/MakingMap2.png")
    floor1_width = 600
    floor1_height = 20
    floor1_ypos = 0
    floor1_xpos = 0
    
#this is code for the game to generate random platforms for the player to spawn on. Also where the sprite for the platforms too. 
def plat(x,y):
    plat = Sprite("https://opensource.com/sites/default/files/uploads/pygame_floating.png")
    plat_width = 100
    plat_height = 20
    plat_ypos = random1
    play_xpos = random2

#This will make the game know if the game is in the menu or not. Also makes the game run. 
class game:  
    SETUP = 0
    PLAY = 1
    state = SETUP
    ground = 0

#setCanvasSize(500, 400) #This will be the size of the gap popout window. Will be updated later. 


#Code for the character where the player will control. It gives all the information for the player, such as where player spawns, sprite and velocity. 
class a_char:
    start_x = 0
    start_y = 0
    start_w = 50
    start_h = 50
    sprite = Sprite("https://mrcuffe.github.io/openGameArt/prototype_sprites/0_circle_yellow_64x64.png",start_x, start_y, start_w, start_h) #This is the makeshift sprit for the player. This will change. I could not get anyother images working.
    isJumping = False 
    velocity = 8
    mass = 2 


#Code foe the player moving x and y
def move(a_char, x, y): 
    a_char.x += x
    a_char.y += y

###CODE BELOW IS SHADED OUT FOR ERROR TESTING.     
#def collisions(floor1_xpos, floor1_ypos, floor1_height, floor1_width, a_char.x, a_char.y, a_char_height, a_char_width, hit_adjust_y = 0): #Code for the collisions of the player and the floor
#    if floor1_xpos + floor_width > a_char.x \
#    and floor1_xpos <= a_char.x + a_char_width \
#    and floor1_ypos <= a_char.y + a_char_height - hit_adjust_y \
#    and floor1_ypos + floor1_height >= a_char.y + hit_adjust_y:
#        return True
#    else:
#        return False


#isCollison = collisions(0,0,10,100,300,200,10,10)
#if isCollision == True:
#    velocity = 0
#    a_char.y = ''

#The code for jumping for the main caracter.  
#def update(a_char): #This section of the code is where the jump code and function is. 
#    if a_char.isJumping:
#        if a_char.velocity > 0:
#            f = (0.5 *a_char.mass * (a_char.velocity * a_char.velocity))
#    else:
#        f -(0.5 *a_char.mass * (a_char.velocity * a_char.velocity))
    
#    a_char.sprite.y = a_char.sprite.y + f
    
#    a_char.velocity = a_char.verlocity - 1
    
#    if a_char.sprite.y <= ground :
#        a_char.sprite.y = ground
#        a_char.isJumping = False 
#        a_char.velocity = a_char.def_velocity
        
#This section of the code will make the game know if the player is pressing down buttons to control the character and move the character around. 
def check_inputs(): 
    if graphics.isKeyPressed(KEY_W):
        a_char.isJumping= True
        
    if graphics.isKeyPressed(KEY_A):
        a_char.x = a_char.x - 1
 
    if graphics.isKeyPressed(KEY_S):
        a_char.x = a_char.x + 1

#def score_board(score):
#    score = 0
#    while a_char.y / 50 score:      
#        score + 1

#    graphics.print("Score: {score}")
    
        
def setup(): #Will start up the game. This section is not complete, therefore it is commented out.
    if game.state == game.SETUP:
        game.state = game.PLAY
        
        graphics.clear(0.0, 0.0, 0.0, 1.0) #Sets the background colour. This part of the code is not working. 
        graphics.drawSprite(a_char.sprite)
        
def start(): #Tells the game to start
    if game.state == game.PLAY:
        check_inputs()
        update(a_char)

def menu():
    graphics.print("Jumping game / n ")

setup()

start()
    
    #References
    #https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/#:~:text=Random%20integer%20values%20can%20be,interval%20%5Bstart%2C%20end%5D.
    #https://www.educba.com/random-number-generator-in-python/
    #https://pyangelo.com/reference
    #https://opensource.com/sites/default/files/uploads/pygame_floating.png1
    #
