# import necessary modules
import pygame
import pygame_gui

# initialize all imported pygame modules
pygame.init()

# Code source:
# https://pygame-gui.readthedocs.io/en/latest/quick_start.html

# define game variables
width = 800
height = 600

# initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# set the current screen caption
pygame.display.set_caption('Quick Start')

# create a background surface
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# set up the UI manager
manager = pygame_gui.UIManager((800, 600))

# Create a button
hello_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 275), (100, 50)),
    text='Say Hello',
    manager=manager
)

# create an object to help track time
clock = pygame.time.Clock()

is_running = True
while is_running:
    time_delta = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')

        manager.process_events(event)

    # update UI elements
    manager.update(time_delta)

    # draw everything
    screen.blit(background, (0, 0))
    manager.draw_ui(screen)

    # update the display
    pygame.display.flip()

# quit Pygame
pygame.quit()