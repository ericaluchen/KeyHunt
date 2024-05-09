import pygame
import time
from character import Character
from obstacle import Obstacle
from key import Key
from door import Door
from floor import Floor

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
o = Obstacle(130, 450)
o1 = Obstacle(0, 400)
o2 = Obstacle(260, 400)
o3 = Obstacle(130, 350)
o4 = Obstacle(0, 300)
o5 = Obstacle(260, 300)
o6 = Obstacle(130, 250)
o7 = Obstacle(0, 200)
o8 = Obstacle(260, 200)
o9 = Obstacle(130, 150)
o10 = Obstacle(0, 100)
o11 = Obstacle(260, 100)

k = Key(295, 90)
d = Door(350, 485)
f = Floor(0, 512)

# Booleans
run = True
got_key = False
isJump = False
y = 10 # a part of jumping

# Main Program Loop
while run:

    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.Kw_d] or keys[pygame.K_RIGHT]:
        c.move_direction("right")
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        c.move_direction("left")
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        c.move_direction("up")
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        c.move_direction("down")

    if keys[pygame.K_SPACE]:
        isJump = True

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
    screen.blit(o1.image, o1.rect)
    screen.blit(o2.image, o2.rect)
    screen.blit(o3.image, o3.rect)
    screen.blit(o4.image, o4.rect)
    screen.blit(o5.image, o5.rect)
    screen.blit(o6.image, o6.rect)
    screen.blit(o7.image, o7.rect)
    screen.blit(o8.image, o8.rect)
    screen.blit(o9.image, o9.rect)
    screen.blit(o10.image, o10.rect)
    screen.blit(o11.image, o11.rect)

    screen.blit(k.image, k.rect)
    screen.blit(d.image, d.rect)
    screen.blit(f.image, f.rect)

    pygame.display.update()