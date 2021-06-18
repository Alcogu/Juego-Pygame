import pygame

from constantes import *

class Fondo(pygame.sprite.Sprite):

    def __init__(self, m):
        pygame.sprite.Sprite.__init__(self)
        self.fondo = m
        self.image = self.fondo
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        info = m.get_rect()
        self.f_ancho=info[2]
        self.f_alto=info[3]
        self.f_x = 0
        self.f_vx = 0
        self.f_y = 0
        self.f_vy = 0
        self.f_limx = ancho - self.f_ancho
        self.f_limy = alto - self.f_alto
        self.lim_d = ancho - 20
        self.lim_a = alto - 20