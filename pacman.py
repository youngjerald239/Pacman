import pygame
from settings import *

class Pacman(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/pacman_o.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2() # x and y direction currently set to 0
        # Get Keyboard input
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0 # stops key from moving after pressed

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0 # stops key from moving after pressed
            
    def update(self):
        self.input()