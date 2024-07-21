# import necessary modules
import pygame
import sys

# initialize all imported pygame modules
pygame.init()

# Code source:
# https://pythonprogramming.net/adding-sounds-music-pygame/
# This code uses the .mixer pygame call to add sounds and music to a game

# Define game variables
width = 800
height = 600

# initialize screen display with width and height 
screen = pygame.display.set_mode((width, height))

# set the current screen caption
pygame.display.set_caption("Sound and Music Example")

# create an object to help track time
clock = pygame.time.Clock()

# load sound
# .mp3 files can be used, but pygame is known to have bugs with those, so .wav is preferred
sound = pygame.mixer.Sound("sound.wav")

# calling load to set-up the music at the file jazz.wav
pygame.mixer.music.load('music.wav')

# variables to manage state and timing
sound_played = False
sound_start_time = 0
music_start_time = 0
action_phase = 0  

# initialize font for displaying text
font = pygame.font.Font(None, 36)

# function to render text on the screen
def render_text(message, color, position):
    text_surface = font.render(message, True, color)
    screen.blit(text_surface, position)

# Main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # manage action phases
    current_time = pygame.time.get_ticks()

    # action_phase = 0 --> display caption that we are abt to play sound
    if action_phase == 0:  
        render_text("Playing crash sound...", (255, 255, 255), (10, 10))
         # update screen to show text
        pygame.display.flip()
        sound_start_time = current_time
        # increment action_phase to move to next action
        action_phase = 1
    
    # action_phase = 1 --> play the sound
    elif action_phase == 1:  
        if current_time - sound_start_time >= 1000:
            sound.play()
            # increment action_phase to move to next action
            action_phase = 2
    
    # action_phase = 2 --> wait for the sound to finish
    elif action_phase == 2:  
        if not pygame.mixer.get_busy():
            render_text("Starting music playback...", (255, 255, 255), (10, 50))
            pygame.display.flip()  # update screen to show text
            music_start_time = current_time
            # increment action_phase to move to next action
            action_phase = 3
    
    # action_phase = 3 --> play the music
    elif action_phase == 3:  
        if current_time - music_start_time >= 1000:
            # tells the game to play the loaded music indefinitely
            pygame.mixer.music.play(-1)
            # increment action_phase to move to next action
            action_phase = 4
    
    # action_phase = 4 --> wait for 3 seconds, and then pause the music
    elif action_phase == 4:  
        if current_time - music_start_time >= 1000 + 3000:
            render_text("Pausing music...", (255, 255, 255), (10, 90))
            pygame.display.flip() # update screen to show text
            pygame.time.wait(1000) # display caption for 1 second
            # tells the game to pause the loaded music
            pygame.mixer.music.pause()
            music_start_time = current_time
            # increment action_phase to move to next action
            action_phase = 5
    
    # action_phase = 5 --> wait for 3 seconds, and then unpause the music
    elif action_phase == 5:  
        if current_time - music_start_time >= 1000 + 3000:
            render_text("Unpausing music...", (255, 255, 255), (10, 130))
            pygame.display.flip() # update screen to show text
            pygame.time.wait(1000) # display caption for 1 second
            # tells the game to unpause the loaded music
            pygame.mixer.music.unpause()
            # increment action_phase to move to next action
            action_phase = 6

    # action_phase = 6 --> end
    elif action_phase == 6: 
        render_text("All actions completed", (255, 255, 255), (10, 170))
        pygame.display.flip() # update screen to show text
        pygame.time.wait(1000) # display caption for 1 second
        # exit the game loop
        running = False

    # update the screen display
    pygame.display.flip()

    # Set limit on number of frames per second that game will render (cap the frame rate)
    clock.tick(60)  

# quit Pygame
pygame.quit()
sys.exit()