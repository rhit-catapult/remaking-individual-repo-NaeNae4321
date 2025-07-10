import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    return math.sqrt((point1_x - point2_x) ** 2 + (point1_y - point2_y) ** 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle_color = (154, 58, 212)
    circle_center1 = (screen.get_width() // 2, screen.get_height() // 2)
    circle_center2 = (screen.get_width() // 2, screen.get_height() - 50)
    circle_center3 = (400, 160)
    circle_radius = 50
    circle_border_width = 3

    message_text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                distance_from_circle = distance(circle_center1, event.pos)
                distance_from_circle2 = distance(circle_center2, event.pos)
                distance_from_circle3 = distance(circle_center3, event.pos)

                if distance_from_circle3 <= circle_radius:
                    pygame.mixer.music.load("laserShoot.wav")
                    message_text = 'Bullseye!'
                    pygame.mixer.music.play(-1)
                elif distance_from_circle2 <= circle_radius:
                    pygame.mixer.music.load("click.wav")
                    message_text = 'Bullseye!'
                    pygame.mixer.music.play(-1)
                elif distance_from_circle <= circle_radius:
                    pygame.mixer.music.load("drums.wav")
                    message_text = 'Bullseye!'
                    pygame.mixer.music.play(-1)
                else:
                    message_text = 'You missed!'
                    pygame.mixer.music.stop()

        screen.fill(pygame.Color("Black"))

        pygame.draw.circle(screen, circle_color, circle_center1, circle_radius, circle_border_width)
        pygame.draw.circle(screen, circle_color, circle_center2, circle_radius, circle_border_width)
        pygame.draw.circle(screen, circle_color, circle_center3, circle_radius, circle_border_width)
        screen.blit(instructions_image, (25, 25))
        screen.blit(font.render(message_text, True, text_color), (10, screen.get_height() - 20))

        pygame.display.update()


main()
