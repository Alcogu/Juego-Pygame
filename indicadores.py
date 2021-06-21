import pygame

from constantes import *

class Indicadores(pygame.sprite.Sprite):

    def __init__(self, pos, mi, lim_anim=[0,2], despi = 0):
        pygame.sprite.Sprite.__init__(self)
        self.mg = mi
        self.anm_ini = lim_anim[0]
        self.anm_fin =lim_anim[1]

        self.col = self.anm_ini
        self.dir = despi

        self.image = self.mg[self.dir][self.col]
        self.rect = self.image.get_rect()
        
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        