import pygame
import sys

# Initialize Pygame
# pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# FPS = 60
# PLAYER_SPEED = 5

# Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# Screen setup
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Player Image Rendering")
# clock = pygame.time.Clock()

# Player class
# class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
    #     super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha() # Add image attribute for our players
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (x, y)
    #     self.speed_x = 0
    #     self.speed_y = 0

    # def update(self):
    #     keys = pygame.key.get_pressed()
        
    #     # Reset speed
    #     self.speed_x = 0
    #     self.speed_y = 0
        
    #     if keys[pygame.K_LEFT]:
    #         self.speed_x = -PLAYER_SPEED
    #     if keys[pygame.K_RIGHT]:
    #         self.speed_x = PLAYER_SPEED
    #     if keys[pygame.K_UP]:
    #         self.speed_y = -PLAYER_SPEED
    #     if keys[pygame.K_DOWN]:
    #         self.speed_y = PLAYER_SPEED
        
    #     # Update player position
    #     self.rect.x += self.speed_x
    #     self.rect.y += self.speed_y
        
    #     # Keep player on screen
    #     if self.rect.left < 0:
    #         self.rect.left = 0
    #     if self.rect.right > SCREEN_WIDTH:
    #         self.rect.right = SCREEN_WIDTH
    #     if self.rect.top < 0:
    #         self.rect.top = 0
    #     if self.rect.bottom > SCREEN_HEIGHT:
    #         self.rect.bottom = SCREEN_HEIGHT

# Initialize player with image
player_image_path = 'player.png'  # Path to your player image and make sure it's in the same directory with your main ***.py file
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, player_image_path)

# Create a group for all sprites
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)

# Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Update all sprites
#     all_sprites.update()
    
#     # Draw everything
#     screen.fill(BLACK)
#     all_sprites.draw(screen)
    
#     # Flip the display
#     pygame.display.flip()
    
#     # Ensure program maintains a rate of FPS frames per second
#     clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
