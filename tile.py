import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Pellet(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/dot.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Teleport(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/portal.png')
        self.rect = self.image.get_rect(topleft = pos)       