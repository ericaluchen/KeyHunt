import pygame
import time
from character import Character
from obstacle import Obstacle
from key import Key
from door import Door

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Key Hunt")

SCREEN_HEIGHT = 530
SCREEN_WIDTH = 370
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

c = Character(0, 480)
o = Obstacle(325, 50)
k = Key(100, 50)
d = Door(300, 480)

# Booleans
run = True
got_key = False

# Main Program Loop
while run:

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        c.move_direction("right")
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        c.move_direction("left")
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        c.move_direction("up")
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        c.move_direction("down")

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