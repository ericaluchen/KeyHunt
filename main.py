import pygame
import time
from character import Character
from obstacle import Obstacle
from key import Key
from fire import Fire
from openedfire import OpenedFire
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

y = 0
x = 0
y_gravity = 1
jump_height = 20
y_velocity = jump_height

clock = pygame.time.Clock()
#
message = "Get the key!"
display_message = my_font.render(message, True,(255, 255, 255))
#

c = Character(0, 455)

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

k = Key(310, 70)
fire = Fire(310, 460)
oFire = OpenedFire(290, 440)
f = Floor(0, 512)

# Booleans
run = True
got_key = False
isJump = False

# Main Program Loop
while run:

    #if c.rect.colliderect(o1.rect or o2.rect or o3.rect or o4.rect or o5.rect or o6.rect or o7.rect or o8.rect or o9.rect or o10.rect or o11.rect):

    # Main Event Loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and isJump == False:
            #isJump = True
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_RIGHT]:
        c.move_direction("right")
    if keys[pygame.K_LEFT]:
        c.move_direction("left")
    if keys[pygame.K_UP]:
        c.move_direction("up")

    if keys[pygame.K_SPACE]:
        isJump = True

    if isJump == True:
        y -= y_velocity
        y_velocity -= y_gravity
        if y_velocity < -jump_height:
            isJump = False
            y_velocity = jump_height

    if c.rect.colliderect(k.rect):
        got_key = True

    # End of Main Program Loop
    new_time = time.time()
    time_diff = new_time - start_time
    time_text = my_font.render("Time Elapsed: " + str(round(time_diff, 2)) + " s", True, (255, 255, 255))

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
    screen.blit(fire.image, fire.rect)
    screen.blit(f.image, f.rect)
    screen.blit(time_text, (0, 15))

    if got_key == True:
        fire = Fire(5000, 5000)
        screen.blit(fire.image, fire.rect)
        screen.blit(oFire.image, oFire.rect)

    if c.rect.colliderect(oFire.rect):
        game_over = my_font.render("Good job!", True, (255, 255, 255))
        screen.fill((r, g, b))
        screen.blit(time_text, (150, 250))
        screen.blit(game_over, (150, 220))

    pygame.display.update()