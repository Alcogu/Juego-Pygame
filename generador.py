import pygame
from constantes import *

class Generador(pygame.sprite.Sprite):

    def __init__(self, pos, mg, lim_anim=[0,2], despg=0):
        pygame.sprite.Sprite.__init__(self)
        self.mg=mg
        self.anm_ini=lim_anim[0]
        self.anm_fin=lim_anim[1]

        self.col=self.anm_ini
        self.dir=despg

        self.image = self.mg[self.dir][self.col]
        self.rect = self.image.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely