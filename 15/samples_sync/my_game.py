"""
Galhindarachchi Enuki
The game works without any errors being present, however I am unsure why the screen freezes after a fruit is not caught. 
"""
from random import *




#Adding sprites
#I decided to scrap the idea of an Introduction since the game was fairly self-explanitory
'''
I kept all the fruits even though I only dre the top three, so that  i may one day be able to fix this issue
of not being able to allow ranodm fruitsto be dropped, three at a time
'''
Apple=TextSprite("🍎",x= randint(0,370),y=350)
Banana=TextSprite("🍌",x=randint(0,370),y=350)
Strawberry=TextSprite("🍓",x=randint(0,370),y=350)
Mango=TextSprite("🥭",x=randint(0,370),y=350)
Grape=TextSprite("🍇",x=randint(0,370),y=350)
Pineapple=TextSprite("🍍",x=randint(0,370), y=350)
Basket=TextSprite("🗑", x=randint(0,370),y=10)
heart_1=TextSprite("❤",x=65,y=360)
heart_2=TextSprite("❤",x=35,y=360)
heart_3=TextSprite("❤",x=5,y=360)
'''
I created a list for the hearts and fruits so that I could later use it for randomly drawing 
different sprites and taking away sprites.
'''
heart_list=[heart_1,heart_2,heart_3]
Fruits=[Apple,Banana,Strawberry,Mango,Grape,Pineapple]
a_fruit_sprite=Fruits[randint(0,5)]
#These are the lives they had
hearts=3
playing= True
global playing
#The score is also part of the code but is not drawn up
score=3   





graphics.playSound("https://mrcuffe.github.io/openGameArt/gal0014/A%20cup%20of%20tea.mp3", volume = 0.1, loop = True)

@loop_animation


#loop_animation allows fruits to move
    

#funtion for the speed of the fruit dropping
def drop_fruit():
     Apple.y=Apple.y-1
     Banana.y=Banana.y-1.5
     Strawberry.y=Strawberry.y-0.8

#defining the keys 
if graphics.isKeyPressed(KEY_A) or graphics.isKeyPressed(KEY_V_LEFT):
     Basket.x = Basket.x-2
if graphics.isKeyPressed(KEY_D) or graphics.isKeyPressed(KEY_V_RIGHT):
     Basket.x = Basket.x+2
    

#Where the fruits will respawn if caught 


#I've only included the first three fruits because I did not know how to program the game to pick three random fruits to drop
if Basket.overlaps(Apple):
     Apple.y=400
     Apple.x=randint(0,370)
     graphics.playSound("https://mrcuffe.github.io/openGameArt/prototype_sounds/8-Bit%20Sound%20Library/Mp3/Collect_Point_00.mp3", volume = 0.1, loop = False)

if Basket.overlaps(Banana):
     Banana.y=400
     Banana.x=randint(0,370)
     graphics.playSound("https://mrcuffe.github.io/openGameArt/prototype_sounds/8-Bit%20Sound%20Library/Mp3/Collect_Point_00.mp3", volume = 0.1, loop = False)

if Basket.overlaps(Strawberry):
      Strawberry.y=400
      Strawberry.x=randint(0,370)
      graphics.playSound("https://mrcuffe.github.io/openGameArt/prototype_sounds/8-Bit%20Sound%20Library/Mp3/Collect_Point_00.mp3", volume = 0.1, loop = False)


#if fruit doesn't get caught
#I wanted to remove a heart if they couldnt catch a fruit, but the game freezes everytime a fruit doesnt get caught at the webpage stops reponding.
#When one fruit wasnt caught, itwould respawn rather than a different fruit respawning 
#After all the hearts are lost, you are no longer playing the game
while Apple.y <= 0 or Banana.y <= 0 or Strawberry.y <= 0 or Mango.y <= 0 or Grape.y <= 0 or Pineapple.y <= 0:
     if score==3:
          heart_list.remove(heart_3)
          graphics.playSound("SFX- The Ultimate 2017 8 bit sound Mini pack/Explosion1/Ogg/", volume = 0.1, loop = True)
          score=score-1
          playing==True
     elif score==2:
          graphics.playSound("SFX- The Ultimate 2017 8 bit sound Mini pack/Explosion1/Ogg/", volume = 0.1, loop = True)
          heart_list.remove(heart_2)
          score=score-1
          playing=True
          hearts=1
     elif score==1:
          graphics.playSound("SFX- The Ultimate 2017 8 bit sound Mini pack/Explosion1/Ogg/", volume = 0.1, loop = True)
          heart_list.remove(heart_1)
          score=0
          playing=False
          

#Starting the game 
#Drop fruit function added so the fruits would move
# draw the first three fruits (apple, banana, strawberry)
#draws all the hearts in the list
if playing==True:
     graphics.clear(0.60, 0.45, 0.30) 
     graphics.drawSprite(Basket)
     drop_fruit()
     graphics.drawSprite(Banana)
     graphics.drawSprite(Apple)
     graphics.drawSprite(Strawberry)
     for heart in heart_list:
         graphics.drawSprite(heart)
#Game over 
if score==0:
     graphics.clear()
     graphics.drawText("Game Over", x=100, y=230, fontSize=40, r=1, g=0, b=0)

#I will create levels in my future game phase

