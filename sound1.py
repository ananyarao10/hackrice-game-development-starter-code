import pygame
import sys

# Initialize all imported pygame modules
pygame.init()

# Define game variables
width = 800
height = 600
FPS = 60

# Initialize screen display with width and height
screen = pygame.display.set_mode((width, height))

# Set the current screen caption
pygame.display.set_caption("Sound and Music Example")

# Create an object to help track time
clock = pygame.time.Clock()

# Load sound
sound = pygame.mixer.Sound("sound.wav")

# Load music
pygame.mixer.music.load('music.wav')

# Initialize font for displaying text
font = pygame.font.Font(None, 36)

# Function to render text on the screen
def render_text(message, color, position):
    screen.fill((0, 0, 0))  # Clear screen before rendering new text
    text_surface = font.render(message, True, color)
    screen.blit(text_surface, position)

# Variables to manage state and timing
sound_played = False
sound_start_time = 0
music_start_time = 0
action_delay = 1000  # Time to display message before next action (in milliseconds)
action_phase = 0  # 0: Show sound caption, 1: Play sound, 2: Show music caption, 3: Play music, etc.

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Manage action phases
    current_time = pygame.time.get_ticks()
    
    if action_phase == 0:  # Show sound caption
        render_text("Playing crash sound...", (255, 255, 255), (10, 10))
        pygame.display.flip()  # Update screen to show text
        sound_start_time = current_time
        action_phase = 1
    
    elif action_phase == 1:  # Play sound
        if current_time - sound_start_time >= action_delay:
            sound.play()
            action_phase = 2
    
    elif action_phase == 2:  # Wait for sound to finish
        if not pygame.mixer.get_busy():
            render_text("Starting music playback...", (255, 255, 255), (10, 50))
            pygame.display.flip()  # Update screen to show text
            music_start_time = current_time
            action_phase = 3
    
    elif action_phase == 3:  # Play music
        if current_time - music_start_time >= action_delay:
            pygame.mixer.music.play(-1)
            action_phase = 4
    
    elif action_phase == 4:  # Wait 2 seconds, then pause music
        if current_time - music_start_time >= action_delay + 2000:
            render_text("Pausing music...", (255, 255, 255), (10, 90))
            pygame.display.flip()  # Update screen to show text
            pygame.time.wait(action_delay)  # Display caption for 1 second
            pygame.mixer.music.pause()
            music_start_time = current_time
            action_phase = 5
    
    elif action_phase == 5:  # Wait 2 seconds, then unpause music
        if current_time - music_start_time >= action_delay + 2000:
            render_text("Unpausing music...", (255, 255, 255), (10, 130))
            pygame.display.flip()  # Update screen to show text
            pygame.time.wait(action_delay)  # Display caption for 1 second
            pygame.mixer.music.unpause()
            action_phase = 6

    elif action_phase == 6:  # End
        render_text("All actions completed", (255, 255, 255), (10, 170))
        pygame.display.flip()
        pygame.time.wait(action_delay)  # Display final message for a short period
        running = False  # Exit the loop

    # Update the screen display
    pygame.display.flip()

    # Set limit on number of frames per second that game will render (cap the frame rate)
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
