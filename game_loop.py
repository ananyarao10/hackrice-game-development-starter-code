import pygame
import sys

# initialize all imported pygame modules
pygame.init()

# set the screen dimensions and other game variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

# initialize a screen w/ correct dimensions for display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# set the current screeb caption
pygame.display.set_caption('Game Loop Example')

# create an object to help track time
clock = pygame.time.Clock()
running = True

while running:
  # iterate through each event in the game's event queue
    for event in pygame.event.get():
      # if an event is of type "QUIT", set game as no longer running
        if event.type == pygame.QUIT:
            running = False

    # add game logic here 

    # clear the screen
    screen.fill(BG_COLOR)

    # draw everything on the screen

    # update the screen display
    pygame.display.flip()

    # set limit on num frames per second game will render (cap the frame rate)
    clock.tick(60)

# quit Pygame
pygame.quit()
sys.exit()
