from turtle import Screen
import pygame
from settings import *


class Pacman(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/pacman/pacman_o.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        
        # graphics setup
        self.import_pacman_assets()

        # movement
        self.direction = pygame.math.Vector2() # x and y direction currently set to 0
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def import_pacman_assets(self):
        character_path = './assets/pacman/'
        self.animations = {'up': [],'down': [],'left': [],'right':[],
        'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            

        # Get Keyboard input
    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
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

    def move(self,speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed 
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
        #self.rect.center += self.direction * speed 
        rotpac = pygame.transform.rotate(pygame.surface)
        position = rotpac.get_rect(center = (pacX))
        wrap_around = False

        if position[0] <  0 :
            # off screen left
            position.move_ip(WIDTH, 0)
            wrap_around = True

        if position[0]  + Pacman.get_width() > WIDTH:
            # off screen right
            position.move_ip(-WIDTH, 0)
            wrap_around = True
        
        if wrap_around:

            Screen.blit(rotpac, position)

        position[0] %= WIDTH 
        pacX %= WIDTH


        Screen.blit(ropac, position)
        pygame.display.update()
        FPS.tick()

    def collision(self,direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left # player will not overlapp with obstacles
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top # player will not overlapp with obstacles
                    if self.direction.y < 0: # moving up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)