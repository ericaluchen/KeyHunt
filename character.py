import pygame

class Character:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 0.1
        self.current_direction = "right"

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
        elif direction == "up":
            self.current_direction = "left"
            self.y = self.y - self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


