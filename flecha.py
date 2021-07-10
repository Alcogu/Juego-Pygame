import pygame
from constantes import *

class Flecha(pygame.sprite.Sprite):

    def __init__(self, pos, mfl, anim = 0, despmfl = 0):
        pygame.sprite.Sprite.__init__(self)
        self.mfl = mfl
        self.anim = anim

        self.col = self.anim
        self.dir = despmfl

        self.image = self.mfl[self.dir][self.col]
        self.rect = self.image.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
