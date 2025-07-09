import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Setup Test")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100)) # Draw a blue square
    pygame.draw.rect(screen, RED, (375, 275, 50, 50)) # Draw a red smaller square

    # Update the display
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()