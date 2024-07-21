# import necessary modules
import pygame
import sys

# initialize all imported pygame modules
pygame.init()

# define game variables
player_size = 50
enemy_size = 50
player_speed = 5
width = 800
height = 600

# initialize the font variable for the game
font = pygame.font.Font(None, 36)

# initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# set the current screen caption
pygame.display.set_caption('Collision Detection Example')

# define player's x-coordinate for initial position
player_x = width // 2
# define player's y-coordinate for initial position
player_y = height // 2

# define enemy's x-coordinate for initial position
enemy_x = 300
# define enemy's y-coordinate for initial position
enemy_y = 300

# create an object to help track time
clock = pygame.time.Clock()
running = True

while running:
  # iterate through each event in the game's event queue
    for event in pygame.event.get():
      # if an event is of type "QUIT", set game as no longer running
        if event.type == pygame.QUIT:
            running = False

    # get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # decrement player's x-coordinate based on num times left arrow key pressed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    # increment player's x-coordinate based on num times right arrow key pressed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    # decrement player's y-coordinate based on num times up arrow key pressed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    # increment player's y-coordinate based on num times down arrow key pressed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # ensure player's x-coordinate stays within screen dimension
    player_x = max(0, min(width - player_size, player_x))
    # ensure player's y-coordinate stays within screen dimension
    player_y = max(0, min(height - player_size, player_y))

    # create a rectangle positioned at (player_x, player_y) with a width and height of PLAYER_SIZE
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    # create a rectangle positioned at (enemy_x, enemy_y) with a width and height of ENEMY_SIZE
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    # check if player's rectangle intersects with enemy's rectangle (indicating a collision)
    collision = player_rect.colliderect(enemy_rect)

    # set background color 
    screen.fill((0, 0, 0))

    # draw the player rectangle on the screen 
    pygame.draw.rect(screen, (255, 0, 0), player_rect)

    # draw the enemy rectangle on the screen
    pygame.draw.rect(screen, (0, 0, 255), enemy_rect)

    # display collision message if the player and enemy rectangles intersect/overlap
    if collision:
        text = font.render('Collision Occurred!', True, (255, 255, 255))
        screen.blit(text, (10, 10))

    # update the screen display
    pygame.display.flip()

    # set limit on num of frames per second that game will render (cap the frame rate)
    clock.tick(60)

# quit Pygame
pygame.quit()
sys.exit()
