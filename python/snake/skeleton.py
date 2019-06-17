# Snake
# Jon Culver - 2014
#
# A basic implementation of 'snake' using pygame
#

# Import modules used within this program
import pygame
import random
# Import all pygame locals. This allows the use of key strings like K_UP etc.
from pygame.locals import *

# Define some colors
BLACK = (   0,   0,   0)
GRAY =  ( 230, 230, 230)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

# Screen size in pixels
SCREEN_WIDTH=500
SCREEN_HEIGHT=400

# Grid size in cells
GRID_WIDTH=20
GRID_HEIGHT=15

# Snake properties
INITIAL_SPEED=300
INITIAL_LENGTH=5

# Define directions as the change in (x,y) location when moving a
# single space in that direction
NORTH = (0,-1)
EAST = (1,0)
SOUTH = (0,1)
WEST = (-1,0)

# Define the possible states that the game can be in.
GAME_BEGIN = 0
GAME_NOT_STARTED = 1
GAME_RUNNING = 2
GAME_OVER = 3
GAME_EXITED = 4

# Event codes. These are used to trigger periodic events.
EVENT_MOVE_SNAKE = USEREVENT+1

# -------- Helper Functions --------

def set_game_state(new_state):
    """ Change the game state to a new state """
    global game_state
    game_state = new_state

def get_game_state():
    """ Return the current global game state """
    global game_state
    return game_state

def set_screen_state(new_state):
    """ Change the screen state to a new state """
    global screen_state
    screen_state = new_state

def get_screen_state():
    """ Return the current global game state """
    global screen_state
    return screen_state

# @5.2 Create functions similar to those above for set_top_score and get_top_score

def add_coords(a, b):
    """ Take two sets of coordinates (p,q) and (r,s) and return (p+r, q+s) """
    p,q = a
    r,s = b
    return (p+r, q+s)

def center_rect (width, height):
    """
    Place a given rectangle in the center of the screen.
    
    Return the (x,y) co-ordinate in which to position the top left corner of a
    rectangle of the given dimensions in order to center it horizontally and
    vertically.
    """
    x=0
    y=0
    if SCREEN_WIDTH - width > 0:
        x = (SCREEN_WIDTH - width) / 2
    if SCREEN_HEIGHT - height > 0:
        y = (SCREEN_HEIGHT - height) / 2
    return (x,y)

#--------- Classes ----------

class Snake():
    """ This class represents the properties of a Snake object """

    def __init__ (self):
        """ Create a new snake object. """
        # ------- Parameters of a Snake obejct --------
        # The following properties can be accessed within this class using
        # e.g. self.direction
        
        # The direction the snake is travelling in
        self.direction = EAST
        # The speed of the snake. This value represents the time in milliseconds
        # between moves. So 1000 = 1 move per second, 200 = 5 moves per sec etc.
        self.set_speed(INITIAL_SPEED)
        # The position of the snake (list of (x,y) tuples). The front of the
        # snake is the first element in the list.
        self.reset_position()
        
    def __iter__ (self):
        """ Iterate the squares taken by this snake """
        # This special method allows code to walk all the squares occupied
        # by the snake using the syntax 'for position in snake'
        for pos in self.position:
            yield pos 

    # ------ Snake methods (things the snake can do) ------

    def length (self):
        """ Return the length of the snake """
        return len(self.position)

    def next_space(self, direction=None):
        """
        Return the square that the snake will move to next (x,y)

        Argument: direction (optional) - the direction the snake will move in.
                                         If not specified then the current
                                         direction is used.
        """
        if direction == None:
            direction = self.direction
        return add_coords(self.position[0], direction)
    
    def grow(self):
        """ Make the snake one square longer by moving forward in direction of
            travel.
        """
        # @1.1 Use the self.next_space() method to find the space the snake
        # will move to next and add this to the front of the self.position list.
        # For example you could use the insert() method of the list.
        pass
    
    def shrink(self):
        """ Make the snake one square shorter (remove the tail) """
        # @1.2 Remove the last element from the position list.
        # For example you could use the pop() method of the list.
        pass

    def move(self):
        """ Move the snake one space """
        # @1.3 Use self.grow() and self.shrink() to add one square to the
        # head then remove one from the tail
        pass

    def change_direction(self, new_direction):
        """ Change the snake's direction to that specified.

        Note that it is not possible to turn 180 degrees
        """
        # @2.1 Update self.direction with the new direction specified.
        #
        # Only do this if moving in the new direction doesn't take us back to
        # where we just came from. (The next_space() method with the
        # appropriate direction will show where we'd end up if we moved this
        # way. Compare this to the previous location, which is now the second
        # item in the position list.) Note: If you have trouble with this part
        # then move on and come back to it later.
        pass           

    def set_speed(self, new_speed):
        """ Set the speed at which the snake moves to a new value """
        self.speed = new_speed
        pygame.time.set_timer(EVENT_MOVE_SNAKE, new_speed)

    def change_speed(self, delta):
        """ Change the current speed by adding the delta """
        self.set_speed(self.speed + delta)

    def reset_position(self):
        """ Reset the size and position of the snake to the starting point """
        self.position = []
        for x in range(INITIAL_LENGTH):
            self.position.insert(0,(x,1))
        self.direction = EAST
        self.set_speed(INITIAL_SPEED)

class Grid():
    """ A two-dimensional array representing the play area """
    # Possible objects in a square of the grid
    EMPTY=0
    SNAKE=1
    FOOD=2

    # Grid square width in pixels
    CELL_WIDTH=20
    LINE_WIDTH=1
    
    def __init__(self, width, height):
        # ------- Grid properties --------
        # Dimensions of of the play area in squares
        self.width = width
        self.height = height

        # Dimensions of the play area in pixels on the screen
        self.screen_width = self.width * self.CELL_WIDTH
        self.screen_height = self.height * self.CELL_WIDTH

        # Position of top left corner of grid on screen
        (self.screen_left, self.screen_top) = center_rect(self.screen_width,
                                                         self.screen_height)
        
        # The grid is a list of lists, such that a point (x,y) corresponds
        # to the grid square self.grid[y][x]
        self.clear_grid()

    #--------- Grid methods ---------
    def get_cell(self, cell):
        """ Return the contents of the cell with the specified (x,y) value """
        x,y = cell
        return self.grid[y][x]

    def set_cell(self, cell, value):
        """ Set the contents of the cell with the specified (x,y) value """
        x,y = cell
        self.grid[y][x] = value
    
    def clear_grid(self):
        """ Reset the grid such that all the squares are empty """
        self.grid = [[self.EMPTY for x in range(self.width)] for y in range(self.height)]

    def clear_cell(self, cell):
        """ Reset the specified cell in the grid """
        self.set_cell(cell, self.EMPTY)
        
    def cell_offset(self, cell):
        """ Return the (x,y) location in pixels on the screen of the top left corner of
            the given cell in the grid """
        x,y = cell
        return (self.screen_left + (x * self.CELL_WIDTH),
                self.screen_top + (y * self.CELL_WIDTH))

    def within_grid(self, cell):
        """ Check if the given cell (x,y) is within the grid """
        # @3.1 Return True if the cell is within the grid, False otherwise
        # First unpack the cell into its constituent x,y parts
        x,y = cell
        return True

    def create_food(self):
        """ Add a food brick to a random square on the grid """
        # @4.1 random.randint(a,b) returns a random integer between a and b,
        # (including both end points). Use this to generate a random grid
        # square and set it's contents to self.FOOD using self.set_cell() 
        pass

    def fill_cell(self, cell, color):
        """ Fill the given cell (x,y) in the grid with the given color """
        x,y = self.cell_offset(cell)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, grid.CELL_WIDTH,
                                                    grid.CELL_WIDTH))
    
    def draw(self):
        """ Display the grid on the screen """
        # Draw a white rectangle as the background
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.screen_left,
                                                    self.screen_top,
                                                    self.screen_width,
                                                    self.screen_height))
                            
        # Draw horizontal lines     
        for y in range(self.height + 1):
            (start_x, start_y) = self.cell_offset((0,y))
            pygame.draw.lines(screen, GRAY, False,
                              [(start_x, start_y),
                               (start_x + self.screen_width, start_y)],
                              self.LINE_WIDTH)

        # Draw vertical lines     
        for x in range(self.width + 1):
            (start_x, start_y) = self.cell_offset((x,0))
            pygame.draw.lines(screen, GRAY, False,
                              [(start_x, start_y),
                               (start_x, start_y + self.screen_height)],
                              self.LINE_WIDTH)

        # @4.2 Walk through all the cells in the grid and if they contain
        # FOOD then color them in BLUE using self.fill_cell()          
            

# -------- Game Setup -----------

# Initialise the pygame module
pygame.init()

# Set the fonts to use
default_font = pygame.font.SysFont(None, 24)
large_font = pygame.font.SysFont(None, 48)

# Set the width and height of the screen [width, height]
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

# Set the initial states for the game and for the display.
set_game_state(GAME_NOT_STARTED)
set_screen_state(GAME_BEGIN)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create the objects we need in our game
snake = Snake()
grid = Grid(GRID_WIDTH,GRID_HEIGHT)
grid.create_food()
# @5.1 Create a top_score variable and initialise it to 0

              
# -------- Game Logic --------

def reset_game():
    """ Reset everything back to the inital state ready for a new game """
    snake.reset_position()
    set_game_state(GAME_NOT_STARTED)

def current_score():
    """ Return the current score """
    # @4.4 Return the current score, which is equal to the snake's length
    # minus its starting length.
    return 0

def crashed(next_space):
    """
    Check if the snake has crashed.
      Argument: next_square - the grid square (x,y) that the snake is about to
                move into
      Return: True if snake has crashed into the wall or itself,
              False otherwise
    """
    # @3.2 Check if the next space is outside the grid (using grid.within_grid()
    # or in the snake itself.
    return False

def move_snake():
    """ Move the snake one space forward, checking if it has hit anything """
    next_space = snake.next_space()
    
    if crashed(next_space):
        # Crashed into something. Stop the game.   
        set_game_state(GAME_OVER)
        # @5.3 If the current score is greater than the top score then
        # update the top score using set_top_score()
        
    else:
        # @4.3 If the next space contains FOOD - use grid.get_cell() then do
        # the following (there are methods in the grid and snake classes for
        # each).
        #   a. Remove the food 
        #   b. Place another bit of food in a random place on the grid
        #   c. Grow the snake (i.e. make it longer)
        #   d. Increase the snake's speed. Lower is faster, so subtract 5.
        # Otherwise move the snake.
        snake.move()

# -------- Event Handling --------

def handle_events():
    """ Handle any user events such as key presses or mouse clicks """  
    # Loop over all the events that have occurred.
    for event in pygame.event.get():
        # Regardless of what state we are in the QUIT event always exits
        if event.type == pygame.QUIT:
            # User clicked close. Exit the loop.
            set_game_state(GAME_EXITED)
        elif get_game_state() == GAME_RUNNING:
            # The game is running.
            if event.type == EVENT_MOVE_SNAKE:
                move_snake()
            if event.type == pygame.KEYDOWN:
                # Handle key presses.
                # @2.2 if event.key is K_UP, K_DOWN, K_LEFT or K_RIGHT then
                # change the snake's direction to NORTH, SOUTH, EAST or WEST.
                pass                
        elif get_game_state() == GAME_OVER:
            # The game has finished. Wait for the user to press space before
            # exiting.
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                reset_game()
        elif get_game_state() == GAME_NOT_STARTED:
            # If the game hasn't started yet then any key continues
            if event.type == pygame.KEYDOWN:
                set_game_state(GAME_RUNNING)

# -------- Draw Screen ----------

def draw_text(text, x=None, y=None, font=default_font, color=BLACK):
    """
    Write text to the screen.

    Arguments:
      text - the string to display
      x - the X co-ordinate to start from, or None to center horizontally
      y - the Y co-ordinate to start from, or None to center vertically
      font - the font to use
      color - the color to use
      
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    if x == None or y == None:
        (center_x, center_y) = center_rect(textrect.width, textrect.height)
        if x == None:
            x = center_x
        if y == None:
            y = center_y
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)

def draw_splash_screen():
    """ Draw the splash screen before the game starts """
    # Clear the existing screen
    screen.fill(WHITE)
    draw_text('Snake', y=100, font=large_font)
    draw_text('Press Any Key to Play', y=300)
    # @2.3 Add some brief instructions e.g.
    # "Use the arrow keys to control the snake"
    
    # Switch to the new screen
    pygame.display.flip()

def draw_game_over_screen():
    """ Draw the screen to display when the game ends """
    draw_text('Game Over', font=large_font, color=RED)
    draw_text('Press Space to Continue', y=300, color=RED)
    # @5.5 If the current score is equal to the top score then display a
    # message to tell the player how awesome they are for getting the top score
    
    # Switch to the new screen
    pygame.display.flip()

def draw_game_screen():
    """ Draw the screen while a game is in progress """
    # Clear the existing screen
    screen.fill(BLACK)
    grid.draw()
    for cell in snake:
        grid.fill_cell(cell, GREEN)
    draw_text('Score: {}'.format(current_score()), x=50, y=30, color=WHITE)
    # @5.4 Display the top score to the top right of the play area (x=350)
    
    # Switch to the new screen
    pygame.display.flip()

def draw_screen ():
    """ Draw the next screen. """
    if get_game_state() == GAME_NOT_STARTED:
        if get_screen_state() != GAME_NOT_STARTED:
            draw_splash_screen()
            set_screen_state(GAME_NOT_STARTED)
    elif get_game_state() == GAME_OVER:
        if get_screen_state() != GAME_OVER:
            draw_game_over_screen()
            set_screen_state(GAME_OVER)
    elif get_game_state() == GAME_RUNNING:
        draw_game_screen()




# -------- Main Program Loop -----------

while get_game_state() != GAME_EXITED:
    # ----- Handle Events -----
    handle_events()
 
    # --- Game logic     

    # --- Draw the screen
    draw_screen()    
    
    # --- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()
