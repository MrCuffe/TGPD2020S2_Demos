#Vincent Djaja
#Shooter game using Pygame

import pygame
import math
import random
import time

#Initialising game
pygame.init()

#Creates a window for the game to run
window = pygame.display.set_mode((900,600))
#Names the title of the window
pygame.display.set_caption("I haven't thought of the game title :)")

#Creating a class for spaceship
class player():
    #Initialising attributes of the spaceship
    def __init__(self,x,y,width,height,health = 3):
        #self parameters
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.speed = 4
        self.img = pygame.image.load("spaceship.png")

    #Defining drawing the spaceship   
    def draw (self,window):
        window.blit(self.img,(self.x,self.y))
    

#Creating a class for enemy_1  
class enemy_1():
    #Initialising attributes of the asteroid
    def __init__(self,x,y,width,height,health = 4):
        #self parameters
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.img = pygame.image.load("asteroid.png")
        self.health = health
        #Varies the trajectory for each asteroid by varying the speed
        self.speed_y = random.randint(2,3)
        self.speed_x = random.uniform(-0.8,0.8)
            
    #Defining drawing the space_debris    
    def draw(self,window):
        window.blit(self.img,(round(self.x),round(self.y)))
        
    #Defining movement for the space_debris
    def move(self,speed):
        self.y += self.speed_y
        self.x += self.speed_x

#Creating a class for enemy_2
class enemy_2():
    #Initialising attributes for alien_1
    def __init__(self,x,y,width,height,health = 2):
        #self parameters
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.img = pygame.image.load("alien_1.png")
        #Varies the x_speed for each alien_1  
        self.speed_x = random.uniform(2, 3)
        #Varies the y_speed, which is responsible for trying to follow the player on the y axis
        self.speed_y = random.uniform(2, 3) 

    #Defining drawing enemy_2
    def draw(self,window):
        window.blit(self.img,(round(self.x),round(self.y)))

    #Defining movement for enemy_2
    def move(self,speed):
        self.x += self.speed_x
        self.y += self.speed_y

#Creating a class for enemy_3
class enemy_3():
    #Initialising attributes for alien_2
    def __init__(self,x,y,width,height,health = 3):
        #self parameters
        self.x = x
        #self.a and self.b are randomly chosen within a range so each alien_2 spawned will have a different path
        #A sin graph is the path that each alien_2 will follow
        #self.a determines the wavelength of the sin graph
        self.a = random.uniform(50,300)
        #self.b determines the amplitude of the sin graph
        self.b = random.uniform(0,200)
        #self.c is a tuple so once self.a and self.b has been randomly generated for an alien_2's path, the path will not keep changing
        self.c = (self.a,self.b)
        #This is the sin graph equation, where (y = self.y), (x = self.x) and (self.c[0] and self.c[1] are constants)
        self.y = (math.sin((-self.x)/self.c[0]) * self.c[0]) + self.c[1]
        self.width = width
        self.height = height
        self.health = health
        self.img = pygame.image.load("alien_2.png")
        #Varies x speed
        self.speed_x = random.uniform(-1.5,-2)

    #Defining drawing enemy_3 
    def draw(self,window):
        window.blit(self.img,(round(self.x),round(self.y)))

    #Defining movement for enemy_3
    def move(self,speed):
        self.x += self.speed_x
        #self.a and self.b are randomly chosen within a range so each alien_2 spawned will have a different path
        #A sin graph is the path that each alien_2 will follow
        #self.a determines the wavelength of the sin graph
        self.a = random.uniform(50,300)
        #self.b determines the amplitude of the sin graph
        self.b = random.uniform(0,200)
        #self.c is a tuple so once self.a and self.b has been randomly generated for an alien_2's path, the path will not keep changing
        self.c = (self.a,self.b)
        #This is the sin graph equation, where (y = self.y), (x = self.x) and (self.c[0] and self.c[1] are constants)
        self.y = (math.sin((-self.x)/self.c[0]) * self.c[0]) + self.c[1]

#Creating a class for projectiles
class projectiles():
    #Initialising attributes of the projectiles
    def __init__(self,x,y,width,height,color,speed_x,speed_y):
        #self parameters
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 3
        self.speed_x = speed_x
        self.speed_y = speed_y
    
    #Defining drawing space_debris 
    def draw(self,window):
        pygame.draw.rect(window,self.color,(round(self.x),round(self.y),round(self.width),round(self.height)))

#Creating a class for enemy_projectiles
class enemy_projectiles():
    #Initialising attributes of the projectiles
    def __init__(self,x,y,width,height,color):
        #self parameters
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
    
    #Defining drawing enemy_projectiles 
    def draw(self,window):
        pygame.draw.rect(window,self.color,(round(self.x),round(self.y),round(self.width),round(self.height)))

    #Defining movement for enemy_projectiles 
    def move(self,speed):
        self.x += self.speed 

#Creating class for powerups
class modifier():
    #Initialising attributes of the powerups
    def __init__(self,x,y,width,height,type):
        #self parameters
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_y = random.randint(-5,-4)
        self.img = pygame.image.load("powerup.png")
        #Varies the type of powerup (for e.g if powerup type == 3, it gives extra health while if powerup type == 2, it allows the player to shoot a fast beam of light)
        self.type = random.randint(0,3)

    #Defining drawing powerups
    def draw(self,window):
        window.blit(self.img,(self.x,self.y))

    #Defining movement for powerups
    def move(self,speed):
        self.y += self.speed_y
        
#Defining a function for updating the window
def update_window():
    #Creates the background for the game
    window.blit(background,(0,0))
    #Draws the spaceship that the player can control
    spaceship.draw(window)
    #Draws the space_debris in the window
    for asteroid in asteroids:
        asteroid.draw(window)
    #Draw lasers
    for laser in lasers:
        laser.draw(window)
    #Draws enemy_lasers
    for enemy_laser in enemy_lasers:
        enemy_laser.draw(window)
    #Draws powerups
    for powerup in powerups:
        powerup.draw(window)
    #Draws alien_1
    for alien_1 in aliens_1:
        alien_1.draw(window)
    #Draws alien_2
    for alien_2 in aliens_2:
        alien_2.draw(window)
    #Starts a score that keeps track of time 
    #Sets the location of where the score will be
    window.blit(score_font.render("SCORE",1,white), (410, 30))
    window.blit(score_font.render(f"{math.trunc(hours)}{math.trunc(minutes)}{math.trunc(seconds%60)}{milliseconds%100}",1,white), (410, 50))
    #Displays lives left
    window.blit(instruction_font.render(f"LIVES = {spaceship.health}",1,white), (520, 35))
    #Displays laser charge or ammo
    window.blit(instruction_font.render(f"LASER CHARGE = {math.trunc(shoot_count)}",1,white), (630, 35))
    #Shows number of enemies killed
    window.blit(instruction_font.render(f"ENEMIES KILLED = {enemies_killed}",1,white), (210, 35))
    #Shows the accuracy of the player
    window.blit(instruction_font.render(f"ACCURACY = {math.trunc(accuracy)}%",1,white), (70, 35))
    #Displays control instructions for 3 seconds after game starts
    if seconds < 3:
        window.blit(instruction_font.render("ARROW KEYS OR",1,white), (575,120))
        window.blit(instruction_font.render("WASD TO MOVE",1,white), (575,140))
        window.blit(instruction_font.render("PRESS 'P' OR 'ESCAPE' TO PAUSE",1,white), (575,180))
        window.blit(instruction_font.render("PRESS SPACEBAR TO SHOOT",1,white), (575,200))

    #Continuously updates the screen with new information
    pygame.display.update()

#Initialising the image for the background
background = pygame.image.load("background.jpg")

#Colours
white = (255,255,255)

#Defines the fonts
score_font = pygame.font.SysFont("couriernew",25)
instruction_font = pygame.font.SysFont("couriernew",15)
title_font = pygame.font.SysFont("couriernew",50)

#Assigning values to the spaceship attributes
spaceship = player(425, 300, 40, 37, 3)
#Assigning values to the enemy attributes
asteroid = enemy_1(0, 0, 50, 50, 4)
alien_1 = enemy_2(0, 0, 47, 41, 2)
alien_2 = enemy_3(0, 0, 33, 43, 3)
#Assigning values to the lasers and powerups
laser = (0, 0, 2.5, 8, 0, 0)
enemy_laser = (0, 0, 8, 2.5)
powerup = modifier(0, 0, 50, 50, 0)

#Creates a list for asteroids
asteroids = []
#Creates list for aliens
aliens_1 = []
aliens_2 = []
#Creates a list for lasers and powerups
lasers = []
enemy_lasers = []
powerups = []

#Time/score variables and information on the screen variables
hours, minutes, seconds, milliseconds = 0,0,0,0
shoot_count = 0
enemies_killed = 0
hit = 0
miss = 0

#Powerup time left
powerup_time1 = 0
powerup_time2 = 0
powerup_time3 = 0

#Sound effects
laser_sound1 = pygame.mixer.Sound("laser_sound1.wav")
laser_sound2 = pygame.mixer.Sound("laser_sound2.wav")
laser_sound3 = pygame.mixer.Sound("laser_sound3.wav")
heal_sound = pygame.mixer.Sound("heal_sound.wav")
spaceship_explosion = pygame.mixer.Sound("spaceship_explosion.wav")
enemy_explosion = pygame.mixer.Sound("enemy_explosion.wav")

#Starts off determining what is running and what is not
running = True
game_running = False
restart_menu = False
pause_menu = False

#Creates the 'infinite' game loop that will only stop once you quit
while running == True:
    #Defining what "key" means
    key = pygame.key.get_pressed()
    #The mouse position on the game window
    mouse_x, mouse_y = pygame.mouse.get_pos()

    #If the player is NOT currently playing and it is NOT paused and NOT on the restart menu
    if game_running == False and restart_menu == False and pause_menu == False:
        #Displays the main menu
        window.blit(background, (0,0))
        pygame.draw.rect(window, (240,240,240),(300,165,300,50),2)
        pygame.draw.rect(window, (240,240,240),(300,265,300,50),2)
        window.blit(instruction_font.render("PLAY",1,white),(430, 180))
        window.blit(instruction_font.render("EXIT",1,white),(430,280))
        window.blit(title_font.render("GAME",1,white), (390,30))

        #If the mouse position is on the PLAY rectangle and the player clicks
        if mouse_x > 300 and mouse_x < 600 and mouse_y > 165 and mouse_y < 215:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Set so the game is running
                game_running = True
                #Start the game off at a clean slate
                milliseconds = 0
                spaceship.health = 3
                asteroids.clear()
                aliens_1.clear()
                aliens_2.clear()
                lasers.clear()
                enemy_lasers.clear()
                powerups.clear()
                shoot_count = 0
                enemies_killed = 0
                hit = 0
                miss = 0
                powerup_time1 = 0
                powerup_time2 = 0
                powerup_time3 = 0
                spaceship.x = 425
                spaceship.y = 300

        #If the mouse position is on the EXIT rectangle and the player clicks
        if mouse_x > 300 and mouse_x < 600 and mouse_y > 265 and mouse_y < 415:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Stop running the ENTIRE game
                running = False

        #Stop running the ENTIRE game if the player presses escape when on the main menu
        if key[pygame.K_ESCAPE]:
            running = False

    #If the game is paused
    if pause_menu == True:
        #Start the pause window
        window.blit(background, (0,0))
        window.blit(instruction_font.render("PRESS 'R' TO RESTART",1,white),(280,270))
        window.blit(instruction_font.render("OR PRESS 'U' TO UNPAUSE",1,white),(280,290))
        window.blit(instruction_font.render("OR PRESS 'E' TO GO BACK TO THE MAIN MENU",1,white),(280,310))
        #If the player presses "u", the game unpauses
        if key[pygame.K_u]:
            pause_menu = False
            game_running = True
        #If the player presses "e", the player exits to the main menu
        if key[pygame.K_e]:
            pause_menu = False
        #If the player presses "r", the game restarts
        if key[pygame.K_r]:
            pause_menu = False
            game_running = True
            milliseconds = 0
            spaceship.health = 3
            asteroids.clear()
            aliens_1.clear()
            aliens_2.clear()
            lasers.clear()
            enemy_lasers.clear()
            powerups.clear()
            shoot_count = 0
            enemies_killed = 0
            hit = 0
            miss = 0
            powerup_time1 = 0
            powerup_time2 = 0
            powerup_time3 = 0
            spaceship.x = 425
            spaceship.y = 300

    #If the player is on the restart menu
    if restart_menu == True:
        #Display the restart menu
        window.blit(background, (0,0))
        window.blit(instruction_font.render("PRESS 'R' TO RESTART",1,white),(255,270))
        window.blit(instruction_font.render("OR PRESS ESCAPE TO GO BACK TO THE MAIN MENU",1,white),(255,290))
        #If the player presses escape, go back to the main menu
        if key[pygame.K_ESCAPE]:
            restart_menu = False
            time.sleep(0.5)
        #If the player presses r, restart the game
        if key[pygame.K_r]:
            restart_menu = False
            game_running = True
            milliseconds = 0
            spaceship.health = 3
            asteroids.clear()
            aliens_1.clear()
            aliens_2.clear()
            lasers.clear()
            enemy_lasers.clear()
            powerups.clear()
            shoot_count = 0
            enemies_killed = 0
            hit = 0
            miss = 0
            powerup_time1 = 0
            powerup_time2 = 0
            powerup_time3 = 0
            spaceship.x = 425
            spaceship.y = 300

    #If the player presses the quit button the game will quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #updates the display     
    pygame.display.update()

    #If the player is currently playing the game
    if game_running == True:
        #Creating a hitbox for the spaceship       
        spaceship.rect = pygame.Rect(spaceship.x,spaceship.y,spaceship.width,spaceship.height)
        #If the spaceship's health reaches 0, it will display the restart menu
        if spaceship.health <= 0:
            #Plays spaceship_exposion sound
            spaceship_explosion.play()
            game_running = False
            restart_menu = True

        #If the player presses p or escape ingame then the game will pause
        if key[pygame.K_p] or key[pygame.K_ESCAPE]:
            game_running = False
            pause_menu = True
            time.sleep(0.5)

        #Allows the score to increase as time goes by
        milliseconds += 1
        seconds = milliseconds/100
        minutes = seconds//60
        hours = minutes//60
        #Increases shootcount/ammo as time goes by
        shoot_count += 1/10
        
        #Calculates the accuracy information that is displayed on the screen
        if hit == 0 and miss == 0:
            accuracy = 0
        else:
            accuracy = hit/(hit + miss)*100

        for enemy_laser in enemy_lasers:
            #Creates the hitbox for the enemy_laser
            enemy_laser.rect = pygame.Rect(round(enemy_laser.x),round(enemy_laser.y),round(enemy_laser.width),round(enemy_laser.height))
            #Makes the enemy_laser move
            enemy_laser.x -= enemy_laser.speed
            #Sets the boundary for the enemy_laser 
            if enemy_laser.x > 900 or enemy_laser.x < 0:
                enemy_lasers.remove(enemy_laser)
            #If the enemy_laser collides with the spaceship, the spaceship will lose 1 health and the enemy_laser will disappear
            if enemy_laser.rect.colliderect(spaceship.rect):
                spaceship.health -= 1
                enemy_lasers.remove(enemy_laser)
                
        #Responsible for removing space asteroids once they reach the edge of the window    
        for asteroid in asteroids:
            #Makes the asteroids move after being spawned
            asteroid.y += asteroid.speed_y
            asteroid.x += asteroid.speed_x
            #Creates the asteroid hitbox
            asteroid.rect = pygame.Rect(round(asteroid.x),round(asteroid.y),asteroid.width,asteroid.height)
            #Sets boundaries for the asteroids
            if asteroid.y > 600 or (asteroid.x > 900 or asteroid.x < -60):
                asteroids.remove(asteroid)
            #If spaceship collides with asteroid, the spaceship will lose a health and the asteroid will disappear
            if spaceship.rect.colliderect(asteroid.rect):
                spaceship.health -= 1
                asteroids.remove(asteroid)

        for alien_1 in aliens_1:
            #Makes alien_1 move
            alien_1.x += alien_1.speed_x
            #Creates hitbox for alien_1
            alien_1.rect = pygame.Rect(round(alien_1.x),round(alien_1.y),alien_1.width,alien_1.height)
            #If alien_1 is on the left of the player
            if alien_1.x < spaceship.x:
                #alien_1 will try to follow the spaceship on the y-axis until they pass they spaceship on the x-axis
                if spaceship.y > alien_1.y:
                    alien_1.y += alien_1.speed_y
                if spaceship.y < alien_1.y:
                   alien_1.y += alien_1.speed_y * -1

            #If spaceship collides with alien_1, the spaceship will lose a health and alien_1 will disappear
            if spaceship.rect.colliderect(alien_1.rect):
                spaceship.health -= 1
                aliens_1.remove(alien_1)
            #Sets boundaries for alien_1
            if alien_1.x > 900:
                aliens_1.remove(alien_1)

        for alien_2 in aliens_2:
            #Creates hitbox for alien_2
            alien_2.rect = pygame.Rect(round(alien_2.x),round(alien_2.y),alien_2.width,alien_2.height)
            #Makes alien_2 move on the x-axis
            alien_2.x += alien_2.speed_x
            #When x changes, the y will move up and down like a sin graph
            alien_2.c = (alien_2.a,alien_2.b)
            alien_2.y = (math.sin((-alien_2.x)/alien_2.c[0]) * alien_2.c[0]) + alien_2.c[1]
            #Sets boundaries for alien_2
            if alien_2.x < -41:
                aliens_2.remove(alien_2)
            #Periodically spawns enemy_lasers that come from alien_2
            if random.randrange(0,60) == 0:
                enemy_laser = enemy_projectiles(alien_2.x,alien_2.y+20,8,2.5,(0,255,0))
                enemy_lasers.append(enemy_laser)
            #If the spaceship collides with alien_2, the spaceship will lose a health and alien_2 will disappear
            if spaceship.rect.colliderect(alien_2.rect):
                spaceship.health -= 1
                aliens_2.remove(alien_2)
    
        for laser in lasers:
            #Creates laser hitbox
            laser.rect = pygame.Rect(round(laser.x),round(laser.y),round(laser.width),round(laser.height))
            #If laser touches an asteroid
            if laser.rect.colliderect(asteroid.rect):
                for asteroid in asteroids:
                #If a laser collides with an asteroid, the asteroid will lose a health
                    asteroid.health -= 1
                    #If asteroid health = 0, the asteroid will be removed
                    if asteroid.health == 0:
                        asteroids.remove(asteroid)
                        #Plays enemy explosion sound
                        enemy_explosion.play()
                        milliseconds += 800
                        enemies_killed += 1
                lasers.remove(laser)
                hit += 1
            #If laser touches an alien_1   
            if laser.rect.colliderect(alien_1.rect):
                #If a laser collides with alien_1, alien_1 will lose a health
                for alien_1 in aliens_1:
                    alien_1.health -= 1
                    if alien_1.health == 0:
                        aliens_1.remove(alien_1)
                        #Plays enemy explosion sound
                        enemy_explosion.play()
                        milliseconds += 800
                        enemies_killed += 1
                lasers.remove(laser)
                hit += 1
                
            if laser.rect.colliderect(alien_2.rect):
                #If a laser collides with alien_2, alien_2 will lose a health
                for alien_2 in aliens_2:
                    alien_2.health -= 1
                    if alien_2.health == 0:
                        aliens_2.remove(alien_2)
                        #Plays enemy explosion sound
                        enemy_explosion.play()
                        milliseconds += 1000
                        enemies_killed += 1
                lasers.remove(laser)
                hit += 1

            #Sets laser speed    
            laser.y += laser.speed_y
            laser.x += laser.speed_x
            
            #Sets laser boundaries
            if laser.y < 0:
                lasers.remove(laser)
                miss += 1
            if laser.x < 0 or laser.x > 900:
                lasers.remove(laser)
                miss += 1
                
        for powerup in powerups:
            #Powerups hitbox
            powerup.rect = pygame.Rect(round(powerup.x),round(powerup.y),powerup.width,powerup.height)

            #If the spaceship collides with a powerup
            if spaceship.rect.colliderect(powerup.rect):
                #Depending on the powerup type, the powerup_time will increase by 500
                if powerup.type == 0:
                    if powerup_time2 == 0 and powerup_time3 == 0:
                        powerup_time1 += 400
                    powerups.remove(powerup)
                if powerup.type == 1:
                    if powerup_time1 == 0 and powerup_time3 == 0:
                        powerup_time2 += 400
                    powerups.remove(powerup)
                if powerup.type == 2:
                    if powerup_time1 == 0 and powerup_time2 == 0:
                        powerup_time3 += 400
                    powerups.remove(powerup)
                #if the powerup.type is 3, the player will gain 1 health instead
                if powerup.type == 3:
                    spaceship.health += 1
                    #Plays heal_sound 
                    heal_sound.play()
                    powerups.remove(powerup)
            #Sets the powerup speed        
            powerup.y += powerup.speed_y
            #Sets powerup boundaries
            if powerup.y < -50:
                powerups.remove(powerup)

        #Creates a new powerup and appends it into the powerups list if the number generated is == 0
        if random.randrange(0, 480) == 0:
            powerup = modifier(random.randrange(0,850),random.randrange(600,1600),powerup.width,powerup.height,powerup.type)
            powerups.append(powerup)

        #If there is powerup_time1 left
        if powerup_time1 > 0:
            #powerup_time will decrease over time 
            powerup_time1 -= 1
            if key[pygame.K_SPACE] and powerup_time1 > 0 and milliseconds % 20 == 0:
                laser_sound2.play()
                #Includes 2 new lasers into the lasers list
                lasers.append(projectiles(spaceship.x + 10,spaceship.y,2.5,8,white,0,-2))
                lasers.append(projectiles(spaceship.x + 30,spaceship.y,2.5,8,white,0,-2))
                #If the shootcount is greater than 0
                if shoot_count > 0:
                    #Deduct from the shoot_count so the player can't spam after the powerup time runs out
                    shoot_count -= 2

        #If there is powerup_time2 left
        if powerup_time2 > 0:
            #powerup_time will decrease over time 
            powerup_time2 -= 1
            if key[pygame.K_SPACE] and powerup_time2 > 0 and milliseconds % 40 == 0:
                laser_sound2.play()
                #Includes 3 new laser into the lasers list
                lasers.append(projectiles(spaceship.x + 20,spaceship.y - 40,2.5,40,white,0,-80))
                lasers.append(projectiles(spaceship.x + 20,spaceship.y - 40,2.5,40,white,0,-80))
                lasers.append(projectiles(spaceship.x + 20,spaceship.y - 40,2.5,40,white,0,-80))
                #If the shootcount is greater than 0
                if shoot_count > 0:
                    #Deduct from the shoot_count so the player can't spam after the powerup time runs out
                    shoot_count -= 5
                    
        #If there is powerup_time3 left
        if powerup_time3 > 0:
            #powerup_time will decrease over time
            powerup_time3 -= 1
            if key[pygame.K_SPACE] and powerup_time3 > 0 and milliseconds % 50 == 0:
                laser_sound2.play()
                #Includes 3 new lasers into the lasers list
                lasers.append(projectiles(spaceship.x + 10,spaceship.y,2.5,8,white,-1,-3))
                lasers.append(projectiles(spaceship.x + 20,spaceship.y,2.5,8,white,0,-3))
                lasers.append(projectiles(spaceship.x + 30,spaceship.y,2.5,8,white,1,-3))
                #If the shootcount is greater than 0
                if shoot_count > 0:
                    #Deduct from the shoot_count so the player can't spam after the powerup time runs out
                    shoot_count -= 4

        #Creating controls for movement and defining game boundaries
        #If 'SPACE' is pressed, the shoot_count is larger than 60 and powerup_time = 0, the spaceship will shoot a standard laser 
        if key[pygame.K_SPACE] and shoot_count > 3 and milliseconds % 10 == 0 and powerup_time1 == 0 and powerup_time2 == 0 and powerup_time3 == 0:
            laser_sound1.play()
            #Decreases the shoot_count by 30 so that the player cannot spam lasers
            shoot_count -= 3
            #Includes a new laser into the lasers list
            lasers.append(projectiles(spaceship.x + 20,spaceship.y,2.5,8,white,0,-3))
        #If 'a' or left_key is pressed the spaceship will move left until x !> 5
        if (key[pygame.K_a] or key[pygame.K_LEFT]) and spaceship.x > 5:
            spaceship.x -= spaceship.speed
        #If 'd' or right_key is pressed the spaceship will move right until x !< 855
        if (key[pygame.K_d] or key[pygame.K_RIGHT]) and spaceship.x < 855:
            spaceship.x += spaceship.speed
        #If 'w' or up_key is pressed the spaceship will move up until y !> 5
        if (key[pygame.K_w] or key[pygame.K_UP]) and spaceship.y > 5:
            spaceship.y -= spaceship.speed
        #If 's' or down_key is pressed, the spaceship will move down until y !< 560
        if (key[pygame.K_s] or key[pygame.K_DOWN]) and spaceship.y < 560:
            spaceship.y += spaceship.speed

        #Limits how many asteroids are allowed on the screen
        if len(asteroids) < 1:
            #Influences the amount of asteroids on the screen
            #Randomly selects x and y coordinates for an space asteroids
            asteroid = enemy_1(random.randrange(0,840),random.randrange(-1000,0),asteroid.width,asteroid.height)
            #Includes the space asteroids into the list
            asteroids.append(asteroid)
            
        #Limits how many aliens_1 are allowed on the screen
        if len(aliens_1) < 1:
            #Influences the amount of aliens_1 on the screen
            #Randomly selects x and y coordinates for an alien_1
            alien_1 = enemy_2(random.randrange(-1000,0),random.randrange(0,600),alien_1.width,alien_1.height)
            #Includes an alien_1 into the list
            aliens_1.append(alien_1)

        #Limits how many aliens_2 are allowed on the screen
        if len(aliens_2) < 1:
            #Influences the amount of aliens_2 on the screen
            #Randomly selects x and y coordinates for aliens_2
            alien_2 = enemy_3(random.randrange(900,1900),random.randrange(0,600),alien_2.width,alien_2.height)
            alien_2.a = random.uniform(50,300)
            alien_2.b = random.uniform(100,500)
            #Includes an alien_2 into the list
            aliens_2.append(alien_2)
        #Calls upon function that includes updating window         
        update_window()

#Quits the game
pygame.quit()
