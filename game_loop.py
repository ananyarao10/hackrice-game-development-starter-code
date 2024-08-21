import pygame
import sys

# initialize all imported pygame modules
pygame.init()

# initialize a screen w/ correct dimensions for display
screen = pygame.display.set_mode((800, 600))

# set the current screen caption
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

    # ADD YOUR OWN CODE FOR GAME LOGIC HERE
    # EXAMPLE: MOVING OBJECTS, COLLISION DETECTION, ETC. 

    # clear the screen (make it black)
    screen.fill((0,0,0))

    # ADD YOUR OWN CODE TO DRAW EVERYTHING ON THE SCREEN HERE
    # EXAMPLE: screen.blit(your_surface, (x, y)) FOR DISPLAYING IMAGES

    # update the screen display
    pygame.display.flip()

    # set limit on num frames per second game will render (cap the frame rate)
    clock.tick(60)

# quit Pygame
pygame.quit()
sys.exit()
