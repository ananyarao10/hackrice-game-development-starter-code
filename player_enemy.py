# import necessary modules
import pygame
import sys

# define game variables
width = 800
height = 600
player_speed = 5

# initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# set the current screen caption
pygame.display.set_caption("Player character behavior")

# create an object to help track time
clock = pygame.time.Clock()

# player setup
player_image = pygame.Surface((50, 50))
player_image.fill((255,255,255))
player_rect = player_image.get_rect()
player_rect.center = (width // 2, height // 2)

def update_player_position():
    keys = pygame.key.get_pressed()
    
    # define speed variables
    speed_x = 0
    speed_y = 0
    
    if keys[pygame.K_LEFT]:
        speed_x = -player_speed
    if keys[pygame.K_RIGHT]:
        speed_x = player_speed
    if keys[pygame.K_UP]:
        speed_y = -player_speed
    if keys[pygame.K_DOWN]:
        speed_y = player_speed
    
    # update player's position
    player_rect.x += speed_x
    player_rect.y += speed_y
    
    # ensure player stays on screen
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > width:
        player_rect.right = width
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > height:
        player_rect.bottom = height

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_player_position()
    
    # draw
    screen.fill((0,0,0))
    screen.blit(player_image, player_rect)
    
    # update the screen display
    pygame.display.flip()

    # set limit on num of frames per second that game will render (cap the frame rate)
    clock.tick(60)

# quit Pygame
pygame.quit()
sys.exit()