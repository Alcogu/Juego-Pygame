import pygame

from constantes import *

class Personaje(pygame.sprite.Sprite):

    def __init__(self, m, lim_anim = [0,2], desp = 0):
        pygame.sprite.Sprite.__init__(self)
        self.m = m
        self.anm_ini = lim_anim[0]
        self.anm_fin = lim_anim[1]

        self.col = self.anm_ini
        self.dir = desp

        self.image = self.m[self.dir][self.col]
        self.rect = self.image.get_rect()

        self.rect.x = 20
        self.rect.y = 20
        self.velx = 0
        self.vely = 0
        self.salud = 1
        self.bloques = pygame.sprite.Group()
        self.generadores = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.morir = pygame.mixer.Sound('sounds/muerte.wav')

    def update(self):
        if self.velx != self.vely:
            self.image = self.m[self.dir][self.col]

            if self.col < self.anm_fin:
                self.col += 1
            else:
                self.col = self.anm_ini

        self.rect.x += self.velx
            
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.velx > 0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
            else:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
            self.velx = 0

        col = pygame.sprite.spritecollide(self, self.generadores, False)
        for g in col: 
            if self.velx > 0:
                if self.rect.right > g.rect.left:
                    self.rect.right = g.rect.left
            else:
                if self.rect.left < g.rect.right:
                    self.rect.left = g.rect.right
            self.velx = 0

        col = pygame.sprite.spritecollide(self, self.enemigos, False)
        for e in col:
            if self.velx > 0:
                if self.rect.right > e.rect.left:
                    self.rect.right = e.rect.left
            else:
                if self.rect.left < e.rect.right:
                    self.rect.left = e.rect.right
            self.velx = 0

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > ancho:
            self.rect.right = ancho

        self.rect.y += self.vely
        
        col = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in col: 
            if self.vely > 0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
            else:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
            self.vely = 0
        
        col = pygame.sprite.spritecollide(self, self.generadores, False)

        for g in col: 
            if self.vely > 0:
                if self.rect.bottom > g.rect.top:
                    self.rect.bottom = g.rect.top
            else:
                if self.rect.top < g.rect.bottom:
                    self.rect.top = g.rect.bottom
            self.vely = 0

        col = pygame.sprite.spritecollide(self, self.enemigos, False)
        for e in col: 
            if self.vely > 0:
                if self.rect.bottom > e.rect.top:
                    self.rect.bottom = e.rect.top
            else:
                if self.rect.top < e.rect.bottom:
                    self.rect.top = e.rect.bottom
            self.vely=0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > alto:
            self.rect.bottom = alto
