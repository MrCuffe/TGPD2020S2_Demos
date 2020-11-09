"""
Bita Afshar Game development final phase
"""
import pygame
import time
from xlrd import open_workbook

# set up a way to use the maze on excel and import it into python
def load_maze(wb_filename=None, sheetnum=0):
    """
    loading maze from excel file by making a function that takes excel file and put all the columns and rows into
    a list inside a list#
    """

    book = open_workbook(wb_filename, 'r')
    sheet = book.sheet_by_index(sheetnum)

    col_list = []
    for col_index in range(sheet.ncols):
        a_col = []
        for row_index in range(sheet.nrows):
            a_col.append(sheet.cell(row_index, col_index).value)
        col_list.append(a_col)

    return col_list

# find all the characters inside the excel file to put as values inside the list
#  in order to tailor specific code to each individual value later on
def find_next(maze, item_character):
    """
    this function finds a character in the maze (list of columns)
    or returns None when nothing is found
    """
    for (x_index, col) in enumerate(maze):
        for y_index, cell_str in enumerate(col):
            if item_character in cell_str:
                # item is found
                return x_index, y_index

    return None


# use the load maze function to load the specific file and assign it as maze
maze = load_maze(wb_filename='babie-maze.xlsx', )
maze_width = len(maze)
maze_height = len(maze[0])
print(f"Maze is {maze_height} width  by {maze_width} height")
# introduce new variables for the display width and height of the maze as we don't want the display to
# show the entire maze but we don't want to change the actual width and height of the maze
# these layers are defined for future expansion for shadowing effects but used to determine display size
inner_square_size = 3
mid_border_size = 1
outer_border_size = 1
# display width and height are the sum of the layers so that of we decide to change the size of the layer(s)
# it will all be consistent
display_maze_width = inner_square_size + mid_border_size + outer_border_size
# maze_width / 2
display_maze_height = display_maze_width
# maze_height / 2

# inital player position
p_x, p_y = find_next(maze, item_character="p")

# Initialize the game engine
# we have to call this at the start,
# if we want to use this module.
pygame.init()

# initialising the flag variables before we use them later on
key_up_pressed = False
key_down_pressed = False
key_left_pressed = False
key_right_pressed = False

# Define the colors we will be using to colour the maze
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
filled = 0
# define time limit seconds
time_limit = 10

# setting the cell size by width and height dimesnions
cell_width = 50
cell_height = 50
# reduce the screen size to make the player view restricted and increase game difficulty
# using the new display variables we've defined for it
screen_size = [int(cell_width * display_maze_width), int(cell_height * display_maze_height)]
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("BABiE mAzE")

# initialising font so we can write a message in the screen window
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 18)

# Initialise variables that will be used in the loop
done = False
game_over = False
player_colour = red
clock = pygame.time.Clock()
first_key_up_is_pressed = False
# Loop until the user clicks the close button. set "done" as an indicater of when the player ends the game
while not done:
    # keep assigning  python time to start time until the player starts the game by pressing a key
    if not first_key_up_is_pressed:
        # once player's started start time is no longer updated
        start_time = time.time()
    # registering pygame events
    for event in pygame.event.get():
        done = event.type == pygame.QUIT
        # using the pygame modules to define when a key is pressed, this is why we put all
        # the variables to False at the start so that python registers the chaange when as key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                key_left_pressed = True
            elif event.key == pygame.K_RIGHT:
                key_right_pressed = True
            elif event.key == pygame.K_UP:
                key_up_pressed = True
            elif event.key == pygame.K_DOWN:
                key_down_pressed = True

    # reacting to pygame events and updating the maze checks if the game is not over,
    # checks for each of the keys being pressed,
    # the controls are not continous so each key press only moves the player one space in the maze
    # therefore the boolean expression is set to false again
    # for each event the loops are the same except for where the player is moved
    if not game_over:
        if key_up_pressed:
            first_key_up_is_pressed = True
            key_up_pressed = False
            dest_p_y = p_y - 1
            if ("W" not in maze[p_x][dest_p_y]):
                maze[p_x][p_y] = maze[p_x][p_y].replace("p", "b")
                p_y = dest_p_y
                maze[p_x][p_y] = maze[p_x][p_y].replace("b", "")
                maze[p_x][p_y] = maze[p_x][p_y] + "p"
        # see if it can move as player has requested (test)
        if key_down_pressed:
            key_down_pressed = False
            dest_p_y = p_y + 1
            if (dest_p_y < maze_height) and ("W" not in maze[p_x][dest_p_y]):
                maze[p_x][p_y] = maze[p_x][p_y].replace("p", "b")
                p_y = dest_p_y
                maze[p_x][p_y] = maze[p_x][p_y].replace("b", "")
                maze[p_x][p_y] = maze[p_x][p_y] + "p"
        # see if it can move as player has requested
        if key_right_pressed:
            key_right_pressed = False
            dest_p_x = p_x + 1
            if "W" not in maze[dest_p_x][p_y]:
                maze[p_x][p_y] = maze[p_x][p_y].replace("p", "b")
                p_x = dest_p_x
                maze[p_x][p_y] = maze[p_x][p_y].replace("b", "")
                maze[p_x][p_y] = maze[p_x][p_y] + "p"
        # see if it can move as player has requested
        if key_left_pressed:
            key_left_pressed = False
            dest_p_x = p_x - 1
            if "W" not in maze[dest_p_x][p_y]:
                maze[p_x][p_y] = maze[p_x][p_y].replace("p", "b")
                p_x = dest_p_x
                maze[p_x][p_y] = maze[p_x][p_y].replace("b", "")
                maze[p_x][p_y] = maze[p_x][p_y] + "p"

    # find the offset in order to move the player position to the centre in the display
    # we had to tweak it by 0.5 to centralise it
    offset_x = display_maze_width / 2 - p_x - 0.5
    offset_y = display_maze_height / 2 - p_y - 0.5

    # Clear the screen and set the screen background
    # default colour for the screen is white
    screen.fill(white)
    # drawing the maze on the game screen
    # put a blue block for each wall cell ("w")
    # and a red block for player position in maze b("p") - phase two replace red square with a sprite

    for (maze_cell_x, col) in enumerate(maze):
        # add the offset to x
        cell_x = offset_x + maze_cell_x
        for maze_cell_y, cell_str in enumerate(col):
            # add the offset to y
            cell_y = offset_y + maze_cell_y

            if "W" in cell_str:
                rect = pygame.Rect(cell_x * cell_width, cell_y * cell_height, cell_width, cell_height)
                pygame.draw.rect(screen, blue, rect, filled)

            if "p" in cell_str:
                rect = pygame.Rect(cell_x * cell_width, cell_y * cell_height, cell_width, cell_height)
                # player rect is red until they reach the end of maze, then game is over
                # rect turns green key controls are disabled
                pygame.draw.rect(screen, player_colour, rect, filled)

    # check if player has reached home
    if p_y < 1:
        game_over = True

        # print congrats
        # we already initialised the module so we can use it here
        textsurface = myfont.render("You're home!", False, black)
        screen.blit(textsurface, (10, 10))
        player_colour = green

    # before the player starts the game print message telling them what to do
    if not first_key_up_is_pressed:
        textsurface = myfont.render("Use arrow keys to find home", False, black)
        screen.blit(textsurface, (10, 10))
        player_colour = red

    # check the elapsed time and if it's over the time limit stop the game
    # but only act if the game is still running, i.e player hasn't reached home
    if not game_over:
        elapsed_time = time.time() - start_time
    # print(time_limit - int(elapsed_time))
    if elapsed_time > time_limit:
        game_over = True
        # print time's up!
        # we do the same thing as when the player makes it to the end
        # it's another game over situation
        textsurface = myfont.render("Too slow!", False, black)
        screen.blit(textsurface, (10, 10))
        player_colour = black
    # updates the entire screen display
    pygame.display.flip()
    # waits 60 milliseconds (tick) before continuing
    clock.tick(60)


pygame.quit()
