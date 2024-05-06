import pygame
import time
from character import Character
from obstacle import Obstacle

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Key Hunt")

SCREEN_HEIGHT = 370
SCREEN_WIDTH = 530
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

r = 64
g = 64
b = 64
screen.fill((r, g, b))

start_time = time.time()

#
message = "Get the key to unlock the door!"
display_message = my_font.render(message, True,(255, 255, 255))
#

c = Character(50, 50)
o = Obstacle(50, 50)

# Boolean
run = True
# Main Program Loop
while run:

    # Main Event Loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    # End of Main Program Loop

    # Fill Screen and Blit
    screen.fill((r, g, b))
    screen.blit(display_message, (0, 0))
    screen.blit(c.image, c.rect)
    screen.blit(o.image, o.rect)

    pygame.display.update()


