import pygame
from constantes import *

class Flecha(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,20])
        self.image.fill(blanco)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vely = 0
        self.velx = 0

        self.personajes = pygame.sprite.Group()

    def update(self):

        """if self.personaje.orientacion == 1:
            self.personaje.rect.midtop
            self.vely = -5
        if self.personaje.orientacion == 2:
            self.personaje.rect.midbottom
            self.vely = 5
        if self.personaje.orientacion == 3:
            self.personaje.rect.midleft
            self.velx = -5
        if self.personaje.orientacion == 4:
            self.personaje.rect.midright
            self.vely = 5"""

        self.rect.y += self.vely
        self.rect.x += self.velx
