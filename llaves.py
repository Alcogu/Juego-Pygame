import pygame

from constantes import *

class Llaves(pygame.sprite.Sprite):

    def __init__(self, idkey, pos, mll, lim_anim = [0,2], despll = 0):
        pygame.sprite.Sprite.__init__(self)
        self.mll = mll
        self.anm_ini = lim_anim[0]
        self.anm_fin = lim_anim[1]

        self.col = self.anm_ini
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