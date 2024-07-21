# import necessary modules
import pygame
import sys

# initialize all imported pygame modules
pygame.init()

# define game variables
width = 800
height = 600
player_speed = 5
player_width = 150  
player_height = 150

# initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# set the current screen caption
pygame.display.set_caption("Importing an image for the player component")

# create an object to help track time
clock = pygame.time.Clock()

# load the player image
player_image = pygame.image.load('player_image.png').convert_alpha()

# scale the player image to the desired size
player_image = pygame.transform.scale(player_image, (player_width, player_height))

# Get the rectangle for the player image
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # set the background color
    screen.fill((0, 0, 0))

    # draw the player image on the screen
    screen.blit(player_image, player_rect)

    # update the screen display
    pygame.display.flip()

    # set limit on num of frames per second that game will render (cap the frame rate)
    clock.tick(60)

# quit Pygame
pygame.quit()
sys.exit()
