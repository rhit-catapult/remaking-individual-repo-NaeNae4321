import pygame
import sys


def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    image1 = pygame.image.load("2dogs.JPG")
    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))

    # Prepare the text caption(s)
    font1 = pygame.font.SysFont("comicsansms", 28)
    font2 = pygame.font.SysFont("comicsansms", 60)

    caption1 = font1.render("Two Dogs", True, BLACK)
    caption2 = font2.render("Boop", True, WHITE)

    # Prepare the music
    bark = pygame.mixer.Sound("bark.wav")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                bark.play()

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        screen.blit(image1, (0, 0))

        # Draw the text onto the screen
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        screen.blit(caption1, (image1.get_width() // 2 - caption1.get_width() // 2, image1.get_height() - 8))
        screen.blit(caption2, (image1.get_width() // 2 - caption2.get_width() // 2, 20))

        # Update the screen
        pygame.display.update()


main()
