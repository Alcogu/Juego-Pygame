import pygame

from constantes import *

class Modificadores(pygame.sprite.Sprite):

    def __init__(self, idmodi, pos, mi, lim_anim = [0,2], despm = 0):
        pygame.sprite.Sprite.__init__(self)
        self.mg = mi
        self.anm_ini = lim_anim[0]
        self.anm_fin = lim_anim[1]

        self.col = self.anm_ini
        self.dir = despm

        self.image = self.mg[self.dir][self.col]
        self.rect = self.image.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.velxx = 0
        self.velyy = 0
        self.idemodi = idmodi

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.rect.x += self.velxx
        self.rect.y += self.velyy