import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

class Ball:
    def __init__(self, screen, color, x, y, radius, grow, max_size, split):
        self.screen = screen
        self.color = color
        self.x = clamp(x, radius, self.screen.get_width() - radius)
        self.y = clamp(y, radius, self.screen.get_height() - radius)
        self.y = y
        self.radius = radius
        self.speed_x = 0
        self.speed_y = 0
        self.grow = grow
        self.max_size = max_size
        self.split = split
        self.bounce = False

        while self.speed_x == 0 and self.speed_y == 0:
            self.speed_x = random.randint(-6, 6)
            self.speed_y = random.randint(-6, 6)

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius - 1)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.radius > self.screen.get_width() or self.x - self.radius < 0:
            self.bounce = True
            self.speed_x *= -1
            if self.grow != 0:
                self.radius += self.grow

        if self.y + self.radius > self.screen.get_height() or self.y - self.radius < 0:
            self.bounce = True
            self.speed_y *= -1
            if self.grow != 0:
                self.radius += self.grow

        self.x = clamp(self.x, self.radius, self.screen.get_width() - self.radius)
        self.y = clamp(self.y, self.radius, self.screen.get_width() - self.radius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    bounce_sound = pygame.mixer.Sound('bounce.wav')
    bounce_sound.set_volume(0.5)
    split_sound = pygame.mixer.Sound('hitHurt.wav')

    font = pygame.font.Font(None, 25)

    instructions = True
    instruction_text = 'Click to spawn balls'
    text_color = (0, 0, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    balls = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                instructions = False

                balls.append(make_ball(screen, event.pos[0], event.pos[1], 200))

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        for ball in balls:
            ball.bounce = False
            ball.move()

            if ball.bounce:
                bounce_sound.play()

            if ball.radius > ball.max_size or ball.radius <= 2:
                if ball.split != 0:
                    split_sound.play()

                    for i in range(ball.split):
                        balls.append(make_ball(screen, ball.x, ball.y, 0, random.randint(8, 16), -1))

                balls.remove(ball)

            ball.draw()

        if instructions:
            screen.blit(instructions_image, (screen.get_width() // 2 - instructions_image.get_width() // 2,
                screen.get_height() - instructions_image.get_height() - 5))

        pygame.display.update()

def clamp(x, minimum, maximum):
    return min(max(x, minimum), maximum)

def make_ball(screen, x, y, split, size=random.randint(4, 10), grow=1):
    return Ball(screen, (random.randint(0, 255), random.randint(0, 255),
        random.randint(0, 255)), x, y, size, grow, 16, split)

main()


# Optional challenges (if you finish and want to play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc.) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
