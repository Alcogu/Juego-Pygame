import pygame
from constantes import *

class Enemigos(pygame.sprite.Sprite):

    def __init__(self, pos, me, lim_anim = [0,2], despe = 0):
        pygame.sprite.Sprite.__init__(self)
        self.me=me
        self.anm_ini=lim_anim[0]
        self.anm_fin=lim_anim[1]

        self.col=self.anm_ini
        self.dir=despe

        self.image = self.me[self.dir][self.col]
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velx = -5
        self.vely = 0
        self.salud = 100
        self.bloques = pygame.sprite.Group()
        self.generadores = pygame.sprite.Group()
        self.disparar = False
        self.temp = 100

    def update(self):

        self.rect.x += self.velx

        if self.rect.right > ancho:
            self.velx = -5
            #self.dir + 2
        
        if self.rect.left < 0:
            self.velx = 5
            #self.dir + 1