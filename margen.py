import pygame

from constantes import *

class Margen(pygame.sprite.Sprite):
    def __init__(self, pos, dim, cl=blanco):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dim)
        self.image.fill(cl)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = 0
        self.vely = 0
        self.velxx = 0
        self.velyy = 0

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.rect.x += self.velxx
        self.rect.y += self.velyy

