import pygame
# Code source:
# https://pythonprogramming.net/adding-sounds-music-pygame/
# This code uses the .mixer pygame call to add sounds and music to a game

# Using Sound
# .mp3 files can be used, but pygame is known to have bugs with those, so .wav is preferred
crash_sound = pygame.mixer.Sound("crash.wav")
# Tells the game to play the sound at the variable crash_sound
pygame.mixer.Sound.play(crash_sound)

# Using music
# Calling load to set-up the music at the file jazz.wav
pygame.mixer.music.load('jazz.wav')
# Tells the game to play the loaded music indefinitely, by passing -1
pygame.mixer.music.play(-1)
# This call will tell the music to stop, even if played with the argument -1
pygame.mixer.music.stop()


# Pausing and Unpausing
pygame.mixer.music.pause()
pygame.mixer.music.unpause()
