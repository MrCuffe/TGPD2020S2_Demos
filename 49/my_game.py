5# "Jumping Jules" designed and created by Victoria Wang


# import pygame module in this program  
import pygame 
   
# activate the pygame library  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init() 
   
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode((500, 500)) 
   
# set the pygame window name  
pygame.display.set_caption("Jumping Jules")

   
#character's current co-ordinates 
x = 50
y = 440
   
# dimensions of the character 
width = 40
height = 60
    
# Force (v) up and mass m. 
v = 4
m = 2

isJump = False
jumpCount = 10





#mainloop   
# Indicates pygame is running

run = True
   
# infinite loop 
while run:
   
    # completely fill the surface object  
    # with black colour  
    win.fill((0, 0, 0)) 
   
    # drawing object on screen which is rectangle here  
    pygame.draw.rect(win, (0, 225, 0), (x, y, width, height)) 
       
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get(): 
           
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT: 
               
            # it will make exit the while loop 
            run = False
            
    # stores keys pressed 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > v:
        x -= v
    if keys[pygame.K_RIGHT] and x < 500 - width - v:
        x += v


    if not(isJump): 
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
        
  
    # creates time delay of 10ms 
    pygame.time.delay(30) 
   
    # it refreshes the window 
    pygame.display.update()  
# closes the pygame window     
pygame.quit() 
