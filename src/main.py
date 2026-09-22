from mazegenerator import MazeGenerator
import pygame



# Initialize pygame
pygame.init()

# Set up the window dimensions (1280x720)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # Handle user input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear/fill the screen with a color
    screen.fill("purple")

    # Update the display
    pygame.display.flip()
    
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
