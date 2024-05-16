import pygame

class Character:

    x = 0
    y = 0
    jump = 0
    v = 5
    m = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.1
        self.current_direction = "right"

    def update_jump_count(self):
        self.jump = 1

    def update_jump(self):
        if self.jump:
            if self.v > 0:
                force = 0.5 * self.m * (self.v ** 2)
            else:
                force = -(0.5 * self.m * (self.v ** 2))

            self.y -= force
            self.v -= 1

        if self.y >= 20:
            self.y = 20
            self.jump = 0
            self.v = 5


    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)

        if direction == "right":
            self.current_direction = "right"
            self.x = self.x + self.delta
        elif direction == "left":
            self.current_direction = "left"
            self.x = self.x - self.delta
        #elif direction == "up":
            #self.current_direction = "left"
            #self.y = self.y - self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


