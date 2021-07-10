import pygame

from constantes import *

class Llaves(pygame.sprite.Sprite):

    def __init__(self, idkey, pos, mll, anim = 0, despll = 0):
        pygame.sprite.Sprite.__init__(self)
        self.anim = anim
        self.mll = mll

        self.col = self.anim
        self.dir = despll

        self.image = self.mll[self.dir][self.col]
        self.rect = self.image.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.idekey = idkey

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely