import pygame

from constantes import *

class Margen(pygame.sprite.Sprite):
    def __init__(self, pos, dimension):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(dimension)
        self.image.fill(negro)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
