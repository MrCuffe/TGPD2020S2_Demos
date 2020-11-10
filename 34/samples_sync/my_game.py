# Scrap Catch! By Reese Firme. A game where you guide a dog to catch falling food

# for picking random numbers
from random import *

# setting up the text sprites
dog = TextSprite("🐶 ", x = 240, y = 10)
meat = TextSprite("🥩 ", x = 150, y = 400)
broccoli = TextSprite("🥦 ", x = 300, y = 400)
bomb = TextSprite("💣 ", x = 225, y = 400)
life = TextSprite("💗 ", x = 100, y = 400)

# set score and lives at the start of the game
score = 0
lives = 3
# the playing variable lets the loop_animation decide whether to play the game or show the game over screen
playing = True

# load and play background music
graphics.loadSound("https://mrcuffe.github.io/openGameArt/fir0003/piano.mp3")
graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/piano.mp3", volume = 0.3, loop = True)

@loop_animation

# make the food fall down at different speeds
meat.y = meat.y - 2.3
broccoli.y = broccoli.y - 1.5
bomb.y = bomb.y - 1.1
life.y = life.y - 0.5

# player controls
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
    dog.x = dog.x - 2.7
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
    dog.x = dog.x + 2.7

# what happens when player catches the food
if dog.overlaps(meat):
    # add to score
    score = score + 1
    # play sound
    graphics.loadSound("https://mrcuffe.github.io/openGameArt/fir0003/burp-sound-effect.mp3")
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/burp-sound-effect.mp3", volume = 0.2)
    # move food back up to the top
    meat.y = 400
    # start at a new random x position
    meat.x = randint (0, 450)
# same logic for the broccoli except score goes down 
if dog.overlaps(broccoli):
    score = score - 1
    broccoli.y = 400
    broccoli.x = randint (0, 450)
    graphics.loadSound("https://mrcuffe.github.io/openGameArt/fir0003/dog-frieda-grunt-96khz-01.mp3")
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/dog-frieda-grunt-96khz-01.mp3", volume = 0.4)
# bomb immediately ends game
if dog.overlaps(bomb):
    graphics.loadSound("https://mrcuffe.github.io/openGameArt/fir0003/bomb.mp3")
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/bomb.mp3", volume = 0.5)
    playing = False
# life (heart) adds a life, position returns to the top
if dog.overlaps(life):
    graphics.loadSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3")
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3", volume = 0.2)
    lives = lives + 1
    life.y = 400
    life.x = randint (0, 450)

# what happens when food falls 'onto the floor'/offscreen
if meat.y <= 0:
    # minus 1 life
    lives = lives - 1
    meat.y = 400
    meat.x = randint (0, 450)
if broccoli.y <= 0:
    # broccoli just returns to top
    broccoli.y = 400
    broccoli.x = randint (0, 450)
if bomb.y <= 0:
    # returns to top
    bomb.y = 400
    bomb.x = randint (0, 450)
if life.y <= 0:
    # returns to top
    life.y = 400
    life.x = randint (0, 450)
    
# level 2 (speed increases to make it harder each level, lives fall slower)
if score >= 5:
    meat.y = meat.y - 2.4
    broccoli.y = broccoli.y - 1.6
    bomb.y = bomb.y - 1.3
    life.y = life.y - 0.4

# level 3
if score >= 10:
    meat.y = meat.y - 2.4
    broccoli.y = broccoli.y - 1.7
    bomb.y = bomb.y - 1.5
    life.y = life.y - 0.3

# level 4
if score >= 15:
    meat.y = meat.y - 2.4
    broccoli.y = broccoli.y - 1.8
    bomb.y = bomb.y - 1.7
    life.y = life.y - 0.2
    
# level 5
if score >= 20:
    meat.y = meat.y - 2.5
    broccoli.y = broccoli.y - 1.9
    bomb.y = bomb.y - 1.9
    life.y = life.y - 0.1
# last level difficulty is level 5

# lives refill and add when level up
if score == 5:
    lives = 5
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3", volume = 0.4)
    
if score == 10:
    lives = 10
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3", volume = 0.4)
    
if score == 15:
    lives = 15
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3", volume = 0.4)

if score == 20:
    lives = 20
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3", volume = 0.4)
    
if score == 30:
    lives = 30
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/shimmer.mp3", volume = 0.4)

# when lives are gone game ends
if lives <= 0:
    playing = False

# depending the value of the playing variable: we either play the game,
# or display the end-game screen
if playing == True:
    graphics.clear(0, 0, 0)
    graphics.drawSprite(meat)
    graphics.drawSprite(broccoli)
    graphics.drawSprite(bomb)
    graphics.drawSprite(life)
    graphics.drawSprite(dog)
    graphics.drawText("Score: " + str(score), x=0, y=370, fontSize=20)
    graphics.drawText("Lives: " + str(lives), x=0, y=340, fontSize=20)
else:
    graphics.clear()
    meat.y = 400
    broccoli.y = 400
    bomb.y = 400
    life.y = 400
    graphics.drawText("Game Over :(", x=90, y=230, fontSize=40, r=1, g=0, b=0)
    graphics.drawText("Score: " + str(score), x=180, y=190, fontSize=25)
    graphics.stopSound("https://mrcuffe.github.io/openGameArt/fir0003/piano.mp3")
    graphics.loadSound("https://mrcuffe.github.io/openGameArt/fir0003/game-over-piano-sound-effect.mp3")
    graphics.playSound("https://mrcuffe.github.io/openGameArt/fir0003/game-over-piano-sound-effect.mp3", volume = 0.05)